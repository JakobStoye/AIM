# AIM 252: independent audit of PR #164

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [ec0a45a8a976049a4fdd6f52af3f618868f414ed](https://github.com/MColbrook/AIM/pull/164), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. Total integrability of the Minkowski billiard in its own norm ball forces an inner-product norm, without an extra symmetry assumption.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The theorem uses exactly a smooth strongly convex planar norm, its own unit ball, the chord-length generating function and a C0 foliation of the whole phase annulus by essential invariant curves. No differentiable leaves, finite symmetry beyond central symmetry, or separate self-polar assumption is imposed.

The strict support maximum of a norm chord over the rotated polar was checked, including the negative odd-variable Hessian and positive twist derivative. Every finite stationary length action is locally maximizing by the continuous-invariant-curve property. The Schur complement transfers this to the alternating signed-area action on the position and momentum boundaries; this is stronger than merely transferring its stationary equations.

The two alternating phase components and their half maps cover the whole original annulus. Their positive mixed-derivative measure is invariant. Testing finite variations equal to one at consecutive vertices and zero at the endpoints, integrating and dividing by the length yields the averaged second-variation inequality. Central antipodes exchange the two determinant-sign halves, allowing the full product torus integrals. Integration by parts gives 2D<=B C_c+A C_d for the two energy matrices; all signs and doubled components were retained.

A centro-affine parametrization gives a common period Omega<=2 sqrt(aa*)<=2pi. The whitened energy matrix, planar isoperimetry and Cauchy–Schwarz give sqrt(det M)>=2pi a/Omega. The averaged upper bound is D<=2AB, while the trace arithmetic-geometric mean gives D>=8pi^2 AB/(Omega_K Omega_P)>=2AB. Equality is forced throughout, and the symmetric polar-area-product equality case makes K a centered ellipse. Its gauge is the stated positive-definite quadratic norm, including at zero.

The actual [Bialy arXiv:1205.3873v2](https://arxiv.org/pdf/1205.3873v2), §3 paragraph following Theorem 3.1, supplies the local-maximum property for continuous essential invariant curves with positive twist; it is not restricted to differentiable leaves. [Bianchi–Kelly arXiv:1312.0244v3](https://arxiv.org/pdf/1312.0244v3), Theorem 1, supplies the symmetric Blaschke–Santaló inequality and ellipse equality case. The cited ordinary isoperimetric inequality is used for a smooth strongly convex plane curve. Prior finite-linear-symmetry and single-symplectic-table theorems are explicitly contextual, so neither an order-three symmetry nor equality of the two alternating tables has been silently assumed.
