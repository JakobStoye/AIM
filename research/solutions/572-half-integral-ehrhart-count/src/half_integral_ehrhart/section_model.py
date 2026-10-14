"""Exact necessary linear inequalities for half-integral polygon sections.

This is a relaxation, not a polygon feasibility model. All arithmetic in the
definition is rational; the proof note justifies every inequality geometrically.
"""
from fractions import Fraction as F

def model(pattern, n):
    if not (pattern in ('EE', 'EO', 'OO') and 2 <= n <= 8):
        raise ValueError('Input or exact invariant check failed')
    W = {'EE': 2 * n + 2, 'EO': 2 * n + 1, 'OO': 2 * n}[pattern]
    coarse = list(range(1 if pattern == 'OO' else 2, W, 2))
    ends = {'EE': [0, W], 'EO': [0], 'OO': []}[pattern]
    bcols = sorted(coarse + ends)
    names = [f'length_{j}' for j in range(W + 1)] + [f'fine_closed_{j}' for j in range(W + 1)] + [f'coarse_interior_{j}' for j in coarse] + [f'coarse_boundary_{j}' for j in bcols]
    ids = {name: k for k, name in enumerate(names)}
    rows, rhs, labels = ([], [], [])

    def add(label, coeffs, bound):
        row = [F(0)] * len(names)
        for name, value in coeffs.items():
            row[ids[name]] = F(value)
        rows.append(row)
        rhs.append(F(bound))
        labels.append(label)
    for j in range(W + 1):
        add(f'closed_length_{j}', {f'fine_closed_{j}': 1, f'length_{j}': -1}, 1)
    for j in range(1, W):
        add(f'concavity_{j}', {f'length_{j - 1}': 1, f'length_{j}': -2, f'length_{j + 1}': 1}, 0)
        add(f'minimum_width_{j}', {f'length_{j}': -1}, -min(F(W, 2), F(j), F(W - j)))
    for j in coarse:
        add(f'coarse_length_upper_{j}', {f'length_{j}': 1, f'coarse_interior_{j}': -2}, 2)
        add(f'coarse_length_lower_{j}', {f'length_{j}': -1, f'coarse_interior_{j}': 2}, 2)
        add(f'coarse_fine_closed_{j}', {f'fine_closed_{j}': 1, f'coarse_interior_{j}': -2, f'coarse_boundary_{j}': -1}, 1)
    for j in ends:
        add(f'end_length_{j}', {f'length_{j}': 1, f'coarse_boundary_{j}': -2}, 0)
        add(f'end_closed_{j}', {f'fine_closed_{j}': 1, f'coarse_boundary_{j}': -2}, 1)
    add('total_i_at_least_17', {f'coarse_interior_{j}': -1 for j in coarse}, -17)
    for j in coarse:
        add(f'interior_boundary_upper_{j}', {f'coarse_boundary_{j}': 1}, 2)
    objective = [F(0)] * len(names)
    for j in range(W + 1):
        objective[ids[f'fine_closed_{j}']] = 1
    for j in coarse:
        objective[ids[f'coarse_interior_{j}']] = -6
    for j in bcols:
        objective[ids[f'coarse_boundary_{j}']] = -2
    return {'pattern': pattern, 'n': n, 'W': W, 'names': names, 'labels': labels, 'A': rows, 'rhs': rhs, 'objective': objective}
