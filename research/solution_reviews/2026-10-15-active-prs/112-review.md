# AIM 112: independent review of PR #135

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#135](https://github.com/MColbrook/AIM/pull/135). Reviewed head: `2d843e8dc4c0ce3b341bbcf44a9d7fc36c744bfa`.

Outcome: **Solved** — The affirmative result covers every admissible prescribed embedded boundary, including curves and filling codimension one.

Proof: [manuscript.pdf](../../../research/solutions/112-fixed-embedded-boundary-steklov/paper/manuscript.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The Rayleigh comparison uses exactly the same boundary measure and zero-mean constraint. Its factor tends to one as the relative metric error tends to zero. For n>=2 a conformal enlargement equal to one on the boundary cannot reduce the quotient.

I reconstructed Lemma 2.2 as a finite primitive-metric argument, rather than assuming an exact smooth isometric embedding. Smooth square amplitudes are obtained by multiplying the compactly supported defect factor by a square partition of unity and positive cone coefficients. On each flow box the longitudinal formal vector is unit for the enlarged metric and genuine where the amplitude vanishes. The parameter-relative and endpoint-relative clauses preserve an open neighborhood of the entire box boundary. Local embedding plus positive separation of the changed compact support from the distant unchanged image preserves global injectivity. At each finite step the new target is the current induced metric plus the next primitive term, so the errors telescope; their sum can be made arbitrarily small relative to the final positive metric. Local normal fields suffice even when the full normal bundle is nontrivial.

For Proposition 2.3 I checked the boundary-fixing collar change matches the full metric at the boundary, including the normal and cross terms. Thus replacing the metric by the original induced metric on a sufficiently small collar is uniformly small for each chosen metric. With chi=psi^2 and k>=c e, the manuscript's enlargement satisfies h-e=chi B with B>= [Kc-(1-c)]e>0. It has unchanged boundary metric, increases the Steklov quotient and meets Lemma 2.2. Choosing the collar and finite errors separately for each threshold is legitimate; a uniform collar over the diverging intrinsic sequence is unnecessary.

For filling dimension at least three the conformal source applies to any starting filling. In dimension two the generic three-dimensional projection is injective and immersive by the stated dimension counts. A Seifert surface for the projected knot lifts as a graph with the original curve as exact boundary; a boundary normal section extends smoothly into the surface. Local interior handles give every sufficiently large orientable genus in the same ambient space. The connected-boundary expander construction can use orientation-reversing circle gluings and genus-zero pieces; removing the tree neighborhood retains orientability and one boundary component. Length rescaling and a boundary arclength map extended over a collar then give precisely the required tangential metric on the chosen embedded filling. The surface classification and metric transfer complete the arbitrary-curve case.

## References and scope

All seven bibliography entries and their uses were checked. The primary [Eliashberg–Mishachev text](https://virtualmath1.stanford.edu/~eliash/Public/257B-2020/intro.pdf), Lemma 21.6.1, explicitly provides epsilon-isometric embeddings for n<m; Lemma 17.5.1(c),(d) and the following endpoint remark supply the required relative control. The finite decomposition is Lemma 21.3.1. The primary [Colbois–El Soufi–Girouard source](https://arxiv.org/html/1701.04125v2), Theorem 1.1(ii), has the required n>=3 fixed-boundary conformal conclusion. The primary [Colbois–Girouard–Raveendran source](https://arxiv.org/pdf/1612.07665), Theorem 7, Section 6.4 and Remark 37, supplies one boundary component and the linear genus lower bound; the orientable gluing choice was checked from its construction. Source sigma_2 is correctly translated to the manuscript's first positive sigma_1.

The [Oberwolfach report](https://ems.press/content/serial-article-files/47475), printed p.2075, already announces the relative Nash–Kuiper transfer with Polymerakis and its circle application. The submission expressly credits this, including in its abstract, and makes no priority claim for that mechanism. Hirsch and Seifert are standard topology dependencies; the needed projection, lift, handle, collar and boundary-map operations are also supplied in the manuscript. No missing proof-critical reference or incorrect scope was found.

## Delivery checks

Read the complete 578-line TeX manuscript, all target-comparison rows, README and BUILD instructions. Visually inspected all eight rendered PDF pages in sheet-1.jpg: title, equations, proof continuations and references are legible and complete, with no clipped content. Root separately owns the fresh build, source/PDF comparison and manifest/hash checks. The audit is analytic and claims no numerical or Lean verification.
