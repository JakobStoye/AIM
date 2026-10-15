# 531. Homology at the second transition of torus-grid Rips complexes

**Area:** Applied topology and persistent homology

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For an integer $`n\ge3`$, equip $`T_n=\{0,\ldots,n-1\}^2`$ with

```math
d((a,b),(c,e))=\min\{|a-c|,n-|a-c|\}+\min\{|b-e|,n-|b-e|\}.
```

Let $`K_n(r)`$ contain precisely the subsets of $`T_n`$ whose diameter is at most $`r`$. Write $`\beta_i(K)=\mathop{\mathrm{rank}}\nolimits H_i(K;\mathbb Z)`$.

Prove or disprove that, for every integer $`k\ge5`$,

```math
\widetilde H_i(K_{3k-2}(k);\mathbb Z)=0\quad(i\notin\{3,4\}),
```



```math
\beta_3(K_{3k-2}(k))=6k-2+(-1)^k,\qquad
\beta_4(K_{3k-2}(k))=6k-3+(-1)^k.
```

No assertion of torsion-freeness in degrees 3 and 4 is included.

## Application

This family would provide exact benchmarks for topology detected from periodic grid data beyond the range where the Rips complex recovers the underlying torus.

## References

1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng and J. Sterling, [Vietoris–Rips Complexes of Torus Grids](https://doi.org/10.1007/s00009-025-02945-9), Mediterranean Journal of Mathematics **22**, 173 (2025), §3.6 and Question 8.4. [Author version](https://arxiv.org/abs/2502.07134v2).

## Status review

Reviewed 15 October 2026 against the original target in [PR #99](https://github.com/MColbrook/AIM/pull/99). An exact integral chain certificate disproves the proposed all-k homology formula at k=5.

[Proof or source](../research/solutions/yuiyuiui-531-integral-counterexample/paper/torus_grid_counterexample.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/531-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For the stated 13-by-13 torus metric grid at Rips scale5, H4 is free abelian of rank2, whereas the proposed formula predicts26.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

This is the $`k\ge5`$ part of Question 8.4, using the integral-homology convention in §3.6. The paper's tables instead use mod-2 computations; these do not establish the displayed integral statement. The neighboring families with grid sizes $`3k`$ and $`3k-1`$ are proved in the paper but have different homology.

Primary-source and announcement checks on 24 September 2026 found no matching resolution. A live [counterexample announcement](https://zenodo.org/records/22250420) concerns third-homology inclusion maps for grids with side length $`3k-1`$, a different family from the side lengths $`3k-2`$ here. Its statements do not settle this target.
