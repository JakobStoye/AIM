# 417. Polynomial growth of reachable neighborhoods for analytic control systems

**Area:** Nonlinear control / minimum-time regularity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`n\ge3`$ and let $`X_0,\ldots,X_m`$ be real-analytic vector fields near $`0\in\mathbb R^n`$, with $`X_0(0)=0`$. For measurable controls $`u(t)\in[-1,1]^m`$, consider

```math
\dot x=X_0(x)+\sum_{j=1}^mu_j(t)X_j(x),\qquad x(0)=0.
```

Let $`R_{\le t}(0)`$ contain all endpoints reached in time at most $`t`$ by trajectories that exist in the vector fields' domain. Assume $`0\in\mathop{\mathrm{int}}\nolimits R_{\le t}(0)`$ for every sufficiently small $`t>0`$. Must there exist $`C,T>0`$ and an integer $`N\ge1`$, depending on the system, such that

```math
B(0,Ct^N)\subseteq R_{\le t}(0)\qquad(0<t<T)?
```

## Application

Qualitative local controllability says nearby maneuvers are possible. The conjecture asks whether analytic dynamics always supply a polynomial time-versus-displacement guarantee, equivalent to Hölder behavior of the minimum-time value function near equilibrium.

## References

1. S. Jafarpour, *On Small-Time Local Controllability*, SIAM Journal on Control and Optimization 58 (2020), 425–446, Conjecture 1.2 and its relation to finite-jet robustness. [DOI](https://doi.org/10.1137/16M1068797); [full preprint, Conjecture 2](https://arxiv.org/html/1604.02432).
2. F. Marbach, *Time-iteration methods for controllability*, lecture notes (2026), §4.7, equation (4.29) and Open Problem 4.24, the related norm-budget formulation. [Full text](https://arxiv.org/html/2602.19272v1).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/417-polynomial-reachable-growth-counterexample/paper/main.pdf) establishes the full original target. Full negative resolution of the exact target.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/417-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #57](https://github.com/MColbrook/AIM/pull/57) at `fff30eeb072395341d9944e4c75d5267b770f3b8`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
