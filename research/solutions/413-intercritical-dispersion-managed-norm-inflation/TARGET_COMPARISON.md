# Comparison with the original AIM 413 target

Source: [AIM 413 at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/413-intercritical-dispersion-managed-norm-inflation.md).

| Original requirement | Manuscript result and location | Scope |
|---|---|---|
| The defocusing quintic equation on R3 with the average over [0,1] | Equation (1.1); Section 3 derives the exact rescaled equation using Q_1[A f(./L)] = A^5 L^2 Q_(L^-2)(f)(./L) | The original sign, power, dimension and averaging window are preserved |
| Every epsilon > 0 | Theorem 1.1; final paragraph of Section 3's proof | A single sufficiently large real parameter g enforces all three strict bounds simultaneously |
| Initial data in Schwartz space | Lemma 2.1 and the Gaussian in equation (3.1), restated in Corollary 3.1 | u_(g,0)(x) = g^(11/4) exp(-g^(9/2) norm(x)^2/4) |
| A smooth solution in an interval containing the witness time | Lemma 2.1, applied in Section 3 | A global smooth solution is obtained from the defocusing global Sigma theory with persistence of higher Sobolev regularity and two spatial weights |
| The homogeneous H^(1/4) norm with the displayed Fourier multiplier | Introduction's Fourier convention; equation (3.3) | Squared norm is the integral of norm(xi)^(1/2) times abs(fhat(xi))^2, with the unitary Fourier transform |
| Initial norm below epsilon | Section 3 after equation (3.8); Corollary 3.1 | Initial norm equals C_phi g^(-1/16) and tends to zero |
| Final norm above epsilon^(-1) | Equation (3.8) and restoration of the original norm; Corollary 3.1 | Final norm is at least c g^(1/16) and tends to infinity |
| Strictly nonzero time with absolute value below epsilon | Section 3's choice of the negative maximizing time; Corollary 3.1 | 0 < abs(t_g) <= g^(-11/2), so the required strict upper bound follows for sufficiently large g |

The source permits either time direction through 0 < |t_epsilon| < epsilon. The construction uses negative times. The result concerns the fixed exponent 1/4 and does not assert all positive intercritical exponents or positive-time norm inflation.

The imported global existence theorem is Kawakami--Murphy, Proposition 5.1 in arXiv:2407.11151v1, for dimension 3 and nonlinearity |v|^4 v. Lemma 2.1 explicitly converts its convention i v_t + Delta v = Q_1(v) through u(t) = v(-t). The remaining localization, finite-endpoint virial, scaling and growth estimates are proved in the note. Keel--Tao and Nirenberg provide the standard analytical estimates used for smoothness persistence.
