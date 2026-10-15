# Correspondence with AIM Problem 458

**Maintainer note, 15 October 2026:** this table describes the submitted complete claim. The [independent AI review](../solution_reviews/2026-10-15-active-prs/458-review.md) found an unverified hypothesis in Section 3.3: the corrected KKW theorem also requires compatible fractional right-inverse estimates. The repository records **partial progress**, rather than accepting the full existence and continuous-dependence claim. The original requirement comparison is preserved below.

Target: [458. Local no-slip Navier--Stokes theory under non-small transport noise](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/458-stochastic-navier-stokes-no-slip-local.md), repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted result: Theorem 1.1 of [the manuscript](paper/paper.pdf), with its complete proof in Sections 2--6. This is a complete solution claim for the specified finite smooth-coefficient target, awaiting independent review.

| Original requirement | Manuscript result and location | Coverage |
| --- | --- | --- |
| Every bounded smooth domain in three dimensions; every positive viscosity | Theorem 1.1; physical weak spaces in Section 2 | Same domain and viscosity quantifiers. The proof uses both boundary channels and full three-dimensional interior tori. |
| Finitely many smooth divergence-free noise fields, tangent to the boundary | Equation (1.1), Theorem 1.1 and equation (2.3) | Same coefficient class. No planar-span restriction is imposed in the interior. |
| Only the displayed stochastic parabolicity condition on amplitude | Theorem 1.1 and equation (2.3); the linear construction in Section 5 | Full positive-parabolicity range. Constants may depend on the fixed coefficients and positivity constant; no uniform estimate as that constant tends to zero is asserted. |
| Every smooth divergence-free datum vanishing at the wall | Theorem 1.1; positive local construction in Section 6.1 | Same initial-data class. The proof also constructs the cutoff equation for the stated Besov trace space. |
| The prescribed projected Ito equation with no-slip boundary | Equation (1.1); weak realization (2.1), linear equation (2.4), convection (6.1) | Identical Ito drift and projected transport noise. The equation is an integral identity in the dual of the zero-trace solenoidal W^(1,4/3) space. |
| Adapted solution on an almost surely positive stopping interval | Theorem 1.1 and the continuous cutoff exit in Section 6.1 | Adapted local construction with positive stopping time. Continuity includes the exit endpoint; no Sobolev value at a single endpoint is required. |
| C([0,tau]; B^(1/2)_(4,4)) intersect L^4(0,tau; W^(1,4)_0) | Equations (1.2), (2.2), and Theorem 2.1 | Exact requested path topology, with the solenoidal and zero-trace constraints. |
| Pathwise uniqueness in that class | Section 6.2, especially (6.5) | Uniqueness for every adapted competing solution in the entire asserted path class. No probability-moment assumption is added to the competitors. |
| Continuous dependence in probability after common stopping | Equations (1.3) and (6.6)--(6.9) | Same Brownian coupling, pairwise common positive stops, convergence in the full path norm, and probability tending to one of reaching one fixed base stop. No positivity of an infinite infimum of exit times is assumed. |

## Imported analytic inputs and what is proved here

The numbered bibliography in the manuscript supplies direct public source links. The external results are used with the following scope:

| Public input | Location and application in the manuscript |
| --- | --- |
| Pruss--Wilke, Section 5 and Proposition 5.1 | Section 2: isotropic weak Stokes and Besov trace identifications on a bounded smooth domain. |
| Kalton--Kunstmann--Weis, Theorem 9.17 | Section 2: isotropic physical Stokes calculus. It is not invoked as a periodic-channel theorem. |
| Girardi--Weis, Corollary 4.4 | Section 3.3: operator-valued multipliers after proving all required derivatives and Hilbert-index uniformity; periodic restriction is proved in the manuscript. |
| Deleaval--Kriegler, Theorem 1 | Section 3.2: vector-valued maximal estimate for the full-line kernels. The reflected kernels are handled by the displayed Hardy estimate. |
| Kalton--Kunstmann--Weis, Theorem 8.2 and the cited Stokes comparison argument | Section 3.3: channel isotropic calculus, with the inverse operators, endpoint spaces and signed image conditions written explicitly. The explicit resolvent supplies the model geometry and consistency. |
| Agresti--Veraar, Theorem 3.14, Proposition 2.1 and Definitions 3.7--3.8 | Sections 2--3: additive stochastic maximal regularity and its time trace. Non-small multiplicative transport is proved separately by translation, localization and continuation. |
| Costabel--McIntosh, formula (3.13), Theorem 3.2, Corollary 3.4 and Remark 3.5 | Section 4.2: one regularized supported divergence solver on fixed convex Euclidean boxes, consistently at the stated orders. |
| Breit--Gaudin, fixed preprint v1, Theorem 4.38, Proposition 4.39, Lemma 2.12 and Proposition 2.4 | Section 4.2: strict-window negative pressure and zero-extension bounds at both dual exponents. |
| Kalton--Kunstmann--Weis, Theorem 6.1, Lemma 6.2 and Proposition 2.2 | Section 4.3: two fractional defect bounds, quantitative root comparison and interpolation. Both smallness conditions are proved in the manuscript. |
| Agresti--Veraar, Lemma A.5 | Section 6.2: stopped variational Ito identity, with its projection-limit justification included. |

The channel pressure resolvent, collision and all kernel derivatives, full-rank interior model, energy-form localizers, pressure defect, quantitative root reconstruction, physical linear continuation, nonlinear cutoff, entire-class uniqueness and common-stop dependence are derived in the manuscript. No general anisotropic square-root theorem is assumed.

The claim addresses the complete original AIM 458 statement. It does not assert a result for every broader rough or infinite-dimensional noise regime of Agresti--Veraar's Open Problem 9, global three-dimensional regularity, a formal proof, or upstream acceptance. AI involvement and the limits of internal review are disclosed in the manuscript and [README](README.md).
