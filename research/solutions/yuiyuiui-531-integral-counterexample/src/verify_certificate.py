"""Independent reconstruction and exact replay of the fixed n=13,r=5 case.

This module does not import the certificate generator. It uses explicit
diamond-core membership and a complete clique recursion, rather than winding
triangles, and checks each integer cancellation against the adjacent maps.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path


def digest(value):
    text = json.dumps(value, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(text.encode('ascii')).hexdigest()


def reconstruct_basis():
    n = 13
    vertices = [(i//n, i % n) for i in range(n*n)]

    def distance(i, j):
        a, b = vertices[i]
        x, y = vertices[j]
        return min(abs(a-x), n-abs(a-x)) + min(abs(b-y), n-abs(b-y))

    adjacency = [{j for j in range(n*n) if i != j and distance(i, j) <= 5}
                 for i in range(n*n)]
    diamonds = []
    for a in range(n):
        for b in range(n):
            for cx, cy in ((2*a+1, 2*b), (2*a, 2*b+1)):
                mask = 0
                for i, (x, y) in enumerate(vertices):
                    dx, dy = abs(2*x-cx), abs(2*y-cy)
                    if min(dx, 2*n-dx) + min(dy, 2*n-dy) <= 5:
                        mask |= 1 << i
                diamonds.append(mask)
    core_through_origin = [f for f in diamonds if f & 1]
    anchored = set()
    visited = 0

    def visit(simplex, candidates, mask):
        nonlocal visited
        visited += 1
        if not any(mask & ~f == 0 for f in core_through_origin):
            anchored.add(simplex)
        possible = mask | sum(1 << i for i in candidates)
        # Every descendant is in this diamond, so none is a relative basis
        # element. This pruning cannot remove a nonliftable simplex.
        if any(possible & ~f == 0 for f in core_through_origin):
            return
        for position, vertex in enumerate(candidates):
            visit(simplex+(vertex,),
                  [j for j in candidates[position+1:] if j in adjacency[vertex]],
                  mask | (1 << vertex))

    visit((0,), sorted(adjacency[0]), 1)
    translated = defaultdict(set)
    for simplex in anchored:
        for a in range(n):
            for b in range(n):
                image = tuple(sorted(((vertices[i][0]+a) % n)*n
                                     +(vertices[i][1]+b) % n for i in simplex))
                translated[len(simplex)-1].add(image)
    basis = {q: sorted(translated[q]) for q in sorted(translated)}
    return basis, {'visited_origin_cliques': visited,
                   'origin_nonliftable_cliques': len(anchored),
                   'core_diamonds': len(diamonds)}


def reconstruct_boundaries(basis):
    indices = {q: {s: i for i, s in enumerate(ss)} for q, ss in basis.items()}
    B = {}
    for q in basis:
        B[q] = {}
        for c, simplex in enumerate(basis[q]):
            column = {}
            for removed in range(len(simplex)):
                face = tuple(v for j, v in enumerate(simplex) if j != removed)
                row = indices.get(q-1, {}).get(face)
                if row is not None:
                    column[row] = -1 if removed % 2 else 1
            B[q][c] = column
    return B


def serialized_boundaries(B):
    return {str(q): [[[r, a] for r, a in sorted(B[q][c].items())]
                    for c in sorted(B[q])] for q in sorted(B)}


def check_square_zero(B):
    for q in B:
        if q-1 not in B:
            continue
        for column in B[q].values():
            total = defaultdict(int)
            for middle, a in column.items():
                if middle not in B[q-1]:
                    raise ValueError('Boundary references a removed basis vector')
                for row, b in B[q-1][middle].items():
                    total[row] += a*b
            if any(total.values()):
                raise ValueError('Boundary squared is nonzero over Z')


def replay(B, dimensions, trace):
    B = {q: {c: dict(v) for c, v in columns.items()} for q, columns in B.items()}
    active = {q: set(range(d)) for q, d in dimensions.items()}
    for step, record in enumerate(trace):
        if len(record) != 4 or any(type(x) is not int for x in record):
            raise ValueError('Malformed cancellation record')
        q, r, c, a = record
        if (a not in (-1, 1) or c not in B.get(q, {})
                or r not in active.get(q-1, set()) or B[q][c].get(r) != a):
            raise ValueError(f'Invalid unit pivot at step {step}')
        pivot = dict(B[q][c])
        multiples = {z: col[r]*a for z, col in B[q].items()
                     if z != c and r in col}

        # Check the changed coordinates of every adjacent upper boundary.
        for col in B.get(q+1, {}).values():
            changed = col.get(c, 0)+sum(factor*col.get(z, 0)
                                      for z, factor in multiples.items())
            if changed:
                raise ValueError('Upper chain identity fails at cancellation')
            col.pop(c, None)

        # The new lower basis vector is a*e_r + sum_i pivot_i*e_i.
        lower = B.get(q-1, {})
        combination = defaultdict(int)
        for i, coefficient in pivot.items():
            for row, value in lower.get(i, {}).items():
                combination[row] += coefficient*value
        if any(combination.values()):
            raise ValueError('Lower chain identity fails at cancellation')

        for z, factor in multiples.items():
            col = B[q][z]
            for row, value in pivot.items():
                value = col.get(row, 0)-factor*value
                if value:
                    col[row] = value
                else:
                    col.pop(row, None)
        del B[q][c]
        active[q].remove(c)
        active[q-1].remove(r)
        lower.pop(r, None)
    check_square_zero(B)
    return active, B


def rank_mod3_by_rows(matrix):
    rows = [[value % 3 for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0]) if rows else 0):
        selected = next((i for i in range(pivot_row, len(rows))
                         if rows[i][column]), None)
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        factor = 1 if rows[pivot_row][column] == 1 else 2
        rows[pivot_row] = [(factor*x) % 3 for x in rows[pivot_row]]
        for i in range(pivot_row+1, len(rows)):
            factor = rows[i][column]
            rows[i] = [(a-factor*b) % 3
                       for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
    return pivot_row


def verify(certificate):
    expected_model = {'n': 13, 'radius': 5, 'k': 5, 'metric': 'periodic Manhattan',
                      'filtration': 'closed diameter <= radius',
                      'vertex_label': '13*a+b', 'orientation': 'increasing labels',
                      'basis_order': 'lexicographic within each degree'}
    if certificate.get('schema_version') != 1 or certificate.get('model') != expected_model:
        raise ValueError('Certificate is not for the frozen n=13,r=5 model')
    basis, enumeration = reconstruct_basis()
    B = reconstruct_boundaries(basis)
    check_square_zero(B)
    dimensions = {q: len(ss) for q, ss in basis.items()}
    if digest({str(q): ss for q, ss in basis.items()}) != certificate['basis_sha256']:
        raise ValueError('Relative basis hash mismatch')
    if digest(serialized_boundaries(B)) != certificate['boundary_sha256']:
        raise ValueError('Initial signed boundary hash mismatch')
    if {str(q): d for q, d in dimensions.items()} != certificate['chain_dimensions']:
        raise ValueError('Chain dimensions mismatch')
    active, residual = replay(B, dimensions, certificate['unit_cancellation_trace'])
    if {str(q): sorted(ids) for q, ids in active.items()} != certificate['active_basis_indices']:
        raise ValueError('Active basis indices mismatch')
    if {str(q): len(ids) for q, ids in active.items()} != certificate['residual_chain_dimensions']:
        raise ValueError('Residual dimensions mismatch')
    if any(col for q, columns in residual.items() if q != 4
           for col in columns.values()):
        raise ValueError('Unexpected nonzero residual differential')
    if active.get(5):
        raise ValueError('A nonzero C5 invalidates the advertised H4 calculation')
    matrix = [[residual[4][c].get(r, 0) for c in sorted(active[4])]
              for r in sorted(active[3])]
    if matrix != certificate['residual_d4']:
        raise ValueError('Residual integer matrix mismatch')
    nonzero = sum(any(row[c] for row in matrix) for c in range(len(matrix[0])))
    lower_rank = rank_mod3_by_rows(matrix)
    if lower_rank != nonzero:
        raise ValueError('Rational rank is not determined by the supplied bounds')
    h4_rank = len(active[4])-lower_rank
    expected = (certificate['nonzero_d4_columns'], certificate['rank_d4_mod3'],
                certificate['rank_d4_Q'], certificate['relative_H4_free_rank'])
    if expected != (nonzero, lower_rank, lower_rank, h4_rank):
        raise ValueError('Advertised exact rank mismatch')
    return {'status': 'PASS', 'case': {'k': 5, 'n': 13, 'radius': 5},
            'enumeration': enumeration,
            'basis_sha256': certificate['basis_sha256'],
            'initial_chain_dimensions': certificate['chain_dimensions'],
            'unit_cancellations_by_degree': dict(Counter(
                record[0] for record in certificate['unit_cancellation_trace'])),
            'residual_chain_dimensions': certificate['residual_chain_dimensions'],
            'nonzero_d4_columns': nonzero, 'rank_d4_mod3': lower_rank,
            'rank_d4_Q': lower_rank, 'relative_H4_free_rank': h4_rank,
            'limitation': 'Finite chain certificate checked. The manuscript supplies the torus-core identification and transfer to H4(K;Z).'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.certificate.read_text()))
    text = json.dumps(report, indent=2)+'\n'
    if args.output:
        if args.output.exists():
            raise SystemExit('Output already exists; choose a fresh path')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text)
