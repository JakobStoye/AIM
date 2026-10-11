"""Independent exact and high-precision checks of the radial library."""

import math
import unittest
import mpmath as mp
import numpy as np

from elliptic_widths import (
    RadialCoefficient, expanded_spectrum, generalized_eigenvalues,
    log_determinant_bound, log_radial_spectrum, log_singular_bound,
    multiplicity, spherical_degrees,
)


def direct_mp_spectrum(d, coefficient, inner, maximum):
    """Independent reference: unscaled arbitrary-precision matrix exponentials."""
    results = []
    with mp.workdps(70):
        radii = [mp.mpf(str(x)) for x in coefficient.radii]
        radial = [mp.mpf(str(x)) for x in coefficient.radial]
        tangential = [mp.mpf(str(x)) for x in coefficient.tangential]
        inside = mp.mpf(str(inner))
        for degree in range(1, maximum + 1):
            angular = mp.mpf(degree * (degree + d - 2))
            gamma = (mp.sqrt((d - 2)**2 + 4 * tangential[0] / radial[0] * angular) - (d - 2)) / 2
            state = mp.matrix([1, radial[0] * gamma])
            energy_inner = None
            if inside <= radii[0]:
                energy_inner = inside**(d - 2) * radial[0] * gamma * (inside / radii[0])**(2 * gamma)
            for shell in range(1, len(radii)):
                start, end = radii[shell - 1], radii[shell]
                matrix = mp.matrix([[0, 1 / radial[shell]], [tangential[shell] * angular, -(d - 2)]])
                targets = [inside, end] if start < inside < end else [end]
                for target in targets:
                    state = mp.expm(matrix * mp.log(target / start)) * state
                    if target == inside:
                        energy_inner = target**(d - 2) * state[0] * state[1]
                    start = target
            energy_outer = radii[-1]**(d - 2) * state[0] * state[1]
            results.append(float(mp.log(energy_inner / energy_outer) / 2))
    return np.array(results)


