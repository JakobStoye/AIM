"""Exact half-integral polygon invariants for bounded research checks.

Vertices are integer pairs describing Q=2P. Arithmetic uses Python integers.
No floating convex hull or tolerance is used.
"""
from math import gcd

def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def hull(points):
    points = sorted(set(map(tuple, points)))
    if len(points) < 3:
        return tuple(points)
    lower, upper = ([], [])
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return tuple(lower[:-1] + upper[:-1])

def edges(vertices):
    return zip(vertices, vertices[1:] + vertices[:1])

def area8(vertices):
    """Return 8*area(P)=2*area(Q) by the integer shoelace identity."""
    return sum((a[0] * b[1] - a[1] * b[0] for a, b in edges(vertices)))

def boundary_counts(vertices):
    """Count boundary Z^2 points of P and of Q using primitive edge steps."""
    coarse, fine = (0, 0)
    for a, b in edges(vertices):
        dx, dy = (b[0] - a[0], b[1] - a[1])
        g = gcd(abs(dx), abs(dy))
        if not g > 0:
            raise ValueError('Input or exact invariant check failed')
        fine += g
        step = (dx // g, dy // g)
        for parity in (0, 1):
            if (a[0] + parity * step[0]) % 2 == 0 and (a[1] + parity * step[1]) % 2 == 0:
                coarse += (g + 1 - parity) // 2
    return (coarse, fine)

def ceil_div(n, d):
    return -(-n // d)

def row_count(vertices, strict=False):
    """Count even-even points of Q by exact half-plane intersection on rows."""
    xmin, xmax = (min((p[0] for p in vertices)), max((p[0] for p in vertices)))
    ymin, ymax = (min((p[1] for p in vertices)), max((p[1] for p in vertices)))
    total = 0
    for y in range(ceil_div(ymin, 2), ymax // 2 + 1):
        lo, hi = (ceil_div(xmin, 2), xmax // 2)
        for a, b in edges(vertices):
            dx, dy = (b[0] - a[0], b[1] - a[1])
            constant = dx * (2 * y - a[1]) + dy * a[0]
            if dy > 0:
                hi = min(hi, (constant - 1 if strict else constant) // (2 * dy))
            elif dy < 0:
                bound = constant // (2 * dy) + 1 if strict else ceil_div(constant, 2 * dy)
                lo = max(lo, bound)
            elif constant < 0 or (strict and constant == 0):
                lo, hi = (1, 0)
                break
        total += max(0, hi - lo + 1)
    return total

def brute_counts(vertices):
    """Slow independent bounding-box enumeration for verifier controls."""
    xmin, xmax = (min((p[0] for p in vertices)), max((p[0] for p in vertices)))
    ymin, ymax = (min((p[1] for p in vertices)), max((p[1] for p in vertices)))
    interior, boundary = ([], [])
    for x in range(ceil_div(xmin, 2), xmax // 2 + 1):
        for y in range(ceil_div(ymin, 2), ymax // 2 + 1):
            determinants = [cross(a, b, (2 * x, 2 * y)) for a, b in edges(vertices)]
            if all((v >= 0 for v in determinants)):
                (interior if all((v > 0 for v in determinants)) else boundary).append((x, y))
    return (interior, boundary)

def invariants(points):
    vertices = hull(points)
    if not (len(vertices) >= 3 and area8(vertices) > 0):
        raise ValueError('Input or exact invariant check failed')
    i = row_count(vertices, strict=True)
    b, B = boundary_counts(vertices)
    if not row_count(vertices) == i + b:
        raise ValueError('Input or exact invariant check failed')
    A = area8(vertices)
    if not (A - B) % 2 == 0:
        raise ValueError('Input or exact invariant check failed')
    return (i, b, A, B)

def thin_strip(i, A):
    if not (i >= 2 and 4 * i + 4 <= A <= 8 * i + 8):
        raise ValueError('Input or exact invariant check failed')
    n = A - 4 * i - 4
    r2, s2 = (n // 2, (n + 1) // 2)
    return hull([(0, -1), (s2, -1), (2 * i + 2, 0), (r2, 1), (0, 1)])

def in_candidate(i, b, A, B):
    """Membership in the attained signature set C_i without enumerating it."""
    if i < 2 or b < 2:
        return False
    if b == 2 and 4 * i + 4 <= A <= 8 * i + 8 and (B == A - 4 * i):
        return True
    if 2 <= b <= 2 * i + 2:
        defect = 12 * i + 2 * b + 8 - A
        max_defect = 2 if b <= 2 * i - 2 else 1 if b <= 2 * i else 0
        if 0 <= defect <= max_defect and B == 2 * b + 4 + defect:
            return True
    if not 2 <= b <= 3 * i + 6:
        return False
    maximum = 12 * i + 2 * b + (8 if b <= 3 * i + 4 else 7 if b == 3 * i + 5 else 6)
    lower = 2 * b + A % 2
    if A == 12 * i + 2 * b + 8 and b != 2 * i + 4 or (b == 2 and A == 12 * i + 10):
        lower += 2
    return 6 * i + 4 * b - 6 <= A <= maximum and (A - B) % 2 == 0 and (lower <= B <= min(A - 6 * i - 2 * b + 6, 3 * i + b + 6, 12 * i + 4 * b + 10 - A))
