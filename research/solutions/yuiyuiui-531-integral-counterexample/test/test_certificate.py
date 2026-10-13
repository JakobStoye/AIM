"""Analytic homology controls and adversarial finite-certificate checks."""
from itertools import combinations
import unittest

from src.torusgrid_certificate import (
    boundaries, cancel_units, check_chain, dense_boundary, distance,
    liftable, make_certificate, rank_mod_prime)
from src.verify_certificate import verify, replay, rank_mod3_by_rows


def simplicial_basis(facets):
    faces = {}
    for facet in facets:
        for size in range(1, len(facet)+1):
            faces.setdefault(size-1, set()).update(combinations(sorted(facet), size))
    return {q: sorted(ss) for q, ss in sorted(faces.items())}


class AnalyticControls(unittest.TestCase):
    def test_closed_metric_and_wrap(self):
        self.assertEqual(distance((0, 0), (8, 0)), 5)
        self.assertEqual(distance((12, 12), (0, 0)), 2)
        self.assertTrue(liftable(((12, 0), (0, 0), (1, 0))))
        self.assertFalse(liftable(((0, 0), (3, 0), (8, 0))))

    def test_four_sphere_boundary(self):
        basis = simplicial_basis(list(combinations(range(6), 5)))
        B = boundaries(basis)
        check_chain(B)
        active, reduced, trace = cancel_units({q: len(ss) for q, ss in basis.items()}, B)
        self.assertEqual(len(active[0]), 1)
        self.assertEqual(len(active[4]), 1)
        self.assertTrue(all(not col for cols in reduced.values() for col in cols.values()))
        replay(B, {q: len(ss) for q, ss in basis.items()}, trace)

    def test_projective_plane_preserves_even_boundary(self):
        # Six-vertex triangulation of RP2: every edge belongs to two facets.
        facets = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 5), (0, 4, 5),
                  (1, 2, 5), (1, 3, 4), (1, 4, 5), (2, 3, 4), (2, 3, 5)]
        basis = simplicial_basis(facets)
        B = boundaries(basis)
        check_chain(B)
        active, reduced, trace = cancel_units({q: len(ss) for q, ss in basis.items()}, B)
        self.assertEqual({q: len(ids) for q, ids in active.items()}, {0: 1, 1: 1, 2: 1})
        matrix = dense_boundary(reduced, active, 2)
        self.assertEqual(abs(matrix[0][0]), 2)
        self.assertEqual(rank_mod_prime(matrix, 2), 0)
        self.assertEqual(rank_mod3_by_rows(matrix), 1)
        replay(B, {q: len(ss) for q, ss in basis.items()}, trace)

    def test_nonunit_is_not_cancelled(self):
        active, reduced, trace = cancel_units({0: 1, 1: 1}, {0: {0: {}}, 1: {0: {0: 2}}})
        self.assertEqual(trace, [])
        self.assertEqual(reduced[1][0], {0: 2})
        self.assertEqual(active, {0: {0}, 1: {0}})

    def test_invalid_pivot_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Invalid unit pivot'):
            replay({0: {0: {}}, 1: {0: {0: 1}}}, {0: 1, 1: 1}, [[1, 0, 0, -1]])


class FixedCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.certificate = make_certificate()

    def test_independent_full_replay(self):
        result = verify(self.certificate)
        self.assertEqual(result['status'], 'PASS')
        self.assertEqual(result['relative_H4_free_rank'], 2)
        self.assertEqual(result['rank_d4_Q'], 24)
        self.assertEqual(result['enumeration']['origin_nonliftable_cliques'], 332)

    def test_frozen_model_required(self):
        certificate = dict(self.certificate)
        certificate['model'] = dict(certificate['model'], radius=4)
        with self.assertRaisesRegex(ValueError, 'frozen'):
            verify(certificate)

    def test_minor_rank_lower_bound_control(self):
        matrix = [[2, 0, 2], [0, -2, 2], [0, 0, 0]]
        self.assertEqual(rank_mod_prime(matrix, 3), 2)
        self.assertEqual(rank_mod3_by_rows(matrix), 2)
        self.assertEqual(rank_mod_prime(matrix, 2), 0)


if __name__ == '__main__':
    unittest.main()
