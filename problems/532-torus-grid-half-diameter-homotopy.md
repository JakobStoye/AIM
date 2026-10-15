# 532. Homotopy type of torus-grid Rips complexes at half the diameter

**Area:** Applied topology and persistent homology

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For an integer $`k\ge3`$, give $`T_{2k}=\{0,\ldots,2k-1\}^2`$ the periodic grid metric

```math
d((a,b),(c,e))=\min\{|a-c|,2k-|a-c|\}+\min\{|b-e|,2k-|b-e|\}.
```

Its diameter is $`2k`$. Let $`K_{2k}(k)`$ be the simplicial complex of subsets of diameter at most $`k`$.

Prove or disprove the homotopy equivalence

```math
K_{2k}(k)\simeq S^3\vee\bigvee_{j=1}^{4k}S^{2k-1}
```

for every integer $`k\ge3`$, where $`\vee`$ denotes a wedge at a common base point.

## Application

An exact homotopy description would identify high-dimensional features that arise when a Rips filtration of periodic data passes beyond local geometric reconstruction.

## References

1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, [Vietoris–Rips Complexes of Torus Grids](https://doi.org/10.1007/s00009-025-02945-9), Mediterranean Journal of Mathematics **22**, 173 (2025), Table 1 and Question 8.6. [Author version](https://arxiv.org/abs/2502.07134v2).

## Status review

Reviewed 15 October 2026 against the original target in [PR #102](https://github.com/MColbrook/AIM/pull/102). The closed Rips complex of the2k-by-2k torus grid at half its diameter has the full conjectured wedge homotopy type for every k>=3.

[Proof or source](../research/solutions/532-torus-grid-half-diameter-homotopy/paper/torus-grid-half-diameter.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/532-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For each k>=3, VR(T_(2k,2k);k) is homotopy equivalent to S3 wedged with4k copies of S^(2k-1).

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

Question 8.6 also includes $`k=2`$, whose nine-sphere wedge is already known; the statement here starts at $`k=3`$. Matching Betti numbers alone would not prove the asserted homotopy equivalence. The cross-polytope result at scale $`2k-1`$ concerns a different scale.

Primary-source and announcement checks on 24 September 2026 found no matching resolution. A live [persistence-map counterexample announcement](https://zenodo.org/records/22250420) does not claim this half-diameter homotopy formula. Its limited overlapping third-homology computations are consistent with the formula and do not establish the required homotopy equivalence.
