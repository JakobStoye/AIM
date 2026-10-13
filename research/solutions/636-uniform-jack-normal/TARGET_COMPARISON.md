# Comparison with AIM 636

Frozen target: [636 — A uniform Gaussian approximation bound for Jack measures](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/636-jack-normal.md), repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Claimed result: Theorem 1.1 of [the manuscript](paper/jack_normal.pdf) gives the universal constant $`C=10`$.

| Original requirement | Manuscript correspondence |
| --- | --- |
| Integer partitions of size $`n`$ with the stated Jack law | Introduction: the hook products $`c_\lambda,c'_\lambda`$ and $`\pi_{n,\alpha}=\alpha^n n!/(c_\lambda c'_\lambda)`$ reproduce that law. Section 2.1 explains its coherent growth and reverse kernels. |
| The stated normalized transposition statistic | Equation (1) reproduces the row/column expression with denominator $`\sqrt{\alpha\binom n2}`$. Section 2.1 identifies its numerator as the sum of contents. |
| Every integer $`n\ge3`$ | Theorem 1.1. Section 3 proves the estimate for $`n\ge5`$; its final paragraph treats $`n=3,4`$ with $`d_{\mathrm K}\le1`$. |
| Every real $`\alpha\ge1`$ | Theorem 1.1. Section 3 uses only $`0\le(\alpha-1)^2/\alpha\le\alpha`$ and inequalities valid throughout this range. |
| One universal constant independent of $`n`$ and $`\alpha`$ | Equation (2) has the explicit constant $`10`$. The final comparison in Section 3 bounds the coefficient by $`3141/320<10`$. |
| Kolmogorov distance from a standard normal | The Introduction defines $`d_{\mathrm K}`$ against the standard normal distribution function. Equation (18) and the proof in Section 3 bound that same metric. |
| Rate $`\max\{n^{-1/2},\sqrt\alpha/n\}`$, with no logarithmic loss | Equation (2). The signed conditional cubic moment in equations (14), (16) and (17) leads directly to that rate. |
| The full transition $`\alpha\asymp n`$ | No transition-range restriction is imposed. The proof uses $`t=\alpha/n`$ and treats all $`t>0`$ in the same inequalities. |

The additional argument is the exact expansion of the conditional cubic increment in $`H_2,H_3,H_4`$, followed by Jack-character orthogonality. The external kernels, identities and Stein inequality are credited at their points of use. Only the displayed low-degree identities are used from Lassalle; the proof does not assume a general character conjecture.

The proof is analytic. Compilation, artifact checks and symbolic diagnostics are supporting checks, not a substitute for mathematical review. This is submitted as a complete solution claim; independent review remains requested.
