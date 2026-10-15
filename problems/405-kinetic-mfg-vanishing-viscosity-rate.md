# 405. An algebraic vanishing-noise rate for kinetic mean-field games

**Area:** Kinetic PDEs / mean-field games

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix $`d\ge1`$, $`T>0`$, and a smooth nonnegative compactly supported probability density $`m_{\rm in}`$ on $`Q=\mathbb T^d\times\mathbb R^d`$. For each $`0\le\nu\le1`$, let $`m_\nu`$ be the density component minimizing

```math
\mathcal J(m,a)=\int_0^T\!\int_Q\left(\frac{|a|^2}{2m}+\frac{m^2}{2}\right)dx\,dv\,dt+\frac12\int_Q m(T)^2dx\,dv
```

subject to

```math
\partial_tm+v\cdot\nabla_xm-\nu\Delta_vm+\nabla_v\cdot a=0,\qquad m(0)=m_{\rm in}.
```

Admissible pairs have narrowly continuous probability densities with finite second velocity moment, the equation holds distributionally, and $`\mathcal J<\infty`$; use $`|a|^2/m=0`$ at $`(m,a)=(0,0)`$ and $`+\infty`$ when $`m=0`$, $`a\ne0`$. Does there exist an exponent $`\eta=\eta(d)>0`$ such that for every such datum and horizon some $`C<\infty`$, independent of $`\nu`$, satisfies

```math
\|m_\nu-m_0\|_{L^2((0,T)\times Q)}\le C\nu^\eta\qquad(0<\nu\le1)?
```

## Application

Here agents control acceleration, and noise diffuses their velocities. The variational formulation is a local-congestion kinetic mean-field game; a rate would quantify the error introduced by stochastic regularization of deterministic traffic and crowd models.

## References

1. W. Tang and Y. P. Zhang, *The Convergence Rate of Vanishing Viscosity Approximations for Mean Field Games*, SIAM Journal on Mathematical Analysis 57 (2025), 3217–3254, §7, problem 4(b). [DOI](https://doi.org/10.1137/24M1640008); [Author PDF](https://www.columbia.edu/~wt2319/VV.pdf).
2. M. Griffin-Pickering and A. R. Mészáros, *A variational approach to first order kinetic mean field games with local couplings*, Communications in Partial Differential Equations 47 (2022), 1945–2022, equation (1.1), §3.2 and existence/uniqueness theorems. [DOI](https://doi.org/10.1080/03605302.2022.2101003); [arXiv:2112.03141](https://arxiv.org/abs/2112.03141).

## Status review

Reviewed 15 October 2026 against the original target in [PR #127](https://github.com/MColbrook/AIM/pull/127). A dimension-independent half-power vanishing-noise density rate.

[Proof or source](../research/solutions/405-kinetic-mfg-vanishing-viscosity-rate/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/405-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The original weak minimizing densities satisfy the spacetime and terminal L2 estimates with exponent1/2 for every diffusivity in(0,1].

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The SIAM source explicitly asks for kinetic vanishing-viscosity rates. This formulation selects the quadratic acceleration and linear local-congestion case and defines the density through a strictly convex variational problem, including the inviscid density. The 2022 work establishes the underlying first-order variational theory, not a noise-dependent approximation rate. Searches through 22 September 2026 for kinetic MFG viscosity rates and acceleration-control convergence found no matching result.
