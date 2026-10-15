# 596. A bounded number of flat transversals for fat convex sets

**Area:** Discrete geometry and geometric transversal theory

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix integers $`d\ge3`$, $`1\le k\le d-2`$, $`p\ge k+2`$, and a real number $`\rho\ge1`$. A compact convex body $`K\subset\mathbb R^d`$ is $`\rho`$-fat if there are a center $`x_K`$ and positive radii $`r_K,R_K`$ with

```math
B(x_K,r_K)\subseteq K\subseteq B(x_K,R_K),\qquad R_K\le\rho r_K.
```

The radii may vary between bodies. A $`k`$-flat is a $`k`$-dimensional affine subspace.

Does there exist a constant $`C=C(d,k,p,\rho)`$ with the following property? Whenever $`\mathcal F`$ is a finite family of such bodies and every $`p`$ members contain $`k+2`$ members intersected by a common $`k`$-flat, at most $`C`$ $`k`$-flats together intersect every member of $`\mathcal F`$.

## Application

The conclusion would turn a condition on small subfamilies into a uniform bound on the number of flat probes needed to reach an entire collection of objects. Such bounds underlie geometric piercing and covering algorithms.

## References

1. A. Jung and D. Pálvölgyi, [k-Dimensional Transversals For Fat Convex Sets](https://doi.org/10.1007/s00454-026-00852-8), *Discrete & Computational Geometry* (2026), Conjecture 1 and Theorems 5 and 7. [arXiv:2311.15646](https://arxiv.org/abs/2311.15646).

## Status review

Reviewed 15 October 2026 against the original target in [PR #108](https://github.com/MColbrook/AIM/pull/108). The fractional flat-transversal theorem can be rounded to boundedly many actual flats for arbitrary concentric-fat convex bodies.

[Proof or source](../research/solutions/aim-596-fat-convex-transversals/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/596-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every parameter range stated in AIM596, a constant depending only on dimension, flat dimension, p and fatness pierces every finite qualifying family, with no radius-ratio restriction.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

Reference [1] proves the corresponding fractional Helly theorem for fat convex bodies and the displayed bounded-piercing conclusion for balls. For general fat bodies the missing step is an appropriate weak epsilon-net theorem. The problem keeps the intermediate dimensions $`0<k<d-1`$, where the unrestricted convex-set theorem fails; fatness and its uniform parameter are essential. Searches found no matching solution announcement or duplicate.
