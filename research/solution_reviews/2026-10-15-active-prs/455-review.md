# AIM 455: independent audit of PR #166

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [cfac7195abf3194016de5c355177b472df8859f2](https://github.com/MColbrook/AIM/pull/166), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. The entire smooth-transport variational SPDE class has a deterministic positive parabolic Hölder exponent on each positive-time strip.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The statement includes nonsymmetric merely measurable diffusion, progressively measurable transport fields, countably many independent Brownian motions, no commutation assumption and arbitrary prescribed smooth initial data. The exponent depends only on permitted deterministic data; the norm and chart sizes may be random and unbounded.

The stochastic cancellation was recomputed with the actual Itô flow drift (1/2) sum b_k dot grad b_k and diffusion -b_k. For v=u composed with the flow, S=a-(1/2)sum b_k tensor b_k is the remaining diffusion, and q=(1/2)sum(div b_k)b_k is the residual drift before pullback. The Piola change gives A=K(S composed with flow)K^T and c=A^T grad(log J)+K(q composed with flow). The transpose is necessary for nonsymmetric a and is correctly retained. The Sobolev Itô–Wentzell hypotheses are satisfied by u in L2H1, its L1H^(-1) drift and L2 ell2 noise, so no pointwise differentiability of the rough diffusion is used.

The decisive deterministic step is local constant affine normalization at each point by the actual invertible matrix K. Continuity makes L^(-1)K close to identity on a sufficiently small random cylinder, fixing lower/upper ellipticity at nu/4 and 4(M+M^2/2). Shrinking its radius also normalizes the bounded random drift. Both truncation signs and every level satisfy the De Giorgi energy class inequality, including its initial-slice form. The exponent from that class is therefore deterministic and uniform, although neighborhoods and resulting constants are not. Compact finite covering preserves this exponent. Backward cylinders and the true L2 continuous trace include the upper terminal face.

The inverse flow is spatially Lipschitz and temporally 1/4 Hölder on compact sets. Composing back yields time exponent alpha/4 and spatial alpha/2, the requested parabolic class. A fixed mollifier sequence and rational tests give an actual measurable representative agreeing with the variational process at every time, rather than an arbitrary unmeasurable pathwise selection.

I checked the primary [Agresti–Sauerbrey–Veraar PDF](https://arxiv.org/pdf/2511.12692v1), Assumptions 2.1/2.5, Theorems 2.3/2.6, Remarks 2.4/2.7, Proposition 2.8 and the distributional Proposition 2.14. It explicitly permits random time-measurable coefficients and countably many Brownian motions; the manuscript's spatial derivative bounds supply its flow regularity. [Liao](https://arxiv.org/pdf/2004.14324v1), Theorems 2.1 and 5.1, provides local boundedness and the fixed oscillation exponent for the proved class membership. The version-sensitive equation numbering is disclosed accurately. No moments for the random Hölder norm or flow volume preservation are claimed or needed.
