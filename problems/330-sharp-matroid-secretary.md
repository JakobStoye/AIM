# 330. The sharp matroid secretary conjecture

**Area:** Online selection and resource allocation

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

A finite matroid is a pair $`M=(E,\mathcal I)`$, where $`E`$ is a finite set and $`\mathcal I\subseteq 2^E`$ contains $`\varnothing`$, is closed under taking subsets, and satisfies augmentation: if $`I,J\in\mathcal I`$ and $`|I|<|J|`$, some $`x\in J\setminus I`$ has $`I\cup\{x\}\in\mathcal I`$. Sets in $`\mathcal I`$ are called independent. [1, 2]

The algorithm knows $`E`$ and the matroid before arrivals, and may test independence of any subset. An adversary fixes nonnegative weights $`w:E\to[0,\infty)`$, hidden from the algorithm. The labeled elements then arrive in a uniformly random permutation $`\pi`$, independent of the weights. On seeing $`x`$, the algorithm learns $`w(x)`$ and must immediately accept or reject it. Decisions are irrevocable, and the accepted set must always belong to $`\mathcal I`$. [1–3]

Define

```math
\mathop{\mathrm{OPT}}\nolimits(M,w)=\max_{I\in\mathcal I}\sum_{x\in I}w(x).
```

Does every finite matroid $`M`$ admit a randomized online policy $`A_M`$, chosen without knowing $`w`$, such that for every $`w`$,

```math
\mathbb E_{\pi,A_M}\!\left[\sum_{x\in A_M(M,w,\pi)}w(x)\right]
\ge \frac{1}{e}\mathop{\mathrm{OPT}}\nolimits(M,w)?
```

Here $`e`$ is Euler's number. The expectation includes the arrival order and the policy's randomness. This is the strong matroid secretary conjecture in its usual expected-weight form. No polynomial running-time bound is imposed. Numerical values of arrived elements are allowed; requiring only comparisons, or requiring each element of a fixed optimal basis to be selected with probability at least $`1/e`$, would strengthen the requirement. [1, 2]

## Application

The model describes committing to valuable requests before future requests are known, subject to a combinatorial feasibility constraint. Matroids include capacity quotas and selecting network links without creating a cycle. Unlike offline selection, where sorting by value permits optimal greedy selection, the online decision maker must reserve capacity without seeing future values. The bound asks whether these constraints can impose a larger universal loss than the classical single-selection problem. [1, §1; 5, §1]

The remaining general question is foundational. Recent claims cover linear matroids and a broader class with modular extensions, including many common allocation models; they do not establish the assertion for every abstract matroid. An unrestricted existence theorem would settle the sharp information limit, but would not automatically provide an efficient allocation method. [4, 7]

## References

