# 555. Maximal gain from randomization with nonadaptive linear measurements

**Area:** Information-based complexity and randomized approximation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`S:X\to Y`$ be a bounded linear operator between real Banach spaces. Inputs lie in the closed unit ball $`B_X`$. A deterministic nonadaptive algorithm has the form

```math
A(x)=\Phi(\lambda_1(x),\ldots,\lambda_n(x)),
```

where $`\lambda_j\in X'`$ are fixed continuous linear functionals and $`\Phi:\mathbb R^n\to Y`$ is unrestricted. Define

```math
e_n^{\rm det}(S)=\inf_A\sup_{x\in B_X}\|Sx-A(x)\|_Y.
```

A randomized nonadaptive algorithm chooses such a complete measurement list and reconstruction using a random seed $`\omega`$ independently of the input. Require the error to be jointly measurable, and set

```math
e_n^{\rm ran}(S)=\inf_{(A_\omega)}\sup_{x\in B_X}\mathbb E_\omega\|Sx-A_\omega(x)\|_Y.
```

Every realization uses at most $`n`$ measurements. The error criterion is expected norm, not root-mean-square norm.

For a nonnegative sequence $`u=(u_n)`$ define

```math
\mathop{\mathrm{rate}}\nolimits(u)=\sup\{\alpha\ge0:u_n=O(n^{-\alpha})\}.
```

Determine the maximal increase

```math
G=\sup_S\left[\mathop{\mathrm{rate}}\nolimits(e_n^{\rm ran}(S))-\mathop{\mathrm{rate}}\nolimits(e_n^{\rm det}(S))\right],
```

where the supremum is over bounded operators between real Banach spaces with finite rates. Current results give $`1/2\le G\le1`$. In particular, can nonadaptive randomization improve the polynomial rate by strictly more than $`1/2`$?

## Application

The answer quantifies the strongest possible information savings from randomly choosing a fixed batch of linear measurements. This distinguishes benefits of random sensing from benefits that require feedback and adaptive measurement selection.

## References

1. D. Krieg and M. Ullrich, [Approximation of functions: Optimal sampling and complexity](https://doi.org/10.1017/S0962492925100287), *Acta Numerica* **35** (2026), 273–457. Section 9.1 defines the error model; Section 10.2, equation (10.10), states the gap.
2. D. Krieg, E. Novak and M. Ullrich, [On the power of adaption and randomization](https://doi.org/10.1017/fms.2025.10101), *Forum of Mathematics, Sigma* **13** (2025), e152. Section 6.1.
3. R. J. Kunsch and M. Wnuk, [Adaptive and non-adaptive randomized approximation of high-dimensional vectors](https://arxiv.org/abs/2410.23067), *Journal of Approximation Theory* (2026), 106318. [DOI](https://doi.org/10.1016/j.jat.2026.106318).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/555-nonadaptive-randomization-gain/paper/main.pdf) establishes the full original target. Affirmative: maximal finite-rate gain from nonadaptive randomization is one.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/555-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #46](https://github.com/MColbrook/AIM/pull/46) at `4f2a858c30c12c9e096ebaa7688c20e44d125721`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
