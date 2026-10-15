# Correspondence with AIM Problem 461

Target: [Comparison for viscosity solutions of infinity-fractional diffusion](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/461-infinity-fractional-evolution-comparison.md),
revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The submitted result is an analytic counterexample to the full stated
subsolution–supersolution comparison implication.

| Original requirement | Manuscript result and location | Coverage |
| --- | --- | --- |
| Every integer n >= 2 | Theorem 1; Lemma 1 constructs a perpendicular direction and a tangent line | Every stated dimension |
| Every 1/2 < s < 1 and fixed C_s > 0 | Section 1 sets p = 2s; equations (1), (6), (10), (12) retain the normalization | Full stated parameter range |
| Domain R^n x [0,T], every T > 0 | Lemma 2 is global in space; Theorem 1 restricts both functions to the prescribed finite cylinder | Every positive finite horizon |
| Symmetric directional integral and gradient-selected direction | Equation (1); radial identity (11) and Lemma 3; opposite directions have identical integrals | Exact operator |
| Zero-gradient subsolution uses sup, supersolution uses inf | Equation (2); flat branch (9) and Lemma 2; radial value of V lies between both directional extrema in Lemma 3 | Exact relaxed convention, including noncentral critical radii |
| Local tests patched to the actual function outside a spatial neighborhood | Proof of Theorem 1 compares every patched directional integral with the smooth tested function | Every admissible upper/lower test |
| Bounded continuous subsolution and supersolution | Theorem 1 supplies bounded spatially C^2 and time C^1 functions; Lemmas 2–3 and final patch argument verify admissibility | Stronger regularity within the allowed class |
| Bounded uniformly continuous initial data, attained uniformly | Common F is smooth and compactly supported; Fourier uniform trace and the explicit U trace bound are in Lemma 3 and the final proof | Identical initial data |
| Initial order implies order throughout the cylinder | The final proof constructs x_* = 2e_1 and an explicit 0 < t_* < T with U(x_*,t_*) > V(x_*,t_*) | Comparison implication refuted |
| No radial symmetry or monotonicity assumed | A radial, nonmonotone annular witness belongs to the unrestricted class | No hypothesis added to the universal target |
| Constant dependence and uniformity | All constants are finite after fixing n,s,C_s,T; the crossing time is explicitly positive | No parameter-independent crossing time is asserted |

The manuscript proves its heat evolution and radial lift directly. Its only
explicit transform import is Schwartz Fourier inversion, with the normalization
shown in Lemma 3. The two PDE references locate the weak definition, restricted
classical comparison, and related elliptic phenomenon; no radial monotonicity
theorem is applied to the annular data.

This is a complete solution claim for the displayed comparison question, pending
independent mathematical review. It does not claim nonuniqueness of two full
solutions, a result for the stronger zero-gradient operator, or uniqueness or
nonuniqueness within a separately selected class of game limits.
