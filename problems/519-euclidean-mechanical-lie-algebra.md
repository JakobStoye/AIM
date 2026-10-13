# 519. Universal identities for Euclidean mechanical Lie brackets

**Area:** Geometric numerical integration and numerical PDEs

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Over $`\mathbb R`$, let $`\mathfrak P`$ consist of Lie algebras $`L=\bigoplus_{n\ge0}L_n`$ satisfying

```math
[L_n,L_m]\subseteq L_{n+m-1}\quad(n+m>0),\qquad [L_0,L_0]=0.
```

Let $`F`$ be freely generated in this class by $`A`$ of degree two and $`B`$ of degree zero: every degree-preserving assignment of these generators extends uniquely to a homomorphism.

For $`d\ge1`$ and $`V\in C^\infty(\mathbb R^d;\mathbb R)`$, define

```math
\Phi_V:F\longrightarrow C^\infty_{\mathrm{pol}}(\mathbb R^{2d}),\qquad A\mapsto\tfrac12|p|^2,\quad B\mapsto V(q).
```

The target consists of smooth functions polynomial in $`p`$, with bracket

```math
\{f,g\}=\sum_{j=1}^d(\partial_{q_j}f\,\partial_{p_j}g-\partial_{p_j}f\,\partial_{q_j}g).
```

Prove or refute

```math
\bigcap_{d\ge1}\ \bigcap_{V\in C^\infty(\mathbb R^d;\mathbb R)}\ker\Phi_V=\{0\}.
```

The quantifier ranges over all dimensions and potentials; injectivity for each individual potential is not asserted.

## Application

The answer determines whether mechanical splitting integrators have additional universal order-condition reductions. It also bears on splitting the Laplacian and potential in Schrödinger evolution.

## References

1. R. I. McLachlan and A. Murua, [The Lie algebra of classical mechanics](https://doi.org/10.3934/jcd.2019017), Journal of Computational Dynamics **6**, 345–360 (2019), Definitions 1–4 and Conjecture 1. [Preprint](https://arxiv.org/abs/1905.07554).
2. S. Blanes, F. Casas and A. Murua, [Splitting methods for differential equations](https://doi.org/10.1017/S0962492923000077), Acta Numerica (2024), discussion of Runge–Kutta–Nyström order conditions.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/519-euclidean-mechanical-lie-algebra/paper/main.pdf) establishes the full original target. Affirmative: no additional universal Euclidean mechanical Lie identities, in every order.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/519-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #40](https://github.com/MColbrook/AIM/pull/40) at `8dc12e3f97d7c2230981ad0d46ab00aa06188bfd`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
