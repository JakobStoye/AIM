# 404. Uniform convergence of value functions in local mean-field games

**Area:** Hamilton–Jacobi / Fokker–Planck PDE systems

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

On $`\mathbb T^d`$, $`1\le d\le3`$, fix $`T>0`$, a nonnegative smooth probability density $`m_{\rm in}`$, and a smooth terminal cost $`g`$. For $`\nu>0`$, let $`(u_\nu,m_\nu)`$ solve

```math
-\partial_tu_\nu-\nu\Delta u_\nu+\tfrac12|\nabla u_\nu|^2=m_\nu,\qquad \partial_tm_\nu-\nu\Delta m_\nu-\nabla\cdot(m_\nu\nabla u_\nu)=0,
```



```math
m_\nu(0)=m_{\rm in},\qquad u_\nu(T)=g.
```

Is there a continuous function $`u`$ on $`(0,T)\times\mathbb T^d`$ such that for every $`0<\tau<T/2`$,

```math
\|u_\nu-u\|_{L^\infty([\tau,T-\tau]\times\mathbb T^d)}\longrightarrow0\quad\text{as }\nu\downarrow0?
```

No strictly positive lower bound on $`m_{\rm in}`$ is imposed; vacuum regions are allowed.

## Application

The value function determines an agent’s optimal future cost. Uniform convergence is needed to interpret artificial diffusion as a stable approximation in models of crowd motion and local congestion, including initially unoccupied regions.

## References

1. W. Tang and Y. P. Zhang, *The Convergence Rate of Vanishing Viscosity Approximations for Mean Field Games*, SIAM Journal on Mathematical Analysis 57 (2025), 3217–3254, §2 assumption (H3*), Theorem 5.5 and §7, problem 2(a). [DOI](https://doi.org/10.1137/24M1640008); [Author PDF](https://www.columbia.edu/~wt2319/VV.pdf).
2. P. J. Graber and A. R. Mészáros, *Sobolev regularity for first order mean field games*, Annales de l’Institut Henri Poincaré C, Analyse non linéaire 35 (2018), 1557–1576, Theorem 1.2. [DOI](https://doi.org/10.1016/j.anihpc.2018.01.002).

## Status review

Reviewed 15 October 2026 against the original target in [PR #131](https://github.com/MColbrook/AIM/pull/131). Whole-family local uniform vanishing-viscosity convergence for the exact quadratic local MFG in dimensions one through three, with initial vacuum allowed.

[Proof or source](../research/solutions/local-mfg-uniform-vanishing-viscosity/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/404-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Averaged finite-energy path perturbations give uniform continuity; exact-initial heat recovery, convex uniqueness and path calibration identify occupied values; homogeneous comparison identifies vacuum values.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The SIAM source asks for local uniform convergence beyond its weighted L2 results. The displayed quadratic Hamiltonian and linear local coupling form an explicit case with possible vacuum, avoiding ambiguities about a weak value function outside the density support by asking directly for convergence of the viscous family. The July 2026 paper “Beyond separability” (DOI 10.1016/j.spa.2026.105061) assumes nonlocal measure dependence. Searches through 22 September 2026 located no resolution for this local-coupling assertion.
