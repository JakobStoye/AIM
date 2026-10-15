# Comparison with AIM problem 467

Target: [467. Continuity for degenerate fractional-pressure porous-medium flow](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/467-fractional-pressure-superquadratic-continuity.md) at commit `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The original assertion is universal over its parameters, data and bounded energy weak solutions. A single admissible solution lacking the requested representative refutes that assertion. The manuscript proves a general obstruction in the strict subrange 1/2 < s < 1 and uses existing global existence to obtain the concrete witness N = 2, m = 3, s = 3/4, u₀ the indicator of the unit ball. The witness is specified by the existence theorem; an explicit formula for the solution is not claimed.

| Original requirement | Manuscript location and coverage |
| --- | --- |
| N ≥ 2, m > 2, 0 < s < 1 | Theorem 1.2 proves non-continuity for all N ≥ 2, m > 2, 1/2 < s < 1. Corollary 1.3 fixes N = 2, m = 3, s = 3/4 inside the original range. |
| Nonnegative, nonzero u₀ in L¹ ∩ L∞ with compact support | Definition 1.1 and Corollary 1.3; the fixed datum is the unit-ball indicator. |
| Distributional equation u_t = div(u^(m−1) ∇p) on R^N | Equation (1), Definition 1.1 and Appendix A use the same equation and the same global solution from the cited existence theorem. |
| p = (−Δ)^(−s) u with multiplier ∣ξ∣^(−2s) | The unitary Fourier convention in Section 1 sets I_β to multiplier ∣ξ∣^(−β), so p = I_(2s)u. |
| Initial trace u₀ | Definition 1.1 and Appendix A give the trace, including at t = 0, without restarting the solution. |
| Continuity into L¹ with its weak topology | Appendix A constructs one representative continuous against every bounded test function. |
| Conservation of mass | Definition 1.1 and Appendix A give mass M = ∫u₀ > 0 at every time. |
| Uniform bound by ∥u₀∥∞ | Definition 1.1 and Appendix A retain the source L∞ bound H. |
| Locally integrable flux | Lemma 2.2 gives the stronger bound ∣F∣ ≤ V u and global flux integrability on each finite slab, for F = −u^(m−1)∇p. |
| Pressure energy inequality with coefficient 1/2 | Equation (2), sourced from Stan–del Teso–Vázquez; Appendix A extends it to every prescribed endpoint. Initial energy finiteness is checked in the proof of Corollary 1.3. |
| Every dissipative L^q inequality, q > 1, with the original coefficient and power | Equation (3) has coefficient 4q(q−1)/(m+q−1)² and power (m+q−1)/2. Appendix A proves all endpoint inequalities for the same representative. |
| Representative continuous on R^N × (0,∞), including across vacuum | Theorem 1.2 excludes any such global jointly continuous representative. Proposition 2.3 uses continuity at vacuum in the exterior halfspaces; Section 3 obtains the dissipation contradiction. Corollary 1.3 supplies an actual solution, so the obstruction is nonvacuous. |

The contradiction uses q = 2, but the selected solution satisfies the entire required family q > 1 and the pressure energy inequality. It does not prove a classification for s ≤ 1/2, spatial discontinuity at every time, a jump profile, or a discontinuity location. The cited existence and m = 2 regularity results are attributed in the manuscript. The public original problem is used for its formulation and curation; no exhaustive novelty claim is made.

This is a complete negative-answer claim to the universal assertion, submitted for independent mathematical review. The package itself makes no catalogue classification change.
