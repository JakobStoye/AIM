# AIM 380: independent audit of PR #151

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [0f1a72e90159ed4a58c53276e05ffd91632d2936](https://github.com/MColbrook/AIM/pull/151), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. Critical Dirichlet spectral equality can coexist with a bounded positive strong-KPP equilibrium on a uniformly smooth unbounded domain.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The domain is fixed in dimension 21, between the graphs z=+/-arccos(-50/(1000+|x|^2)). It is connected and unbounded with uniformly bounded graph derivatives and uniform separation. The logistic reaction on [0,1], extended above one by 1/s-1, has the exact globally C^(1,gamma) signs and strictly decreasing quotient required by AIM380.

Lemma 2.1 was recomputed. Vertical interval Poincaré produces a deficit at most 80/(1000+|x|^2); horizontal twenty-dimensional Hardy energy supplies 81/|x|^2. Their difference proves the compact-test spectral infimum is at least one. Compact product tests in the contained width-pi slab give the reverse bound, including the vertical cutoff limit. Thus lambda_1=f'(0)=1 exactly, rather than asymptotically.

For t=1000+|x|^2, v=cos(z)/t+50/t^2 is positive in the domain, vanishes on its boundary, is uniformly below one, and has residual Delta v+v>=6/t^2 while v^2<=441/(400t^2). It is therefore a strict global subsolution. Ordered iteration on bounded truncations produces v<=U_R<=1. The weak Dirichlet equations, dominated convergence and the energy difference identity justify the iteration limit; local Schauder estimates and a diagonal subsequence yield a classical positive entire-domain solution.

Crucially the final boundary value is proved, not inferred from interior convergence: in the collar q=cos z+b between zero and 1/4, the explicit function (1-exp(-4q))/(1-exp(-1)) is a uniform supersolution, dominates v and the artificial collar boundary, and vanishes on the true boundary. Passing this comparison gives continuous zero trace at every physical boundary point. This supplies an actual counterexample to nonexistence with all original hypotheses.

The exact conjecture is [Berestycki–Graham, Conjecture 1.7](https://arxiv.org/abs/2212.06611v1). Related [Rossi–Tough work](https://arxiv.org/abs/2610.17121v1) is contextual rather than a substitute for uniform-boundary verification. The Fernández-Real–Ros-Oton elliptic notes and Hunter's Lax–Milgram theorem supply only standard bounded-domain and local regularity inputs; their hypotheses are met by identity principal coefficients, bounded data and fixed smooth patches. No optimal-dimension or dynamical assertion is inferred.
