# Correspondence with AIM problem 507

Original target: [Sharp interactive privacy rates for spectral density estimation](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/507-interactive-private-spectral-density.md), repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`. Manuscript: *Sharp minimax rates for spectral density estimation under sequential local differential privacy*, Kaiwen Jin, 13 October 2026.

This comparison uses the original public problem and the submitted manuscript. Theorem 1 claims the full target; the argument and citation uses remain subject to independent review.

| Original requirement | Corresponding manuscript location |
| --- | --- |
| Fixed known $`s>1/2,C_0>1,C_1>0`$ | Section 1, opening model paragraph and Theorem 1; mechanisms and estimators may use the parameters. |
| Even, nonnegative, $`2\pi`$-periodic spectral density | Section 1, definitions preceding (1)–(2). |
| $`\gamma_f(h)=\int_{-\pi}^{\pi} f(\lambda)e^{ih\lambda}\,d\lambda`$, $`\rho_f(h)=\gamma_f(h)/\gamma_f(0)`$ | Equation (1), with no change of Fourier normalization. |
| Variance in $`[C_0^{-1},C_0]`$ | Class (2); the lower-bound alternatives have variance one, which lies in this interval. |
| $`\sum_{h\ne0}|h|^{2s}|\rho_f(h)|^2\le C_1^2`$ | Class (2); Section 4 verifies this bound, including both positive and negative lags. The cited upper bound applies to the same class. |
| Consecutive dependent observations of a centered real stationary Gaussian process | Section 1, observation model; Section 4 constructs legal stationary Gaussian alternatives. Independence of the observations is not assumed. |
| Kernels $`Q_i(\cdot\mid X_i,Z_{<i})`$ | Section 1, equation (3) and its preceding paragraph. |
| Each release uses only its own raw observation and earlier private outputs; no earlier raw observations | Section 1, specified access rule; Lemma 3 and Proposition 6 use it to protect an innovation in the entire output prefix. Theorem 7 preserves it under a fixed raw shift. |
| Arbitrary standard Borel output spaces | Section 1, spaces $`E_i`$; Lemmas 3–4 and Proposition 6 retain general kernels and use regular conditional laws on these spaces. |
| Pointwise $`\alpha`$-LDP for every history, raw-input pair and measurable event | Equation (3); Lemma 3 proves privacy of the full prefix and Proposition 6 applies the current kernel at a common history. |
| Infimum over every admissible sequential mechanism | Risk (4); Proposition 6 and Theorem 7 are uniform in the mechanism, and Section 4 takes the infimum after its lower bound. |
| Measurable $`L^2([-\pi,\pi])`$-valued estimators | Risk (4); Section 4 proves measurability of finite coefficient decisions and the loss comparison (19), including complex estimators and zero ties. |
| Integrated squared loss with Lebesgue measure | Section 1; equations (4)–(5) and orthogonal projection in (19). |
| Uniformly all $`n\ge2`$ and $`0<\alpha\le1`$ | Theorem 1; Proposition 6/Theorem 7 hold already for $`n\ge1`$. The packing choice (16) includes effective sample sizes at most one. |
| Constants depend only on $`C_0,C_1,s`$ | Theorem 1 and the final lower/upper estimates in Section 4. |
| Matching joint $`n,\alpha`$ dependence | Equation (5): $`1\wedge(n\alpha^4)^{-2s/(2s+1)}`$. The lower bound is newly proved for the sequential class; the upper bound is Issartel–Roueff Theorem 3. |
| Necessary logarithmic factors | No logarithmic factor is required: the proposed lower and upper bounds match without one. |
| Inconsistency regime and consistency boundary | Theorem 1 and the final paragraph of Section 4: risk tends to zero exactly when $`n\alpha^4\to\infty`$. Every bounded-effective-size subsequence has risk bounded away from zero. |
| Non-interactive lower bounds do not establish the sequential lower bound | The introduction states the restriction explicitly. Sections 2–3 prove the sequential divergence estimate; Section 4 applies it to the actual sequential output laws. |

The proof does not cover mechanisms with access to previous raw observations, non-Gaussian time series or a different loss/data class. Those settings lie outside the stated original target.

The sources used for the existing upper bound and comparison with interactive estimators are [Issartel–Roueff v1](https://arxiv.org/abs/2608.24847v1) and [Butucea–Klockmann–Krivobokova, JMLR 27(168)](https://www.jmlr.org/papers/v27/25-0680.html). Precise theorem, lemma and page locators are given in the manuscript. The proposed lower bound requires its new sequential argument; it is not a reassertion of the cited non-interactive theorem.
