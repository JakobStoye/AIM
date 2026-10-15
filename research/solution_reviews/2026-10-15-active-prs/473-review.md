# AIM 473: independent audit of PR #158

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [60a2396440ccdeab2c3a0090c91d1164433845a5](https://github.com/MColbrook/AIM/pull/158), compared with the original a153f469ee0ea64e876b2ad97c79d252c19a3e22 target and current problem page.

**Decision:** Solved. Every weak dual solution in the stated spatial-L1 class conserves its initial mass at every finite time.

**Scope:** The entire manuscript, bibliography, package README, target comparison, AI disclosure and ancillary build/manifest material were read. The analytic proof was independently reconstructed; submission-internal AI reviews were not treated as evidence of correctness. Every submitted PDF page was visually inspected in the maintainer-rendered contact sheets. No clipping, missing mathematics, unreadable glyphs or broken cross-reference was found. Package hash and independent rebuild results are recorded separately by the maintainer.

Theorem 2.2 applies to every prescribed WDS, not only the semigroup/minimal solution. Its weighted continuity, compact dual tests and initial trace match AIM473 exactly. No boundedness, finite initial energy, uniform mass bound or global nonlinear integrability is added as an assumption.

Linear conservativeness follows from the ordinary Laplacian cutoffs under the lower Ricci bound and then subordination. The normalized spectral inverse G is reconciled explicitly with the printed Green-kernel normalization. Semigroup splitting gives its weak-Lp bound and heat-regularized boundedness.

The order-to-mass lemma is essential: Gh>=0 with h in L1 implies integral h>=0, although Gh need not be integrable. For a conservative resolvent T, the difference W-TW is integrable. Applying the positive-part inequality to (W-ell)_+, which is integrable by weak-Lp, and sending ell down to zero gives the mass sign. If W is integrable, conservativeness gives equality instead. This supplies the needed global mass information using only permitted compact dual tests.

Weighted continuity extends the potential equation to every time endpoint, yielding Gu(a)-Gu(b)=integral_a^b u^m>=0. The lemma gives a uniform mass upper bound and strong L1 initial trace. Heat regularization of u and its potential has finite energy even for arbitrary initial L1 data. The mixed terms cancel by symmetry; partitioned endpoint identities plus Fatou give positive-time dissipation without testing the WDS by an inadmissible nonlinear function. HLS and interpolation yield an energy-versus-dissipation exponent beta<1. The explicit scalar decay comparison removes dependence on the possibly infinite limiting initial energy. It follows that u^(m+1), and then u^m, is globally integrable on every positive interval. The potential difference is now L1, so the equality part of the order lemma proves identical masses at all positive endpoints. Strong initial L1 continuity identifies that mass with the initial one.

I checked [BBGM](https://arxiv.org/pdf/2109.10732v2), Lemma 5.2 and the heat/Green assumptions, and [Bianchi–Setti](https://arxiv.org/pdf/1607.06008v1), Corollary 2.3: curvature exponent zero gives precisely the Laplacian cutoff decay used. The source normalization factor is retained. The cited 2026 conservation result has its narrower constructed-solution/nonnegative-Ricci scope identified and is not used to identify the arbitrary WDS here. Spectral calculus and smooth-domain exhaustion are standard and the required consequences are shown in the manuscript.
