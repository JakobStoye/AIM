# 507. Sharp interactive privacy rates for spectral density estimation

**Area:** Statistical inference, time series and local differential privacy

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix $`s>1/2`$, $`C_0>1`$ and $`C_1>0`$. For an even, nonnegative, $`2\pi`$-periodic spectral density $`f`$, write

```math
\gamma_f(h)=\int_{-\pi}^{\pi}f(\lambda)e^{ih\lambda}\,d\lambda,
\qquad \rho_f(h)=\gamma_f(h)/\gamma_f(0).
```

Consider the class

```math
\mathcal F(C_0,C_1,s)=\left\{f:\ C_0^{-1}\le\gamma_f(0)\le C_0,
\quad\sum_{h\in\mathbb Z\setminus\{0\}}|h|^{2s}|\rho_f(h)|^2\le C_1^2\right\}.
```

The data $`X_1,\ldots,X_n`$ are consecutive observations of a centered, real stationary Gaussian process with spectral density $`f\in\mathcal F(C_0,C_1,s)`$.

A sequentially interactive mechanism releases $`Z_i`$ through a Markov kernel $`Q_i(\cdot\mid X_i,Z_{<i})`$ into a standard Borel space. Require, for every measurable output set $`B`$, every history $`z_{<i}`$ and all $`x,x'\in\mathbb R`$,

```math
Q_i(B\mid x,z_{<i})\le e^\alpha Q_i(B\mid x',z_{<i}).
```

Let $`\mathcal Q^{\mathrm{seq}}_{n,\alpha}`$ be the class of these mechanisms. Each release can use its own raw observation and earlier releases; it has no access to earlier raw observations.

Determine the joint dependence on $`n`$ and $`\alpha`$ of

```math
\mathcal R^{\mathrm{seq}}_{n,\alpha}
=\inf_{Q\in\mathcal Q^{\mathrm{seq}}_{n,\alpha}}\inf_{\widehat f}
\sup_{f\in\mathcal F(C_0,C_1,s)}
\mathbb E_{f,Q}\!\left[\int_{-\pi}^{\pi}|\widehat f(Z_{1:n})(\lambda)-f(\lambda)|^2\,d\lambda\right],
```

uniformly for $`n\ge2`$ and $`0<\alpha\le1`$. Here $`\widehat f`$ ranges over measurable $`L^2([-\pi,\pi])`$-valued estimators. The fixed class parameters are known to the mechanism and estimator. Seek matching bounds up to constants depending only on $`C_0,C_1,s`$, including any necessary logarithmic factors and the regime in which consistent estimation is impossible.

## Application

Spectral densities describe temporal dependence in correlated measurements. Sharp interactive rates would quantify how much accuracy can be recovered when each data holder may consult earlier privatized releases before transmitting a private measurement.

## References

1. C. Butucea, K. Klockmann and T. Krivobokova, [Nonparametric Spectral Density Estimation using Interactive Mechanisms under Local Differential Privacy](https://www.jmlr.org/papers/v27/25-0680.html), Journal of Machine Learning Research **27**(168) (2026), 1–49. The open question on p.5, the sequential privacy definition in §2, and global estimation in §2.4. [arXiv:2504.00919v3](https://arxiv.org/abs/2504.00919v3).
2. Y. Issartel and F. Roueff, [On the privacy cost for dependent Gaussian data: spectral density estimation under local differential privacy](https://arxiv.org/abs/2608.24847), arXiv:2608.24847v1 (25 August 2026). Equation (3), Theorems 1 and 3, and §3.4, “Interactive privacy.”

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/507-sequential-private-spectral-density/paper/main.pdf) establishes the full original target. Matching sequentially private Gaussian spectral-density minimax rate and consistency boundary.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/507-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #74](https://github.com/MColbrook/AIM/pull/74) at `1986a0aaa93ef42709e196bfa9c4746fab250351`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
