# 038. Dixmier’s unitarizability problem for countable groups

**Area:** Group representations and operator theory

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`G`$ be a countable discrete group. Suppose that for every complex Hilbert space $`H`$ and every representation $`\pi:G\to GL(H)`$ with $`\sup_{g\in G}\|\pi(g)\|<\infty`$, there exists a bounded invertible $`S`$ such that $`S^{-1}\pi(g)S`$ is unitary for every $`g`$.

Must $`G`$ be amenable? Here amenability means that $`\ell^\infty(G)`$ has a positive linear functional $`m`$ with $`m(1)=1`$ and $`m(f(g^{-1}\cdot))=m(f)`$ for all $`g\in G`$. The reverse implication is the Day–Dixmier theorem.

## Application

A positive answer would identify precisely when every uniformly bounded symmetry representation admits an invariant Hilbert energy norm. This is a structural question underlying stable representations of symmetry, with indirect applied relevance.

## References

1. M. Miglioli and P. Schlicht, [Geometric aspects of similarity problems](https://arxiv.org/abs/1506.06523), preprint 2015; International Mathematics Research Notices (2018), 7171–7197. Introduction and positive-operator geometry.
2. J. M. F. Castillo and V. Ferenczi, [Group Actions on Twisted Sums of Banach Spaces](https://doi.org/10.1007/s40840-023-01531-0), Bulletin of the Malaysian Mathematical Sciences Society (2023). States the countable-group Dixmier problem.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf), result family 251 (2026). Statement locator: `build/sections/introduction.tex, thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem proves amenability iff unitarizability for all discrete groups, including the exact countable target. Uniform boundedness and arbitrary complex Hilbert spaces agree.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-038) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/251.md). docs/251 covers full equivalence; DixmierAllDiscrete and Dixmier comparators. Available formalization, not locally kernel verified. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/038-dixmier-unitarizability.md).