1. Kiarash Banihashem, MohammadTaghi Hajiaghayi, Dariusz R. Kowalski, Piotr Krysta, Danny Mittal and Jan Olkowski, *Beating Competitive Ratio 4 for Graphic Matroid Secretary*, ESA 2025, LIPIcs 351, 52:1–52:16. [Publication and full text](https://doi.org/10.4230/LIPIcs.ESA.2025.52), §1, p. 52:2; Theorems 1–2, p. 52:3.
2. José A. Soto, Abner Turkieltaub and Victor Verdugo, *Strong Algorithms for the Ordinal Matroid Secretary Problem*, Mathematics of Operations Research 46 (2021), 642–673, [DOI](https://doi.org/10.1287/moor.2020.1083). [Author manuscript](https://arxiv.org/abs/1802.01997), §§1–1.1: strong conjecture and distinct performance measures.
3. Sahil Singla, *The Matroid Secretary Conjecture is True*, [arXiv:2609.14555v1](https://arxiv.org/html/2609.14555v1), September 13, 2026, preprint. Theorem 3.1 and §4, “Improving the constant.”
4. Hamed Abdi, Kiarash Banihashem, MohammadTaghi Hajiaghayi and Danny Mittal, *On the Strong Matroid Secretary Conjecture and Beyond*, [arXiv:2609.19118v1](https://arxiv.org/html/2609.19118v1), September 16, 2026, preliminary preprint. Conjecture 1.1; Theorem 1.2; Corollary 1.4; §2; Appendix B.2, Theorem B.6.
5. Maryam Bahrani, Hedyeh Beyhaghi, Sahil Singla and S. Matthew Weinberg, *Formal Barriers to Simple Algorithms for the Matroid Secretary Problem*, WINE 2021, LNCS 13112, 280–298. [Author manuscript](https://arxiv.org/abs/2111.04114), §1 and Theorems 6 and 18.
6. José A. Soto and Felipe Valdevenito, *Secretary Problems with Interactive Ordinal Queries*, [arXiv:2609.19016v1](https://arxiv.org/html/2609.19016v1), 2026 preprint. §3.1, Definitions 3.6–3.7; Theorems 3.10 and 3.12.
7. Kristóf Bérczi, Shaddin Dughmi, Vasilis Livanos, José A. Soto and Victor Verdugo, *The Strong Secretary Conjecture is True for Linear Matroids*, [arXiv:2609.20797v1](https://arxiv.org/html/2609.20797v1), September 17, 2026, preprint. Theorem 1; §4, Corollaries 1–2 and the concluding scope discussion.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: affirmative

[Proof or source](https://arxiv.org/pdf/2609.30421v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_90_114.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** Independent review of the complete external proof remains outstanding.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-330). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-18)

**Literature check:** Open in cited literature; no later resolution located.

The explicit strong conjecture in [1, 2] is retained in September 2026 sources [3, 4]. Singla's Theorem 3.1 claims expected reward at least $`\mathop{\mathrm{OPT}}\nolimits/4`$ for arbitrary matroids, and §4 expressly leaves the factor $`e`$ open. Its suggested factor near $`3.16`$ is labeled unverified by the author and would still fall short. This catalogue does not count the weaker constant-factor question separately.

Theorem 1.2 of [4] claims the $`1/e`$ guarantee for linear matroids using finite, potentially expensive computation. Its general-matroid guarantee is $`1/64`$. Theorem 1.3 concerns a prophet model with independent value samples; its $`1/2`$ guarantee does not transfer unchanged to this input model. The truncation counterexample in Appendix B refutes monotonicity in rank, not the $`1/e`$ conjecture. These recent preprints are reported as claims; their proofs have not been independently certified here.

The concurrent paper [7] extends its claim to known matroids admitting a finitary modular extension. Its §4 explains that this assumption is not universal, giving the Vámos matroid as an example outside the covered class. The extension theorem therefore does not settle the stated general question.

The barriers in [5] restrict particular greedy and partition strategies. They do not exclude all online policies. The guarantees in [6] use oracle responses about unseen weights, which the present model does not provide.

Searches on September 18, 2026 covered the strong conjecture, both competitive-ratio conventions, proofs and counterexamples, 2025–2026 and unrestricted dates, revisions, corrections and author records. Exact queries, theorem comparisons, review results and access details are in the [evidence ledger](../research/expansion-2026-09/candidates/sharp-matroid-secretary.json).

The published DOI for [2] blocked the direct link check; its accessible author manuscript supplied the full formulation. Review was performed by the researching agent with a separated adversarial self-pass.

[Entry 316](315-online-bin-packing-optimal-ratio.md) minimizes bin count under adversarial arrival order. [Entries 279](278-unrelated-machine-makespan.md) and [280](279-general-santa-claus.md) concern offline scheduling and max-min allocation. [Entry 324](323-strong-thin-tree.md) asks for one tree satisfying all cut inequalities. None asks for this random-order selection guarantee.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 5 audit](../research/expansion-2026-09/batch-05-review.md). No matching later resolution was located.
