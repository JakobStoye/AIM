# 398. Boundary control to equilibrium for a parabolic obstacle problem

**Area:** PDE control / variational inequalities

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`I=(0,1)`$ and $`\psi\in C^\infty([0,1])`$ satisfy $`\psi(0),\psi(1)<0`$ and $`\max\psi>0`$. Let $`\bar y\in H^1_0(I)`$ be the unique minimizer of $`\int_I|y_x|^2`$ subject to $`y\ge\psi`$. For every $`y_0\in H^1_0(I)`$ with $`y_0\ge\psi`$, do there exist a finite $`T>0`$ and endpoint controls $`g_0,g_1\in H^1(0,T)`$, with $`g_i(0)=g_i(T)=0`$ and $`g_i(t)\ge\psi(i)`$, such that the variational solution of

```math
\min\{y_t-y_{xx},y-\psi\}=0,\qquad y(t,i)=g_i(t),\qquad y(0)=y_0,
```

satisfies $`y(T)=\bar y`$ in $`L^2(I)`$? The minimum equation means $`y\ge\psi`$, $`y_t-y_{xx}\ge0`$ and $`(y-\psi)(y_t-y_{xx})=0`$, interpreted by the associated parabolic variational inequality.

## Application

Obstacle evolution models contact constraints and American-option exercise regions. Exact boundary steering requires simultaneous control of the field and the unknown contact region.

## References

1. B. Geshkovski, *Control in moving interfaces and deep learning*, doctoral thesis, Universidad Autónoma de Madrid (2021), §1.5.1, pp. 37–39, equations (1.5.1)–(1.5.3). [Thesis](https://repositorio.uam.es/bitstream/10486/696540/1/geshkovski_borjan.pdf).
2. D. Pighin and E. Zuazua, *Controllability under positivity constraints of semilinear heat equations*, Mathematical Control and Related Fields 8 (2018), 935–964, §7, discussion of controllability of the obstacle problem. [DOI](https://doi.org/10.3934/mcrf.2018041); [arXiv:1711.07678](https://arxiv.org/abs/1711.07678).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/398-parabolic-obstacle-counterexample/paper/obstacle_control_counterexample.pdf) establishes the full original target. Full negative resolution of the exact target.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/398-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #56](https://github.com/MColbrook/AIM/pull/56) at `a44c2c3ff89538a75e814dda1b958bd8c688485f`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
