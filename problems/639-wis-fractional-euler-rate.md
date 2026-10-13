# 639. Strong convergence rate of the fractional WIS Euler integrator

**Area:** Numerical stochastic differential equations

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix $`T>0`$, $`H\in(0,1)`$, $`\alpha,\beta,x_0\in\mathbb R`$, and a globally Lipschitz function $`a:\mathbb R\to\mathbb R`$ of at most linear growth. Let $`B^H`$ be centered fractional Brownian motion with covariance

```math
\mathbb E[B^H(t)B^H(s)]=\tfrac12(t^{2H}+s^{2H}-|t-s|^{2H}).
```

Consider

```math
dX(t)=[\alpha X(t)+a(X(t))]dt+\beta X(t)\,dB^H(t),\qquad X(0)=x_0,
```

where the stochastic integral has the Wick–Itô–Skorohod interpretation of [1].

For $`n\ge1`$, set $`h=T/n`$, $`t_i=ih`$, and

```math
J_i=\exp\!\left(-\alpha t_i+\frac{\beta^2}{2}[T^{2H}-(T-t_i)^{2H}]-\beta B^H(t_i)\right),\qquad 0\le i\le n.
```

Using exact samples from the same fractional Brownian path as $`X`$, define

```math
Z_0=x_0,\qquad Z_{i+1}=Z_i+hJ_i a(Z_i/J_i),\qquad X_n=Z_n/J_n.
```

This is the terminal-time GfBm_EM scheme in [1, equations (3.12)–(3.13)]. Does every such fixed problem admit a finite constant $`C`$, independent of $`n`$, such that

```math
\bigl(\mathbb E|X(T)-X_n|^2\bigr)^{1/2}\le C h^{\min\{H+1/2,1\}}?
```

The question concerns the autonomous drift and the stated scheme; the constant may depend on all fixed problem data.

## Application

This determines the time-step accuracy attainable when simulating stochastic models with correlated multiplicative noise.

## References

1. U. Erdoğan, G. J. Lord and R. B. Schieven, [Numerical approximation of SDEs driven by fractional Brownian motion for all H ∈ (0,1) using WIS integration](https://doi.org/10.1093/imanum/drag055), *IMA Journal of Numerical Analysis* (2026). [arXiv:2404.07013v2](https://arxiv.org/abs/2404.07013v2), conjectured estimate (1.3), Assumption 3.1, equations (3.12)–(3.13), Theorem 3.6 and Section 6.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/639-wis-fractional-euler-rate/paper/main.pdf) proves the full displayed terminal error rate for every original fixed Lipschitz problem, using the unchanged recurrence and exact samples of the same noise path. It covers all Hurst values, including Brownian noise, zero initial values, zero crossings and degenerate coefficients.

**Independent review:** the [complete argument audit](../research/solution_reviews/2026-10-13-yui-prs/639-review.md) and [separate fresh stress test](../research/solution_reviews/2026-10-13-yui-prs/639-second-check.md) reconstruct the conditional quadrature, Brownian localization, terminal stability and primary-source interface. Both are independent Codex AI audits during maintainer processing; neither asserts human peer review or Lean verification.

The reviewed submission is [PR89](https://github.com/MColbrook/AIM/pull/89) at `7c5a97db1d7f13732cdfe8900e14a9e52ab6d64b`, compared with the unchanged original target at `c9929805cece044705abaaebe1cebddac1ba11a6`. Its source, PDF, references, ancillary documents and original hashes were checked. The proof and documented independent reviews meet the repository's **Solved** criterion. No uniform-in-H, simulated-noise or supremum-in-time rate is asserted.
