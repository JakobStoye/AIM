# 593. A linear threshold for extracting a segment grid

**Area:** Computational geometry and graph drawing

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For each integer $`k\ge 1`$, consider $`3k`$ pairwise disjoint red straight-line segments and $`3k`$ pairwise disjoint blue straight-line segments in the plane. Suppose every red segment crosses every blue segment in their relative interiors.

Must there be $`k`$ red and $`k`$ blue segments whose arrangement is combinatorially equivalent to the arrangement of $`k`$ horizontal segments crossing $`k`$ vertical segments?

Here combinatorial equivalence concerns the embedded planar graph obtained by subdividing segments at their crossings, including its cyclic orders and unbounded face, with the red and blue segment families preserved. Thus the required conclusion is a rectangular grid arrangement, not merely the already assumed complete red–blue intersection pattern.

## Application

The proposed linear threshold would improve a geometric extraction step used to construct sparse graphs with large geometric thickness. It would replace an exponential-size ingredient in those constructions.

## References

1. R. Jain, M. Ricci, J. Rollin and A. Schulz, [On the geometric thickness of 2-degenerate graphs](https://jocg.org/index.php/jocg/article/view/5176), *Journal of Computational Geometry* **15**(2) (2024), 94–123, Section 3.1 and Section 4, Question 1. [arXiv:2302.14721](https://arxiv.org/abs/2302.14721).

## Status review

Reviewed 15 October 2026 against the original target in [PR #106](https://github.com/MColbrook/AIM/pull/106). Every arrangement in the question contains the required embedded rectangular grid; the proof also gives the stronger2k−1 sufficient threshold.

[Proof or source](../research/solutions/aim-593-segment-grids/paper/segment_grids.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/593-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The original3k-by-3k properly crossing straight-segment target is proved for every k, with crossing orders, cyclic orders, endpoints and the unbounded face preserved.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The source proves an exponential sufficient size and explicitly asks whether $`3k`$ segments of each color suffice. It also gives arrangements with $`3k`$ segments of each color containing no grid of size $`k+1`$, which do not refute the displayed size-$`k`$ target. General intersection-graph grid statements use a weaker notion and do not resolve this embedding requirement. Current searches found no matching resolution or duplicate.
