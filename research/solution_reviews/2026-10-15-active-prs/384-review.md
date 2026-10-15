# AIM 384: independent audit of PR #152

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [f42708c58003e4f7663f6f9edda17626921cd27f](https://github.com/MColbrook/AIM/pull/152), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. Two disjoint disks admit two distinct bounded positive monostable Dirichlet equilibria for one admissible reaction.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The counterexample uses two equal finite disks in R2, with radius 16,003,200,160 and gap 11/5. The explicit smoothed plateau reaction is positive on (0,1), negative above one, and has endpoint derivatives +/-1/100 and globally Lipschitz first derivative. AIM384 permits an increasing per-capita quotient; no strong-KPP hypothesis has been removed.

The interval energy inequality in Lemma 2.1 was reconstructed by splitting the superlevel set above theta=1/4, retaining the endpoint ramps and minimizing the quadratic derivative energy on each component. The maximum of m^3(L-m) gives exactly the stated 16theta/3 criterion. For the chosen reaction and channel width, Corollary 2.2 gives energy at least (1/40) times squared mass.

The explicit parabolic/linear strip profile has the correct upward derivative jumps for a weak zero-extended subsolution and a squared transverse mass exceeding 1/8. It is zero at the two obstacles and supported in the narrow strip. Monotone bounded-domain exhaustion yields one equilibrium U dominating that profile, so the finite neck has squared mass strictly above 5000.

For the other solution the unconstrained variational problem is legitimate after the stated globally bounded odd extension: clipping absolute values and values above one lowers energy, preserving a true global minimizer and its stability. Suppressing its middle channel part with a cutoff costs only the two end collars. The Caccioppoli calculation gives the numerical energy bound 225/2; the sliced interval coercivity therefore gives neck squared mass at most 4500. Stability passes locally to the limit. A zero limit would force the Dirichlet spectral infimum of the exterior to be at least f'(0)>0, contradicted by test balls arbitrarily far from the obstacles. Hence the limiting minimizer is positive and distinct from U.

Appendix A verifies interior regularity and continuous zero values on both complete circles through an explicit annular supersolution. The stability and strong maximum arguments exclude both zero and one as invalid limiting equilibria. Both constructions are therefore solutions on the full exterior, not only on a truncated channel.

The original question in [Berestycki–Graham's 2026 article](https://doi.org/10.1007/s00205-026-02168-6), §8.5, is correctly credited. The elliptic notes reference explicitly identifies its 2020 author version; its theorem locators are not silently attributed to the later edition. The imported trace, compactness, truncation and local Poisson/Schauder tools are used in their standard bounded smooth domain setting. All geometry, energy constants and nonvanishing arguments needed for the counterexample are included.
