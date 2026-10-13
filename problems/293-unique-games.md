# 293. The Unique Games Conjecture

**Area:** Constraint satisfaction and approximation algorithms

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

A unique game consists of a finite bipartite graph $`G=(L\sqcup R,E)`$, with $`E\ne\varnothing`$, an alphabet $`[r]=\{1,\ldots,r\}`$ and a permutation $`\pi_e:[r]\to[r]`$ for each edge $`e=(u,v)`$ directed from $`L`$ to $`R`$. A labeling $`\ell:L\sqcup R\to[r]`$ satisfies $`e`$ when $`\ell(v)=\pi_e(\ell(u))`$. Define the classical value

```math
\mathop{\mathrm{val}}\nolimits(G,\pi)=
\max_{\ell}\frac{1}{|E|}\sum_{e=(u,v)\in E}
\mathbf 1\{\ell(v)=\pi_e(\ell(u))\}.
```

Is it true that, for every $`0<\varepsilon<1/2`$, there exists an integer $`r=r(\varepsilon)`$ such that it is NP-hard to distinguish instances satisfying

```math
\mathop{\mathrm{val}}\nolimits(G,\pi)\ge 1-\varepsilon
\qquad\text{from those satisfying}\qquad
\mathop{\mathrm{val}}\nolimits(G,\pi)\le\varepsilon?
```

The alphabet is fixed for each $`\varepsilon`$, independently of the number of vertices. This is a promise problem: behavior on intermediate values is unrestricted. The value uses ordinary classical labelings.

## Application

The conjecture is a proposed foundation for sharp limits on approximation algorithms for discrete optimization. For example, Heilman's 2026 Theorem 1.4 uses it to derive sharp approximation hardness for MAX-3-CUT, whose objective is to divide a graph into three classes while maximizing the number of edges between classes. Such hardness consequences remain conditional on this conjecture.

## References

1. Y. Fei, D. Minzer and S. Wang, [*On the Hardness of 4-to-1 Games with Perfect Completeness*](https://eccc.weizmann.ac.il/report/2026/179/download/), ECCC TR26-179, September 14, 2026; Definitions 1.1 and 1.3, Conjecture 1.4, Theorem 1.6 and the discussion in §1.1, printed pp. 4–6.
2. J. Kempe, O. Regev and B. Toner, [*Unique Games with Entangled Provers are Easy*](https://arxiv.org/pdf/0710.0655v3), arXiv:0710.0655v3, October 3, 2009; Conjecture 1.2, p. 2, and Theorem 1.3, p. 5.
3. S. Heilman, [*Sharp Hardness for MAX-3-CUT and Quantum MAX-CUT*](https://arxiv.org/pdf/2608.00333v1), arXiv:2608.00333v1, submitted July 31, 2026; §1.1 and Theorem 1.4. The served manuscript bears August 24, 2026.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf), result family 102 (2026). Statement locator: `Theorem thm:ugc`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Take the theorem errors epsilon=delta equal to AIM epsilon. The fixed alphabet F2^s depends only on the errors; translations are permutations. Output graphs are nonempty explicit unweighted simple bipartite instances, and value is ordinary classical fraction of satisfied edges. The deterministic polynomial reduction from 3SAT supplies exactly the NP-hard promise gap.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-293) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/102.md). Actual theorem11 returns BinaryGapReduction with a fixed alphabet/program before inputs, simple bipartite outputs, translations, completeness and soundness. No local replay/axiom log. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/293-unique-games.md).
