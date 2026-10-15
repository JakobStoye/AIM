# AIM 482: independent audit of PR #163

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [9aabeaaf7407f10ca578391fa632de4f2b1d3c32](https://github.com/MColbrook/AIM/pull/163), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. The unrestricted finite-entropy renormalized reaction–diffusion uniqueness assertion is false.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The example is exactly admissible: two species with unit diffusivity on the smooth three-dimensional unit ball, polynomial quasi-positive reaction (-b^2(a-b),b^2(a-b)), entropy shifts zero and initial concentrations (10000/|x|,0). The entropy sign is -b^2(a-b)(log a-log b)<=0. This datum belongs to L1 log L and L2; the target explicitly permits unbounded initial concentrations and missing species. No claim is made for bounded data.

The scalar total m is the Neumann heat evolution of C/|x|. Its explicit lower/upper comparison functions give C/sqrt(6t+r^2)<=m<=C/r+Cr^2/2+3Ct and uniformly vanishing small-ball mass. The compact self-similar seed t^(-1/2)(1-r^2/t)_+^2 is a weak subsolution up to time 1/4: its front is C1, so there is no omitted surface Laplacian measure. The two polynomial regimes in the displayed residual bound were recomputed with C=10000, and the seed is below m/2.

Starting at epsilon with this seed, scalar comparison for b_t=Delta b+b^2(m-2b) gives seed<=b<=m/2. Bounded positive-time total prevents finite-time blow-up. Analytic semigroup smoothing and compact interpolation give a nested diagonal positive-time limit, hence a global b that is not zero. The initial trace is a separate argument: cutoff mass away from the singularity is O(t exp(M_rho^2 t)), while the remaining small-ball mass is uniformly small. Sending t to zero and then rho to zero proves b(t)->0 in L1 and a(t)->a_0 in L1. It is not enough merely to note that each seed has small mass; the cutoff estimate supplies uniform trace control.

The regularized entropy estimate gives square-root gradients in L2 over every finite horizon. The entropy has the correct actual initial trace by a common radial integrable bound. Every compact-gradient renormalization has bounded reaction and gradient multipliers on its support, so the positive-time chain identity extends to zero using these Fisher bounds and the L1 trace. Thus both (m,0) and (m-b,b) belong to the full stated renormalized comparison class and differ on positive space-time measure. This is not a weak–strong uniqueness contradiction.

The [Fischer reference](https://arxiv.org/abs/1703.00730v1) is accurately limited to weak–strong uniqueness. Schnaubelt's primary linear/nonlinear notes were checked at the Neumann heat example, compact interpolation Proposition 2.13 and semigroup smoothing/local blow-up interface; smooth bounded balls and p=6 satisfy their assumptions. The submission intentionally supplies an anonymous manuscript, as its manifest states. Its blank author field is therefore not evidence of a mathematical omission; attribution should follow the PR metadata without inventing authorship.
