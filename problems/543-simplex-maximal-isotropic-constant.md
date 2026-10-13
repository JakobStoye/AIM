# 543. Simplices maximize the isotropic constant

**Area:** Geometric probability and covariance bounds

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`K\subset\mathbb R^n`$ be a compact convex set with nonempty interior, and let $`X`$ be uniformly distributed on $`K`$. Write

```math
c_K=\mathbb E X,\qquad A_K=\mathbb E[(X-c_K)(X-c_K)^T],\qquad L_K=\left(\frac{\det A_K}{\mathop{\mathrm{vol}}\nolimits_n(K)^2}\right)^{1/(2n)}.
```

The quantity $`L_K`$ is invariant under invertible affine transformations. For every $`n\ge1`$ and every such $`K`$, is

```math
L_K\le L_{\Delta_n}=\frac{(n!)^{1/n}}{(n+1)^{(n+1)/(2n)}\sqrt{n+2}},
```

where $`\Delta_n`$ is any nondegenerate $`n`$-simplex?

This is the strong isotropic constant conjecture, stated in [1, equation (1.2)]. The target is the displayed sharp inequality. No additional uniqueness or stability assertion is imposed. Equivalently, it asks for the sharp upper bound

```math
\det A_K\le \frac{(n!)^2}{(n+1)^{n+1}(n+2)^n}\mathop{\mathrm{vol}}\nolimits_n(K)^2.
```

## Application

For a uniform distribution on a convex region, the covariance determinant measures the squared volume scale of its covariance ellipsoid. The conjecture would bound that spread sharply in terms of the region's volume, independently of its affine coordinates. It provides an extremal benchmark for covariance normalization and geometric probability, both used in the analysis of sampling from convex sets.

## References

1. C. Kipp, [Shadow Systems, Decomposability and Isotropic Constants](https://doi.org/10.1007/s00454-026-00829-7), Discrete & Computational Geometry (2026), §1, equations (1.1)–(1.2) and Theorem 1.2; [revised preprint](https://arxiv.org/abs/2411.08722v2).
2. B. Klartag and J. Lehec, [Affirmative Resolution of Bourgain's Slicing Problem using Guan's Bound](https://arxiv.org/abs/2412.15044), for the dimension-independent bound that settles the weaker slicing problem.
3. L. Rademacher, [A simplicial polytope that maximizes the isotropic constant must be a simplex](https://doi.org/10.1112/S0025579315000133), Mathematika **62** (2016), 307–320; [preprint](https://arxiv.org/abs/1404.5662).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf), result family 101 (2026). Statement locator: `Theorem intro:simplex; equation intro:simplex-bound`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The source definition of L_K is exactly (det covariance/volume^2)^(1/(2n)), and its all-dimensional arbitrary-convex-body inequality has precisely AIM simplex constant. No symmetry/polytope restriction appears. Equality uniqueness is extra. This resolves the sharp target, not merely the weaker uniform slicing constant.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-543) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/543-simplex-maximal-isotropic-constant.md).
