# 559. Deciding nonnegativity of unnormalized univariate trace polynomials

**Area:** Real algebraic geometry and matrix inequalities

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Given a positive integer $`d`$ and a polynomial $`F\in\mathbb Q[z_1,\ldots,z_d]`$, determine whether there is an algorithm that always terminates and correctly decides the statement

```math
F\bigl(\mathop{\mathrm{tr}}\nolimits(A),\mathop{\mathrm{tr}}\nolimits(A^2),\ldots,\mathop{\mathrm{tr}}\nolimits(A^d)\bigr)\ge0
\quad\text{for every }n\ge1\text{ and every real symmetric }A\in\mathbb R^{n\times n}.
```

Here $`\mathop{\mathrm{tr}}\nolimits`$ is the ordinary, unnormalized matrix trace. The input polynomial is a finite rational expression; matrix dimension is universally quantified and is not bounded in the input.

This uses the pure trace convention of [1, Definition 6.1]: there is no additional free matrix factor. In its symmetric-function formulation, the positive power sums are the generators and the zeroth symbol is the constant 1.

Equivalently, decide whether

```math
F\left(\sum_{i=1}^n x_i,\sum_{i=1}^n x_i^2,\ldots,\sum_{i=1}^n x_i^d\right)\ge0
```

for every $`n\ge1`$ and every $`(x_1,\ldots,x_n)\in\mathbb R^n`$. Give a decision algorithm or prove that this decision problem is undecidable.

## Application

A decision procedure would certify matrix trace inequalities uniformly over all dimensions. An undecidability theorem would establish a fundamental limit on automated symbolic verification of such inequalities, even with just one matrix variable.

## References

1. J. Acevedo, G. Blekherman, S. Debus and C. Riener, [The wonderful geometry of the Vandermonde map](https://doi.org/10.1007/s10208-025-09718-6), *Foundations of Computational Mathematics* **26** (2026), 2005–2051. Definition 6.1, Theorems 6.2 and 6.5, and Section 7. [arXiv:2303.09512](https://arxiv.org/abs/2303.09512).
2. I. Klep, J. E. Pascoe and J. Volčič, [Positive univariate trace polynomials](https://arxiv.org/abs/2009.10081), arXiv:2009.10081.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/559-univariate-trace-decidability/paper/trace_decidability.pdf) establishes the full original target. Undecidability: universal positivity of univariate unnormalized trace polynomials admits no algorithmic decider.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/559-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #77](https://github.com/MColbrook/AIM/pull/77) at `8112a718b350324672c81c059624d5a561e20907`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
