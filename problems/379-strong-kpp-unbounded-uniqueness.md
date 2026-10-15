# 379. Uniqueness of strong-KPP equilibria on general unbounded domains

**Area:** Reaction–diffusion; population equilibria

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, be connected, unbounded, and uniformly $`C^{2,\gamma}`$ for some $`0<\gamma<1`$: its boundary has graph charts of a common positive radius with uniformly bounded $`C^{2,\gamma}`$ norms. Let $`f\in C^{1,\gamma}([0,\infty))`$ satisfy $`f(0)=f(1)=0`$, $`f'(0)>0`$, $`f>0`$ on $`(0,1)`$, $`f<0`$ on $`(1,\infty)`$, and $`f(s)/s`$ strictly decreasing on $`(0,1]`$. For each fixed $`\beta\in[0,1)`$, is there at most one bounded positive classical solution of

```math
-\Delta u=f(u)\quad\hbox{in }\Omega,\qquad \beta\partial_nu+(1-\beta)u=0\quad\hbox{on }\partial\Omega?
```

Here $`n`$ is the outward normal, and $`\beta=0`$ denotes Dirichlet boundary conditions. No periodicity or spectral-gap assumption at spatial infinity is made.

## Application

The strong KPP condition expresses a decreasing per-capita growth rate. Uniqueness would show that an irregular unbounded habitat with a fixed boundary loss law cannot support multiple positive stationary populations.

## References

1. H. Berestycki and C. Graham, [*The steady states of strong-KPP reactions in general domains*](https://arxiv.org/abs/2212.06611), Journal of the European Mathematical Society, published online (2025), §1, Conjecture 1.3 and Theorem 1.1; DOI [10.4171/JEMS/1578](https://doi.org/10.4171/JEMS/1578).
2. H. Berestycki and C. Graham, [*A Stable-Compact Method for Qualitative Properties of Semilinear Elliptic Equations*](https://doi.org/10.1007/s00205-026-02168-6), Archive for Rational Mechanics and Analysis 250 (2026), article 21, §8.1, Open Question 3.

## Status review

Reviewed 15 October 2026 against the original target in [PR #149](https://github.com/MColbrook/AIM/pull/149). Universal strong-KPP uniqueness fails on a uniformly smooth connected unbounded domain in dimension 21.

[Proof or source](../research/solutions/379-uniform-kpp-multiplicity/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/379-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Universal strong-KPP uniqueness fails on a uniformly smooth connected unbounded domain in dimension 21.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using strong-KPP uniqueness in arbitrary unbounded domains. The 2026 paper explicitly retains this question. The JEMS theorem establishes uniqueness when the linear growth rate avoids the closure of the domain's principal spectrum; irregular domains at the remaining spectral values are not covered. The 2026 bounded-Lipschitz-domain theorem resolves a different earlier conjecture and is excluded from this collection. Weak KPP nonlinearities can admit multiplicity, but strict decrease of $`f(s)/s`$ excludes those examples. No resolution of the unrestricted strong-KPP assertion was located.
