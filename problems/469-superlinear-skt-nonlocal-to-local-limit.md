# 469. The local limit of superlinear multispecies nonlocal diffusion

**Area:** Cross-diffusion PDEs; population dispersal

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\Omega\subset\mathbb R^d`$ be smooth, bounded and connected, $`n\ge2`$, and $`s>1`$. Set

```math
P_i(u)=u_i(a_{i0}+\sum_j a_{ij}u_j^s),\qquad
f_i(u)=b_{i0}-\sum_jb_{ij}u_j,
```

where $`a_{i0}>0`$, $`b_{i0},b_{ij}\ge0`$, and the symmetric matrix $`(a_{ij})`$ has nonnegative entries and satisfies

```math
a_{ii}>C(s)\sum_{j\ne i}a_{ij},\quad
C(s)=\begin{cases}s^2/[2(s+1)(s-1)],&1<s<2,\\{[4(s-1)^2+1]}/[4(s+1)(s-1)],&s\ge2.\end{cases}
```

Choose a smooth nonnegative radial compactly supported kernel $`J`$, positive near zero, normalized by $`\tfrac12\int_{\mathbb R^d}J(z)z_1^2\,dz=1`$, and $`J_\varepsilon(z)=\varepsilon^{-d}J(z/\varepsilon)`$. Let $`u^\varepsilon`$ be the global nonnegative strong solution of

```math
\partial_tu_i^\varepsilon=\varepsilon^{-2}\int_\Omega J_\varepsilon(x-y)[P_i(u^\varepsilon(y))-P_i(u^\varepsilon(x))]dy+u_i^\varepsilon f_i(u^\varepsilon)
```

with fixed nonnegative $`u_i^0\in L^\infty(\Omega)\cap BV(\Omega)`$.

As $`\varepsilon\downarrow0`$, does a subsequence converge strongly in $`L^1((0,T)\times\Omega)^n`$ for every finite $`T`$ to a global weak solution of

```math
\partial_tu_i=\Delta P_i(u)+u_if_i(u),\qquad\partial_\nu P_i(u)=0,\qquad u_i(0)=u_i^0?
```

The limiting fluxes and reactions must pass to the limit in the weak formulation, not just the densities.

## Application

The limit would justify replacing finite-range population dispersal by a local SKT cross-diffusion law when the interaction range is small.

## References

1. P. Hirvonen, A. Jüngel and A. Pollino, *Superlinear nonlocal diffusion systems for multispecies populations: well-posedness and discrete chain rules* (September 2026 preprint), §1.1, assumptions (A1)–(A5a), and Theorem 1. [Full preprint](https://arxiv.org/html/2609.09921v1).
2. G. Galiano and J. Velasco, *Convergence of solutions of a rescaled evolution nonlocal cross-diffusion problem to its local diffusion counterpart*, Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A Math. **116**, 93 (2022), the two-species $`s=1`$ result. [Article](https://doi.org/10.1007/s13398-022-01231-7).

## Status review

Reviewed 15 October 2026 against the original target in [PR #155](https://github.com/MColbrook/AIM/pull/155). The regional superlinear SKT strong solutions converge along one global subsequence to a genuine no-flux local weak solution for every fixed s>1.

[Proof or source](../research/solutions/superlinear-skt-localization/paper/localization.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/469-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** The regional superlinear SKT strong solutions converge along one global subsequence to a genuine no-flux local weak solution for every fixed s>1.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The September 2026 source explicitly calls extension of the localization argument to $`s\ne1`$ open. Its global nonlocal theorem uses the stronger coefficient condition written here; merely copying the weaker condition for the local equation would not justify the approximating solutions. Searches on 2026-09-22 for superlinear SKT localization and the paper title found no subsequent resolution. Local limits for convolution inside the pressure or triangular diffusion matrices are different models or restrictions.
