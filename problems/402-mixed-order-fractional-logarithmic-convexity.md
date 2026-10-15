# 402. Logarithmic convexity for two coupled subdiffusion orders

**Area:** Fractional PDE systems / inverse problems

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\Omega\subset\mathbb R^n`$ be a bounded smooth domain and fix $`0<\alpha_1<\alpha_2<1`$ and $`T>0`$. For homogeneous Dirichlet boundary conditions consider

```math
\partial_t^{\alpha_1}u_1=\Delta u_1+u_1+u_2,\qquad \partial_t^{\alpha_2}u_2=\Delta u_2+u_1+u_2,
```

with initial pair $`U_0\in L^2(\Omega)^2`$. Each derivative is Caputo: $`\partial_t^\alpha h=\Gamma(1-\alpha)^{-1}\int_0^t(t-s)^{-\alpha}h'(s)\,ds`$. Writing $`U=(u_1,u_2)`$ and using the product $`L^2`$ norm, is there a constant $`C=C(\Omega,\alpha_1,\alpha_2,T)`$ independent of $`U_0`$ such that

```math
\|U(t)\|\le C\|U_0\|^{1-t/T}\|U(T)\|^{t/T}\qquad(0<t<T)
```

for every mild solution?

## Application

Coupled materials or chemical species can have different memory exponents. An interpolation estimate would support stable inverse recovery for such multi-component anomalous diffusion systems.

## References

1. S.-E. Chorfi, *Logarithmic convexity of evolution equations and application to inverse problems*, preprint (2025), §5, open problem 1, displaying this mixed-order system. [Full text](https://arxiv.org/html/2506.19954v1).
2. S.-E. Chorfi, L. Maniar and M. Yamamoto, *The backward problem for time-fractional evolution equations*, Applicable Analysis 103 (2024), 2194–2212, logarithmic convexity and conditional stability theorems. [DOI](https://doi.org/10.1080/00036811.2023.2290273); [arXiv:2211.16493](https://arxiv.org/abs/2211.16493).

## Status review

Reviewed 15 October 2026 against the original target in [PR #159](https://github.com/MColbrook/AIM/pull/159). The exact product-L2 logarithmic interpolation inequality holds for the two distinct Caputo orders and every initial pair.

[Proof or source](../research/solutions/402-mixed-order-fractional-logarithmic-convexity/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/402-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The exact product-L2 logarithmic interpolation inequality holds for the two distinct Caputo orders and every initial pair.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The recent source poses this exact coupled system. Its two distinct time orders prevent reduction to the single-order self-adjoint theorem. Searches through 22 September 2026 for mixed-order coupled diffusion, logarithmic convexity and backward recovery found no matching resolution. This concerns coupling of distinct memory laws, separate from nonsymmetric spatial drift.
