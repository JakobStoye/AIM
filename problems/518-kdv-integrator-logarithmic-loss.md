# 518. Removing the logarithmic loss in the Li–Wu KdV integrator

**Area:** Numerical PDE analysis and dispersive equations

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Consider the real periodic KdV equation

```math
\partial_tu+\partial_x^3u=\tfrac12\partial_x(u^2),\qquad x\in\mathbb T=\mathbb R/(2\pi\mathbb Z),\qquad u(0)=u_0,
```

where $`u_0\in H^\gamma(\mathbb T)`$ has mean zero and $`0<\gamma\le1`$. Let $`S_t=e^{-t\partial_x^3}`$, let $`P_0f=(2\pi)^{-1}\int_{\mathbb T}f`$, and let $`P=I-P_0`$. The multiplier $`D^{-1}=\partial_x^{-1}`$ has symbol $`(ik)^{-1}`$ for $`k\ne0`$ and zero for $`k=0`$; set $`D^{-2}=(D^{-1})^2`$.

For $`\tau=T/L`$, define the Li–Wu time discretization by $`u^0=u_0`$ and

```math
u^{n+1}=S_\tau u^n+F_\tau(u^n)+H_\tau(u^n),
```

where

```math
F_\tau(f)=\tfrac16P[(S_\tau D^{-1}f)^2]-\tfrac16S_\tau P[(D^{-1}f)^2],
```

and

```math
\begin{aligned}
H_\tau(f)={}&\tfrac13P[(S_\tau D^{-1}f)D^{-1}F_\tau(f)]
+\tfrac\tau9(S_\tau D^{-1}f)P_0(f^2)\\
&-\tfrac1{54}\left[S_{\tau-s}D^{-1}[(S_sD^{-1}f)^3]\right]_{s=0}^{s=\tau}\\
&-\tfrac1{27\tau}\left[S_{\tau-s}D^{-2}[(S_{s-\tau}D^{-2}F_\tau(f))(S_sD^{-1}f)]\right]_{s=0}^{s=\tau}.
\end{aligned}
```

The brackets denote the value at $`s=\tau`$ minus the value at $`s=0`$. This is the time discretization in equation (1.4) of reference [1], without a spatial frequency cutoff.

For every $`T>0`$ and $`0<\gamma\le1`$, can the bound be sharpened to

```math
\max_{0\le n\le L}\|u(n\tau)-u^n\|_{L^2(\mathbb T)}\le C\tau^\gamma,
```

with $`C`$ and the admissible upper bound $`\tau_0>0`$ depending only on $`T`$, $`\gamma`$ and $`\|u_0\|_{H^\gamma}`$, for all $`\tau=T/L\le\tau_0`$? Prove this estimate or refute it for this particular scheme. No additional smoothness of $`u_0`$ is allowed.

## Application

KdV describes nonlinear dispersive waves, including long shallow-water waves. Rough measured or random initial data can reduce the accuracy of time-stepping methods. Removing the logarithmic loss would give a sharper relation between timestep and guaranteed error without requiring a frequency filter or smoother data.

## References

1. B. Li and Y. Wu, [An Unfiltered Low-Regularity Integrator for the KdV Equation with Solutions Below H1](https://doi.org/10.1007/s10208-025-09702-0), Foundations of Computational Mathematics **26**, 1321–1380 (2026), equation (1.4), Theorem 1.1 and §11, p.1378. [Author manuscript](https://www.polyu.edu.hk/ama/profile/byli/FoCM-3.pdf); [earlier preprint](https://arxiv.org/abs/2206.09320).
2. J. Cao, B. Li, Y. Wu and F. Yao, [Computing rough solutions of the KdV equation below L2](https://arxiv.org/abs/2506.21969v1), 2025, equation (2.1) and Theorem 2.1.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/kaiwen-jin-518/paper/main.pdf) establishes the full original target. Affirmative: logarithm-free unfiltered Li-Wu L2 convergence for every0<gamma<=1, uniformly on bounded Hgamma balls.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/518-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #37](https://github.com/MColbrook/AIM/pull/37) at `24ab3fa10db1f33a143f32876c6ae5b023782933`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
