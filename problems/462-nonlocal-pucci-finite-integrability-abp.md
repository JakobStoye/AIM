# 462. A finite-integrability ABP estimate for general nonlocal Pucci operators

**Area:** Fully nonlinear nonlocal PDEs; maximum principles

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Fix $`n\ge2`$, $`0<s<1`$ and $`0<\lambda\le\Lambda`$. For $`\delta^2u(x,y)=u(x+y)+u(x-y)-2u(x)`$ define

```math
\mathcal M^+u(x)=\frac12\int_{\mathbb R^n}
\frac{\Lambda(\delta^2u(x,y))_+-\lambda(\delta^2u(x,y))_-}{|y|^{n+2s}}\,dy.
```

Do there exist $`1\le p<\infty`$, $`\vartheta>0`$ and $`C<\infty`$, depending only on $`n,s,\lambda,\Lambda`$, such that every bounded upper-semicontinuous viscosity subsolution

```math
\mathcal M^+u\ge f\ \text{in }B_1,\qquad u\le0\ \text{in }\mathbb R^n\setminus B_1,
```

with continuous $`f`$ and $`\|f\|_\infty\le1`$, satisfies

```math
\sup_{B_1}u\le C\|f_-\|_{L^p(B_1)}^\vartheta?
```

Viscosity testing uses a smooth function near its contact point and the original $`u`$ outside that neighborhood. The constants must be independent of the size of the support of $`f`$.

## Application

Such a maximum principle would control a value function for a jump-process control problem by an integrable source and support a nonlinear nonlocal analogue of Calderón–Zygmund theory.

## References

1. X. Fernández-Real and X. Ros-Oton, *Integro-Differential Elliptic Equations*, Progress in Mathematics **350**, Birkhäuser (2024). [Book](https://doi.org/10.1007/978-3-031-54242-8); [author manuscript](https://arxiv.org/abs/2411.12455).

2. N. Guillén and R. Schwab, *Aleksandrov–Bakelman–Pucci type estimates for integro-differential equations*, Arch. Ration. Mech. Anal. **206** (2012), 111–157, structured-kernel estimates. [Author preprint](https://arxiv.org/abs/1101.0279).
3. S. Kitano, *$`W^{\sigma,p}`$ a priori estimates for fully nonlinear integro-differential equations* (2022), the restricted matrix-kernel setting. [Preprint](https://arxiv.org/abs/2207.06728).

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-462). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

This is Open Question 3.3 in §3.6.2 of the book, with the extremal operator expanded explicitly. Searches on 2026-09-22 checked nonlocal ABP estimates, finite $`L^p`$ data and Kitano's later work. The located finite-integrability theorems impose matrix-angular structure on kernels; they do not cover the full Pucci class above. Existing $`L^\infty`$ source estimates do not imply a bound tending to zero with $`\|f_-\|_p`$.
