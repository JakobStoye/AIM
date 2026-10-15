# 525. Maximal TC weight from positive homological norm

**Area:** Applied topology and robot motion planning

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`M`$ be a closed, connected, oriented aspherical $`n`$-manifold, and let $`2\le k\le n`$. All homology and cohomology below have rational coefficients. Suppose there is $`\alpha\in H_k(M;\mathbb Q)`$ with

```math
\|\alpha\|_1=\inf\left\{\sum_j|a_j|:\ \sum_j a_j\sigma_j\text{ is a singular cycle representing }\alpha\right\}>0.
```

For $`u\in H^k(M;\mathbb Q)`$ write

```math
\bar u=1\times u-u\times1\in H^k(M\times M;\mathbb Q).
```

Let $`e:C([0,1],M)\to M\times M`$ be the endpoint fibration, with the compact-open topology on the path space. The unreduced Schwarz genus of a fibration is the least number of open sets covering its base on which it has continuous sections. Define

```math
\mathop{\mathrm{wgt}}\nolimits_{\mathop{\mathrm{TC}}\nolimits}(\bar u)=\sup\{r\ge0:\ f^*\bar u=0\text{ for every continuous }f:Y\to M\times M\text{ with }\mathop{\mathrm{genus}}\nolimits(f^*e)\le r\},
```

where $`r`$ ranges over integers and $`Y`$ over topological spaces.

Must there exist a nonzero $`u\in H^k(M;\mathbb Q)`$ such that

```math
\mathop{\mathrm{wgt}}\nolimits_{\mathop{\mathrm{TC}}\nolimits}(\bar u)\ge k?
```

Prove the assertion or give a counterexample. The cohomology class may be chosen freely; the question does not assert the bound for every class or specify a dual to $`\alpha`$. This is Question 5.1(a) of [1].

## Application

TC weight strengthens cohomological lower bounds for the number of continuous local motion-planning rules. This question asks whether a homology class with positive norm forces a cohomological obstruction of maximal possible weight in its degree, providing a way to certify planning complexity from geometric information.

## References

1. C. Neofytidis, [Topological complexity, asphericity and connected sums](https://doi.org/10.1007/s41468-025-00205-z), Journal of Applied and Computational Topology **9**, article 10 (2025), Definitions 2.1/2.4, Theorems 2.2/3.4 and Question 5.1(a), p.13. [arXiv:2212.08962v2](https://arxiv.org/abs/2212.08962v2).

## Status review

Reviewed 15 October 2026 against the original target in [PR #98](https://github.com/MColbrook/AIM/pull/98). A positive-norm surface product has no degree-four class of the proposed TC weight.

[Proof or source](../research/solutions/525-positive-norm-tc-weight/paper/counterexample.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/525-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** For M=Sigma2×Sigma2 the rational fundamental class has norm at least24, but every nonzero u in H4(M;Q) has weight(bar(u)) at most2<4.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

The degree bound for sectional weight makes the requested inequality an equality. Theorem 3.4 of [1] proves weight at least two for every nonzero degree-at-least-two class on a negatively curved manifold; it does not establish the requested degree-$`k`$ bound for general $`M`$ and $`k`$.

For even-dimensional manifolds, an affirmative answer would imply the [positive-volume maximal-complexity statement](524-positive-volume-motion-planning.md), by applying the product-weight estimate to the fundamental cohomology class. This implication does not identify the two questions: the present target also concerns lower-degree classes and a specific cohomological invariant.

Primary-source and announcement checks on 24 September 2026 found no matching general proof or counterexample. These included indexed arXiv/Zenodo/GitHub searches and the official Palomar search API.
