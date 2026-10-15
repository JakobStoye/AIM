# AIM 383: independent audit of PR #148

Date: 2026-10-15. Reviewer: independent OpenAI Codex AI context; no human or Lean verification is claimed.

Pinned submission: [09b60bb381c35eb5567fb251c6cf6a33f13ba220](https://github.com/MColbrook/AIM/pull/148), compared with the current problem page and its cited a153f469ee0ea64e876b2ad97c79d252c19a3e22 statement.

**Decision:** Solved. Finite-cluster mass is continuous and equals one at every finite positive onset of Flory gelation in the stated kernel class.

**Scope:** The entire submitted manuscript, package README, target comparison, disclosure and build instructions were read. This mathematical report is separate from the maintainer package checksum, rebuild and PDF-render records; it does not claim visual checks that have not been recorded.

The entire original weak formulation and all quantifiers are retained. Total coagulation and gel-loss rates are bounded using $`x^\alpha\le1+x`$. Equality on compact continuous tests determines equality of finite measures, giving the bounded-Borel identity and total-variation time estimate. The measure-kernel argument justifies subsequent time-space integration; telescoping yields bounded time-dependent tests. No higher moment is silently assumed.

For the clipped first moment, the defect bound is $`KD_R\le2CR^\alpha xy`$. Gel loss has the same scale, so its decrease over a duration h is at most $`ChR^\alpha`$, including across a possible jump. The concave test has uniformly integrable defect and gives $`\kappa\int H_R^2\le R^{-\alpha}`$. Before onset, mass conservation and the decreasing truncated mass make the complementary tail nondecreasing; this yields the upper tail bound without presupposing continuity at onset.

The decisive new bounded exponential test was reconstructed. For $`f_r(x)=\mathbf1_{[R,\infty)}e^{-a(r)x/R}`$ and $`a(r)=e^{2C(t-r)R^\alpha}`$, its time derivative absorbs both the coagulation loss and the gel loss. The estimate $`y^\alpha(1-e^{-qy})\le q^{1-\alpha}y`$ is valid on both sides of qy=1. Every test, time derivative and separated gain/loss integral is bounded and integrable at fixed R. This gives a strictly positive band-retention fraction independent of R.

A hypothetical onset jump delta forces a delta/2 lower tail at size R, while choosing a fixed larger multiplier A leaves at least delta/4 in [R,AR] at time $`T-dR^{-\alpha}`$. The retention estimate then forces a fixed positive tail of the single finite measure Q_T at arbitrarily large R, impossible. The supremum of continuous clipped moments gives lower semicontinuity, hence right continuity for the nonincreasing mass. Both endpoints therefore agree with one.

The sole research reference, Fournier–Laurençot arXiv:0706.2057v1, Proposition 2.3 and its following question, was checked in the primary full text. The prior after-onset theorem is credited accurately. The actual endpoint argument is proved in this submission, not supplied by that prior theorem. No computational certificate or uniqueness premise is needed.

**PDF visual check:** Every submitted PDF page was subsequently inspected in the maintainer-rendered contact sheets. No clipped content, missing mathematics, unreadable glyph or broken cross-reference was found. The independent rebuild and checksum evidence is recorded separately.
