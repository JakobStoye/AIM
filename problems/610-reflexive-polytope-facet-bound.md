# 610. Nill's facet bound for reflexive lattice polytopes

**Area:** Discrete geometry and toric geometry

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

A full-dimensional lattice polytope $`P\subset\mathbb R^d`$ is reflexive if $`0\in\mathop{\mathrm{int}}\nolimits P`$ and its polar

```math
P^*=\{y\in\mathbb R^d:\langle x,y\rangle\le1\text{ for every }x\in P\}
```

is also a lattice polytope. Write $`f_{d-1}(P)`$ for its number of facets.

Prove or disprove that every reflexive lattice polytope satisfies

```math
f_{d-1}(P)\le6^{d/2}.
```

The unresolved range is $`d\ge5`$. No simplicity, simpliciality or symmetry assumption is imposed.

## Application

A sharp bound would constrain the combinatorial complexity of reflexive polytopes used in toric geometry and support their enumeration.

## References

1. A. Mori, K. Mori and H. Ohsugi, [Facet Numbers of Non-Centrally Symmetric Reflexive Polytopes Arising from Posets](https://doi.org/10.1007/s00454-026-00879-x), *Discrete & Computational Geometry* (2026), Conjecture 1.1. [arXiv:2511.22981](https://arxiv.org/abs/2511.22981).

## Status review

Reviewed 15 October 2026 against the original target in [PR #107](https://github.com/MColbrook/AIM/pull/107). An explicit45-dimensional reflexive polytope violates the conjectured facet bound.

[Proof or source](../research/solutions/aim-610-reflexive-facet-counterexample/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/610-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The constructed standard-lattice reflexive polytope has330303106984181765 facets, strictly more than6^(45/2).

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The September 2026 source proves the bound for twinned chain polytopes and explicitly retains the general conjecture. Dimensions at most four are covered by classification. Polarity makes the corresponding vertex bound equivalent; it is not a separate problem. Nill's different conjecture generalizing Ewald's conjecture concerns lattice points, not this facet count.
