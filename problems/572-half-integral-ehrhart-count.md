# 572. Counting Ehrhart quasipolynomials of half-integral polygons

**Area:** Discrete geometry and Ehrhart theory

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For a two-dimensional convex polygon $`P`$ with vertices in $`\tfrac12\mathbb Z^2`$, define its Ehrhart quasipolynomial by

```math
L_P(t)=|tP\cap\mathbb Z^2|\qquad(t\in\mathbb Z_{\ge0}).
```

Its coefficient functions have period dividing two; integral polygons and polygons with period collapse are included.

For an integer $`i\ge2`$, let $`E(i)`$ be the number of distinct functions $`L_P`$ arising from such polygons with exactly $`i`$ interior lattice points and at least two boundary lattice points. Prove or disprove that

```math
E(i)=\frac92 i^3+36i^2+\frac{175}{2}i+53\qquad(i\ge2).
```

Different polygons with the same lattice-point counting function contribute only once. There is no collinearity assumption on the interior points.

## Application

Ehrhart quasipolynomials describe lattice-point counts under dilation, a central operation in integer optimization and polyhedral geometry. An exact count would characterize the diversity of possible counting functions in the first nonintegral denominator class.

## References

1. M. Bohnert and J. Springer, [Classifying Rational Polygons with Small Denominator and Few Interior Lattice Points](https://doi.org/10.1007/s00454-026-00822-0), *Discrete & Computational Geometry* **76** (2026), 1238–1265, Section 2 and Conjecture 6.8. [arXiv:2410.17244](https://arxiv.org/abs/2410.17244).
2. J. Springer and M. Bohnert, [Half-integral polygons with few interior lattice points](https://doi.org/10.5281/zenodo.13928298), computational dataset (2024).
3. M. Bohnert and J. Springer, [Generalizations of Scott's inequality and Pick's formula to rational polygons](https://arxiv.org/abs/2411.11187), arXiv:2411.11187 (2024), Section 3.

## Status review

Reviewed 15 October 2026 against the original target in [PR #125](https://github.com/MColbrook/AIM/pull/125). Exact cubic count of entire Ehrhart functions for every requested half-integral polygon interior count, including integral polygons and period collapse.

[Proof or source](../research/solutions/572-half-integral-ehrhart-count/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/572-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Complete necessity/attainment/count argument checked; all21 rational certificates and15 exact fixed-source full-function-set comparisons independently replayed and passed, relative to published catalogue completeness.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The March 2026 version of record [1] states this conjecture with at least two boundary lattice points and reports computational verification through $`i=16`$. This published statement is the one used here. The earlier related preprint [3] prints a different boundary threshold in its conjecture; it is not being substituted for the published formulation.

Sharp area and coefficient bounds in [3], and classifications for period-collapse polygons, do not provide the full enumeration. The dataset [2] and its companion code supply finite computations. Current searches found no matching solution announcement or repository duplicate.
