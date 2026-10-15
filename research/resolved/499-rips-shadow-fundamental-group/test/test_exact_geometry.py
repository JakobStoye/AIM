from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from exact_geometry import points, squared_distance, rips_faces, verify


class ExactGeometryTests(unittest.TestCase):
    def test_all_pair_types_against_symbolic_formulas(self):
        a, b, s = F(9, 20), F(501, 1000), F(309, 1000)
        types = {
            4 * s * s: [(0, 1), (4, 5)],
            (a + b) ** 2 + s * s: [(0, 2), (1, 2), (3, 4), (3, 5)],
            (b - a) ** 2 + s * s: [(0, 3), (1, 3), (2, 4), (2, 5)],
            4 * a * a + 2 * s * s: [(0, 4), (0, 5), (1, 4), (1, 5)],
            4 * b * b: [(2, 3)],
        }
        sample = points()
        expected = {pair: value for value, pairs in types.items() for pair in pairs}
        self.assertEqual(len(expected), 15)
        self.assertEqual({p: squared_distance(sample[p[0]], sample[p[1]]) for p in combinations(range(6), 2)}, expected)
        self.assertTrue(all(value != 1 for value in expected.values()))

    def test_strict_boundary_convention(self):
        sample = [(F(0),), (F(1),)]
        self.assertNotIn((0, 1), rips_faces(sample, F(1)))
        self.assertIn((0, 1), rips_faces(sample, F(101, 100)))

    def test_scaling_padding_and_retraction(self):
        baseline = verify()
        transformed = verify(9, F(7, 3))
        self.assertEqual(transformed["normalized_squared_distances"], baseline["normalized_squared_distances"])
        self.assertEqual(transformed["maximal_simplices"], baseline["maximal_simplices"])
        self.assertTrue(transformed["retraction_is_carried"])
        self.assertEqual(transformed["integer_cocycle_cycle_value"], 1)


if __name__ == "__main__":
    unittest.main()