class RadialTests(unittest.TestCase):
    def test_isotropic_formula_including_core_and_interfaces(self):
        for d in (2, 3):
            for inner in (0.05, 0.1, 0.31, 0.5, 0.9):
                coefficient = RadialCoefficient([0.1, 0.5, 1.0], [2.0]*3, [2.0]*3)
                logs = log_radial_spectrum(d, coefficient, inner, 100)
                exact = (np.arange(1, 101) + (d - 2)/2) * math.log(inner)
                np.testing.assert_allclose(logs, exact, rtol=3e-14, atol=2e-12)

    def test_constant_polar_anisotropy_formula(self):
        for d in (2, 3):
            coefficient = RadialCoefficient([0.01, 0.3, 1.0], [4]*3, [0.25]*3)
            degrees = np.arange(1, 81)
            gamma = (np.sqrt((d-2)**2 + degrees*(degrees+d-2)/4) - (d-2))/2
            expected = (gamma + (d-2)/2) * math.log(0.47)
            np.testing.assert_allclose(log_radial_spectrum(d, coefficient, 0.47, 80), expected, atol=5e-12)

    def test_independent_high_precision_exponential(self):
        coefficient = RadialCoefficient([0.07, 0.25, 0.6, 1], [1, 4, 0.2, 2], [0.3, 0.5, 5, 1])
        for d in (2, 3):
            for inside in (0.025, 0.25, 0.47):
                actual = log_radial_spectrum(d, coefficient, inside, 8)
                expected = direct_mp_spectrum(d, coefficient, inside, 8)
                np.testing.assert_allclose(actual, expected, rtol=2e-13, atol=3e-13)

    def test_large_exponents_do_not_overflow(self):
        coefficient = RadialCoefficient([0.001, 0.2, 1], [0.02, 8, 0.05], [7, 0.03, 9])
        actual = log_radial_spectrum(3, coefficient, 0.2, 1000)
        self.assertTrue(np.all(np.isfinite(actual)))
        self.assertTrue(np.all(actual < 0))
        expected = direct_mp_spectrum(3, coefficient, 0.2, 3)
        np.testing.assert_allclose(actual[:3], expected, atol=1e-12)

    def test_layer_splitting_invariance(self):
        original = RadialCoefficient([0.2, 0.5, 1], [1, 3, 0.2], [2, 0.3, 4])
        split = RadialCoefficient([0.1, 0.2, 0.3, 0.5, 0.7, 1], [1, 1, 3, 3, 0.2, 0.2], [2, 2, 0.3, 0.3, 4, 4])
        for d in (2, 3):
            np.testing.assert_allclose(log_radial_spectrum(d, original, 0.4, 100), log_radial_spectrum(d, split, 0.4, 100), atol=2e-12)

    def test_geometric_scaling_invariance(self):
        original = RadialCoefficient([0.1, 0.4, 1], [1, 0.3, 3], [2, 4, 0.5])
        scaled = RadialCoefficient(original.radii * 7.25, original.radial, original.tangential)
        for d in (2, 3):
            np.testing.assert_allclose(log_radial_spectrum(d, original, 0.3, 80), log_radial_spectrum(d, scaled, 0.3 * 7.25, 80), atol=2e-12)

    def test_common_coefficient_scaling_invariance(self):
        original = RadialCoefficient([0.1, 0.4, 1], [1, 0.3, 3], [2, 4, 0.5])
        scaled = RadialCoefficient(original.radii, original.radial * 19, original.tangential * 19)
        for d in (2, 3):
            np.testing.assert_allclose(log_radial_spectrum(d, original, 0.3, 80), log_radial_spectrum(d, scaled, 0.3, 80), atol=2e-12)

    def test_one_core_model(self):
        coefficient = RadialCoefficient([1], [1], [1])
        for d in (2, 3):
            np.testing.assert_allclose(log_radial_spectrum(d, coefficient, 0.5, 20), (np.arange(1,21)+(d-2)/2)*math.log(0.5), atol=1e-14)

    def test_coefficient_constructor_rejects_invalid_data(self):
        for args in (([], [], []), ([0,1],[1,1],[1,1]), ([1,1],[1,1],[1,1]), ([1],[0],[1]), ([1],[1],[-1]), ([1],[np.nan],[1]), ([1],[1,2],[1]), ([[1]],[1],[1])):
            with self.subTest(args=args), self.assertRaises(ValueError):
                RadialCoefficient(*args)

    def test_invalid_spectrum_parameters(self):
        coefficient = RadialCoefficient([0.1,1],[1,1],[1,1])
        for d, inside, degree in ((1,0.5,2),(2,0,2),(3,1,2),(2,np.nan,2),(2,0.5,0),(2,0.5,1.5),(2,0.5,True)):
            with self.subTest(values=(d,inside,degree)), self.assertRaises(ValueError):
                log_radial_spectrum(d, coefficient, inside, degree)

    def test_unsupported_core_dynamic_ranges_fail_clearly(self):
        for radial, tangential in ((1e300, 1e-300), (1e-300, 1e300), (1e308, 1e308)):
            coefficient = RadialCoefficient([1], [radial], [tangential])
            for d in (2, 3):
                with self.subTest(d=d, radial=radial, tangential=tangential):
                    with self.assertRaises(FloatingPointError):
                        log_radial_spectrum(d, coefficient, 0.5, 2)

    def test_unsupported_shell_dynamic_ranges_fail_clearly(self):
        for radial, tangential in ((1e300, 1e-300), (1e-300, 1e300), (5e-324, 5e-324)):
            coefficient = RadialCoefficient([0.25, 1], [1, radial], [1, tangential])
            for d in (2, 3):
                with self.subTest(d=d, radial=radial, tangential=tangential):
                    with self.assertRaises(FloatingPointError):
                        log_radial_spectrum(d, coefficient, 0.5, 2)

    def test_constructor_copies_inputs(self):
        input_array = np.array([1.0,2.0])
        coefficient = RadialCoefficient([0.5,1], input_array, input_array)
        input_array[0] = 100
        self.assertEqual(coefficient.alpha,1)
        self.assertEqual(coefficient.beta,2)
        with self.assertRaises(ValueError):
            coefficient.radial[0] = 3


