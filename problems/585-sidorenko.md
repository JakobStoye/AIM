# 585. Sidorenko's lower bound for bipartite homomorphism counts

**Area:** Information theory and graphical models

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`H`$ be a finite simple bipartite graph with $`v`$ vertices and $`e\geq1`$ edges. For a finite simple graph $`G`$ on $`n\geq1`$ vertices, let $`\mathop{\mathrm{hom}}\nolimits(H,G)`$ count all maps $`f:V(H)\to V(G)`$ that preserve adjacency. These maps need not be injective. Define the edge density $`p=2|E(G)|/n^2`$.

Prove or disprove that, for every such pair of graphs,

```math
\frac{\mathop{\mathrm{hom}}\nolimits(H,G)}{n^v}\geq p^e.
```

This is Sidorenko's conjecture. It says that the density of any fixed bipartite pattern is at least the corresponding independent-edge baseline. The displayed inequality is the unweighted specialization of Conjecture I.1 in [1].

## Application

Homomorphism counts are partition functions of finite-state graphical models. A general lower bound gives a rigorous baseline for counting and approximate inference, and helps assess variational approximations such as the Bethe free energy. Entropy inequalities are one of the principal tools for proving the bound.

## References

1. P. Csikvári, N. Ruozzi, and S. Shams, [Markov Random Fields, Homomorphism Counting, and Sidorenko's Conjecture](https://doi.org/10.1109/TIT.2022.3169487), *IEEE Transactions on Information Theory* **68**(9) (2022), 6052–6062. Conjecture I.1 and the following unweighted specialization; [author manuscript](https://real.mtak.hu/162333/1/Markov_random_fields_Sidorenko.pdf), page 2.
2. Y. Zhao, [Conjugacy Class Averages and Sidorenko's Conjecture](https://arxiv.org/abs/2606.15368), arXiv:2606.15368 (2026).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf), result family 161 (2026). Statement locator: `Theorem 1.1, PDF page 1; Main theorem label thm:main, introduction.tex lines18-26; definitions lines1-15.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete counterexample to the original target.

**Statement comparison:** Main theorem explicitly produces a finite simple unweighted host G with at least one edge and a fixed finite simple bipartite incidence graph H with35 vertices and66 edges for which t(H,G)<p(G)^66. Definitions t=hom/n^v and p=2|E|/n^2 match AIM, including noninjective maps. Thus this is a complete negative resolution, not only a weighted or graphon counterexample.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-585) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/161.md). SidorenkoCounterexample comparator explicitly defines the22 triples, incidence graph, all homomorphisms and finite simple host deficit. Main declaration uses sorry; forcing consequence is outside selected Lean statement and irrelevant to AIM585. No local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/585-sidorenko.md).
