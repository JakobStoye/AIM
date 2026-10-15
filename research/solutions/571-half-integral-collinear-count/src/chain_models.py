"""Exact five-row polygon encodings and Burnside polyhedra.

Coordinates encode Q=2P. Both left coordinates f(y) and right distances
g(y)=2n-x_right(y) are convex functions. Integer translations of P remain
even translations of Q. All matrices use coefficients followed by a constant.
The accompanying manuscript proves the geometric and fixed-class correspondence.
"""
from fractions import Fraction
from itertools import combinations


def height_sets(a, b):
    interior = list(range(-a + 1, b))
    for k in range(len(interior) + 1):
        for middle in combinations(interior, k):
            yield (-a, *middle, b)


def center_edge(heights):
    return next((u, v) for u, v in zip(heights, heights[1:]) if u <= 0 < v)


def gauge_pairs(heights):
    u, v = center_edge(heights)
    d = v - u
    for delta in range(d):
        for x in range(-2, 3):
            intercept = d * x - u * delta
            if 0 <= intercept < 2 * d:
                yield {u: x, v: x + delta}


def add(*vectors):
    return [sum(items) for items in zip(*vectors)]


def scale(c, vector):
    return [c * x for x in vector]


def make_model(a, b, left_heights, right_heights, fixed_left, action):
    """Return one integer polyhedron for identity, H, V, or HV fixed classes."""
    names = [f"l_{y}" for y in left_heights if y not in fixed_left]
    if action in ("identity", "V"):
        names.extend(f"r_{y}" for y in right_heights)
    if action in ("H", "V"):
        names.append("m")
    names.append("n")
    dim = len(names)

    def variable(name):
        row = [0] * (dim + 1)
        row[names.index(name)] = 1
        return row

    def constant(value):
        row = [0] * (dim + 1)
        row[-1] = value
        return row

    f = {y: constant(fixed_left[y]) if y in fixed_left else variable(f"l_{y}")
         for y in left_heights}
    n = variable("n")
    m = variable("m") if action in ("H", "V") else None
    if action == "H":
        g = {y: add(f[y], scale(y, m)) for y in right_heights}
    elif action == "HV":
        g = {y: f[-y] for y in right_heights}
    else:
        g = {y: variable(f"r_{y}") for y in right_heights}

    inequalities = [add(n, constant(-4))]
    equations = []
    for heights, coords in ((left_heights, f), (right_heights, g)):
        for u, v, w in zip(heights, heights[1:], heights[2:]):
            # Strict convexity; the cross-multiplied integer expression is >=1.
            inequalities.append(add(scale(w - v, coords[u]),
                                    scale(-(w - u), coords[v]),
                                    scale(v - u, coords[w]), constant(-1)))
        u, v = center_edge(heights)
        numerator = add(scale(v, coords[u]), scale(-u, coords[v]))
        inequalities.extend([numerator,
                             add(scale(-1, numerator), constant(2 * (v - u) - 1))])
    for y in (-a, b):
        inequalities.append(add(scale(2, n), scale(-1, f[y]), scale(-1, g[y])))

    if action == "V":
        for heights, coords, sign in ((left_heights, f, -1), (right_heights, g, 1)):
            for y in heights:
                if y > 0:
                    equations.append(add(coords[-y], scale(-1, coords[y]), scale(sign * y, m)))

    # Remove duplicate and identically satisfied rows; retain infeasible rows.
    inequalities = sorted(set(tuple(row) for row in inequalities
                              if any(row[:-1]) or row[-1] < 0))
    equations = sorted(set(tuple(row) for row in equations if any(row)))
    return {"a": a, "b": b, "left_heights": list(left_heights),
            "right_heights": list(right_heights), "fixed_left": fixed_left,
            "action": action, "variables": names,
            "inhom_inequalities": [list(row) for row in inequalities],
            "inhom_equations": [list(row) for row in equations],
            "grading": [[int(name == "n") for name in names]]}


def models(action="identity"):
    for a in (1, 2):
        for b in (1, 2):
            if action in ("V", "HV") and a != b:
                continue
            for left in height_sets(a, b):
                if action == "H":
                    rights = [left]
                elif action == "HV":
                    rights = [tuple(-y for y in reversed(left))]
                else:
                    rights = list(height_sets(a, b))
                if action == "V" and tuple(-y for y in reversed(left)) != left:
                    continue
                for right in rights:
                    if action == "V" and tuple(-y for y in reversed(right)) != right:
                        continue
                    for fixed in gauge_pairs(left):
                        yield make_model(a, b, left, right, fixed, action)


def series_coefficients(series, maximum):
    """Expand Normaliz [numerator, denominator exponents, shift] exactly."""
    numerator, degrees, shift = series
    coeffs = [0] * (maximum + 1)
    if shift <= maximum:
        for j, value in enumerate(numerator):
            if 0 <= j + shift <= maximum:
                coeffs[j + shift] += value
    for degree in degrees:
        assert degree > 0
        for j in range(degree, maximum + 1):
            coeffs[j] += coeffs[j - degree]
    return coeffs


def conjectured_count(i):
    value = (i + 1) * (512*i**6 + 12928*i**5 + 137740*i**4 + 685145*i**3
                      + 1582743*i**2 + 1665222*i + 710640)
    result = Fraction(value, 1260)
    assert result.denominator == 1
    return result.numerator
