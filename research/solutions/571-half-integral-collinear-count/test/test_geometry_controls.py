"""Independent integer-geometry controls for the exact chain count.

The geometric enumeration does not use the model generator's constraints or
Normaliz. It constructs vertex sets, computes their convex hulls and interior
even-lattice points, and compares finite shear/reflection orbits independently.
"""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from chain_models import models, series_coefficients


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) < 3:
        return tuple(points)
    lower, upper = [], []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return tuple(lower[:-1] + upper[:-1])


def interior_even_points(poly):
    if len(poly) < 3:
        return set()
    xlo, xhi = min(x for x, y in poly), max(x for x, y in poly)
    ylo, yhi = min(y for x, y in poly), max(y for x, y in poly)
    return {(x, y) for x in range(xlo, xhi+1) if x % 2 == 0
            for y in range(ylo, yhi+1) if y % 2 == 0
            if all(cross(poly[j], poly[(j+1) % len(poly)], (x, y)) > 0
                   for j in range(len(poly)))}


def normalize_shear(poly):
    # In the CCW hull, its left boundary is traversed downwards.
    edge = next((p, q) for p, q in zip(poly, poly[1:]+poly[:1]) if p[1] > 0 >= q[1])
    p, q = edge
    slope = Fraction(p[0]-q[0], p[1]-q[1])
    shear = -(slope.numerator // slope.denominator)
    return hull((x+shear*y, y) for x, y in poly)


def transformed(poly, n, action):
    if action == "identity":
        return poly
    if action == "H":
        points = ((2*n-x, y) for x, y in poly)
    elif action == "V":
        points = ((x, -y) for x, y in poly)
    elif action == "HV":
        points = ((2*n-x, -y) for x, y in poly)
    else:
        raise ValueError(action)
    return normalize_shear(hull(points))


def boundary_data(poly, n):
    a = -min(y for x, y in poly)
    b = max(y for x, y in poly)
    f, g = {}, {}
    for y in (-a, b):
        xs = [x for x, h in poly if h == y]
        f[y], g[y] = min(xs), 2*n-max(xs)
    for j, (x, y) in enumerate(poly):
        if -a < y < b:
            prev, following = poly[j-1], poly[(j+1) % len(poly)]
            if prev[1] > y > following[1]:
                f[y] = x
            elif prev[1] < y < following[1]:
                g[y] = 2*n-x
            else:
                raise AssertionError("An intermediate horizontal extreme face is invalid.")
    return a, b, f, g


def enumerate_geometry(n, height, integral=False):
    """Fixed finite control: extrema +/-height, optional zero-height vertices."""
    # The proven linear coordinate bounds make this a nonadaptive finite check.
    step = 2 if integral else 1
    right_values = list(range(-4*n-4, 2*n+3, step))
    left_candidates = []
    for bottom, top in product(range(-2, 3, step), repeat=2):
        if 0 <= Fraction(bottom+top, 2) < 2 and 0 <= Fraction(top-bottom, 2*height) < 1:
            left_candidates.append([(bottom, -height), (top, height)])
    for middle in range(0, 2, step):
        for top in range(middle, middle+height, step):
            for bottom in range(-2, 6*n+5, step):
                left_candidates.append([(bottom, -height), (middle, 0), (top, height)])
    right_candidates = []
    for bottom, top in product(right_values, repeat=2):
        right_candidates.append([(2*n-bottom, -height), (2*n-top, height)])
        for middle in range(0, 2, step):
            right_candidates.append([(2*n-bottom, -height), (2*n-middle, 0), (2*n-top, height)])
    expected = {(2*j, 0) for j in range(1, n)}
    result = set()
    for left in left_candidates:
        for right in right_candidates:
            if left[0][0] > right[0][0] or left[-1][0] > right[-1][0]:
                continue
            points = set(left+right)
            poly = hull(points)
            if len(poly) < 3 or set(poly) != points:
                continue
            if interior_even_points(poly) != expected:
                continue
            assert normalize_shear(poly) == poly
            result.add(poly)
    return result


def orbit_counts(polygons, n):
    fixed = {action: 0 for action in ["H", "V", "HV"]}
    classes = set()
    for poly in polygons:
        orbit = [transformed(poly, n, action) for action in ["identity", "H", "V", "HV"]]
        for action, image in zip(["H", "V", "HV"], orbit[1:]):
            assert image in polygons
            fixed[action] += image == poly
        classes.add(min(orbit))
    assert (len(polygons)+sum(fixed.values())) % 4 == 0
    assert len(classes) == (len(polygons)+sum(fixed.values())) // 4
    return {"identity": len(polygons), **fixed, "orbits": len(classes)}


class GeometryControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.n = 4
        cls.thin = enumerate_geometry(cls.n, 1)
        cls.integral = enumerate_geometry(cls.n, 2, integral=True)
        cls.model_index = {}
        for model in models("identity"):
            key = (model["a"], model["b"], tuple(model["left_heights"]), tuple(model["right_heights"]),
                   tuple(sorted(model["fixed_left"].items())))
            assert key not in cls.model_index
            cls.model_index[key] = model

    def test_thin_geometry_and_fixed_points_match_rational_series(self):
        counts = orbit_counts(self.thin, self.n)
        for action in ["identity", "H", "V", "HV"]:
            data = json.loads((ROOT / "numerical_case/exact_series.json").read_text())
            cell_models = list(models(action))
            actual = sum(series_coefficients(group["series"], self.n)[self.n]
                         for group in data["groups"] for member in group["members"]
                         if member["action"] == action
                         and cell_models[member["index"]]["a"]
                         == cell_models[member["index"]]["b"] == 1)
            self.assertEqual(counts[action], actual, action)

    def test_integral_benchmark_and_model_inclusion(self):
        # Published Bohnert-Springer paragraph before Conjecture 3.7 reports
        # Koelman's count (i+3)(2i^2+15i+16)/6: at i=3 it is 79.
        counts = orbit_counts(self.integral, self.n)
        self.assertEqual(counts["orbits"], 79)
        for poly in self.integral:
            self.assertTrue(all(x % 2 == y % 2 == 0 for x, y in poly))
            a, b, f, g = boundary_data(poly, self.n)
            heights = tuple(sorted(f))
            u, v = next((u, v) for u, v in zip(heights, heights[1:]) if u <= 0 < v)
            key = (a, b, heights, tuple(sorted(g)), tuple(sorted([(u, f[u]), (v, f[v])])))
            self.assertIn(key, self.model_index)
            model = self.model_index[key]
            values = [self.n if name == "n" else (f if name.startswith("l") else g)[int(name.split("_")[1])]
                      for name in model["variables"]] + [1]
            self.assertTrue(all(sum(a*b for a, b in zip(row, values)) >= 0
                                for row in model["inhom_inequalities"]))

    def test_shear_group_and_point_extrema(self):
        diamond = hull([(0,0), (4,-2), (8,0), (4,2)])
        expected = {(2,0), (4,0), (6,0)}
        self.assertEqual(interior_even_points(diamond), expected)
        normal = normalize_shear(diamond)
        for s in [-7, -1, 0, 3, 8]:
            self.assertEqual(normalize_shear(hull((x+s*y, y) for x, y in diamond)), normal)
        for poly in [normal, *list(self.integral)[:5]]:
            for action in ["H", "V", "HV"]:
                self.assertEqual(transformed(transformed(poly, self.n, action), self.n, action), poly)
            self.assertEqual(transformed(transformed(poly, self.n, "H"), self.n, "V"),
                             transformed(transformed(poly, self.n, "V"), self.n, "H"))

    def test_half_translation_is_not_admitted(self):
        first = hull([(0,-2), (7,-2), (7,2), (2,2), (0,0)])
        second = hull((x+1, y) for x, y in first)
        expected = {(2,0), (4,0), (6,0)}
        self.assertEqual(interior_even_points(first), expected)
        self.assertEqual(interior_even_points(second), expected)
        first, second = normalize_shear(first), normalize_shear(second)
        orbit = {transformed(first, self.n, action) for action in ["identity", "H", "V", "HV"]}
        self.assertNotIn(second, orbit)


if __name__ == "__main__":
    unittest.main(verbosity=2)
