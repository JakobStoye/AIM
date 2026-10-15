# 217. Does subcritical heat flow always decay faster?

**Area:** Heat propagation / Schrödinger semigroups

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`(M,g)`$ be a connected, complete, noncompact smooth Riemannian manifold without boundary. For $`j\in\{0,+\}`$, let $`V_j\in C^\infty(M;\mathbb R)`$ be bounded below and let $`H_j=-\Delta_g+V_j`$ denote its Friedrichs realization on $`L^2(M,d\mathrm{vol}_g)`$. Assume $`H_j\ge0`$ and $`\inf\sigma(H_j)=0`$. Write $`k_j(t,x,y)>0`$ for the heat kernel of $`e^{-tH_j}`$.
Assume, for some distinct $`x_*,y_*\in M`$,

```math
\int_0^\infty k_+(t,x_*,y_*)\,dt<\infty,
\qquad
\int_0^\infty k_0(t,x_*,y_*)\,dt=\infty,
```

and assume $`\ker_{L^2}H_0=\{0\}`$. These assumptions specify a subcritical operator and a null-critical reference operator. Must

```math
\lim_{t\to\infty}\ \sup_{(x,y)\in K}
\frac{k_+(t,x,y)}{k_0(t,x,y)}=0
\quad\text{for every compact }K\subset M\times M?
```

No pointwise ordering between $`V_+`$ and $`V_0`$ is assumed.

## Application

Heat kernels give the temperature response to a localized pulse and also imaginary-time quantum propagation. This asks whether the potential-theoretic distinction between criticality and subcriticality universally determines their relative long-time decay, even when both spectral thresholds are zero.

## References

1. Martin Fraas, David Krejčiřík, and Yehuda Pinchover, [*On some Strong Ratio Limit Theorems for Heat Kernels*](https://arxiv.org/abs/0912.4337), *Discrete and Continuous Dynamical Systems A* 28 (2010), 495–509, Conjecture 1, Theorem 3.1, and Corollary 1. Original conjecture and conditional symmetric results.
2. David Krejčiřík, [*Large-time behavior of the heat equation: subcriticality versus criticality*](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-18/2015-18_AIM_Krejcirik_2.pdf), AIM workshop problem contribution (2015), Conjecture 2. Reaffirmation of the unresolved heat-kernel comparison.

## Status review

Reviewed 15 October 2026 against the original target in [PR #147](https://github.com/MColbrook/AIM/pull/147). One fixed pair of smooth bounded potentials violates the proposed unordered critical/subcritical heat-kernel comparison.

[Proof or source](../research/solutions/217-critical-subcritical-heat-ratio/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/217-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** One fixed pair of smooth bounded potentials violates the proposed unordered critical/subcritical heat-kernel comparison.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

This is the self-adjoint potential case of the cited conjecture, restricted to equal zero spectral thresholds and a null-critical reference. A positive spectral threshold or a positive-critical reference is already understood. The 2010 paper proves the comparison for nonnegative potential perturbations and under additional heat-kernel comparison assumptions; these are absent here. Counterexamples to Davies’ different, single-operator ratio conjecture do not themselves decide this two-operator question.

**Search audit:** Searched “Fraas Krejcirik Pinchover heat kernel ratio conjecture solved”, “critical subcritical strong ratio limit 2025 2026”, and “null critical heat kernel comparison counterexample”. Searches included later proofs, counterexamples, and 2025–2026 updates. No resolution matching the stated hypotheses was located.
