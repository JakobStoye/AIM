# 602. A linear genus–girth bound for facial cycles

**Area:** Graph theory and topological graph embeddings

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\Sigma`$ be a connected closed surface of positive genus $`g`$: either the orientable surface with $`g`$ handles or the nonorientable surface with $`g`$ crosscaps. Fix an integer $`\ell\ge3`$.

Consider any finite simple graph $`G`$ embedded without crossings on $`\Sigma`$, with girth at least $`\ell`$, that is maximal for this fixed embedding: adding any edge between previously nonadjacent vertices without crossings would create a cycle of length less than $`\ell`$. Embeddings need not be cellular. A facial cycle must be a simple cycle forming the entire boundary of one face.

Is there an absolute constant $`C`$ such that every facial cycle in every such embedding has length at most

```math
Cg\ell?
```

The same constant must work for both types of surface and for all $`g,\ell`$.

## Application

A bound linear in both parameters would relate topological complexity and local cycle constraints to the size of mesh faces. It would sharpen structural and saturation estimates for networks embedded on surfaces.

## References

1. M. Axenovich, L. Kießle, A. Sagdeev and M. Zhukovskii, [Faces in Girth-Saturated Graphs on Surfaces](https://doi.org/10.1007/s00454-026-00833-x), *Discrete & Computational Geometry* (2026), Theorem 2 and Section 6, Question 2. [arXiv:2410.13481](https://arxiv.org/abs/2410.13481).

## Status review

Reviewed 15 October 2026 against the original target in [PR #123](https://github.com/MColbrook/AIM/pull/123). A facial-cycle bound 100000 times genus times girth holds uniformly for both closed-surface types, including the stated noncellular embeddings.

[Proof or source](../research/solutions/602-surface-girth-facial-linear-bound/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/602-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** A facial-cycle bound 100000 times genus times girth holds uniformly for both closed-surface types, including the stated noncellular embeddings.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The source gives the universal upper bound $`24(2g+1)\ell^2`$. Fixed-girth growth is known to be linear in genus for $`\ell\ge6`$, but the quadratic dependence on varying girth has not been reduced to linear uniformly. The planar leading-constant question concerns genus zero and is a separate target. Searches found no matching resolution or duplicate.
