# Target comparison

Target: [AIM 457 at a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/457-stochastic-navier-stokes-negative-half-critical-data.md).
Result: [Theorem 1.1 of the manuscript](paper/paper.pdf).
This table compares the mathematical statements; it is not an independent audit.

| Original requirement | Submitted statement and proof |
|---|---|
| Space R^3; any nu>0 | Equation (1.1), Theorem 1.1 and all function spaces use R^3 and arbitrary positive viscosity. |
| Any finite real smooth compactly supported divergence-free family b_k | The assumptions before (1.2) are identical. Section 2.2 verifies the whole-space linear theorem for these variable fields. |
| nu I - (1/2) sum b_k tensor b_k >= delta I for some delta>0 | Equation (1.2) is the same strict stochastic parabolicity condition. No additional size hypothesis is introduced. |
| Every deterministic divergence-free u_0 in usual inhomogeneous B^{-1/2}_{6,4} | Theorem 1.1 quantifies over this entire space. Equation (2.1) includes the low-frequency block. Lemma 2.1 treats distributional initial data without assuming u_0 in L^6. |
| Original Ito equation with projected variable transport noise | Equations (1.1), (1.3) and (2.7) retain P[(b_k dot grad)u]. The projection is not commuted through b_k. |
| Heat semigroup in drift and stochastic mild convolutions | Equation (1.3) is the required identity. Section 2.3 verifies strong/mild agreement and the continuous convolution versions. |
| Positive stopping time and adapted local solution | Section 3.2 constructs the progressive truncated solution and a strictly positive stopping time (3.5); the cutoff is one throughout that stopped interval. |
| C([0,tau];B^{-1/2}_{6,4}) intersect L^4(0,tau;L^6), almost surely | Theorem 1.1 states exactly these spaces; Lemma 2.1, (2.11) and Section 3.2 supply the trace and time norm. |
| Pathwise uniqueness in this entire class | Section 3.3 compares arbitrary solutions with only almost-sure norms, on bounded-norm random slabs. No fourth-probability-moment assumption is added to the solution class. |
| Initial-data continuity in probability in both norms on common local intervals | Theorem 1.1 and Section 3.4 give both-norm convergence after stopping on tau_n wedge tau. They also give rho>0 with P(tau_n<rho) tending to zero, so the common intervals are nondegenerate. |
| No extra smallness assumption | Section 3.2 chooses a cutoff radius from finite coefficient-dependent constants and works on the whole process Banach space for arbitrary data. The radius is a proof choice, not a condition on the initial velocity or fields. |

The manuscript claims the complete written target above. It does not claim
global well-posedness, an optimal critical data class, or an independent proof
of the external linear maximal-regularity theorem. That published theorem and
its localized interface are stated and cited explicitly in Proposition 2.2.
Independent mathematical review of this solution claim is requested.
