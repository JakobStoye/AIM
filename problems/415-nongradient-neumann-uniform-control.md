# 415. Uniform control of Neumann advection–diffusion for non-gradient flows

**Area:** PDE control / transport with weak diffusion

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, be a bounded connected smooth domain, $`\omega\Subset\Omega`$ nonempty open, and $`B\in W^{2,\infty}(\mathbb R^d;\mathbb R^d)`$. Assume $`B\cdot\nu\ge c_0>0`$ on $`\partial\Omega`$. Write $`X'(s)=-B(X(s))`$, $`X(0)=x`$. Assume that some $`T_0,r_0>0`$ satisfy: for each $`x\in\overline\Omega`$ there is $`s_x\in(0,T_0)`$ with $`X(s_x;B(x,r_0))\subset\omega`$.
For $`\varepsilon>0`$, consider

```math
y_t-\varepsilon\Delta y+B\cdot\nabla y=1_\omega h,\quad \partial_\nu y=0,\quad y(0)=y_0\in L^2(\Omega).
```

Must there exist $`T_*<\infty`$ such that, for every $`T>T_*`$, some $`C_T,\varepsilon_T>0`$ satisfy: every $`0<\varepsilon<\varepsilon_T`$ and every $`y_0`$ admit $`h\in L^2((0,T)\times\omega)`$ with $`y(T)=0`$ and

```math
\|h\|_2\le C_T\|y_0\|_2?
```

No scalar potential representation $`B=\nabla f`$ is imposed.

## Application

This asks whether a sensor-actuator region reached by all backward flow paths can uniformly control a weakly diffusive concentration in a bounded vessel. Rotational drift is allowed, which is important for realistic transport fields.

## References

1. F. Et-Tahri, J. A. Bárcena-Petisco, I. Boutaayamou and L. Maniar, *On uniform null controllability of transport-diffusion equations with vanishing viscosity limit*, Mathematical Methods in the Applied Sciences 48 (2025), 6531–6552, equation (1), Definition 1.3, Theorem 1.5 and Remark 1.6. [DOI](https://doi.org/10.1002/mma.10693); [full text](https://arxiv.org/html/2412.16660v1).
2. J. A. Bárcena-Petisco, *Cost of null controllability for parabolic equations with vanishing diffusivity and a transport term*, ESAIM: Control, Optimisation and Calculus of Variations 27 (2021), 106, introduction and main control-cost results. [DOI](https://doi.org/10.1051/cocv/2021103).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/415-nongradient-neumann-uniform-control/paper/main.pdf) establishes the full original target. Uniform Neumann null control for every strictly outward autonomous drift satisfying the original flushing condition.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/415-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #58](https://github.com/MColbrook/AIM/pull/58) at `060bceb02fd167080976f6bb780f4be9dc1b9910`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
