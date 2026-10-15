# 635. Small mod-two area cycles in drawings with bounded pairwise intersections

**Area:** Topological graph theory and discrete geometry

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix $`k\ge2`$. For $`n\ge3`$, consider drawings of $`K_n`$ entirely inside the unit square. Vertices are distinct points; edges are non-self-intersecting piecewise smooth arcs avoiding other vertices. Interior intersections are transverse crossings, and each pair of distinct edges has at most $`k`$ intersection points, counting a shared endpoint when present.

A nonzero $`\mathbb F_2`$-cycle is a nonempty subset of graph edges in which every vertex has even degree. It may be disconnected. For such a cycle $`z`$, define $`A(z)`$ as the area of the set of points having odd crossing parity with $`z`$ along a generic path to the unbounded component of its complement. This is the mod-two interior, so self-crossings do not require the cycle to bound a Jordan domain.

Does there exist a function $`\varepsilon_k(n)\to0`$ as $`n\to\infty`$ such that every such drawing contains a nonzero cycle $`z`$ with

```math
A(z)\le\varepsilon_k(n)?
```

The bound must be uniform over drawings, while $`k`$ remains fixed.

## Application

This extends small-area phenomena in geometric point configurations to graph drawings whose edges may curve and cross repeatedly. It asks whether a uniform local intersection bound forces a global region of small parity area.

## References

1. A. Hubard and A. Suk, [Disjoint Faces in Drawings of the Complete Graph and Topological Heilbronn Problems](https://doi.org/10.1007/s00454-025-00721-w), *Discrete & Computational Geometry* **74** (2025), 899–916, Section 5 and Problem 5.1. [arXiv:2212.01311](https://arxiv.org/abs/2212.01311).
2. J. Zeng, [Note on disjoint faces in simple topological graphs](https://arxiv.org/abs/2308.04742), 2023.

## Status review

Reviewed 15 October 2026 against the original target in [PR #114](https://github.com/MColbrook/AIM/pull/114). Bounded pairwise intersections force a mod-two area four-cycle with area tending uniformly to zero.

[Proof or source](../research/solutions/635-bounded-crossing-heilbronn/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/635-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every fixed intersection bound k, the manuscript gives an explicit epsilon_k(n) tending to zero and a nonzero original-edge four-cycle for n>=4, under the full piecewise-smooth curved-edge target.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** For simple drawings, corresponding to $`k=1`$, Zeng proves an $`O(1/n)`$ area bound for a non-self-intersecting four-cycle. Without a uniform bound on intersections, Hubard and Suk construct drawings in which every nonzero mod-two cycle has area bounded below by a positive constant.

**Remaining target:** Decide the vanishing-area statement for every fixed $`k\ge2`$. The later improvement for simple drawings does not allow an edge pair to intersect more than once. This question uses all nonzero mod-two cycles, not just triangles or Jordan cycles.
