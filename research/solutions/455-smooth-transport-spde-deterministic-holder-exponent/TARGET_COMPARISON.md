# Comparison with the original AIM 455 target

Original problem: [455. A deterministic Hölder exponent for smooth-transport parabolic SPDEs](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/455-smooth-transport-spde-deterministic-holder-exponent.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submission: Kaiwen Jin, *A deterministic Hölder exponent for parabolic SPDEs with smooth transport noise*, [complete manuscript](manuscript.pdf), [source](manuscript.tex).

| Original requirement | Manuscript result and location | Coverage |
| --- | --- | --- |
| Scalar Itô equation on the unit torus, every integer dimension at least two | Section 1, equation (1), Theorem 1.1 | Entire domain and dimension range |
| Arbitrary deterministic smooth initial data | Theorem 1.1 and the displayed variational identity in Section 1 | No special profile or amplitude restriction |
| Bounded measurable diffusion, without symmetry | Equations (2)–(3), Lemma 2.1 and equation (17) | Full matrix norm controls cutoff terms; the Jacobian drift retains the required transpose |
| Progressive coefficients and every prescribed spatial derivative bound on the transport | Equation (4) and Section 3.1 | Time-random coefficients remain merely measurable in time |
| Countably many independent Brownian motions | Equation (1), the ℓ² bounds and the flow interface in Section 3.1 | Countable noise retained throughout |
| Coercivity of diffusion minus one half of the transport covariance | Equations (3) and (11) | Same stochastic parabolicity assumption |
| No commutation or spatial constancy requirement | Theorem 1.1; general flow (13) | No added structural restriction on the fields |
| Every finite positive-time strip, including its terminal time | Lemmas 2.1–2.2 and proof of Theorem 1.1 | Backward-cylinder estimates and the actual continuous L² trace cover the upper face |
| One deterministic positive exponent with the permitted parameter dependence | Lemma 2.2 and Section 3.2 | With Λ₀ = M + M²/2, choose α from Lemma 2.1 at λ = ν/4 and Λ = 4Λ₀, and γ = α/2; dependence only on dimension, ν and M is sufficient |
| Almost-sure membership in the requested parabolic Hölder class | Theorem 1.1 and Section 3.2 | Temporal exponent γ/2 = α/4 and spatial exponent γ = α/2; the representative agrees with the variational process at every time |
| Hölder norm allowed to be random and unbounded | Lemma 2.2 and the closing result paragraph | Chart sizes and norms may depend on the realization; no norm-moment assertion is made |

The conclusion is the full affirmative alternative requested in the problem. The contribution beyond the cited sources is the local affine normalization in Lemma 2.2: a continuous invertible matrix field can be normalized near each point with fixed local ellipticity data. Compact patching preserves the common exponent.

## Imported results

- Agresti, Sauerbrey and Veraar, [arXiv:2511.12692v1](https://arxiv.org/pdf/2511.12692v1), Assumptions 2.1 and 2.5, Theorems 2.3 and 2.6, Remarks 2.4 and 2.7, and Proposition 2.8 supply the flow and inverse-flow interfaces. Proposition 2.14 supplies the distributional Itô–Wentzell formula. Section 3.1 verifies their hypotheses and calculates the transformed coefficients. The manuscript locators use the PDF dated November 18, 2025; its bibliography identifies the different equation numbering in the HTML dated August 24, 2026.
- Liao, [*Remarks on parabolic De Giorgi classes*](https://doi.org/10.1007/s10231-021-01084-8), definitions (1.1)–(1.2), Theorems 2.1 and 5.1 supply local boundedness and a fixed oscillation exponent. Lemma 2.1 proves membership in the required class for both truncation signs and every level, including nonsymmetric diffusion and bounded drift.

The manuscript contains the stochastic cancellation, distributional spatial change of variables, local normalization, endpoint and representative arguments. The solution claim is supported by an analytic argument; compilation and automated review are reported as checks of the supplied artifacts and argument, with no human-review or formal-verification claim. This package leaves catalogue classification to maintainer review.
