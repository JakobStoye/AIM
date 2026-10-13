"""Exact rational checks for the polynomial profiles in Lemma 3."""
if not __debug__:
    raise RuntimeError("Run this check without Python optimization flags.")

from fractions import Fraction as F
import json


def add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for p in (a, b):
        for i, c in enumerate(p):
            out[i] += c
    return out


def scale(a, c):
    return [c * x for x in a]


def derivative(a):
    return [i * a[i] for i in range(1, len(a))] or [F(0)]


def multiply(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power(a, n):
    out = [F(1)]
    for _ in range(n):
        out = multiply(out, a)
    return out


def integral(a):
    return sum((c / (i + 1) for i, c in enumerate(a)), F(0))


def value(a, x):
    out = F(0)
    for c in reversed(a):
        out = out * x + c
    return out


def solve(a, b):
    aug = [list(row) + [rhs] for row, rhs in zip(a, b)]
    n = len(b)
    for i in range(n):
        pivot = next(j for j in range(i, n) if aug[j][i])
        aug[i], aug[pivot] = aug[pivot], aug[i]
        div = aug[i][i]
        aug[i] = [x / div for x in aug[i]]
        for j in range(n):
            if j != i:
                aug[j] = [x - aug[j][i] * y for x, y in zip(aug[j], aug[i])]
    return [row[-1] for row in aug]


endpoint_jet = [F(1), F(3, 4), F(-3, 16)]
matching_matrix = [[F(1), F(1), F(1)], [F(3), F(4), F(5)], [F(6), F(12), F(20)]]
h = [F(0)] * 3 + solve(matching_matrix, endpoint_jet)
k = endpoint_jet[:2] + [endpoint_jet[2] / 2]
rhs = [-value(k, F(1)), -value(derivative(k), F(1)), -value(derivative(derivative(k)), F(1))]
k += solve(matching_matrix, rhs)

for patch, left, right in ((h, [F(0)] * 3, endpoint_jet), (k, endpoint_jet, [F(0)] * 3)):
    for order in range(3):
        d = patch
        for _ in range(order):
            d = derivative(d)
        assert value(d, F(0)) == left[order]
        assert value(d, F(1)) == right[order]


def moments(p):
    dp = derivative(p)
    ddp = derivative(dp)
    q = add(multiply(p, ddp), scale(power(dp, 2), F(1, 3)))
    A = integral(power(dp, 4))
    E = integral(power(q, 2))
    H = integral(power(multiply(p, ddp), 2))
    boundary = value(p, F(1)) * value(dp, F(1))**3 - value(p, F(0)) * value(dp, F(0))**3
    assert E == H - A / 9 + F(2, 9) * boundary
    return {"A": A, "E": E, "H": H, "boundary": boundary}


mh, mk = moments(h), moments(k)
assert mh['boundary'] + mk['boundary'] == 0
E0 = mh['E'] + mk['E']
A0 = mh['A'] + mk['A']
assert E0 > 0 and A0 > 0
assert mh['H'] + mk['H'] - A0 / 9 == E0
alpha = F(3, 4)
assert alpha * (alpha - 1) + alpha**2 / 3 == 0
central_A_coefficient = alpha**4
central_H_coefficient = (alpha * (alpha - 1))**2
assert central_H_coefficient / central_A_coefficient == F(1, 9)
result = {
    "arithmetic": "exact rational", "assertions_passed": True,
    "lower_h_coefficients_ascending": [str(c) for c in h],
    "upper_k_coefficients_ascending": [str(c) for c in k],
    "lower_moments": {name: str(v) for name, v in mh.items()},
    "upper_moments": {name: str(v) for name, v in mk.items()},
    "E0": str(E0), "A0": str(A0),
    "central_A_log_coefficient": str(central_A_coefficient),
    "identity": "A_epsilon = A0 + (81/256) log(c/epsilon); E_epsilon = E0",
    "verification_scope": "Polynomial endpoint jets and rational moments only; the full theorem is proved analytically in the paper"
}
print(json.dumps(result, indent=2))