class SpectralTests(unittest.TestCase):
    def test_exact_degree_multiplicities(self):
        np.testing.assert_array_equal(spherical_degrees(2,7), [1,1,2,2,3,3,4])
        np.testing.assert_array_equal(spherical_degrees(3,10), [1,1,1,2,2,2,2,2,3,3])
        self.assertEqual(len(spherical_degrees(3,0)),0)
        self.assertEqual(multiplicity(3,80),161)

    def test_all_small_prefix_sums(self):
        for d in (2,3):
            counts = np.arange(1,10001)
            sums = np.cumsum(spherical_degrees(d,10000)+d-2)
            lower = counts**2/4 if d == 2 else (2/3)*counts**1.5
            self.assertTrue(np.all(sums >= lower))

    def test_bound_invariants(self):
        bound = log_determinant_bound(3,25,0.5,1,0.2,4)
        np.testing.assert_allclose(log_singular_bound(3,25,0.5,1,0.2,4), bound/(2*np.arange(1,26)))
        np.testing.assert_allclose(log_determinant_bound(3,25,5,10,2,40),bound)

    def test_invalid_bound_parameters(self):
        for values in ((2,0,0.5,1,1,1),(2,1,1,1,1,1),(2,1,0.5,1,2,1),(3,1,0.5,np.inf,1,1)):
            with self.subTest(values=values),self.assertRaises(ValueError):
                log_determinant_bound(*values)

    def test_finite_modes_are_sorted_by_singular_value(self):
        np.testing.assert_array_equal(expanded_spectrum(2,[-3,-1,-2]),[-1,-1,-2,-2,-3,-3])
        self.assertEqual(len(expanded_spectrum(3,np.arange(80,dtype=float))),6560)

    def test_generalized_eigenvalue_diagonal_reference(self):
        np.testing.assert_allclose(generalized_eigenvalues(np.diag([3,4]),np.diag([1,2])),[2,3])

    def test_generalized_eigenvalues_basis_invariance(self):
        q = np.array([[2,0.4],[0.4,5]])
        g = np.array([[3,0.5],[0.5,2]])
        basis = np.array([[1,0.2],[-0.5,2]])
        np.testing.assert_allclose(generalized_eigenvalues(q,g), generalized_eigenvalues(basis.T@q@basis,basis.T@g@basis),atol=1e-13)

    def test_generalized_eigenvalues_independent_polynomial(self):
        q = np.array([[3,0.5],[0.5,2]])
        g = np.array([[2,0.2],[0.2,1]])
        # det(Q-lambda G) is an independently expanded quadratic.
        quadratic = [np.linalg.det(g), -(q[0,0]*g[1,1]+q[1,1]*g[0,0]-2*q[0,1]*g[0,1]),np.linalg.det(q)]
        np.testing.assert_allclose(generalized_eigenvalues(q,g),np.sort(np.roots(quadratic)),atol=1e-14)

    def test_invalid_forms(self):
        for q,g in (([[1,2],[0,1]],np.eye(2)),(np.eye(2),np.diag([1,0])),(np.eye(2),np.diag([1,-1])),([[np.nan]],[[1]]),([1],[1])):
            with self.subTest(q=q,g=g),self.assertRaises(ValueError):
                generalized_eigenvalues(q,g)

    def test_determinant_bound_on_discontinuous_model(self):
        coefficient = RadialCoefficient([0.1,0.3,0.5,1],[1,4,0.2,2],[0.4,1,5,0.5])
        for d in (2,3):
            logs = expanded_spectrum(d,log_radial_spectrum(d,coefficient,0.5,30))
            bound = log_determinant_bound(d,len(logs),0.5,1,coefficient.alpha,coefficient.beta)
            self.assertTrue(np.all(2*np.cumsum(logs) <= bound+1e-10))


if __name__ == "__main__":
    unittest.main()
