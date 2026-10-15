# Correspondence with AIM 469

The source is [problem 469 at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/469-superlinear-skt-nonlocal-to-local-limit.md). Locations below refer to the accompanying manuscript. This is a complete analytic solution claim awaiting independent review.

| Original requirement | Manuscript result and location | Relation |
|---|---|---|
| Every smooth bounded connected nonempty domain in dimension d >= 1; n >= 2; fixed s > 1 | Section 1.1, Theorem 1.1 | Identical |
| Positive linear diffusion; symmetric nonnegative interactions and the stated piecewise strict diagonal dominance; nonnegative reaction coefficients | Equations (1)--(2), power margin and Lemma 2.1 | Identical assumptions, no replacement by an extra condition |
| Smooth radial nonnegative compactly supported kernel, positive near zero, half-second-moment normalization | Section 1.1 and equation (3); Lemma 2.2 checks dimension one separately | Identical |
| Regional epsilon-scaled jump operator acting on the actual nonlinear pressure | Equation (4), quotient identity (25), pressure identification (28)--(29) | Identical model and normalization |
| Fixed nonnegative bounded BV data and the given global strong solutions | Section 1.1; entropy tests at fixed epsilon | Identical; strong norms are not assumed uniform in epsilon |
| Strong L1 convergence on every finite time interval | Theorem 1.1, equation (5); Lemma 3.2; final diagonal extraction | Stronger convergence in Lp for every 1 <= p < 2s, along one global subsequence |
| Pass nonlinear pressures and reactions to the local equation | Equation (6), paragraph following Lemma 3.2 | Strong L1 convergence of both actual nonlinear expressions |
| Genuine no-flux local weak solution | Equations (7)--(8); Section 3.3 | Pressure in Lr(W1r), r > 1, and arbitrary-boundary first-order tests give weak homogeneous Neumann pressure flux |
| Preserve original initial data | Equation (8) and Section 3.3 time representative | Same datum, weak Ls initial trace and weak Ls time continuity |
| One global weak solution and one subsequence for all finite horizons | End of Theorem 1.1 proof | Identical global quantifier |

Theorem 1.1 contains no proof-only free cutoff: the logarithmic regularization is removed at fixed epsilon, and the absorption threshold in Lemma 2.3 is fixed by the given coefficients. Constants may depend on the fixed exponent and other data. The endpoint s = 1, uniqueness, rates and convergence without subsequence are outside the claim.

The main specialized imported input is Ponce, *An estimate in the spirit of Poincare's inequality*, Theorems 1.1--1.3. Lemma 2.2 gives its exact probability-kernel normalization, L2 form-domain/mean interface, the required one-dimensional dilation condition and the fixed interval scaling. That input alone does not supply time compactness, product convergence or the boundary/initial identification; those are proved in Section 3.
