# 169. Strict convexity of the planar exponential first-passage shape

**Area:** Stochastic growth and random media

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Give each nearest-neighbor edge $`e`$ of $`\mathbb Z^2`$ an independent exponential random variable $`\tau_e`$ of mean one. Let $`T(x,y)`$ be the minimum of $`\sum_{e\in\gamma}\tau_e`$ over lattice paths from $`x`$ to $`y`$, and let $`\mu(v)=\lim_{n\to\infty}T(0,\lfloor nv\rfloor)/n`$, the deterministic time constant. Is the unit ball $`B_\mu=\{v\in\mathbb R^2:\mu(v)\le1\}`$ strictly convex? Equivalently, must $`\mu(su+(1-s)v)<1`$ hold for distinct $`u,v\in\partial B_\mu`$ and every $`0<s<1`$? The exponential law is fixed; no curvature or straightness hypothesis may be assumed.

## Application

This asks whether the macroscopic front of a lattice growth model has flat facets. The same random metric models travel times through heterogeneous media.

## References

- [Antonio Auffinger, Michael Damron and Jack Hanson, *50 Years of First-Passage Percolation* (AMS University Lecture Series 68, 2017); author manuscript](https://sites.math.duke.edu/~rtd/FPP/50yrsFPP.pdf), §§2.5 and 2.8, Questions 4 and 11.
- [Steven P. Lalley, *Strict Convexity of the Limit Shape in First-Passage Percolation* (2003)](https://doi.org/10.1214/ECP.v8-1089), conditional strict-convexity criteria.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf), result family 212 (2026). Statement locator: `Theorem 1.1, PDF page 3; The exponential limit shape theorem, label thm:exponential-shape, introduction.tex lines 21-32.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The exponential limit-shape theorem covers undirected nearest-neighbor Z^2 FPP with independent exponential weights of any positive rate, including rate1. It explicitly gives strict convexity and the strict interpolation inequality for every pair of distinct boundary points, with no assumed curvature or geodesic hypothesis.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-169) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/212.md). Family212 docs explicitly say strict convexity is outside its selected differentiability comparators. A C1 boundary or unique supporting line does not imply strict convexity. No complete AIM169 formalization/verification supported by these links. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/169-strict-convexity-fpp.md).
