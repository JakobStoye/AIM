"""Uniform body witnesses; integer vertices of Q=2P."""
from .geometry import hull

def bulk(i, b, j, k, e):
    m = 3 * i - b + 6
    if not (b >= 3 and j >= k and (j + k <= m) and (e in (0, 1))):
        raise ValueError('Input or exact invariant check failed')
    if e == 1 and j == k:
        if not 2 * k + 1 <= m:
            raise ValueError('Input or exact invariant check failed')
        return hull([(0, 1), (2 * k + 1, 1), (2 * i + 2, 0), (2 * b - 6, -2), (0, -2)])
    if not 2 * (j - k) >= e:
        raise ValueError('Input or exact invariant check failed')
    return hull([(0, 1), (2 * k, 1), (2 * i + 2, 0), (i + b - 2 + j - k, -1), (2 * b - 6 + e, -2), (0, -2)])

def outer_two(i, b, j, k, e):
    m = 3 * i - b + 6
    if not (i >= 2 and b >= 2 and (e in (0, 1)) and (k >= 1)):
        raise ValueError('Input or exact invariant check failed')
    if not (j + k + e == m + 2 and 2 * k + e <= m):
        raise ValueError('Input or exact invariant check failed')
    f = 2 * k + e - 2
    return hull([(0, 1), (f, 1), (4 * i + 4 - f, -1), (2 * b - 3, -2), (1, -2), (0, -1)])

def outer_one(i, b, j, k, e):
    m = 3 * i - b + 6
    if not (i >= 2 and b >= 2 and (e in (0, 1)) and (j + k + e == m + 1)):
        raise ValueError('Input or exact invariant check failed')
    if e == 0 and k == 0:
        if not b == 2 * i + 4:
            raise ValueError('Input or exact invariant check failed')
        return hull([(-1, -2), (4 * i + 3, -2), (1, 2)])
    if b >= 3:
        f = 2 * k + e - 1
        if not (f >= 0 and 2 * k + e <= m):
            raise ValueError('Input or exact invariant check failed')
        return hull([(0, 1), (f, 1), (4 * i + 4 - f, -1), (2 * b - 5, -2), (0, -2)])
    if 2 * k + e == m:
        return hull([(0, 1), (3 * i, 1), (3, -2), (1, -2), (0, -1)])
    if e == 1 and k == 0:
        return b2_high_difference(i, j, k, e)
    f = 2 * k + e - 2
    if not (f >= 0 and 2 * k + e <= m - 1):
        raise ValueError('Input or exact invariant check failed')
    return hull([(0, 1), (f, 1), (4 * i + 3 - f, -1), (1, -2), (0, -2)])

def b2_high_difference(i, j, k, e):
    m = 3 * i + 4
    if not (i >= 2 and e in (0, 1) and (j - k >= 2) and (j + k + e <= m + 1)):
        raise ValueError('Input or exact invariant check failed')
    f = 2 * k + e - 1
    if not f >= 0:
        raise ValueError('Input or exact invariant check failed')
    return hull([(0, 1), (f, 1), (2 * i + 2, 0), (i + j - k, -1), (1, -2), (0, 0)])

def b2_low_difference(i, j, k, e):
    delta = j - k
    t = 2 * k + e
    if not (i >= 2 and delta in (0, 1) and (e in (0, 1)) and (t <= 3 * i + 4)):
        raise ValueError('Input or exact invariant check failed')
    if t <= 3 * i + 1 + delta:
        d = 6 * i + 2 + 2 * delta - 2 * t
        return hull([(0, 0), (0, 1), (t, 1), (d, -2)])
    if delta == 0:
        shaved = 3 * i + 4 - t
        if not shaved in (0, 1, 2):
            raise ValueError('Input or exact invariant check failed')
        points = [(7, -2), (3, -2)]
        if shaved >= 1:
            points.extend([(1, 0), (1, 1)])
        else:
            points.append((0, 1))
        if shaved == 2:
            points.extend([(3 * i - 3, 1), (2 * i + 1, 0)])
        else:
            points.append((3 * i - 2, 1))
        return hull(points)
    if not t in (3 * i + 3, 3 * i + 4):
        raise ValueError('Input or exact invariant check failed')
    if t == 3 * i + 4:
        return hull([(0, 1), (3 * i, 1), (3, -2), (1, -2), (0, -1)])
    return hull([(0, 1), (3 * i - 1, 1), (2 * i + 1, 0), (3, -2), (1, -2), (0, -1)])

def b2_minimum_fine_boundary(i, j):
    if not (i >= 2 and 0 <= j <= 3 * i + 3):
        raise ValueError('Input or exact invariant check failed')
    h = 3 * i + 1 if j == 0 else 3 * i + 2
    upper = 0 if j == 0 else j - 1
    return hull([(0, 0), (1, upper), (2, 0), (3, -h)])

def body_polygon(i, b, j, k, e):
    m = 3 * i - b + 6
    layer = j + k + e - m
    if layer == 2:
        return outer_two(i, b, j, k, e)
    if layer == 1:
        return outer_one(i, b, j, k, e)
    if b >= 3:
        return bulk(i, b, j, k, e)
    if e == 0 and k == 0:
        return b2_minimum_fine_boundary(i, j)
    if j - k <= 1:
        return b2_low_difference(i, j, k, e)
    return b2_high_difference(i, j, k, e)
