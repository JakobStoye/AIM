# 473. Mass conservation for fractional porous-medium flow on noncompact manifolds

**Area:** Nonlocal PDEs; conservation of diffusing mass

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`(M,g)`$ be a complete, connected, noncompact Riemannian manifold of dimension $`N\ge2`$, with $`\mathrm{Ric}\ge-(N-1)k`$ for some $`k\ge0`$ and the uniform Faber–Krahn inequality
$`\lambda_1(D)\ge c\,\mathrm{Vol}(D)^{-2/N}`$ for all relatively compact smooth domains $`D\subset M`$, with $`c>0`$. Fix $`m>1`$ and $`0<s<1`$ and use the spectral fractional Laplace–Beltrami operator in

```math
\partial_tu+(-\Delta_M)^s(u^m)=0.
```

Write $`G_s(x,y)=\Gamma(s)^{-1}\int_0^\infty p_t(x,y)t^{s-1}\,dt`$, where $`p_t`$ is the heat kernel, and set

```math
\|f\|_{1,x_0,G_s}=\int_{B_1(x_0)}|f|+\int_{M\setminus B_1(x_0)}|f(x)|G_s(x,x_0).
```

All integrals use Riemannian volume. A nonnegative weak dual solution has $`u\in C([0,T];L^1_{x_0,G_s})`$ for every $`x_0,T`$, $`u^m\in L^1((0,T);L^1_{\rm loc}(M))`$, and

```math
\int_0^T\!\int_M\bigl[(-\Delta_M)^{-s}u\,\partial_t\psi-u^m\psi\bigr]=0
```

for every compactly supported smooth space-time test function $`\psi`$.

For every $`u_0\ge0`$ in $`L^1(M)`$ and every such weak dual solution with $`u(0)=u_0`$ and $`u(t)\in L^1(M)`$, prove or disprove

```math
\int_M u(t,x)\,d\mathrm{Vol}(x)=\int_Mu_0(x)\,d\mathrm{Vol}(x)\qquad(t>0).
```

This asks for conservation at every finite time, not merely the known upper bound on the total mass.

## Application

The assertion rules out loss of material at spatial infinity in fractional diffusion models on unbounded curved media.

## References

1. E. Berchio, M. Bonforte, G. Grillo and M. Muratori, *The fractional porous medium equation on noncompact Riemannian manifolds*, Math. Ann. **389** (2024), 3603–3651, Assumption 2.1, Definition 2.1 and §7. [Article](https://doi.org/10.1007/s00208-023-02731-6); [accepted manuscript](https://iris.polito.it/retrieve/handle/11583/2984889/691780).
2. G. Grillo, *The Fractional Porous Medium Equation on noncompact Riemannian manifolds*, Oberwolfach Reports 14/2025, contribution on weak dual solutions and unresolved uniqueness/fundamental solutions. [Workshop report](https://ems.press/content/serial-article-files/51358?nt=1).

## Status review

Reviewed 15 October 2026 against the original target in [PR #158](https://github.com/MColbrook/AIM/pull/158). Every weak dual solution in the stated spatial-L1 class conserves its initial mass at every finite time.

[Proof or source](../research/solutions/473-manifold-fractional-pme-mass-conservation/paper/mass_conservation.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/473-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Every weak dual solution in the stated spatial-L1 class conserves its initial mass at every finite time.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Mass conservation under these geometric assumptions is explicitly listed in §7 of the final paper; the difficulty is constructing cutoffs with suitable fractional Laplacian bounds. Searches on 2026-09-22 checked conservation, stochastic completeness, and subsequent fractional diffusion papers. Results for compact manifolds, the ordinary Laplace–Beltrami operator, or fast diffusion do not settle this assertion. The separate uniqueness entry asks whether solutions coincide; this entry asks for a quantitative conservation law for each admissible solution.
