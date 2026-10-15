# 578. A real nearest matrix with spectrum in the closed left half-plane

**Area:** Numerical linear algebra and matrix optimization

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

For $`\mathbb F\in\{\mathbb R,\mathbb C\}`$ and $`n\ge1`$, define

```math
\mathcal H_n(\mathbb F)=\{B\in\mathbb F^{n\times n}:\mathop{\mathrm{Re}}\nolimits\lambda\le0\text{ for every }\lambda\in\sigma(B)\}.
```

For $`A\in\mathbb R^{n\times n}`$ put

```math
d_{\mathbb F}(A)=\min_{B\in\mathcal H_n(\mathbb F)}\|A-B\|_F,
```

where $`\|M\|_F^2=\sum_{i,j}|M_{ij}|^2`$.

Prove or disprove the Noferini–Poloni conjecture that

```math
d_{\mathbb R}(A)=d_{\mathbb C}(A)
```

for every real square matrix $`A`$. Equivalently, does the complex minimization problem always have a real global minimizer?

The admissible spectral region is the **closed** left half-plane. Eigenvalues on the imaginary axis may have arbitrary Jordan blocks; no semisimplicity condition is imposed. The minima exist because these feasible sets are nonempty and closed and the objective is coercive.

## Application

Approximating an unstable model by a nearby matrix with nonpositive spectral abscissa is a basic matrix correction problem in control and system identification. The conjecture asks whether allowing complex entries can ever improve the best achievable Frobenius error for real input data. It does not assert asymptotic or bounded dynamical behavior for every matrix on the boundary of the admissible set.

## References

1. V. Noferini and F. Poloni, [Nearest $`\Omega`$-stable matrix via Riemannian optimization](https://doi.org/10.1007/s00211-021-01217-4), *Numerische Mathematik* **148** (2021), 817–851; [arXiv:2002.07052](https://arxiv.org/abs/2002.07052). Section 7.6, Conjecture 1; the closed-half-plane convention is specified on page 818.
2. [Authors' accompanying code](https://github.com/fph/nearest-omega-stable).

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Negative

[Proof or source](https://arxiv.org/pdf/2609.14828v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-source-scope-review_90_114.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The source explicitly includes defective imaginary-axis eigenvalues, exactly as AIM578 requires. For m>=4 it gives A=[[-m^4,m²,0],[0,0,m²],[m^6,1,0]]. Its columns are orthogonal and its smallest singular value is m². Its determinant is positive, while every real3-by-3 matrix with spectrum in the closed left half-plane has nonpositive determinant. The segment to any real stable matrix therefore meets a singular matrix, forcing Frobenius distance at least m². Zeroing the(2,3) entry attains that bound, with characteristic polynomial z²(z+m^4).

The complex competitor C=[[-m^4,m²+2mi,2mi−3],[0,0,m²],[m^6,0,0]] has characteristic polynomial(z−im³)²(z+m^4+2im³), so it is feasible in the closed half-plane, including its repeated imaginary eigenvalue. Direct expansion verifies that polynomial and ||A−C||_F²=8m²+10. For m=4,8m²+10=138<256=m^4, giving d_C(A)<16=d_R(A). This stronger direct Frobenius comparison suffices without the general unitarily invariant norm estimate. Thus the exact counterexample needed for the catalogue was independently checked, although the source's other matrix-nearness results were not recertified.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-578). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-24)

The source provides numerical evidence and proves that a real minimizer gives a stationary point of the complex Schur-form optimization problem (Theorem 7.2). Stationarity does not prove global minimality over complex matrices. Taking the real part of a complex feasible matrix also need not preserve feasibility.

The current arXiv record retains version 2 from February 2021. The later Riemann-Oracle work develops numerical methods for matrix nearness problems, including distance to instability; its improved local optimization algorithms do not establish this real-global-minimizer conjecture.

No matching proof or announcement was found in the literature, arXiv, authors' materials, public GitHub or native Palomar checks. Native Zenodo access returned HTTP 403; indexed searches found no matching announcement. The existing static-output-feedback stabilization problem concerns a different constrained family and is not equivalent.
