# 396. Polynomial decay for KdV with three critical linear modes

**Area:** Dispersive PDEs / boundary stabilization

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Set $`L=14\pi`$. For the real-valued KdV problem

```math
y_t+y_x+y_{xxx}+yy_x=0,\quad 0<x<L,\qquad y(t,0)=y(t,L)=y_x(t,L)=0,
```

do there exist $`\delta,C,\alpha>0`$ such that every solution with $`\|y(0)\|_{L^2(0,L)}\le\delta`$ satisfies

```math
\|y(t)\|_{L^2(0,L)}\le C(1+t)^{-\alpha}\qquad(t\ge0)?
```

Solutions are taken in the usual energy class $`C([0,\infty);L^2)\cap L^2_{\mathrm{loc}}([0,\infty);H^1_0)`$. This length has three undamped linear modes: the integer pairs $`(7,7),(2,11),(11,2)`$ satisfy $`L=2\pi\sqrt{(k^2+k\ell+\ell^2)/3}`$.

## Application

KdV models long shallow-water waves. At critical channel lengths the boundary fails to damp some linear modes, so nonlinear energy transfer determines whether a quantitative algebraic stabilization rate exists.

## References

1. J. Niu and S. Xiang, *Small-time local controllability of a KdV system for all critical lengths*, preprint, version 2 (16 December 2025), §2.4.5. [arXiv:2501.13640](https://arxiv.org/abs/2501.13640).
2. H.-M. Nguyen, *Decay for the nonlinear KdV equations at critical lengths*, Journal of Differential Equations 295 (2021), 249–291, main decay theorems and discussion of the dimension of the undamped subspace. [DOI](https://doi.org/10.1016/j.jde.2021.05.057); [arXiv:2012.08792](https://arxiv.org/abs/2012.08792).

## Status review

Reviewed 15 October 2026 against the original target in [PR #130](https://github.com/MColbrook/AIM/pull/130). Uniform small-data L2 decay with exponent one half at the exact critical length fourteen pi, for every real energy-class datum in one common small ball.

[Proof or source](../research/solutions/kdv-14pi-polynomial-decay/paper/manuscript.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/396-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Periodic stable quadratic response and invisible resonant center motion yield coercive whole-center observation, rough-data quartic energy loss and all-time reciprocal-energy decay.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The December 2025 paper expressly identifies polynomial decay for odd undamped dimension greater than one as open. The length 14π is a concrete instance with dimension three. Its completed classification of small-time controllability does not establish uncontrolled polynomial decay. Searches through 22 September 2026 for this length, odd critical modes and later decay results located no resolution.
