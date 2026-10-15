# 298. The Li–Li multiple-unicast conjecture

**Area:** Applied geometry, control and information

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

Let $`G=(V,E)`$ be a finite connected undirected graph with capacities $`c_e\geq0`$. Specify finitely many sessions $`(s_i,t_i)`$, with $`s_i\ne t_i`$. Session $`i`$ has its own independent message, initially known at $`s_i`$, and requests its exact recovery at $`t_i`$.

Use noiseless links and causal network coding: each transmitted symbol may be any function of the sender's initial messages and previously received symbols. Both directions of an edge share its capacity. Define the zero-error throughput region $`\mathcal C_{\mathrm{NC}}`$ by arbitrary finite block protocols and asymptotic packet scaling: at scale $`b`$, messages have $`br_i`$ symbols and edge $`e`$ carries at most $`bc_e`$ symbols in total, with integer rounding and closure as $`b\to\infty`$. A common finite alphabet may be chosen for each protocol. There is no additional completion-time constraint.

For each session, let $`\mathcal P_i`$ be its set of simple source-to-destination paths. Its fractional routing region is

```math
\mathcal C_{\mathrm{MCF}}=
\left\{r\geq0:\ \exists x_{i,P}\geq0,\quad
\sum_{P\in\mathcal P_i}x_{i,P}\geq r_i\ \text{for all }i,\quad
\sum_i\sum_{\substack{P\in\mathcal P_i\\e\in P}}x_{i,P}\leq c_e\ \text{for all }e
\right\}.
```

Is $`\mathcal C_{\mathrm{NC}}=\mathcal C_{\mathrm{MCF}}`$ for every such graph, capacity assignment and session collection? Equivalently, can coding ever increase independent-unicast throughput over fractional routing? Coding need not be linear, and terminal locations may be shared across sessions. [1, 2, 5]

## Application

The question determines whether routers can increase sustained data-transfer rates by mixing independent streams instead of optimally splitting and forwarding packets. It connects the information-theoretic performance of a bidirectional communication network to a multicommodity-flow optimization problem. [1, 2]

## References

1. Zongpeng Li and Baochun Li, *Network Coding: The Case of Multiple Unicast Sessions*, 42nd Allerton Conference, 2004, §3.2, especially the conjectural Proposition 3.1, pp. 4–6. [Author manuscript](https://iqua.ece.utoronto.ca/papers/allerton04.pdf).
2. Sirui Liu, Li Que, Zongpeng Li and Baochun Li, *On the Multiple-Unicast Conjecture: Beyond Cut Metrics*, arXiv:2608.06070v1, 6 August 2026, §III, Conjecture 1; Theorems 4–8. [Full text](https://arxiv.org/html/2608.06070v1).
3. Mark Braverman and Zhongtian He, *Undirected Multicast Network Coding Gaps via Locally Decodable Codes*, arXiv:2510.18737v1, 21 October 2025, §1, Theorem 1.1 and Appendix A. [Full text](https://arxiv.org/html/2510.18737v1).
4. Sirui Liu, Zongpeng Li, Xiying Fan and Haifeng Chen, *A Session Interaction Framework for The Multiple-Unicast Conjecture*, arXiv:2608.06042v1, 6 August 2026, Theorems III.2–III.7. [Full text](https://arxiv.org/html/2608.06042v1).
5. Bernhard Haeupler, David Wajc and Goran Zuzic, *Network Coding Gaps for Completion Times of Multiple Unicasts*, FOCS 2020; author manuscript, Theorems 1.2–1.3 and Appendix A. [Full text](https://www.cs.cmu.edu/~dwajc/pdfs/haeupler19.pdf).
6. Cheuk Ting Li, *Undecidability of Network Coding, Conditional Information Inequalities, and Conditional Independence Implication*, IEEE Transactions on Information Theory 69(6), 2023, 3493–3510, DOI [10.1109/TIT.2023.3247570](https://doi.org/10.1109/TIT.2023.3247570). Scope checked in [arXiv:2205.11461v3](https://arxiv.org/pdf/2205.11461v3), §IV, Theorems 22–23.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: negative

[Proof or source](https://arxiv.org/pdf/2610.10108v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_90_114.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** Independent review of the complete external proof remains outstanding.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-298). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-17)

**Literature check:** Open in cited literature; no later resolution located.

The August 2026 formulation [2] still treats the general conjecture as open. Its positive results restrict the terminal count, planar embedding, session pattern or number of coding nodes; its final reduction is conditional. Independent corroboration [3] explicitly distinguishes the unresolved unicast problem from its multicast separation. Multicast lets several destinations request the same message and is a different demand model.

The interaction framework [4] gives an equivalence and sufficient structural conditions, leaving universal independence of irreducible cores unproved. The completion-time separation [5] concerns finite packet demands; it does not establish an asymptotic throughput separation. The undecidability theorem [6] uses directed acyclic networks with general message demands and does not settle this undirected subclass. The equivalent transmission-cost formulation is included in this single entry.

The [evidence record](../research/expansion-2026-09/candidates/li-li-multiple-unicast.json) documents exact searches, source access, scope comparisons, duplicate screening and the separate adversarial self-review.

The September 17, 2026 review included named and mathematical formulations, author/citation searches, 2025–2026 results, and unrestricted proof, counterexample, resolution and correction searches; these were refreshed before integration.
