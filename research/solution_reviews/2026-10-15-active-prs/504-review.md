# AIM 504: independent review of PR #92

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#92](https://github.com/MColbrook/AIM/pull/92). Reviewed head: `01f7a36c56ffb3d94bf103a68c387ef6ac9efe9b`.

Outcome: **Solved** — The exact exponential excursion-height rate is kappa*beta throughout the specified strict subcritical interval.

Proof: [ising_disks_excursion.pdf](../../../research/solutions/504-ising-disks-excursion-tail/paper/ising_disks_excursion.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The finite stopped graph retains every state up to size T and preserves actual jump probabilities below T. The reversible weight beta^(#C-1) gives edge conductance beta^n, and the singleton has precisely four exits, so p_T=capacity/(4 beta). Dirichlet and flow bounds follow by finite summation by parts; the terminal cut gives the required upper exponential rate. For the lower bound, the rightmost-lowest port and the leftmost-lowest port produce only full-edge contacts, with two/three consecutive occupied quadrants, and all block homotopies paste while fixing the bridge and the pinned square. Each arbitrary size-m unrooted block is allowed, preserving a_m's full growth entropy. Cumulative column counts strictly increase and uniquely recover each completed parent and block word. This separates parents while allowing merging of microscopic paths within one parent. The resulting sum of squared flows and conductance lower bound give L beta^-L sum_j(a_m beta^L)^-j. Fixing m with a_m beta^(m+1)<1, taking T→infinity first, then m→infinity, gives the lower rate kappa beta. The ceiling step covers all thresholds, not a subsequence. Positive finite recurrence time yields the equivalent normalization.

## References and scope

The sole mathematical source is Baryshnikov–Onaran2410.22611v3 / JACT10(2026)article16. Definitions4.2/4.4 retain the local retraction constraint; Theorem5.1 has two deletable squares before pinning; Remark6.3 and equation6.4 identify unrooted polygon counts and rooted bound n a_n; Theorem6.5 and Definition7.2 supply ergodicity/finite mean recurrence. The extension of the source's t<1 support condition to t=1 uses closedness and continuity correctly. No stronger unproved mixing or enumeration statement is imported.

## Delivery checks

Read the complete source, README and target comparison. Visually inspected all five PDF pages. The package is entirely analytic; no numerical or formal certificate is claimed.
