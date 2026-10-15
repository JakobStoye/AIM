# 647. Connectivity when the last isolated point disappears in a polytope

**Area:** Applied topology / stochastic geometry
**Status:** ✅ SOLVED
**Last checked:** 2026-10-15

## Problem statement

Fix $`d\ge3`$ and a compact convex polytope $`A\subset\mathbb R^d`$ with nonempty interior. Let $`X_1,X_2,\ldots`$ be independent points uniformly distributed in $`A`$. For $`n\ge2`$, let $`G_n(r)`$ have vertex set $`\{X_1,\ldots,X_n\}`$ and join two vertices when their Euclidean distance is at most $`r`$.

Define

```math
L_n=\max_{1\le i\le n}\min_{j\ne i}\|X_i-X_j\|,
\qquad M_n=\inf\{r\ge0:G_n(r)\text{ is connected}\}.
```

Thus $`L_n`$ is the radius at which the graph first has no isolated vertices, and $`L_n\le M_n`$.

Is it true for every such polytope $`A`$ that

```math
\lim_{n\to\infty}\Pr\{L_n=M_n\}=1?
```

## Application

For a wireless network or a graph built from sampled data, the statement would make the disappearance of isolated points an asymptotically reliable certificate of global connectivity, including domains with sharp edges and corners.

## References

1. M. D. Penrose, X. Yang and F. Higgs, [Largest nearest-neighbour link and connectivity threshold in a polytopal random sample](https://doi.org/10.1007/s41468-023-00154-5), Journal of Applied and Computational Topology **8** (2024), 1723–1750, Remark 2.9 and Theorems 2.1 and 2.5. [Preprint](https://arxiv.org/abs/2301.02506).
2. M. D. Penrose and X. Yang, [Fluctuations of the connectivity threshold and largest nearest-neighbour link](https://doi.org/10.1214/25-AAP2210), Annals of Applied Probability **35** (2025), 3906–3941; [preprint](https://arxiv.org/abs/2406.00647), Theorem 1.1 and equation (1.5).

## Status review

Reviewed 15 October 2026 against the original target in [PR #121](https://github.com/MColbrook/AIM/pull/121). For every fixed full-dimensional convex polytope in every fixed dimension at least three, connectivity occurs exactly when the last isolated vertex disappears with high probability.

[Proof or source](../research/solutions/647-polytopal-connectivity-last-isolated-point/paper/connectivity-polytope.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/647-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every fixed full-dimensional convex polytope in every fixed dimension at least three, connectivity occurs exactly when the last isolated vertex disappears with high probability.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** The equality holds with probability tending to one for a cube. The later Penrose–Yang result proves it for convex polygons and for compact Euclidean domains with $`C^2`$ boundary. For every polytope in the question, the source already proves $`M_n/L_n\to1`$ almost surely.

**Remaining target:** Exact equality with high probability for arbitrary convex polytopes in dimension at least three; asymptotic equality of the ratio does not establish this.

Remark 2.9 explicitly identifies this extension beyond cubes. Current searches found no solution or announced proof for the general polytopal case.
