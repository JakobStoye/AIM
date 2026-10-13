# 506. Minimax rates for private density estimation with mixed anisotropy

**Area:** Statistical inference and local differential privacy

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix $`d\ge2`$, $`R^2>d`$, $`A>0`$, and vectors $`\boldsymbol\beta,\boldsymbol\delta\in\mathbb N_{>0}^d`$ such that $`\beta_m/\delta_m`$ is independent of $`m`$. Assume that some $`\delta_m<d`$ and some $`\delta_k>d`$.

Use the real Fourier basis $`\phi_1(t)=1`$, $`\phi_{2j}(t)=\sqrt2\cos(2\pi jt)`$ and $`\phi_{2j+1}(t)=\sqrt2\sin(2\pi jt)`$ for $`j\ge1`$, and its tensor products $`\phi_{\mathbf j}(x)=\prod_m\phi_{j_m}(x_m)`$. Write $`\theta_{\mathbf j}(h)=\int_{[0,1]^d}h\phi_{\mathbf j}`$ and define

```math
W^{\mathbf s}(r)=\left\{h\in L^2([0,1]^d):
\sum_{\mathbf j\in\mathbb N_{>0}^d}\left(\sum_{m=1}^d j_m^{2s_m}\right)|\theta_{\mathbf j}(h)|^2\le r^2\right\}.
```

Let $`\mathcal F_{\boldsymbol\beta,R}`$ be the probability densities in $`W^{\boldsymbol\beta}(R)`$, and set

```math
d_{\boldsymbol\delta}(h,f)=\sup_{g\in W^{\boldsymbol\delta}(1)}\left|\int_{[0,1]^d}(h-f)g\right|.
```

Given $`n`$ independent observations with density $`f`$, a sequentially interactive $`\alpha`$-locally private mechanism releases $`Z_i`$ through a channel $`Q_i(\cdot\mid X_i,Z_1,\ldots,Z_{i-1})`$ satisfying

```math
Q_i(B\mid x,z_{<i})\le e^\alpha Q_i(B\mid x',z_{<i})
```

for every measurable $`B`$, all $`x,x'`$ and all histories $`z_{<i}`$. Denote the class of these mechanisms by $`\mathcal Q_\alpha`$.

Determine, up to multiplicative constants independent of $`n`$ and $`\alpha`$, the minimax risk

```math
\mathcal R_{n,\alpha}(\boldsymbol\beta,\boldsymbol\delta)
=\inf_{Q\in\mathcal Q_\alpha}\inf_{\widehat f}
\sup_{f\in\mathcal F_{\boldsymbol\beta,R}}
\mathbb E_{f,Q}\,d_{\boldsymbol\delta}(\widehat f,f),
```

for $`0<\alpha\le A`$ and $`n\alpha^2\ge1`$. Estimators are measurable $`L^2`$-valued functions of the released data. The parameters $`d,R,\boldsymbol\beta,\boldsymbol\delta`$ are known and fixed. Matching lower and upper bounds must include any necessary logarithmic factors.

## Application

Different coordinates of a multivariate density can have different smoothness. Sharp rates would quantify the information lost when individuals privatize their observations before sharing them, under a loss that measures the accuracy of generated distributions through smooth test functions.

## References

1. M. Albert, J. Chevallier, B. Laurent and O. Sacko, [Minimax density estimation in the adversarial framework under local differential privacy](https://www.jmlr.org/papers/v27/24-0494.html), Journal of Machine Learning Research **27**(69) (2026), 1–43. Equations (1), (3)–(5), and §3, Theorems 10–11 and the explicit open question on p.15. [Published PDF](https://www.jmlr.org/papers/volume27/24-0494/24-0494.pdf); [arXiv record](https://arxiv.org/abs/2403.18357).

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/yuiyuiui-506-private-density-mixed-anisotropy/paper/mixed_private_density.pdf) establishes the full original target. Matching mixed-anisotropy full-history private density minimax rates, including the critical unsquared logarithmic rate.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/506-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #72](https://github.com/MColbrook/AIM/pull/72) at `6a5fae3b6a465b6afa0dd01544993e8c90ef0070`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
