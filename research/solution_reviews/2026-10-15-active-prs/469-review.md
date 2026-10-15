# AIM 469: independent audit of PR #155

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [13ab904c45cb6205f534546826d0b88208834692](https://github.com/MColbrook/AIM/pull/155), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. The regional superlinear SKT strong solutions converge along one global subsequence to a genuine no-flux local weak solution for every fixed s>1.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The theorem keeps the original dimension/species ranges, all fixed s>1, positive linear diffusivities, symmetric interactions, prescribed piecewise strict diagonal condition, reaction coefficients, normalized kernels and bounded BV initial data. It derives strong space-time Lp convergence for every p<2s, which includes the requested L1 convergence. No endpoint s=1, rate, uniqueness or whole-family convergence is claimed.

The power-entropy coercivity was recomputed in entropy variables u^(s-1). The off-diagonal pair estimate leaves the stated positive margins, and integrating along entropy-variable segments gives coercivity in differences of u^(s/2) and u^s, including vacuum by continuity. Ponce's mean-restored inequality yields higher integrability L^(2s), not a false bound on arbitrary means.

The regularized logarithmic entropy supplies the additional unweighted and species-weighted square-root difference energy. Its low/high estimate absorbs negative cross terms using the positive linear diffusion, with remaining terms controlled by the power entropy. The product pressure quotient is then bounded in Lr, r=4s/(3s+1)>1, by the weighted square-root energy and L^(2s) factors. This yields the time derivative in the dual of W^(1,r'), including arbitrary boundary-valued test functions.

The nonlinear Ehrling argument combines spatial compactness of u^s with the negative time norm to prove actual L1 space-time compactness. Higher integrability upgrades this below 2s; since s+1<2s and 2<2s, the actual pressures and reactions converge strongly in L1. Interior quotient tests identify the weak pressure gradient, then strong convergence of smooth test quotients up to the boundary gives the first-order no-flux identity for arbitrary boundary values. The initial term and weak Ls continuous representative follow from the same time estimate. Thus the limit is not merely a second-order distributional solution with an unverified boundary condition.

I checked the primary [Ponce paper](https://ems.press/content/serial-article-files/31515), Theorems 1.1–1.3. The normalized probability kernels and the one-dimensional dilation-infimum hypothesis are exactly those in Lemma 2.2, and a connected one-dimensional domain is an interval. The current [Hopf–Jüngel–Parton source](https://arxiv.org/html/2609.09921v1), Theorem 1 and assumptions, supplies the fixed-epsilon strong solutions used only before deriving uniform estimates. Its strong norms are not assumed uniformly bounded. The density, product, time and boundary limit arguments are supplied here; the earlier linear-rate convergence reference is contextual.
