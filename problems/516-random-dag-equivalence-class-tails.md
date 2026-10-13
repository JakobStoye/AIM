# 516. Tail bounds for causal equivalence classes of uniform random DAGs

**Area:** Statistical inference and random graphical models

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\mathcal D_n`$ be the finite set of simple directed acyclic graphs on the labeled vertex set $`[n]=\{1,\ldots,n\}`$, and sample $`G_n`$ uniformly from $`\mathcal D_n`$. Its skeleton is the undirected graph obtained by forgetting edge orientations. A $`v`$-structure is a triple $`i\to k\leftarrow j`$ with $`i,j`$ nonadjacent. Define

```math
M(G)=\{H\in\mathcal D_n:H\text{ has the same skeleton and }v\text{-structures as }G\}.
```

This is the Markov equivalence class of $`G`$: its members encode the same conditional independence relations.

For every $`\varepsilon\in(0,1)`$, do constants $`C_\varepsilon<\infty`$ and $`t_\varepsilon>1`$ exist such that, simultaneously for every $`n\ge1`$ and every real $`t\ge t_\varepsilon`$,

```math
\Pr\bigl(|M(G_n)|>t\bigr)\le C_\varepsilon\exp\!\left[-(\log t)^{2-\varepsilon}\right]?
```

Here $`\log`$ is the natural logarithm. Prove this bound or refute it for some fixed $`\varepsilon`$. The distribution is uniform over labeled DAGs; uniform sampling of equivalence classes, or choosing an order and then random forward edges, gives different distributions.

## Application

Even exact observational independence information can leave several causal graphs indistinguishable. A tail bound quantifies how frequently this ambiguity becomes large under a specified model prior. It sharpens an average-size guarantee by controlling rare cases with many possible causal explanations. The uniform-DAG model chiefly describes dense graphs; the question does not claim the same behavior for sparse causal networks.

## References

1. D. Schmid and A. Sly, [On the number and size of Markov equivalence classes of random directed acyclic graphs](https://arxiv.org/abs/2209.04395v2), revised 28 September 2024, Theorem 1.1 and the open question immediately following it, p.2. [PDF](https://arxiv.org/pdf/2209.04395v2).
2. C. Squires and C. Uhler, [Causal Structure Learning: A Combinatorial Perspective](https://doi.org/10.1007/s10208-022-09581-9), Foundations of Computational Mathematics **23**, 1781–1815 (2023), p.1796, for the preceding average-size questions.
3. E. L. Jahn, F. Eberhardt and L. J. Schulman, [Lower Bounds on the Size of Markov Equivalence Classes](https://proceedings.mlr.press/v286/jahn25a.html), PMLR **286**, 1819–1836 (2025).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/kaiwen-jin-516/paper/main.pdf) establishes the full original target. Uniform labeled-DAG Markov equivalence-class tail with every required near-quadratic logarithmic exponent.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/516-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #75](https://github.com/MColbrook/AIM/pull/75) at `49687d565a727aeda3ae7a9134ad628a6fc48d4a`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
