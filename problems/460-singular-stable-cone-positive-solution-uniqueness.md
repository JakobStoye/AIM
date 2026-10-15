# 460. Uniqueness of positive harmonic profiles for singular stable operators in cones

**Area:** Nonlocal elliptic PDEs; free-boundary blow-up profiles

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`n\ge2`$, $`0<s<1`$, and let $`\mu`$ be a finite even nonnegative measure on $`S^{n-1}`$ such that

```math
\mu(S^{n-1})\le\Lambda,\qquad\inf_{|e|=1}\int_{S^{n-1}}|e\cdot\theta|^{2s}\,\mu(d\theta)\ge\lambda>0.
```

Define the stable operator

```math
Lu(x)=\frac12\int_{S^{n-1}}\int_0^\infty[2u(x)-u(x+r\theta)-u(x-r\theta)]\frac{dr}{r^{1+2s}}\,\mu(d\theta).
```

Let $`\Sigma\subsetneq\mathbb R^n`$ be a closed convex cone with nonempty interior. Suppose $`w_1,w_2`$ are continuous on $`\mathbb R^n`$, zero on $`\Sigma`$, strictly positive on $`\Sigma^c`$, and satisfy $`Lw_i=0`$ in $`\Sigma^c`$ in the viscosity sense. Assume $`|w_i(x)|\le C_i(1+|x|)^{\beta_i}`$ for some $`\beta_i<2s`$, so the tails in the equation are integrable. Must $`w_1=cw_2`$ for a constant $`c>0`$? Allow $`\mu`$ to be singular, including measures supported on finitely many directions.

## Application

Uniqueness of these profiles is an ingredient in classifying contact interfaces for obstacle problems driven by anisotropic jumps.

## References

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. X. Ros-Oton and M. Weidner, *Obstacle problems with singular kernels*, Ann. Scuola Norm. Sup. Pisa Cl. Sci. **27** (2026), 535–588, Introduction and angular integrability assumptions. [Article](https://doi.org/10.2422/2036-2145.202309_010); [preprint](https://arxiv.org/abs/2308.01695).

## Status review

Reviewed 15 October 2026 against the original target in [PR #156](https://github.com/MColbrook/AIM/pull/156). Positive integrable-growth harmonic profiles outside every admitted convex cone are proportional, including singular spectral measures.

[Proof or source](../research/solutions/460-singular-stable-cone-positive-solution-uniqueness/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/460-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Positive integrable-growth harmonic profiles outside every admitted convex cone are proportional, including singular spectral measures.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

This is the integrable-growth version of Open Question 4.4. The published 2026 paper obtains results under an $`L^p`$ angular-density hypothesis with $`p>n/(2s)`$ and explicitly identifies the general stable class as unresolved. Its preprint dates from 2023; publication in 2026 is not a new resolution for singular spectral measures. Searches on 2026-09-22 for positive cone profiles and singular stable boundary Harnack principles found no general uniqueness result. Interior Harnack inequalities themselves may fail in this class.
