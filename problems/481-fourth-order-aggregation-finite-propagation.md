# 481. Finite propagation in fourth-order aggregation–diffusion

**Area:** Degenerate parabolic PDEs; moving tissue boundaries

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Fix $`d\ge2`$ and $`\chi>0`$. For every compactly supported $`\rho_0\in H^1(\mathbb R^d)`$ with $`\rho_0\ge0`$ and $`\int\rho_0=1`$, does

```math
\partial_t\rho=-\nabla\cdot(\rho\nabla\Delta\rho)-\chi\Delta(\rho^2),\qquad \rho(0)=\rho_0,
```

admit a nonnegative global weak solution with the following finite-propagation property: for every $`T<\infty`$, some $`R_T<\infty`$ satisfies $`\rho(t,x)=0`$ for almost every $`(t,x)\in(0,T)\times(\mathbb R^d\setminus B_{R_T})`$?

Here a weak solution is a narrowly continuous probability-valued curve with finite second moment and

```math
\rho\in L^\infty(0,T;H^1)\cap L^2(0,T;H^2)
```

for every finite $`T`$, satisfying, for all $`\phi\in C_c^2(\mathbb R^d)`$ and $`0\le a<b`$,

```math
\int\phi[\rho(b)-\rho(a)]=-\int_a^b\!\int\bigl(\rho\Delta\rho\Delta\phi+\Delta\rho\nabla\rho\cdot\nabla\phi+\chi\rho^2\Delta\phi\bigr)\,dx\,dt.
```

Narrow continuity means continuity against bounded continuous spatial tests. Only existence of a solution preserving bounded support on finite time intervals is requested; weak uniqueness is a separate question.

## Application

This would justify a genuine moving edge for compact tissue aggregates in a fourth-order local adhesion model.

## References

1. J. A. Carrillo, A. Esposito, C. Falcó and A. Fernández-Jiménez, *Competing effects in fourth-order aggregation–diffusion equations*, Proc. Lond. Math. Soc. **129**, e12623 (2024), Introduction, Definition 2.1 and Theorem 2.2. [Article](https://doi.org/10.1112/plms.12623).
2. C. Falcó, R. E. Baker and J. A. Carrillo, *A nonlocal-to-local approach to aggregation-diffusion equations*, SIAM Review **67** (2025), 353–372, §4. [Article](https://doi.org/10.1137/25M1726248).

## Status review

Reviewed 15 October 2026 against the original target in [PR #169](https://github.com/MColbrook/AIM/pull/169). Every stated compactly supported H1 probability datum admits one global fourth-order weak curve with bounded support on each finite horizon.

[Proof or source](../research/solutions/481-fourth-order-aggregation-finite-propagation/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/481-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Every stated compactly supported H1 probability datum admits one global fourth-order weak curve with bounded support on each finite horizon.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

The 2024 paper constructs weak solutions and explicitly identifies preservation of compact support as an unresolved free-boundary question, supported there by computations. The $`m=2`$ case above lies in its globally existing subcritical range in every finite dimension. Searches on 2026-09-22 for fourth-order aggregation–diffusion finite propagation and compact support found no later resolution for this model and class of initial data. Propagation results for other thin-film mobilities or for purely attractive second-order equations do not answer this statement.
