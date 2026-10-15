# 367. A universal quantitative error bound for small-BV hyperbolic flows

**Area:** Hyperbolic conservation laws; reliable simulation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`f\in C^4(U;\mathbb R^N)`$ be strictly hyperbolic near $`0\in U`$, with every characteristic field genuinely nonlinear, and a uniformly strictly convex entropy pair $`(\eta,q)`$ satisfying $`Dq=D\eta Df`$. Write $`S_tu_0`$ for its standard small-total-variation entropy solution of $`u_t+f(u)_x=0`$ on $`\mathbb R`$. Fix $`T,R,M>0`$ and sufficiently small $`\delta>0`$.
For $`0<\varepsilon<e^{-1}`$ consider every approximate flow $`u:[0,T]\to L^1(\mathbb R;U)`$ supported in $`[-R,R]`$ with $`\sup_t\mathop{\mathrm{TV}}\nolimits u(t)\le\delta`$, $`\|u(0)-u_0\|_1\le\varepsilon`$ and $`\|u(t)-u(s)\|_1\le M|t-s|+\varepsilon`$. For a scalar test function $`\phi\in C_c^1(\mathbb R^2)`$ define

```math
\mathcal R_{g,h}(s,t;\phi)=\int g(u(s,x))\phi(s,x)\,dx-\int g(u(t,x))\phi(t,x)\,dx+\int_s^t\!\int[g(u)\phi_t+h(u)\phi_x]\,dx\,dr.
```

Assume, for all $`0\le s<t\le T`$,

```math
|\mathcal R_{\mathrm{id},f}|\le\varepsilon(t-s+\varepsilon)\|\phi\|_{W^{1,\infty}},\qquad\mathcal R_{\eta,q}\ge-\varepsilon(t-s+\varepsilon)\|\phi\|_{W^{1,\infty}}\quad(\phi\ge0).
```

Is there $`C=C(f,\eta,U,\delta,T,R,M)`$ such that every such approximation satisfies

```math
\sup_{0\le t\le T}\|u(t)-S_tu_0\|_1\le C\sqrt\varepsilon\,|\log\varepsilon|?
```

## Application

A universal bound would certify computed shock flows using measured conservation residuals, entropy residuals and total variation, without tying the certificate to one particular numerical scheme.

## References

1. A. Bressan, [*One Dimensional Hyperbolic Conservation Laws: Past and Future*](https://arxiv.org/abs/2310.16707), Journal of Hyperbolic Differential Equations 21 (2024), 523–561, §7, Definition 7.1, Corollary 7.1 and Open Problem 3.
2. A. Bressan and G. Guerra, [*Unique Solutions to Hyperbolic Conservation Laws with a Strictly Convex Entropy*](https://arxiv.org/abs/2305.10737), Journal of Differential Equations (2024), uniqueness theorem and qualitative approximate-solution convergence.
3. A. Bressan, F. Huang, Y. Wang and T. Yang, [*On the Convergence Rate of Vanishing Viscosity Approximations for Nonlinear Hyperbolic Systems*](https://doi.org/10.1137/120869249), SIAM Journal on Mathematical Analysis 44 (2012), 3537–3563, main convergence-rate theorem.

## Status review

Reviewed 15 October 2026 against the original target in [PR #133](https://github.com/MColbrook/AIM/pull/133). Counterexample to the proposed universal square-root logarithmic error bound, with one fixed compactly supported small-BV initial datum.

[Proof or source](../research/solutions/367-hyperbolic-error-counterexample/paper/paper.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/367-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Counterexample satisfies every stated strict-hyperbolicity, genuine-nonlinearity, convex-entropy, residual, support, variation and time-modulus hypothesis; the normalized error diverges.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Checked on 22 September 2026 using Bressan's universal convergence-rate problem, approximate entropy solutions and the square-root logarithmic rate. Compactness and uniqueness give some modulus tending to zero, without the displayed rate. The SIAM theorem concerns actual viscous approximations, which are a smaller class. The 2026 Glimm–Lax uniqueness advance concerns regularization and uniqueness for rough exact solutions, not residual-based quantitative estimates. No proof of the displayed universal bound or a counterexample was located. In the residual definition the terminal test value is at time $`t`$, as required by the weak conservation law.
