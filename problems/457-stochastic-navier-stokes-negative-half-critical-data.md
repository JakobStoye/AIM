# 457. Transport-noise Navier–Stokes at critical smoothness minus one half

**Area:** Stochastic fluid PDEs; rough initial velocity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

On $`\mathbb R^3`$, let $`\nu>0`$ and let $`b_1,\ldots,b_K\in C_c^\infty(\mathbb R^3;\mathbb R^3)`$ be divergence-free, with

```math
\nu I-\tfrac12\sum_k b_k(x)\otimes b_k(x)\ge\delta I\quad(\delta>0).
```

Write $`\mathbb P`$ for the Helmholtz projection onto divergence-free fields. Is the Itô equation

```math
du=[\nu\Delta u-\mathbb P\nabla\cdot(u\otimes u)]dt+\sum_k\mathbb P[(b_k\cdot\nabla)u]dW^k_t
```

locally well posed for every deterministic divergence-free $`u_0\in B^{-1/2}_{6,4}(\mathbb R^3)`$? More precisely, does it admit a positive stopping time $`\tau`$ and an adapted mild solution with

```math
u\in C([0,\tau];B^{-1/2}_{6,4})\cap L^4(0,\tau;L^6)\quad\hbox{almost surely},
```

pathwise uniqueness in this class, and continuous dependence in probability in these norms after stopping on common local intervals? The mild equation uses the heat semigroup for both the drift and stochastic convolution. The initial Besov space is the usual inhomogeneous Littlewood–Paley space. The assertion must cover all such spatially varying transport fields, with no extra smallness assumption.

## Application

This random-advection fluid model represents incompressible flow with spatially varying transport noise. Local well-posedness at the stated roughness would allow such initial velocity distributions to determine a unique short-time evolution and make that evolution stable under approximation of the initial data, in the specified norms and probability sense.

## References

1. A. Agresti and M. Veraar, *Nonlinear SPDEs and maximal regularity: an extended survey*, NoDEA **32**, 123 (2025), Open Problem 10 and Theorem 8.26. [Article](https://doi.org/10.1007/s00030-025-01090-2).
2. A. Agresti, *On the absence of blow-up in the 3D Navier–Stokes equations with transport noise* (2026 preprint), local theory and noise-selection hypotheses. [Preprint](https://arxiv.org/abs/2607.15140).

## Status review

Reviewed 15 October 2026 against the original target in [PR #167](https://github.com/MColbrook/AIM/pull/167). Local well-posedness holds at the exact inhomogeneous B^(-1/2)_(6,4) endpoint for all prescribed transport families in AIM457.

[Proof or source](../research/solutions/transport-noise-navier-stokes-negative-half-data/paper/paper.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/457-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Local well-posedness holds at the exact inhomogeneous B^(-1/2)_(6,4) endpoint for all prescribed transport families in AIM457.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

This fixes an endpoint case of Open Problem 10, rather than asking vaguely for the largest critical space. The existing result covers smoothness strictly above $`-1/2`$ (spatial integrability below six); the requested $`B^{-1/2}_{6,4}`$ and $`L^4_tL^6_x`$ norms have the Navier–Stokes critical scaling at high frequencies. Searches on 2026-09-22 checked critical Besov transport-noise theory and recent global-noise results. Results for lower-order multiplicative noise, including general $`L^3`$ initial data, do not treat the derivative noise above. No matching endpoint theorem was found.
