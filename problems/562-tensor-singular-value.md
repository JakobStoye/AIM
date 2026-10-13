# 562. Sharp least-singular-value bounds for independent random tensor columns

**Area:** Random matrices and tensor methods

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix $`K>0`$. For each $`n`$, let $`d=d(n)\ge1`$ satisfy $`d=o(\sqrt{n/\log n})`$, and fix $`\varepsilon\in(0,1/2]`$. Put $`N=n^d`$ and $`m=\lfloor(1-\varepsilon)N\rfloor`$. Let $`x_{ik}\in\mathbb R^n`$, $`1\le i\le m`$, $`1\le k\le d`$, have mutually independent coordinates, all with mean zero, variance one and subgaussian norm at most $`K`$. Here $`\|\xi\|_{\psi_2}=\inf\{s>0:\mathbb E\exp(\xi^2/s^2)\le2\}`$.

Form the $`N\times m`$ matrix $`A`$ whose $`i`$th column is $`x_{i1}\otimes\cdots\otimes x_{id}`$. Does there exist $`c_K>0`$, independent of $`n,d,\varepsilon`$, such that

```math
\mathbb P\{s_{\min}(A)\ge c_K\varepsilon n^{d/2}\}\longrightarrow1
```

for every such sequence of dimensions and coordinate distributions? The probability convergence is for each fixed $`\varepsilon`$, while the lower-bound constant is uniform in $`\varepsilon`$.

This asks for the natural ambient-dimension scale in the improvement proposed in [1, Section 1.5]. The order $`d`$ may grow; bounds whose constants deteriorate exponentially with $`d`$ do not settle the question.

## Application

The columns model independent rank-one tensor features. A quantitative lower bound controls noise amplification in linear recovery of their coefficients, with applications to tensor decomposition and latent-variable learning.

## References

1. R. Vershynin, [Concentration inequalities for random tensors](https://doi.org/10.3150/20-BEJ1218), *Bernoulli* **26**(4) (2020), 3139–3162. Sections 1.3 and 1.5, Corollary 6.2; [updated author manuscript](https://arxiv.org/html/1905.00802v5).
2. X. Hu and G. Paouris, [Small ball probabilities for simple random tensors](https://doi.org/10.1016/j.jfa.2025.111309), *Journal of Functional Analysis* **290**(6) (2026), 111309. [Author preprint](https://arxiv.org/abs/2403.20192).
3. K. Luh, [Linear Independence of Random Boolean Tensor Powers at the Dimension Threshold](https://arxiv.org/abs/2609.23858), September 2026.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/kaiwen-jin-562-tensor-singular-values/paper/main.pdf) establishes the full original target. Sharp ambient-scale smallest singular-value lower bound with a K-only constant throughout the stated growing-order regime.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/562-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #76](https://github.com/MColbrook/AIM/pull/76) at `a1cb3d593a70a09257d8df249433ba5dc14da1e6`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
