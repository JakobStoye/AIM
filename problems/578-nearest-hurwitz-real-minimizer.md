# 578. A real nearest matrix with spectrum in the closed left half-plane

**Area:** Numerical linear algebra and matrix optimization

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

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

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-578). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-24)

The source provides numerical evidence and proves that a real minimizer gives a stationary point of the complex Schur-form optimization problem (Theorem 7.2). Stationarity does not prove global minimality over complex matrices. Taking the real part of a complex feasible matrix also need not preserve feasibility.

The current arXiv record retains version 2 from February 2021. The later Riemann-Oracle work develops numerical methods for matrix nearness problems, including distance to instability; its improved local optimization algorithms do not establish this real-global-minimizer conjecture.

No matching proof or announcement was found in the literature, arXiv, authors' materials, public GitHub or native Palomar checks. Native Zenodo access returned HTTP 403; indexed searches found no matching announcement. The existing static-output-feedback stabilization problem concerns a different constrained family and is not equivalent.
