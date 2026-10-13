# 576. Uniform covariance bounds for constrained Ising replicas

**Area:** Probability, statistical mechanics and sampling

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix $`n\geq1`$, a real symmetric interaction matrix $`J\in\mathbb R^{n\times n}`$, and a partition $`\mathcal A`$ of $`[n]`$. For $`N\geq2`$, write a spin configuration as $`\sigma=(\sigma(1),\ldots,\sigma(N))\in(\{-1,1\}^n)^N`$. Choose integers $`M_A`$, one for each $`A\in\mathcal A`$, such that

```math
\Omega_{N,M}=\left\{\sigma:\sum_{i=1}^N\sum_{j\in A}\sigma_j(i)=M_A\text{ for every }A\in\mathcal A\right\}
```

is nonempty. For an arbitrary external field $`v\in\mathbb R^{Nn}`$, define the probability measure

```math
\nu_{N,M,v}(\sigma)=\frac{\mathbf1_{\Omega_{N,M}}(\sigma)}{Z_{N,M,v}}
\exp\left\{\frac12\sum_{i=1}^N\sigma(i)^TJ\sigma(i)+\sum_{i=1}^N\sum_{j=1}^n v_{ij}\sigma_j(i)\right\}.
```

Does there exist a finite constant $`C(J,\mathcal A)`$ such that

```math
\bigl\|\mathop{\mathrm{Cov}}\nolimits_{\nu_{N,M,v}}(\sigma)\bigr\|_{\mathrm{op}}\leq C(J,\mathcal A)
```

for every $`N`$, every feasible $`M`$, and every $`v`$? The covariance is that of all $`Nn`$ spins, with the ordinary Euclidean operator norm. The constant may grow with the fixed interaction and dimension, but must be independent of the replica count, conserved magnetizations and external fields. Since there are finitely many partitions for fixed $`n`$, allowing dependence on $`\mathcal A`$ is equivalent to taking a maximum over partitions.

This is the tilted canonical-Ising covariance conjecture in [1, Section 4.5], with the constrained state space and measure expanded from equations (1.23)–(1.24).

## Application

The estimate would control fluctuations in particle systems that exchange spins while preserving specified magnetizations. The authors identify it as a route to entropy decay estimates uniform in the number of replicas, and consequently to quantitative convergence of nonlinear spin-exchange sampling at arbitrary interaction strengths.

## References

1. P. Caputo and M. Morellini, [Kac's Program and Relative Entropy Decay for Nonlinear Spin-Exchange Dynamics](https://arxiv.org/html/2511.05223v1), arXiv:2511.05223 (2025). Section 4.5; equations (1.23)–(1.24); Sections 3.3–3.4.
2. P. Caputo and A. Sinclair, [Entropy production in nonlinear recombination models](https://doi.org/10.3150/17-BEJ959), *Bernoulli* **24**(4B) (2018), 3246–3282. This journal article introduced the related reversible quadratic-system framework; the present conjecture is explicitly formulated in its later follow-up [1].

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/576-ising-replica-covariance/paper/ising_replica_covariance.pdf) establishes the full original target. Uniform covariance bound for all fixed real symmetric interactions, partitions, feasible magnetizations and replica-dependent fields.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/576-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #78](https://github.com/MColbrook/AIM/pull/78) at `9f7637ced9f656199f8ce36eba7feb7d857c764a`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
