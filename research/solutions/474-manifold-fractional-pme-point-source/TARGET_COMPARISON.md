# Comparison with AIM 474

The target is the
[original statement at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/474-manifold-fractional-pme-point-source.md).
The submitted result is Theorem 1.1 of the [manuscript](paper/manuscript.pdf).
All page and equation numbers below refer to the supplied seven-page PDF.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Complete, connected, noncompact Riemannian manifold; dimension N ≥ 2 | Setting on p.1 and Theorem 1.1 on p.2 | Every such manifold satisfying the two stated geometric inequalities |
| Ricci curvature bounded below by −(N−1)k for some k ≥ 0 | Equation (1), p.1; source-compatibility discussion, p.2 | Same bound; the k = 0 case is included |
| Uniform Faber–Krahn inequality for every relatively compact smooth domain, with c > 0 | Equation (1), p.1; Rayleigh-quotient argument on p.2 | The smooth-domain hypothesis suffices for the cited open-set convention |
| Every m > 1 and 0 < s < 1 | Equations (1)–(2), Theorem 1.1, pp.1–2 | Entire parameter range |
| Spectral fractional Laplace–Beltrami operator | Nonnegative Friedrichs operator L = −Δ and B = L^s, p.1; equation (14), p.4 | Same operator and sign convention |
| Every source point o and every mass A > 0 | Theorem 1.1, p.2; concentrating smooth data, p.4 | Arbitrary point and positive mass |
| Nonnegative distributional solution | Theorem 1.1; equation (3), p.1; passage to the weak equation, p.6 | Compactly supported smooth space-time tests, with the full nonlocal term |
| Strong L1 continuity at every positive time | Equation (4); global convergence (23), p.6 | One curve in C((0,∞); L1(M)) |
| Local boundedness and locally integrable u^m | Equation (4); the bound M_A(t), p.4; final passage, p.6 | Every compact subset of positive space-time |
| Integrable right side in the distributional identity | Bound on Bφ and global convergence of the powers, p.6 | Absolute integrability over all of M for each admissible test |
| 0 < sup over 0 < t < T of the L1 mass ≤ A for every T > 0 | Equation (5), p.2; closing argument, p.7 | The proof gives equality of this supremum to A; it does not require all-time mass conservation |
| Actual initial trace Aδ_o against every bounded continuous test | Equation (6); compact-test trace and final cutoff argument, p.7 | Every bounded continuous function and the actual t ↓ 0 limit |
| No radial symmetry or homogeneity | Setting and proof throughout | Neither is assumed |

Theorem 1.1 is a claim covering the complete existence target. It does not
claim uniqueness, a universal asymptotic profile, or acceptance by the
receiving repository.

## Imported results and the additional argument

The manuscript uses the bounded-data semigroup of
[Berchio–Bonforte–Grillo–Muratori, arXiv:2109.10732v2](https://arxiv.org/abs/2109.10732v2):
Assumption 2.1 and (2.3) for the heat kernel; Proposition 5.1 and (5.5)–(5.7)
for the mild semigroup and Euler construction; Proposition 5.3 and Section 6.1
for the same solution selection; and Theorem 2.6, (2.13), for smoothing.
Lemma 2.1 states precisely the bounded-data interface used here. The
smooth-domain/open-set convention and the Ricci-bound convention are
checked on p.2 of the submitted paper.

Stochastic completeness follows from
[Grigor’yan, Theorem 15.4(a), author version pp.87–88](https://www.math.uni-bielefeld.de/~grigor/recor.pdf).
The admissible radial comparison function is given on p.2 of the manuscript.
The Euclidean finite-measure result of
[Grillo–Muratori–Punzo, arXiv:1312.6076v3, Theorem 3.2](https://arxiv.org/abs/1312.6076v3)
is cited for context and is not substituted for the manifold argument.

Sections 2–4 supply the additional bridge: the Euler energy and bounded
graph-domain test identities, heat-average tests with uniformly small
fractional generator, spatial tightness on finite horizons, compactness of
the powers, and contraction from common good times. The global L1 limit
permits the full nonlocal equation to pass to the limit. Integrability of
the nonlinear flux near time zero gives the point-mass trace. These steps
are included in the public manuscript.

OpenAI Codex assisted development and internal AI review. Independent
mathematical review is requested; no human, formal or upstream certification
is claimed.
