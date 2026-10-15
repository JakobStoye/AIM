# AIM 463: independent audit of PR #150

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [3f046208c5834b548da08c6253c1508c25c90644](https://github.com/MColbrook/AIM/pull/150), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. The proposed kernel-uniform full-order Sobolev estimate fails at every finite sufficiently large p for strict ellipticity pairs.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The theorem addresses exactly the original uniform-over-kernels estimate, with sigma=2s and every strict pair lambda<Lambda. It treats Slobodeckij order away from one and ordinary W^(1,p) at order one. It does not assert that every fixed operator fails or address the equal-constant isotropic class.

The annular Gram-matrix construction yields even compactly supported smooth jump perturbations with moment vectors (1,0) and (0,1) at frequencies one and two. Independent disk controls on disjoint geometric jump annuli keep the same pointwise ellipticity bounds while producing the Bellman expression kappa A minus epsilon times the sum of two-dimensional moment norms. The finite kernel family parameters are compact; all operators are translation invariant and smooth away from zero.

I reconstructed the scale interactions for V_N=N^-1 sum k_j^(-sigma)(cos(k_j x_1)+cos(2k_j x_1)). The annular errors are geometrically summable uniformly in N, with separate low/high-frequency exponents sigma and 2-sigma. Multiplication by a smooth background adds a uniformly controllable k_0 error. Lacunary averaging kills the linear mean-zero part in every finite Lp but retains the strictly positive nonlinear average of sqrt(cos^2+cos^2(2t)), whose square is at least 7/16. The choices R, then N, then k_0 are in the correct order. Nonvanishing of each annular two-vector makes each constructed forcing smooth, even though no uniform higher forcing norms are asserted.

For a bounded smooth background w with Aw>=0, the chosen positive amplitude gives Iu_N tending to zero in Lp and u_N tending globally uniformly to w. Gradient convergence for sigma>1 and the separate sine-average argument at sigma=1 justify the respective limiting norms; difference-quotient Fatou handles fractional seminorms. The supplied heat/Fourier calculation proves the Riesz-potential identity with its normalization. Concentrating its negative potential gives fixed global supremum and Sobolev lower bound c r^(n/p-sigma), which diverges for p>n/sigma. Thus any proposed finite large-p threshold is contradicted.

The book's Open Question 3.2 has the uniform quantifier used here. Kitano's restricted kernel class, Serra's global Hölder assumptions and Vivas's bounded-forcing estimate are credited as restricted comparisons, not invoked to prove this statement. All novel estimates and the potential identity are provided in the manuscript; Kwaśnicki's [equivalent definitions](https://arxiv.org/abs/1507.07356v2) are compatible with its normalization. No missing external computational certificate is needed.
