# 431. Analytic boundary diffusion on continuous functions for Lipschitz domains

**Area:** Elliptic PDEs and analytic semigroups

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13
## Problem statement

For a bounded connected Lipschitz domain $`\Omega\subset\mathbb R^d`$, $`d\ge2`$, let $`C`$ be real symmetric uniformly positive definite with Lipschitz entries on $`\overline\Omega`$. Let $`N`$ be the weak Dirichlet-to-Neumann operator for $`-\mathop{\mathrm{div}}\nolimits(C\nabla)`$, defined by harmonic extension and conormal differentiation. Its semigroup restricts to a strongly continuous semigroup $`T(t)`$ on $`C(\partial\Omega)`$ with the supremum norm.
Must there exist $`\theta>0`$ such that $`T`$ extends to an operator-valued holomorphic semigroup on $`\{z\ne0:|\arg z|<\theta\}`$, with $`\sup_{0<|z|\le1,\ |\arg z|\le\theta'}\|T(z)\|<\infty`$ for each $`0<\theta'<\theta`$?

## Application

Analyticity supplies time regularization for boundary evolution driven by flux from a conducting bulk. It matters when boundary data are continuous and the geometry includes corners.

## References

1. A. F. M. ter Elst and E. M. Ouhabaz, [Five Open Problems on the Dirichlet-to-Neumann Operator with Variable Coefficients](https://doi.org/10.1007/s00020-025-02796-9), *Integral Equations and Operator Theory* **97** (2025), article 14, final paragraph of problem 4.
2. W. Arendt and A. F. M. ter Elst, [The Dirichlet-to-Neumann operator on C(partial Omega)](https://arxiv.org/abs/1707.05556), *Annali della Scuola Normale Superiore di Pisa* **20** (2020), 1169–1196, main semigroup theorem.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/431-dtn-analyticity-continuous-boundary/paper/dtn_analyticity.pdf) establishes the full original target. Continuous-boundary Dirichlet-to-Neumann holomorphy for the full symmetric Lipschitz class, with angle pi/2.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/431-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #64](https://github.com/MColbrook/AIM/pull/64) at `e601b95efa8c1c3a570734191d65b18d9ddd4438`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
