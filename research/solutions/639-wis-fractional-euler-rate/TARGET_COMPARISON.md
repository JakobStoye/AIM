# Comparison with AIM 639

Target: [Strong convergence rate of the fractional WIS Euler integrator](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/639-wis-fractional-euler-rate.md), revision c9929805cece044705abaaebe1cebddac1ba11a6.

Manuscript: [complete PDF](paper/main.pdf), [source](paper/main.tex). Theorem 2.1 is the complete solution claim; its proof concludes on page 12. Page numbers refer to this submitted 12-page PDF.

| Target requirement | Manuscript location |
|---|---|
| Scalar WIS equation $`dX_t=(\alpha X_t+a(X_t))dt+\beta X_t\,dB_t^H`$, with the source paper's solution convention | Section 2, equation (1), page 2; terminal representation (3), from reference [1], Theorem 3.2 and equations (3.6)–(3.9). |
| Every fixed $`T>0`$, $`H\in(0,1)`$, real $`\alpha,\beta,x_0`$ | Section 2 opening data declaration, page 2; Theorem 2.1, page 3. |
| Autonomous globally Lipschitz $`a:\mathbb R\to\mathbb R`$ of at most linear growth | Same declaration and theorem; (7)–(13) use Lipschitz continuity without higher derivatives. |
| Standard centered fractional Brownian covariance $`\frac12(t^{2H}+s^{2H}-\lvert t-s\rvert^{2H})`$ | Section 2, page 2; (16) constructs a realization with exactly this law, page 4. |
| $`J_i=\exp(-\alpha t_i+\frac12\beta^2[T^{2H}-(T-t_i)^{2H}]-\beta B^H_{t_i})`$, $`h=T/n`$, $`t_i=ih`$ | Equation (2) and the grid declaration, page 2. |
| Fixed recurrence $`Z_0=x_0`$, $`Z_{i+1}=Z_i+hJ_i a(Z_i/J_i)`$, $`X_n=Z_n/J_n`$ | Equations (3)–(4), page 2: $`F(c(t_i),B^H_{t_i},z)=J_i a(z/J_i)`$. No scheme change is introduced. |
| Exact samples from the same noise path | Section 2 immediately after (4), page 3; exact and approximate terminal quotients use the same $`J_T`$. |
| Root mean-square terminal error at most $`Ch^{\min\{H+1/2,1\}}`$, with $`C`$ independent of $`n`$ | Theorem 2.1, equation (6), page 3; proof on pages 11–12. |
| Every $`H<1/2`$ without loss in the exponent, and every $`H>1/2`$ | Proposition 3.2, (22), pages 5–7; stability on pages 11–12. |
| $`H=1/2`$, including $`a(0)\ne0`$, $`x_0=0`$ and zero crossings | Lemmas 4.1–4.2 and Proposition 4.3, pages 7–11; logarithms only away from zero and (32)–(36) handle the zero region. |
| Degenerate coefficients and every integer $`n\ge1`$ | Proposition 4.3 treats $`\beta=0`$, $`a(0)=0`$ and constant drift; final proof treats deterministic Euler stability, exactness when $`a=0`$, and finitely many larger steps, pages 11–12. |

The claimed estimate is terminal and uses exact noise samples. It does not assert a rate for approximated noise, a supremum-in-time error, or an optimality lower bound.

The integrating-factor representation and prescribed recurrence are imported with explicit credit to Erdoğan, Lord and Schieven. The necessary additional analysis is the random-state conditional quadrature estimate for $`H\ne1/2`$ and the Lipschitz Brownian endpoint estimate including zero crossings. Related additive-noise, occupation-time and random-ODE results are discussed with their distinct hypotheses in the Introduction.

This mapping identifies the scope of the submitted analytic argument. It is not an independent mathematical audit or formal verification certificate.
