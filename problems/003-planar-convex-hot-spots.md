# 003. Hot spots on convex planar domains

**Area:** Heat flow and Neumann eigenfunctions

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\Omega\subset\mathbb R^2`$ be any bounded convex domain with $`C^\infty`$ boundary. Let $`\mu_1>0`$ be its first nonzero Neumann eigenvalue. For every nonzero real solution

```math
-\Delta u=\mu_1u\quad\hbox{in }\Omega,\qquad\partial_\nu u=0\quad\hbox{on }\partial\Omega,
```

prove or disprove that every global maximum and every global minimum of $`u`$ on $`\overline\Omega`$ lies on $`\partial\Omega`$. Here $`\nu`$ is the outward unit normal; the assertion applies to every vector in the eigenspace when the eigenvalue is multiple.

## Application

The first nonconstant Neumann mode controls the long-time temperature profile in an insulated planar body. Its extreme values predict where the hottest and coldest regions persist.

## References

1. J. Rohleder, [A note on hot-spots free subregions of convex domains](https://doi.org/10.1007/s11785-026-01910-y), Complex Analysis and Operator Theory 20, 57 (2026), introduction and Theorem 1.1.
2. H. Deng, X. Jiang and X. Yang, [Critical points of second Neumann eigenfunctions on some convex domains in two-dimensional space forms](https://arxiv.org/abs/2607.17882), preprint (2026).
3. J. de Dios Pont, [Convex sets can have interior hot spots](https://arxiv.org/abs/2412.06344), preprint (2024).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/main.pdf), result family 369 (2026). Statement locator: `build/sections/01-introduction.tex, thm:main and eq:hotspots`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Every nonzero real eigenfunction in the first positive Neumann eigenspace on every smooth bounded simply connected planar domain has no interior critical point and obeys strict interior inequalities against boundary extrema. Every convex target domain is simply connected; multiplicities and every vector in the eigenspace are explicitly included.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-003) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/369.md). docs/369 covers the full strict hot-spots conclusion via HotSpots. No local kernel log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/003-planar-convex-hot-spots.md).
