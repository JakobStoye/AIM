# 412. Sharp vanishing-viscosity control time for downstream transport

**Area:** PDE control / advection–diffusion

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Fix $`L,M>0`$. For $`\varepsilon>0`$, consider

```math
y_t+My_x-\varepsilon y_{xx}=0\quad\text{in }(0,T)\times(0,L),\qquad y(t,0)=h(t),\quad y(t,L)=0,
```

with $`y(0)=y_0\in L^2(0,L)`$, interpreted by transposition for boundary inputs $`h\in L^2(0,T)`$. Define

```math
C(T,\varepsilon)=\sup_{\|y_0\|_2\le1}\inf\{\|h\|_{L^2(0,T)}:y(T)=0\}.
```

Is it true that for every $`T>L/M`$,

```math
\lim_{\varepsilon\downarrow0}C(T,\varepsilon)=0?
```

The actuator is at the inflow endpoint and $`M`$ is strictly positive.

## Application

Advection carries a contaminant or temperature perturbation out of a channel in time L/M. The problem asks whether arbitrarily small diffusion changes that sharp control horizon or requires nonvanishing actuation after the flushing time.

## References

1. J.-M. Coron and S. Guerrero, *Singular optimal control: A linear 1-D parabolic–hyperbolic example*, Asymptotic Analysis 44 (2005), 237–257, introduction and conjecture on optimal times. [DOI](https://doi.org/10.3233/ASY-2005-707).
2. C. Laurent and M. Léautaud, *On uniform controllability of 1D transport equations in the vanishing viscosity limit*, Comptes Rendus Mathématique 361 (2023), 265–312, §1.1 and §4.4. [DOI](https://doi.org/10.5802/crmath.405); [Full PDF](https://www.numdam.org/item/10.5802/crmath.405.pdf).
3. P. Lissy, *Explicit lower bounds for the cost of fast controls for some 1-D parabolic or dispersive equations, and a new lower bound concerning the uniform controllability of the 1-D transport-diffusion equation*, Journal of Differential Equations 259 (2015), 5331–5352, Theorem 1.3 and comparison with positive transport. [Author PDF](https://cermics.enpc.fr/~lissyp/Publi/chal.pdf).

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-412). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

The negative-velocity part of the original Coron–Guerrero conjecture has been disproved and is deliberately absent from this formulation. The 2023 treatment still records a gap between the positive-velocity lower and upper times. Searches through 22 September 2026 found no matching resolution for T>L/M; Lissy’s August 2026 arXiv:2608.08041 establishes a heat-control cost coefficient, not the displayed transport limit.
