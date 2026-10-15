# 325. A constant bound for fixed-order prefix discrepancy

**Area:** Discrepancy, cumulative allocation and integer optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Does there exist an absolute constant $`C>0`$ with the following property? For every pair of positive integers $`d,T`$ and every ordered sequence $`v_1,\ldots,v_T\in\mathbb R^d`$ with Euclidean norms $`\|v_i\|_2\le1`$, one can choose signs $`\varepsilon_1,\ldots,\varepsilon_T\in\{-1,1\}`$ such that

```math
\max_{1\le k\le T}
\left\|\sum_{i=1}^{k}\varepsilon_i v_i\right\|_\infty
\le C,
\qquad
\|z\|_\infty=\max_{1\le j\le d}|z_j|?
```

The order is fixed. The signs may depend on the entire sequence, but the same signs must work for every prefix and coordinate. The constant must be independent of $`d`$, $`T`$ and the vectors. This is the strong, or prefix, Komlós conjecture. No online decision rule or efficient algorithm is required. [1, 2]

Taking $`k=T`$ gives only terminal-sum control. Controlling each prefix with a separately chosen signing would not answer the stronger question here.

## Application

View each vector as the feature or resource contributions of one indivisible item in a prescribed sequence. Its sign assigns it to one of two groups. The prefix sums then measure cumulative imbalance at each stage, so the conjecture asks for a uniform buffer independent of the number of items and tracked resources. Equivalently, putting $`x_i=(1+\varepsilon_i)/2`$ rounds a half-allocation to whole items with coordinate error at most $`C/2`$ at every prefix. These are interpretations of the stated model. Prefix discrepancy also feeds into Steinitz rearrangement bounds, which have applications in integer programming and scheduling. [1, §1] An existence result alone would not supply an efficient allocation algorithm.

## References

1. Nikhil Bansal, Haotian Jiang, Raghu Meka, Sahil Singla and Makrand Sinha, *Prefix Discrepancy, Smoothed Analysis, and Combinatorial Vector Balancing*, ITCS 2022, LIPIcs 215, 13:1–13:22, [publication record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2022.13). Accessible [arXiv:2111.07049v1](https://arxiv.org/html/2111.07049v1), November 13, 2021: §1, Theorems 1.1–1.6, and §6 Open Problem 6.1.
2. Sankeerth Rao Karingula and Shachar Lovett, *An elementary proof of the Komlos conjecture*, [ECCC TR26-188](https://eccc.weizmann.ac.il/report/2026/188/), September 17, 2026, preprint. [Full text](https://eccc.weizmann.ac.il/report/2026/188/download), §1, Theorem 1.2 and Conjecture 1.6, pp. 1–3.
3. Shengtao Guo, Ethan X. Fang and Junwei Lu, *Vector Balancing via Directional Total Variation*, [arXiv:2609.11189v1](https://arxiv.org/html/2609.11189v1), September 10, 2026, preprint, Theorem 1.1, Corollary 1.2 and §1.2.
4. Ishaq Aden-Ali, *Optimal Online Discrepancy Minimization in Linear Time*, [arXiv:2607.04388v1](https://arxiv.org/html/2607.04388v1), July 5, 2026, preprint, §1, Theorems 1–2 and Corollary 3.
5. Antonios Hmadi, *Online balancing of vectors with small coordinates*, [arXiv:2608.12490v1](https://arxiv.org/html/2608.12490v1), August 12, 2026, preprint, Theorems 1.1–1.2, Proposition 6.2 and Theorem 7.1.
6. Gleb Smirnov and Roman Vershynin, *Discrepancy and Fisher information*, [arXiv:2605.13107v1](https://arxiv.org/html/2605.13107v1), May 13, 2026, preprint, §§1.1–1.4 and Theorem 1.1.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-325). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-18)

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-18. The independently authored source [2, Conjecture 1.6] explicitly retains this question. The September manuscripts [2, 3] claim universal constants for the final sum and explicitly distinguish that result from controlling all prefixes.

For general fixed inputs, [4, Theorem 2] gives an $`O(\sqrt{\log(2T)})`$ prefix bound at fixed positive success probability, with an online algorithm. Its online optimality does not establish an offline lower bound. The smoothed-input theorem and branching-path counterexamples in [1] change, respectively, the input assumptions and the family of constraints.

The constant bounds in [5] require sufficiently small coordinates; their failure estimates can be vacuous without that restriction. Its lower bound concerns online signing, while the signs here may use future vectors. Source [6] permits discarding some terms, which this question forbids.

The [evidence record](../research/expansion-2026-09/candidates/strong-komlos-prefix-discrepancy.json) also compares complex colors, adaptive games, partial colorings and structured flow/assignment rounding at full relevant statement level. Historical results were read through explicit scholarly restatements where noted. Source research and a separated adversarial self-pass examine scope and status, without certifying the complete technical proofs.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 4 audit](../research/expansion-2026-09/batch-04-review.md). No matching later resolution was located.
