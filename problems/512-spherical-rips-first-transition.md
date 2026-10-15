# 512. The first Rips homotopy transition for higher-dimensional spheres

**Area:** Applied and computational topology

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For $`n\ge3`$, equip the unit sphere $`S^n\subset\mathbb R^{n+1}`$ with the round geodesic metric $`d(x,y)=\arccos\langle x,y\rangle`$. Write $`K_n(r)`$ for the ordinary CW realization of its Vietoris–Rips complex: a finite subset spans a simplex exactly when its diameter is strictly less than $`r`$.

Set

```math
r_n=\arccos\!\left(-\frac1{n+1}\right).
```

This is the common distance between distinct vertices of a regular $`(n+1)`$-simplex inscribed in $`S^n`$. Its orientation-preserving symmetry group identifies the alternating group $`A_{n+2}`$ with a subgroup of $`\mathop{\mathrm{SO}}\nolimits(n+1)`$. Let $`Q_n=\mathop{\mathrm{SO}}\nolimits(n+1)/A_{n+2}`$ be the resulting quotient space. Write $`X*Y`$ for the topological join, obtained from $`X\times Y\times[0,1]`$ by collapsing the $`Y`$ coordinate at $`0`$ and the $`X`$ coordinate at $`1`$.

Is it true that for every integer $`n\ge3`$ there exists $`\varepsilon_n\in(0,\pi-r_n)`$ such that

```math
K_n(r)\simeq S^n*Q_n\qquad\text{whenever }r_n<r<r_n+\varepsilon_n?
```

Prove this assertion, or find a dimension in which no such interval exists.

## Application

Rips filtrations model the topology inferred from data as the distance threshold grows. For a spherical data model, this question identifies the first topology that replaces the underlying sphere when regular-simplex configurations become available. The quotient $`Q_n`$ records the rotational family of those configurations, giving a concrete candidate model for the transition.

## References

1. H. Adams, J. Bush and Ž. Virk, [The connectivity of Vietoris–Rips complexes of spheres](https://doi.org/10.1007/s41468-025-00214-y), Journal of Applied and Computational Topology **9**, article 15 (2025). Conjecture 7.2, p.21; §2.5 and §3. [arXiv:2407.15818v2](https://arxiv.org/abs/2407.15818v2).
2. S. Lim, F. Mémoli and O. B. Okutan, [Vietoris–Rips persistent homology, injective metric spaces, and the filling radius](https://msp.org/agt/2024/24-2/agt-v24-n2-p10-s.pdf), Algebraic & Geometric Topology **24** (2024). Conjecture 7.8, p.1047, explicitly records the known cases $`n=1,2`$.

## Status review

Reviewed 15 October 2026 against the original target in [PR #95](https://github.com/MColbrook/AIM/pull/95). The proposed join is the homotopy type of the ordinary strict spherical Rips complex throughout a nonempty interval after the first transition.

[Proof or source](../research/solutions/512-kaiwen-jin-spherical-rips-first-transition/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/512-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For every n>=3, an epsilon_n>0 gives VR(S^n;r) homotopy equivalent to S^n*(SO(n+1)/A_(n+2)) for every r in the stated strict interval.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The displayed target excludes the known dimensions one and two. The identification at exactly $`r_n`$ for a non-strict metric thickening, recalled in [1, §2.5], does not identify the strict simplicial complexes on an interval beyond $`r_n`$. Reference [1] retains that interval statement as a conjecture.

Primary formulations, known cases and later announcements were checked on 24 September 2026, including indexed arXiv, Zenodo, GitHub and Palomar searches. No matching general resolution was located. Recent equivariant-coindex estimates provide information about maps to or from these complexes, rather than the required homotopy equivalence.
