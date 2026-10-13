# 556. Does integration of uniformly derivative-bounded analytic functions suffer the dimensional curse?

**Area:** Numerical integration and information-based complexity

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For each $`d\ge1`$, define

```math
F_d=\{f\in C^\infty([0,1]^d):\|D^\alpha f\|_\infty\le1\text{ for every }\alpha\in\mathbb N_0^d\},\qquad
I_d(f)=\int_{[0,1]^d}f(x)\,dx.
```

The derivative condition includes $`\alpha=0`$ and every mixed derivative, with the same bound one at all orders.

Let $`n(\varepsilon,d)`$ be the smallest number of exact function evaluations needed by a deterministic algorithm to approximate $`I_d(f)`$ with absolute error at most $`\varepsilon`$ for every $`f\in F_d`$. Sampling may be adaptive and reconstruction may be nonlinear; there is no restriction to positive quadrature weights.

Does this integration problem suffer from the curse of dimensionality? Specifically, do there exist $`\varepsilon_0\in(0,1)`$, $`c>0`$ and $`\rho>1`$ such that

```math
n(\varepsilon_0,d)\ge c\rho^d
```

for infinitely many dimensions $`d`$?

## Application

This problem tests whether uniformly controlling derivatives of every order is enough to prevent exponential sampling cost for high-dimensional integration. It would clarify what analytic regularity alone can guarantee before extra structure or randomness is imposed.

## References

1. D. Krieg and M. Ullrich, [Approximation of functions: Optimal sampling and complexity](https://doi.org/10.1017/S0962492925100287), *Acta Numerica* **35** (2026), 273–457. Section 8.1, equation (8.5) and the discussion following Proposition 8.3.
2. E. Novak and F. Pillichshammer, [Intractability results for integration in tensor product spaces](https://arxiv.org/abs/2404.17163), arXiv:2404.17163. Section 5.2 compares related classes of infinitely smooth functions.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/556-uniform-derivative-integration/paper/uniform_derivative_integration.pdf) establishes the full original target. Affirmative: the dimensional curse holds, with exponential deterministic sampling complexity.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/556-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #83](https://github.com/MColbrook/AIM/pull/83) at `73683304bcf7d3e748eb1c3f4db614175c938170`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
