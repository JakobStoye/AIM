"""Generate an exact signed-chain certificate for the fixed case n=13, r=5.

No third-party packages, floating-point ranks, or unbounded-parameter claims
are used. See the manuscript for the torus-core and chain-cancellation proofs.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations
import hashlib
import json

N = 13
RADIUS = 5


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                         separators=(',', ':')).encode('ascii')).hexdigest()


def signed_step(a, b):
    step = (b - a) % N
    return step if step <= N // 2 else step - N


def distance(a, b):
    return sum(abs(signed_step(a[j], b[j])) for j in range(2))


def liftable(simplex):
    anchor = simplex[0]
    lifted = [tuple(signed_step(anchor[j], v[j]) for j in range(2))
              for v in simplex]
    return all(sum(abs(a[j] - b[j]) for j in range(2)) <= RADIUS
               for a, b in combinations(lifted, 2))


def relative_basis():
    """Enumerate every nonliftable clique via an anchored winding triangle."""
    vertices = [(a, b) for a in range(N) for b in range(N)]
    origin = (0, 0)
    neighbors = [v for v in vertices if v != origin
                 and distance(origin, v) <= RADIUS]
    triangles = [(origin, a, b) for a, b in combinations(neighbors, 2)
                 if distance(a, b) <= RADIUS and not liftable((origin, a, b))]
    anchored = set()
    max_common = 0
    for triangle in triangles:
        candidates = [v for v in vertices if v not in triangle
                      and all(distance(v, t) <= RADIUS for t in triangle)]
        max_common = max(max_common, len(candidates))

        def extend(simplex, remaining):
            anchored.add(tuple(sorted(simplex)))
            for i, v in enumerate(remaining):
                extend(simplex + (v,), [w for w in remaining[i+1:]
                                       if distance(v, w) <= RADIUS])

        extend(triangle, candidates)
    result = defaultdict(set)
    for simplex in anchored:
        for a in range(N):
            for b in range(N):
                translated = tuple(sorted(((x+a) % N)*N+(y+b) % N
                                          for x, y in simplex))
                result[len(simplex)-1].add(translated)
    basis = {q: sorted(result[q]) for q in sorted(result)}
    metadata = {'origin_wrapping_triangles': len(triangles),
                'origin_nonliftable_cliques': len(anchored),
                'max_common_neighbors': max_common}
    return basis, metadata


def boundaries(basis):
    """Signed relative boundary; omitted faces belong to the torus core."""
    index = {q: {s: i for i, s in enumerate(ss)} for q, ss in basis.items()}
    result = {}
    for q, ss in basis.items():
        result[q] = {}
        for c, simplex in enumerate(ss):
            col = {}
            for j in range(len(simplex)):
                face = simplex[:j] + simplex[j+1:]
                if face in index.get(q-1, {}):
                    col[index[q-1][face]] = 1 if j % 2 == 0 else -1
            result[q][c] = col
    return result


def boundary_serialization(B):
    return {str(q): [[[r, value] for r, value in sorted(B[q][c].items())]
                    for c in sorted(B[q])] for q in sorted(B)}


def check_chain(B):
    for q, cols in B.items():
        if q-1 not in B:
            continue
        for col in cols.values():
            square = defaultdict(int)
            for r, coefficient in col.items():
                for row, value in B[q-1][r].items():
                    square[row] += coefficient * value
            if any(square.values()):
                raise ValueError('Signed boundary squared is nonzero')


def cancel_units(dimensions, initial):
    """Integral chain contraction using only pivots +1 and -1."""
    active = {q: set(range(d)) for q, d in dimensions.items()}
    B = {q: {c: dict(col) for c, col in cols.items()}
         for q, cols in initial.items()}
    trace = []
    for q in sorted(B, reverse=True):
        while True:
            selected = None
            for c, col in B[q].items():
                units = [r for r, value in col.items() if abs(value) == 1]
                if units:
                    selected = (min(units), c)
                    break
            if selected is None:
                break
            r, c = selected
            pivot = B[q][c]
            a = pivot[r]
            trace.append([q, r, c, a])
            for z, column in B[q].items():
                if z == c or r not in column:
                    continue
                factor = column[r] * a
                for i, value in pivot.items():
                    column[i] = column.get(i, 0) - factor * value
                    if not column[i]:
                        del column[i]
            del B[q][c]
            active[q].remove(c)
            active[q-1].remove(r)
            for col in B.get(q+1, {}).values():
                col.pop(c, None)
            B.get(q-1, {}).pop(r, None)
    return active, B, trace


def dense_boundary(B, active, q):
    rows = sorted(active.get(q-1, set()))
    columns = sorted(active.get(q, set()))
    return [[B[q][c].get(r, 0) for c in columns] for r in rows]


def rank_mod_prime(matrix, prime):
    """Exact sparse column elimination over the given prime field."""
    if not matrix:
        return 0
    pivots = {}
    for c in range(len(matrix[0])):
        v = {r: matrix[r][c] % prime for r in range(len(matrix))
             if matrix[r][c] % prime}
        while v:
            r = min(v)
            if r not in pivots:
                a = pow(v[r], -1, prime)
                pivots[r] = {i: a*x % prime for i, x in v.items()}
                break
            a = v[r]
            for i, x in pivots[r].items():
                v[i] = (v.get(i, 0) - a*x) % prime
                if not v[i]:
                    del v[i]
    return len(pivots)


def make_certificate():
    basis, metadata = relative_basis()
    B = boundaries(basis)
    check_chain(B)
    dimensions = {q: len(ss) for q, ss in basis.items()}
    active, residual, trace = cancel_units(dimensions, B)
    check_chain(residual)
    matrix = dense_boundary(residual, active, 4)
    nonzero_columns = sum(any(row[c] for row in matrix)
                          for c in range(len(matrix[0])))
    rank3 = rank_mod_prime(matrix, 3)
    if rank3 != nonzero_columns:
        raise ValueError('The minor lower bound does not close the rational rank')
    if any(col for q, cols in residual.items() if q != 4
           for col in cols.values()):
        raise ValueError('Unexpected nonzero residual differential')
    return {
        'schema_version': 1,
        'model': {'n': N, 'radius': RADIUS, 'k': 5, 'metric': 'periodic Manhattan',
                  'filtration': 'closed diameter <= radius',
                  'vertex_label': '13*a+b', 'orientation': 'increasing labels',
                  'basis_order': 'lexicographic within each degree'},
        'enumeration': metadata,
        'basis_sha256': canonical_hash({str(q): ss for q, ss in basis.items()}),
        'boundary_sha256': canonical_hash(boundary_serialization(B)),
        'chain_dimensions': {str(q): d for q, d in dimensions.items()},
        'unit_cancellation_trace': trace,
        'active_basis_indices': {str(q): sorted(ids) for q, ids in active.items()},
        'residual_chain_dimensions': {str(q): len(ids) for q, ids in active.items()},
        'residual_d4': matrix,
        'nonzero_d4_columns': nonzero_columns,
        'rank_d4_mod3': rank3,
        'rank_d4_Q': rank3,
        'relative_H4_free_rank': len(active[4]) - rank3,
        'rank_argument': 'Mod-3 rank gives a nonzero integral minor; nonzero column count gives the matching rational upper bound.'}
