# 258 — Global constrained null control of a two-phase Stefan interface

**Area:** Free-boundary control / thermal processing

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix $`L,d_l,d_r,\lambda,T>0`$, $`L_0,L_T\in(0,L)`$, and arbitrary $`y_0\in C_c^\infty(0,L_0)`$, $`z_0\in C_c^\infty(L_0,L)`$. Can two controls $`v_l,v_r\in L^\infty(0,T)`$ produce a solution on the whole interval $`[0,T]`$ of

```math
\begin{aligned}
y_t-d_ly_{xx}&=0&& (0<x<\ell(t)),\\
z_t-d_rz_{xx}&=0&& (\ell(t)<x<L),\\
y(\ell(t),t)=z(\ell(t),t)&=0,\qquad y(0,t)=v_l(t),\quad z(L,t)=v_r(t),\\
d_ly_x(\ell(t)^-,t)-d_rz_x(\ell(t)^+,t)&=-\lambda\ell'(t),
\end{aligned}
```

with initial data $`(y_0,z_0,L_0)`$ and terminal conditions $`y(\cdot,T)=z(\cdot,T)=0`$, $`\ell(T)=L_T`$? Require $`\ell\in C^1([0,T])`$ and $`0<\ell(t)<L`$ throughout, with the temperatures continuous in $`L^2`$ after extension by zero to $`(0,L)`$. These smooth data satisfy the initial interface compatibility conditions. No sign restrictions or smallness assumptions are imposed on the data or controls.

## Application

This asks whether arbitrary temperature profiles and a phase interface can be reset in a prescribed time by heating or cooling at both ends of a rod.

## References

1. E. Fernández-Cara, *Remarks on control and inverse problems for PDEs* (2025), [SeMA Journal 82, 267–288](https://doi.org/10.1007/s40324-024-00363-7), §3, equations (6)–(7), Theorem 3 and Problem 5. Provides this boundary model and asks whether global control or a data-dependent minimal time holds.
2. R. K. C. Araújo, E. Fernández-Cara, J. Límaco and D. A. Souza, *Remarks on the control of two-phase Stefan free-boundary problems* (2022), [SIAM JCO 60, 3078–3099](https://doi.org/10.1137/21M1402261); [manuscript](https://arxiv.org/abs/2402.06710), introduction and main theorem. Establishes local constrained control for two distributed actuators and gives an obstruction with one actuator.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/258-signed-stefan-control/stefan_signed_control.pdf) establishes the full original target. Full affirmative resolution of the exact target.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/258-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #51](https://github.com/MColbrook/AIM/pull/51) at `8f5c27ab02df36559997f106dcbccfb6f6c3738a`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
