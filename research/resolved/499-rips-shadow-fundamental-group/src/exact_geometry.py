"""Exact arithmetic checks for the six-point Rips shadow counterexample.

The mathematical homotopies are proved in the accompanying manuscript.
This module checks the finite geometry, simplices, and vertex retraction.
It uses only Python's standard library.
"""
from fractions import Fraction
from itertools import combinations
import json


def points(dimension=3, scale=Fraction(1)):
    if not isinstance(dimension, int) or dimension < 3:
        raise ValueError("dimension must be an integer at least three")
    scale = Fraction(scale)
    if scale <= 0:
        raise ValueError("scale must be positive")
    a, b, s = Fraction(9, 20), Fraction(501, 1000), Fraction(309, 1000)
    xyz = [(a, s, 0), (a, -s, 0), (-b, 0, 0), (b, 0, 0), (-a, 0, s), (-a, 0, -s)]
    return [tuple(scale * c for c in v) + (Fraction(0),) * (dimension - 3) for v in xyz]


def squared_distance(a, b):
    if len(a) != len(b):
        raise ValueError("point dimensions differ")
    return sum((x - y) ** 2 for x, y in zip(a, b))


def rips_faces(sample, scale):
    scale = Fraction(scale)
    if scale <= 0:
        raise ValueError("scale must be positive")
    return [f for size in range(1, len(sample) + 1) for f in combinations(range(len(sample)), size)
            if all(squared_distance(sample[i], sample[j]) < scale * scale for i, j in combinations(f, 2))]


def verify(dimension=3, scale=Fraction(1)):
    sample = points(dimension, scale)
    scale = Fraction(scale)
    faces = rips_faces(sample, scale)
    maximal = [f for f in faces if not any(set(f) < set(g) for g in faces)]
    expected = [(0, 1, 2), (0, 1, 3), (2, 4, 5), (3, 4, 5)]
    if maximal != expected:
        raise AssertionError("unexpected maximal simplex list")
    retraction = {0: 0, 1: 0, 2: 2, 3: 3, 4: 4, 5: 4}
    core = {(0, 2), (0, 3), (2, 4), (3, 4)}
    for face in faces:
        image = tuple(sorted({retraction[v] for v in face}))
        assert image in faces
        assert len(image) == 1 or image in core
        assert any(set(face) | set(image) <= set(f) for f in maximal)
    assert all(retraction[v] == v for v in [0, 2, 3, 4])

    # An independent integer cocycle detects the displayed cycle.
    cocycle = {(0, 2): -1, (1, 2): -1}
    def value(i, j):
        return cocycle.get((i, j), 0) if i < j else -cocycle.get((j, i), 0)
    for i, j, k in [f for f in faces if len(f) == 3]:
        assert value(i, j) + value(j, k) + value(k, i) == 0
    loop = [2, 0, 3, 4, 2]
    assert sum(value(i, j) for i, j in zip(loop, loop[1:])) == 1
    report = {"dimension": dimension, "scale": str(scale),
              "normalized_squared_distances": {f"{i}-{j}": str(squared_distance(sample[i], sample[j]) / (scale * scale))
                                                 for i, j in combinations(range(6), 2)},
              "maximal_simplices": [list(f) for f in maximal], "four_cycle": loop,
              "retraction_is_carried": True, "integer_cocycle_cycle_value": 1,
              "scope": "Exact finite arithmetic and simplicial checks; the homotopy proof is in the manuscript."}
    return report


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2))
