# 337. Reed's bound for the chromatic number

**Area:** Combinatorial optimization and conflict scheduling

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-13

## Problem statement

Let $`G=(V,E)`$ be any finite nonempty simple undirected graph. Write $`\Delta(G)`$ for the maximum vertex degree and $`\omega(G)`$ for the largest number of pairwise adjacent vertices. A proper $`k`$-colouring is a function $`c:V\to\{1,\ldots,k\}`$ satisfying $`c(u)\ne c(v)`$ whenever $`\{u,v\}\in E`$. The chromatic number $`\chi(G)`$ is the smallest such $`k`$.

Prove or disprove **Reed's colouring conjecture**:

```math
\chi(G)\leq
\left\lceil\frac{\Delta(G)+1+\omega(G)}{2}\right\rceil
\qquad\text{for every finite nonempty simple undirected graph }G.
```

The bound concerns ordinary integral colourings with a common palette, at every finite graph size and degree. It requires neither a large-degree hypothesis nor a restriction on induced subgraphs. The target is existence of a colouring, without an algorithmic running-time requirement. The ceiling cannot simply be removed: a cycle on five vertices has $`\Delta=2`$, $`\omega=2`$ and $`\chi=3`$. [1–3]

## Application

Consider unit-duration tasks with pairwise incompatibilities: vertices represent tasks, an edge means two tasks cannot run in the same slot, and colours represent slots. A proper colouring is exactly a feasible schedule in this model. A clique requires that many separate slots, while the elementary greedy argument guarantees at most $`\Delta+1`$ slots. The conjecture asks whether the rounded average of these lower and upper bounds always suffices.

This would give a universal guarantee for arbitrary conflict patterns. The connection is to the number of slots whose existence can be guaranteed; the conjecture by itself supplies neither an efficient way to compute a maximum clique nor a polynomial-time scheduling algorithm. Durations, precedence constraints and job-specific availability lists are outside this model.

## References

1. Marthe Bonamy, Thomas Perrett and Luke Postle, *Colouring Graphs with Sparse Neighbourhoods: Bounds and Applications*, [arXiv:1810.06704v1](https://arxiv.org/html/1810.06704v1), October 15, 2018. Cited preprint version: §1, Conjecture 1.1 and Theorem 1.7.
2. Eoin Hurley, Rémi de Joannis de Verclos and Ross J. Kang, *An Improved Procedure for Colouring Graphs of Bounded Local Density*, Advances in Combinatorics **2022:7**, 33 pp. [DOI](https://doi.org/10.19086/aic.2022.7); [published-version PDF, arXiv:2007.07874v3](https://arxiv.org/pdf/2007.07874v3), September 10, 2022. §1.2, Conjecture 1.7 and Theorem 1.10; §3.2, Theorem 3.2 and Remark 3.1.
3. Ken-ichi Kawarabayashi and Lucas Picasarri-Arrieta, *Coloring digraphs with $`\tilde{\Delta}-b`$ colors*, [arXiv:2607.06928v1](https://arxiv.org/html/2607.06928v1), July 8, 2026, preprint. §1, Conjectures 1 and 4, Corollary 3 and Theorem 7.
4. Andrew D. King and Bruce A. Reed, *Claw-free graphs, skeletal graphs, and a stronger conjecture on $`\omega`$, $`\Delta`$, and $`\chi`$*, [arXiv:1212.3036v1](https://arxiv.org/pdf/1212.3036v1), December 13, 2012. §1.1, Conjecture 1.1 and Theorems 1.3 and 1.6; cited as the arXiv version.
5. Shenwei Huang, Yidong Zhou and Yeonsu Chang, *The optimal chromatic bound for even-hole-free graphs without induced seven-vertex paths*, [arXiv:2602.04403v1](https://arxiv.org/pdf/2602.04403v1), February 4, 2026, preprint. §1, Theorem 1.1 and following remark; §2, graph conventions.
6. Ken-ichi Kawarabayashi and Lucas Picasarri-Arrieta, *An analogue of Reed's conjecture for digraphs*, [arXiv:2407.05827v4](https://arxiv.org/html/2407.05827v4), revised September 8, 2026, preprint; a shorter version appeared in SODA 2025. §1, Conjectures 1.1 and 1.6, Theorem 1.7 and following discussion; §2.1, conventions.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf), result family 184 (2026). Statement locator: `Theorem 1.1, PDF page 2; Correspondence-coloring main theorem label thm:main, introduction.tex lines24-33; chi<=chi_list<=chi_DP preceding.`.

## Status review

**Known cases:** For each fixed clique cap, the correspondence-coloring bound implies the exact Reed inequality at all sufficiently large maximum degrees; the threshold depends on that cap.

**Remaining target:** Prove the stated bound for arbitrary clique numbers and all degrees, or give a counterexample. The fixed-clique asymptotic subcase does not cover that full quantifier.

**Statement comparison:** For each fixed integer r>=4, correspondence coloring of every K_r-free simple graph is at most ceil(C_r Delta/log Delta) for sufficiently large Delta. Since ordinary chi<=chi_DP, taking Delta sufficiently large that C_r/log Delta<=1/2 implies the exact Reed inequality for this bounded-clique subcase. The constants and threshold depend on the fixed clique cap; this does not handle arbitrary graph-dependent clique number or all degrees. This is a derived subset consequence rather than a manuscript theorem named Reed.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-337) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/184.md). Family184 selected Lean docs only formalize the logarithmic independence lower bound (CliqueFreeLog), not the correspondence-coloring theorem used here; no full or direct partial Reed verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/337-reed-colouring.md).
