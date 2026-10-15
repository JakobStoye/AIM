# 628. Odd Euler characteristic for flag-no-square four-manifolds

**Area:** Combinatorial topology and geometric group theory

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

A finite simplicial complex is **flag** if every clique of its one-skeleton is a simplex. It is **flag-no-square** if it is flag and its one-skeleton has no induced cycle of length four.

Does there exist a closed connected topological $`4`$-manifold $`M`$ with odd Euler characteristic that admits a finite flag-no-square triangulation? Here closed means compact without boundary; orientability is not required.

## Application

Flag-no-square complexes connect triangulated manifolds with negatively curved geometric constructions and hyperbolic Coxeter groups. This question asks whether the local combinatorial restriction forces a global parity obstruction.

## References

1. D. Kalmanovich, E. Nevo and G. Sorcar, [On Flag-No-Square 4-Manifolds](https://doi.org/10.1007/s00454-025-00774-x), *Discrete & Computational Geometry* **76** (2026), 298–312, Problem 4.1. [arXiv:2310.13495](https://arxiv.org/abs/2310.13495).

## Status review

Reviewed 15 October 2026 against the original target in [PR #110](https://github.com/MColbrook/AIM/pull/110). There exists a closed connected PL four-manifold with odd Euler characteristic and a finite flag-no-square triangulation.

[Proof or source](../research/solutions/628-odd-euler-flag-no-square/paper/odd_euler_flag_no_square.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/628-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The constructed actual PL manifold has Euler characteristic2*chi(Y)-3, with its quotient triangulation proved flag and free of induced four-cycles.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The source constructs flag-no-square four-manifolds of every sufficiently large even Euler characteristic, including examples that are not aspherical. Its separate odd-characteristic existence question remains unresolved. The requirement is an actual manifold, not a pseudomanifold, and no prescribed vertex link is required.
