# AIM 217: independent audit of PR #147

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [96149f92d7f66bfb1772aec423a32f676e2dc1d1](https://github.com/MColbrook/AIM/pull/147), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. One fixed pair of smooth bounded potentials violates the proposed unordered critical/subcritical heat-kernel comparison.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The Euclidean line is an allowed complete noncompact manifold. The fixed distinct integral-test pair is (0,1); the failure of local uniform convergence is tested on the admissible compact singleton {(0,0)}. Both Friedrichs operators are nonnegative with spectral bottom zero. The reference has no nonzero square-integrable zero mode.

For the numerator, a nonzero nonnegative compact bump has a positive even zero-energy solution linear at both ends. The exact one-dimensional resistance Green formula makes the (0,1) time integral finite. A fixed positive bridge followed by the half-line image kernel gives a t^(-3/2) lower bound at (0,0).

The reference is built as V=w''+(w')^2 with w>=0, uniformly bounded first two derivatives, and factorization of its form. Every finite approximation has slope-one tails and a strictly positive spectral gap, proved by a normalized minimizing sequence and compactness rather than an assumed common gap. At stage n choose its own large time, then a protecting radius. The Feynman–Kac bridge exit estimate controls every later exterior modification by exp(-R^2/t), so the final single potential retains the chosen small diagonal heat values. Infinitely many preserved unit intervals at height zero make both resistance integrals infinite. Resistance-tent form tests prove spectral bottom zero for the final potential, and factorization makes its only possible form-zero vectors multiples of exp(w), which is not in L2. The quotient therefore diverges along the selected times for this fixed pair.

Appendix A was checked in full: large exterior killing identifies the Dirichlet semigroup via strong resolvent convergence and bounded functional calculus; the bridge boundary event has no atom; exhaustion gives the half-line kernel. The explicit interval Green inverse, its time integral and monotone exhaustion establish the actual operator realization used above. These steps avoid substituting a formal Green expression for the Friedrichs kernel.

The cited [Fraas–Krejčiřík–Pinchover source](https://arxiv.org/abs/0912.4337v3) and workshop question concern exactly the unordered comparison. The conditional ordered-perturbation result is not contradicted. Simon's [Feynman–Kac formula](https://arxiv.org/abs/math-ph/9907022v1), Teschl's spectral/form framework and the reflection formula are used with their standard bounded-potential hypotheses. The original construction and limiting protection argument are fully included, with no computational premise.
