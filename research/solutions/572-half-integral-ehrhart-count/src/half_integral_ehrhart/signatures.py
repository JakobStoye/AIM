"""The attained integer signatures and exact integer-vertex witnesses."""
from .geometry import hull, thin_strip, in_candidate
from .body import body_polygon
from .top import top_polygon


def _integer(value, name):
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")


def _interior(i):
    _integer(i, "i")
    if i < 2:
        raise ValueError("The signature theorem requires i >= 2")


def signature_parts(i):
    """Return the disjoint body, top and line sets at fixed i >= 2."""
    _interior(i)
    body, top, line = set(), set(), set()
    for b in range(2, 3*i+7):
        q = 8 if b <= 3*i+4 else 7 if b == 3*i+5 else 6
        for A in range(6*i+4*b-6, 12*i+2*b+q+1):
            lower = 2*b+(A % 2)
            if ((A == 12*i+2*b+8 and b != 2*i+4)
                    or (b == 2 and A == 12*i+10)):
                lower += 2
            upper = min(A-6*i-2*b+6, 3*i+b+6, 12*i+4*b+10-A)
            for B in range(lower, upper+1, 2):
                body.add((A, b, B))
    for d in range(3):
        for b in range(2, 2*i+3-2*d):
            top.add((12*i+2*b+8-d, b, 2*b+4+d))
    for A in range(4*i+4, 8*i+9):
        line.add((A, 2, A-4*i))
    return body, top, line


def signatures(i):
    """Return C_i; enumerating it has output size of order i**3."""
    body, top, line = signature_parts(i)
    return body | top | line


def signature_count(i):
    _interior(i)
    return (9*i**3+72*i**2+175*i+106)//2


def _checked_signature(i, signature):
    _interior(i)
    if len(signature) != 3:
        raise ValueError("A signature is (A, b, B)")
    A, b, B = signature
    for x, name in zip(signature, ("A", "b", "B")):
        _integer(x, name)
    if not in_candidate(i, b, A, B):
        raise ValueError("Signature is outside the attained set C_i")
    return A, b, B


def witness(i, signature):
    """Return counterclockwise integer vertices of Q=2P for the signature."""
    A, b, B = _checked_signature(i, signature)
    if b == 2 and B == A-4*i and 4*i+4 <= A <= 8*i+8:
        return thin_strip(i, A)
    d = 12*i+2*b+8-A
    if d in (0, 1, 2) and B == 2*b+4+d and b+2*d <= 2*i+2:
        return top_polygon(i, b, d)
    e = A % 2
    j = (A-6*i-4*b+6-e)//2
    k = (B-2*b-e)//2
    return body_polygon(i, b, j, k, e)


def ehrhart_value(i, signature, t):
    """Evaluate the entire Ehrhart function exactly at integer t >= 0."""
    A, b, B = _checked_signature(i, signature)
    _integer(t, "t")
    if t < 0:
        raise ValueError("The point-count domain is t >= 0")
    numerator = (A*t*t+4*b*t+8*i+4*b-A if t % 2
                 else A*t*t+2*B*t+8)
    if numerator % 8:
        raise ValueError("Nonintegral constituent value")
    return numerator//8


def has_period_collapse(i, signature):
    A, b, B = _checked_signature(i, signature)
    return B == 2*b and A == 8*i+4*b-8
