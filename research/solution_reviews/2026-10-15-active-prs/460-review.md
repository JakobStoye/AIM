# AIM 460: independent audit of PR #156

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [21242c912966a018dfa8f0f48f61f493b67f1cda](https://github.com/MColbrook/AIM/pull/156), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. Positive integrable-growth harmonic profiles outside every admitted convex cone are proportional, including singular spectral measures.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

The operator, factor 1/2, all n>=2 and 0<s<1, even finite nondegenerate measure, proper closed convex cone and separate growth exponents below 2s agree exactly with AIM460. No homogeneity or directional monotonicity of the profiles is assumed.

I reconstructed the viscosity/distributional interface, including tail-integrable mollification, strict comparison and the bounded-ball Dirichlet bridge. The stopped-process formula is justified by the finite-measure Lévy construction, full support from spanning jump directions, strong Markov and quasi-left-continuity, and polynomial exit integrability at an exponent strictly between profile growth and 2s. Exit times are bounded by a large-jump exponential time. Thus optional stopping does not assume bounded harmonic data or overlook exit overshoots.

The boundary compactness argument uses stable scaling and full support to obtain cone entry arbitrarily soon on a germ zero-one event. Convexity translates this to vanishing exit time as the starting point approaches the cone, and the moment/tail barrier gives uniform boundary smallness for every normalized profile. Interior Hölder estimates and this boundary bound give compactness on closed balls. A ball barrier gives the uniform lower bound c distance^q, with one q between s and 2s.

For an individual profile, choose a growth exponent p above its growth and q but below 2s. The scale maximizing U(R)/R^p exists. Rescaling at that scale produces a member of the compact normalized class; evaluation at one fixed interior point and the distance lower bound control the entire weighted growth norm by that point value. This is the critical uniform-tail estimate. An annular forcing function then compares normalized profiles on a ball, and dilation makes the ratio bound global. For kappa=inf(u/v), a nonzero nonnegative harmonic difference u-kappa v would itself be positive and globally comparable, forcing its ratio above zero and contradicting the infimum. The difference must vanish.

The downloaded primary [Fernández-Real–Ros-Oton book, arXiv:2411.12455v1](https://arxiv.org/abs/2411.12455v1) was checked at Definitions 2.1.18/2.1.21, Theorems 2.4.3, 2.4.15(b), 2.6.12 and Lemma B.1.4. These results genuinely permit general spectral measures; their constants and polynomial tail spaces fit the proof. The ball barrier gives q in (s,2s), as needed. Schilling's Lévy framework is used with process generator -L and explicitly controlled moments. The angular-density hypotheses in earlier Ros-Oton–Weidner comparison results are not imported. The audit supports the full target, including atomic directions.
