"""Uniform exact realization of the width-two top Ehrhart signatures.

Vertices are those of Q=2P. The universal argument is in width2_top_lemma.md;
finite exact checks are regression controls, not a substitute for that argument.
"""
from .geometry import hull

def top_polygon(i, b, d):
    if not (i >= 2 and b >= 2 and (d in (0, 1, 2)) and (b + 2 * d <= 2 * i + 2)):
        raise ValueError('Input or exact invariant check failed')
    middle_boundary = 2 - d
    left_capacity = i if d == 0 else i - 1
    right_capacity = i if d <= 1 else i - 1
    outer = b - middle_boundary
    if not 0 <= outer <= left_capacity + right_capacity:
        raise ValueError('Input or exact invariant check failed')
    left = min(left_capacity, outer)
    right = outer - left
    lower_left = 1
    lower_right = 3 if d == 2 else 1
    lower_at_one = 0
    lower_at_three = 1 if d == 2 else 0
    upper_at_one = 2 * i + 2 if d == 0 else 2 * i + 1
    upper_at_three = 2 * i + 2
    return hull([(0, lower_left), (0, lower_left + 2 * left), (1, upper_at_one), (3, upper_at_three), (4, lower_right + 2 * right), (4, lower_right), (3, lower_at_three), (1, lower_at_one)])
