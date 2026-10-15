# 648. Location of the most isolated point in a random polyhedral sample

**Area:** Applied topology / stochastic geometry
**Status:** ✅ SOLVED
**Last checked:** 2026-10-15

## Problem statement

Let $`A\subset\mathbb R^3`$ be a compact convex polyhedron with nonempty interior, and let $`X_1,X_2,\ldots`$ be independent uniform points in $`A`$. Set

```math
R_{n,i}=\min_{j\ne i}\|X_i-X_j\|.
```

Let $`I_n`$ be the smallest index attaining $`\max_{1\le i\le n}R_{n,i}`$, and put $`Z_n=X_{I_n}`$. Thus $`Z_n`$ is a most isolated sample point, with an explicit rule for ties.

For each edge $`e`$ of $`A`$, let $`\alpha_e\in(0,\pi)`$ be its interior dihedral angle, and set

```math
\alpha_* = \min_e\alpha_e,\qquad E_* = \bigcup_{\alpha_e=\alpha_*}e.
```

Prove or disprove the following two-regime statement:

- If $`\alpha_*>\pi/2`$, then $`Z_n`$ converges in distribution to normalized surface-area measure on $`\partial A`$.
- If $`\alpha_*<\pi/2`$, then $`Z_n`$ converges in distribution to normalized length measure on $`E_*`$.

Explicitly, the proposed limits are respectively $`\mathcal H^2|_{\partial A}/\mathcal H^2(\partial A)`$ and $`\mathcal H^1|_{E_*}/\mathcal H^1(E_*)`$, where $`\mathcal H^s`$ denotes $`s`$-dimensional Hausdorff measure. The critical case $`\alpha_*=\pi/2`$ is outside this question.

## Application

The result would locate the sample points most vulnerable to isolation in geometric networks and clarify how sharp edges influence the final stages of connectivity in data sampled from three-dimensional domains.

## References

1. M. D. Penrose, X. Yang and F. Higgs, [Largest nearest-neighbour link and connectivity threshold in a polytopal random sample](https://doi.org/10.1007/s41468-023-00154-5), Journal of Applied and Computational Topology **8** (2024), 1723–1750, Introduction, p. 1724, and Corollary 2.3. [Preprint](https://arxiv.org/abs/2301.02506).

## Status review

Reviewed 15 October 2026 against the original target in [PR #118](https://github.com/MColbrook/AIM/pull/118). Both noncritical spatial limits for the actual most-isolated point, with the stated tie rule.

[Proof or source](../research/solutions/648-polyhedral-most-isolated-point-location/paper/polyhedral_isolation.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/648-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Both noncritical spatial limits for the actual most-isolated point, with the stated tie rule.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The source explicitly proposes both spatial limits. Its strong law determines the leading size of the largest nearest-neighbour distance and identifies the dihedral-angle transition, but does not establish the proposed distribution of its location. Later connectivity results for smooth domains and polygons do not resolve this three-dimensional polyhedral statement. Current searches found no matching solution or announcement.
