# Correspondence with AIM 556

Original statement:
[Does integration of uniformly derivative-bounded analytic functions suffer the dimensional curse?](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/556-smooth-integration-dimensional-curse.md)

Target revision: `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted argument: *An exponential lower bound for integration under
uniform derivative bounds*, Kaiwen Jin, October 13, 2026.

| Original requirement | Manuscript location | Scope |
|---|---|---|
| Dimension d >= 1; domain [0,1]^d; Lebesgue integral | Section 1, equation (1); Theorem 1 | Identical domain and normalization, every dimension |
| Every mixed/repeated partial derivative has supremum at most one, including order zero | Equation (1); Lemma 1 and its product-rule estimate | Exact all-order bound one; no finite truncation |
| Exact function-evaluation information | Lemma 2 | The fooling function vanishes exactly at every prescribed sample site |
| Adaptive sampling and stopping; nonlinear reconstruction | Final proof of Theorem 1 | The zero-input path and the signed pair f,-f give identical data and output |
| No restriction to positive quadrature weights | Theorem 1 and its final proof | No weights are used in the lower-bound argument |
| Fixed absolute error epsilon_0 in (0,1) | Theorem 1, equations (2)--(3) | Any epsilon in (0,1); the moment matrix has trace one |
| Constants c>0 and rho>1 independent of dimension | Paragraph after Theorem 1 | epsilon_0=c=1/2 and rho=(1/2+sin(1/2))^(-1)>1 |
| Exponential lower bound for infinitely many d | Theorem 1, equation (3) | Stronger: for every d>=1 |

The proof is self-contained apart from elementary calculus and finite
linear algebra. The research references provide background and methodological
credit. The all-order derivative inclusion and the moment normalization
needed for this particular class are proved explicitly in Lemmas 1 and 2.
No positive-weight, finite-summability, periodic-function, or
dimension-independent-complexity assertion is substituted for the target.

This is a complete analytic solution claim submitted for independent
mathematical review. It is not a catalogue acceptance or a formal
verification claim.
