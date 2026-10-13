# 386. Boundary observation of a Schrödinger field with slower surface dispersion

**Area:** PDE control / dispersive boundary dynamics

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

On $`\Omega=\{x\in\mathbb R^2:1<|x|<2\}`$ let $`\Gamma_1`$ and $`\Gamma_0`$ be the inner and outer circles. Consider

```math
iz_t+\Delta z=0\quad\text{in }\Omega,\qquad z=0\quad\text{on }\Gamma_0,
```



```math
z_\Gamma=z|_{\Gamma_1},\qquad
iz_{\Gamma,t}+\tfrac12\Delta_\Gamma z_\Gamma-\partial_\nu z=0\quad\text{on }\Gamma_1.
```

With $`\nu`$ outward from $`\Omega`$, set

```math
\|Z\|_{\mathcal E}^2=\int_\Omega|\nabla z|^2\,dx+
\tfrac12\int_{\Gamma_1}|\nabla_\Gamma z_\Gamma|^2\,dS.
```

Is it true that for every $`T>0`$ a constant $`C_T`$ satisfies

```math
\|Z(0)\|_{\mathcal E}^2\le C_T\int_0^T\int_{\Gamma_0}|\partial_\nu z|^2\,dS\,dt
```

for every smooth compatible solution? The fixed coefficient $`1/2`$ selects a concrete case of the unresolved regime in which surface dispersion is weaker than bulk dispersion.

## Application

Dynamic boundary conditions represent surface degrees of freedom coupled to a quantum or dispersive bulk field. The estimate would permit exact control using only the exterior boundary.

## References

1. A. Mercado and R. Morales, *Exact Controllability for a Schrödinger Equation with Dynamic Boundary Conditions*, SIAM Journal on Control and Optimization 61 (2023), 3501–3525, main observability and controllability theorems. [DOI](https://doi.org/10.1137/21M1439407); [author preprint](https://arxiv.org/abs/2301.02573).
2. S. E. Chorfi, L. Maniar and R. Morales, *Controllability and Inverse Problems for Hyperbolic and Dispersive Equations with Dynamic Boundary Conditions*, preprint (2025), equations (4.1)–(4.4) and §5.1. [arXiv:2505.14795](https://arxiv.org/abs/2505.14795).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/386-slow-surface-schrodinger-observability/paper/exterior_observability.pdf) establishes the full original target. Full negative resolution of the exact target.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/386-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #54](https://github.com/MColbrook/AIM/pull/54) at `6b03556d5c8ba561a30fb600d7bc0348074361dc`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
