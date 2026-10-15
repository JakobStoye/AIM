# 501. Integral optimal flat-norm decompositions in codimension one

**Area:** Applied topology, geometric measure theory and shape comparison

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`T`$ be a compactly supported integral $`d`$-current in $`\mathbb R^{d+1}`$, $`d\ge1`$. Thus $`T`$ and its boundary are integer-multiplicity rectifiable currents of finite mass. Write $`\mathbf M`$ for mass and define the real flat norm by

```math
\mathbb F(T)=\inf\{\mathbf M(X)+\mathbf M(S):T=X+\partial S,\ X\in\mathcal N_d^c,\ S\in\mathcal N_{d+1}^c\},
```

where $`\mathcal N_k^c`$ consists of compactly supported real normal $`k`$-currents in the same ambient space.

Must there exist compactly supported **integral** currents $`X_I`$ and $`S_I`$ such that

```math
T=X_I+\partial S_I,\qquad \mathbb F(T)=\mathbf M(X_I)+\mathbf M(S_I)?
```

The input is not required to satisfy $`\partial T=0`$. The question asks for at least one integral optimum of the real problem. Integrality of every optimum and optimality only within the integral class are different assertions.

## Application

The flat norm compares oriented shapes by balancing a residual against a filling. An integral optimum would preserve the integer-multiplicity interpretation of the input, supporting geometric interpretation of optimal decompositions and their discrete approximations.

## References

1. S. Ibrahim, B. Krishnamoorthy and K. R. Vixie, [Flat norm decomposition of integral currents](https://doi.org/10.20382/jocg.v7i1a14), Journal of Computational Geometry **7**(1) (2016), 285–307. §1.1, Theorem 3.7, Corollary 3.8 and §5; [author preprint](https://arxiv.org/abs/1411.0882).

## Status review

Reviewed 15 October 2026 against the original target in [PR #91](https://github.com/MColbrook/AIM/pull/91). An integral optimum exists for every compactly supported integral codimension-one current, including noncycles.

[Proof or source](../research/solutions/501-integral-flat-norm-codimension-one/paper/integral_flat_norm.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/501-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Equality of the real flat norm with an attained integral decomposition in every ambient dimension d+1, d>=1.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** Corollary 3.8 of [1] proves the result for integral one-currents in the plane. The introduction records the known case of codimension-one boundaries. Theorem 3.7 gives a conditional extension through the subdivision/approximation statement associated with Conjecture 3.4.

**Remaining target:** General compactly supported integral $`d`$-currents in $`\mathbb R^{d+1}`$ for $`d\ge2`$, allowing nonzero boundary, without assuming that subdivision conjecture.

The source's counterexamples in ambient dimension at least $`d+3`$ do not settle this codimension-one question. Searches on 23 September 2026 found no matching resolution or announcement. Later results concerning integral homogeneous flat norms or approximation of cycles have different targets.
