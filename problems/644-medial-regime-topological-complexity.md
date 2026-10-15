# 644. Topological complexity in the homogeneous medial regime for all sample sizes

**Area:** Applied topology / random complexes
**Status:** ✅ SOLVED
**Last checked:** 2026-10-15

## Problem statement

Fix $`p\in(0,1)`$. For every nonempty subset $`\sigma\subseteq[n]`$, independently choose a Bernoulli variable $`\xi_\sigma`$ with success probability $`p`$. Define the random simplicial complex

```math
X_n=\{\sigma\subseteq[n]:\sigma\ne\varnothing,\ \xi_\tau=1
\text{ for every nonempty }\tau\subseteq\sigma\}.
```

This is the homogeneous medial regime of the lower multiparameter model; vertices, as well as higher-dimensional faces, are sampled.

For a path-connected space $`Y`$, use the reduced topological complexity $`\mathop{\mathrm{TC}}\nolimits(Y)`$: the smallest $`k\ge0`$ such that $`Y\times Y`$ has an open cover by $`k+1`$ sets, each admitting a continuous local section of the endpoint map

```math
Y^{[0,1]}\longrightarrow Y\times Y,\qquad
\gamma\longmapsto(\gamma(0),\gamma(1)).
```

Is it true, for every fixed $`p\in(0,1)`$, that

```math
\Pr\{\,|X_n|\text{ is path-connected and }\mathop{\mathrm{TC}}\nolimits(|X_n|)=2\,\}
\longrightarrow1\qquad(n\longrightarrow\infty),
```

with the limit taken over all positive integers $`n`$?

## Application

Topological complexity counts the continuous local rules needed for motion planning. The statement would show that a typical large complex in this model requires exactly three such rules, uniformly along the full sequence of ambient sample sizes.

## References

1. M. Farber, [Large simplicial complexes: universality, randomness, and ampleness](https://doi.org/10.1007/s41468-023-00134-9), Journal of Applied and Computational Topology **8** (2024), 1551–1574, Remark 8.2.
2. J. A. Barmak and M. Farber, [Topology of medial regime random simplicial complexes](https://arxiv.org/abs/2608.07969), August 2026, Theorems 16 and 19 and §10, Question 2.

## Status review

Reviewed 15 October 2026 against the original target in [PR #113](https://github.com/MColbrook/AIM/pull/113). The reduced topological complexity is2 with probability tending to one along all sample sizes in the homogeneous lower model.

[Proof or source](../research/solutions/644-medial-regime-topological-complexity/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/644-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every fixed p in(0,1), the complex is path connected and has reduced TC=2 asymptotically through all integers n, with a proved Euler-characteristic anti-concentration bound.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** The 2026 preprint proves the upper bound $`\mathop{\mathrm{TC}}\nolimits(|X_n|)\le2`$ with probability tending to one along all $`n`$. It proves equality with probability tending to one when $`n`$ is restricted to a suitable subset of the positive integers having natural density one.

**Remaining target:** Remove that restriction on $`n`$ in the homogeneous model with fixed $`p`$.

The authors explicitly retain this question after proving their density-one result. The difficult sample sizes occur near transitions where two consecutive face counts have comparable magnitude. Current searches found no subsequent solution or announcement.
