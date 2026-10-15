# 474. Point-source solutions of fractional porous-medium diffusion on manifolds

**Area:** Nonlocal PDEs; anomalous diffusion from a point source

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`(M,g)`$ be a complete, connected, noncompact Riemannian manifold of dimension $`N\ge2`$, with $`\mathrm{Ric}\ge-(N-1)k`$ for some $`k\ge0`$ and the uniform Faber–Krahn inequality
$`\lambda_1(D)\ge c\,\mathrm{Vol}(D)^{-2/N}`$ for all relatively compact smooth domains $`D\subset M`$, with $`c>0`$. Fix $`m>1`$ and $`0<s<1`$ and use the spectral fractional Laplace–Beltrami operator in

```math
\partial_tu+(-\Delta_M)^s(u^m)=0.
```

For every $`o\in M`$ and $`A>0`$, does there exist a nonnegative distributional solution $`u`$ for $`t>0`$ with

```math
u\in C((0,\infty);L^1(M))\cap L^\infty_{\rm loc}((0,\infty)\times M),\qquad
0<\sup_{0<t<T}\|u(t)\|_1\le A\quad(T>0),
```

whose initial trace is $`A\delta_o`$? Precisely, require $`u^m\in L^1_{\rm loc}((0,\infty)\times M)`$, the identity

```math
\int_0^\infty\!\int_M u\,\partial_t\phi=\int_0^\infty\!\int_Mu^m(-\Delta_M)^s\phi
```

for compactly supported smooth tests (with integrable right side), and
$`\lim_{t\downarrow0}\int_Mu(t)\psi=A\psi(o)`$ for every bounded continuous $`\psi`$. No radial symmetry or homogeneity of $`M`$ is assumed.

## Application

A fundamental solution represents release of a concentrated amount of material and supplies a candidate reference profile for the spread of general concentrations.

## References

1. E. Berchio, M. Bonforte, G. Grillo and M. Muratori, *The fractional porous medium equation on noncompact Riemannian manifolds*, Math. Ann. **389** (2024), 3603–3651, Assumption 2.1, Definition 2.1 and §7. [Article](https://doi.org/10.1007/s00208-023-02731-6); [accepted manuscript](https://iris.polito.it/retrieve/handle/11583/2984889/691780).
2. G. Grillo, *The Fractional Porous Medium Equation on noncompact Riemannian manifolds*, Oberwolfach Reports 14/2025, contribution on weak dual solutions and unresolved uniqueness/fundamental solutions. [Workshop report](https://ems.press/content/serial-article-files/51358?nt=1).

## Status review

Reviewed 15 October 2026 against the original target in [PR #157](https://github.com/MColbrook/AIM/pull/157). Every admitted complete manifold and positive point mass has a nonnegative distributional fractional porous-medium solution with the required positive-time continuity and initial trace.

[Proof or source](../research/solutions/474-manifold-fractional-pme-point-source/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/474-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Every admitted complete manifold and positive point mass has a nonnegative distributional fractional porous-medium solution with the required positive-time continuity and initial trace.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Both §7 of the 2024 paper and the 2025 Oberwolfach report explicitly leave existence for Dirac initial data open on this manifold class. Searches on 2026-09-22 checked fundamental solutions, measure data and later manifold diffusion publications. Known measure-data results for Euclidean fractional diffusion and nonfractional negatively curved diffusion do not cover this combination of geometry and operator. Only existence is requested; no unsupported universal asymptotic profile on arbitrary manifolds is asserted.
