# 385. Observability of an acoustic shell at equal bulk and surface speeds

**Area:** PDE control / acoustic boundary dynamics

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\Omega=\{x\in\mathbb R^2:1<|x|<2\}`$, $`\Gamma_1=\{|x|=1\}`$ and $`\Gamma_0=\{|x|=2\}`$. Consider

```math
z_{tt}-\Delta z=0\quad\text{in }\Omega,\qquad z=0\quad\text{on }\Gamma_0,
```



```math
z_\Gamma=z|_{\Gamma_1},\qquad
z_{\Gamma,tt}-\Delta_\Gamma z_\Gamma+\partial_\nu z=0\quad\text{on }\Gamma_1.
```

Here $`\nu`$ is the outward normal of the annulus and $`\Delta_\Gamma`$ is the circle's Laplace operator. Define the conserved energy

```math
E(t)=\int_\Omega(|z_t|^2+|\nabla z|^2)\,dx+
\int_{\Gamma_1}(|z_{\Gamma,t}|^2+|\nabla_\Gamma z_\Gamma|^2)\,dS.
```

Does there exist a finite $`T_0`$ such that for every $`T>T_0`$ there is $`C_T<\infty`$ with

```math
E(0)\le C_T\int_0^T\int_{\Gamma_0}|\partial_\nu z|^2\,dS\,dt
```

for every smooth compatible solution? By density this is an energy-space observability question. This annular equal-speed case is a concrete instance of the open threshold problem.

## Application

The inequality asks whether measurements on the exterior determine all vibration energy when an elastic inner surface and the surrounding medium propagate disturbances at the same speed.

## References

1. L. Baudouin, J. Dardé, S. Ervedoza and A. Mercado, *A unified strategy for observability of waves in an annulus with various boundary conditions*, Mathematical Reports 24 (2022), 59–112, §2 and Theorem 2.4. [Journal PDF](https://imar.ro/journals/Mathematical_Reports/Pdfs/2022/1-2/5.pdf).
2. S. E. Chorfi, L. Maniar and R. Morales, *Controllability and Inverse Problems for Hyperbolic and Dispersive Equations with Dynamic Boundary Conditions*, preprint (2025), §3.1 and §5.1. [arXiv:2505.14795](https://arxiv.org/abs/2505.14795).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/385-equal-speed-wentzell-wave-observability/paper/equal_speed_observability.pdf) establishes the full original target. Full negative resolution of the exact target.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/385-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #53](https://github.com/MColbrook/AIM/pull/53) at `1b29cbe43828ce9b9fa1eeff602756fba40ff879`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
