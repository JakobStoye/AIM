# 214. Optimal spectral signings of regular graphs

**Area:** Spectral graph theory / network design

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

For an integer $`d\ge2`$, let $`G=(V,E)`$ be any finite simple undirected $`d`$-regular graph. A signing is a map $`s:E\to\{-1,1\}`$. Its signed adjacency matrix is the real symmetric matrix

```math
(A_s)_{uv}=\begin{cases}s(\{u,v\}),&\{u,v\}\in E,\\0,&\text{otherwise}.\end{cases}
```

Does every such graph admit a signing for which every eigenvalue $`\lambda`$ of $`A_s`$ satisfies

```math
|\lambda|\le2\sqrt{d-1}?
```

Both ends of the spectrum must satisfy the bound.

## Application

A signing defines a two-sheeted graph lift: positive edges stay in the same sheet and negative edges cross sheets. This conjecture would let network designers double a regular network while controlling all newly introduced spectral modes at the optimal universal-cover threshold.

## References

1. Yonatan Bilu and Nathan Linial, [*Lifts, discrepancy and nearly optimal spectral gap*](https://www.wisdom.weizmann.ac.il/~dinuri/courses/20-expanders/projects/bilu-linial.pdf), *Combinatorica* 26 (2006), 495–519, Conjecture 3.1, p. 500. Original conjecture and its graph-lift interpretation.
2. Zhiqiang Xu and Xinyue Zhang, [*An Improved Upper Bound for the Bilu–Linial Conjecture via Interlacing Families*](https://arxiv.org/abs/2606.28797), preprint, 27 June 2026, abstract and introduction. General two-sided bound with an extra factor $`\sqrt3`$.
3. Vaibhav Suvagiya, [*Parity families and a kernel-averaged L-function for near-Ramanujan signings*](https://arxiv.org/abs/2607.17343), preprint, 19 July 2026, abstract and main results. Approximate bounds under additional graph hypotheses.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: negative

[Proof or source](https://arxiv.org/pdf/2609.15591v4) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_90_114.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** Independent review of the complete external proof remains outstanding.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-214). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-13)

**Known cases:** The optimal two-sided spectral signing bound is established for bipartite regular graphs.

**Remaining target:** The same optimal two-sided bound for every finite simple regular graph.

**Literature check:** Open in cited literature; no later resolution located.

The bipartite case is known, because a one-sided signing bound then controls both spectral ends. The June 2026 general result gives $`2\sqrt{3(d-1)}`$, which leaves the requested constant unresolved. The July preprint imposes structural hypotheses and allows an error factor; its companion result on specific circulants does not cover all regular graphs.

**Search audit:** Searched “Bilu Linial conjecture solved proof signing 2026”, “two-sided Ramanujan signings”, and June–September 2026 follow-ups, including arXiv:2607.17343 and arXiv:2607.18334. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
