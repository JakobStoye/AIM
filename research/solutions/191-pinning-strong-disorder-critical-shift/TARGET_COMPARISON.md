# Target comparison for problem 191

Target: [Strong disorder versus a shifted pinning threshold](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/191-pinning-strong-disorder-critical-shift.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted work: Kaiwen Jin, *Strong disorder and critical-point shift for a Gaussian pinning model*, 15 October 2026. References below are to the [manuscript](paper/manuscript.pdf).

| Original requirement | Result and manuscript location | Scope |
| --- | --- | --- |
| Iid renewal gaps proportional to n^(-5/4), normalized by their sum | Equation (1.1) fixes exactly K(n)=n^(-5/4)/zeta(5/4). Section 2 uses s=5/4 and alpha=1/4. | Same law and normalization. |
| Independent standard real Gaussian disorder, independent of the renewal | Introduction immediately before (1.2); Section 2 defines eta_n=exp(beta omega_n-beta^2/2). | Same data and independence. |
| Partition function rewards contacts 1 through N and has a free endpoint | Equation (1.2) and the paragraph following it; (2.1) relates it to constrained C_n using the final renewal tail. | The contact at zero is excluded; the physical endpoint is free. |
| F is the expected-log free-energy limit, and h_c is the threshold for positive F | Equation (1.2) and its following definition. Proposition 4.3 bounds the expected logarithm above and below at a strictly larger field. | Same F and h_c. |
| Every beta>0, conditional on P(W_infinity=0)=1 | Theorem 1.1; the final proof uses Proposition 5.3 to exclude this premise for beta<=beta_2 and Proposition 4.3 for beta>beta_2. | Entire inverse-temperature quantifier is covered. No zero-one dichotomy is assumed. |
| Strict h_c(beta)>-beta^2/2 | Proposition 4.3 gives a Delta>0 with F(beta,-beta^2/2+Delta)=0; monotonicity concludes Theorem 1.1. | Complete target claim, with an existential Delta depending on beta. No uniform quantitative shift is claimed. |
| Public dependency giving finite R=sum_{n>=1}u(n)^2 | Berger, *Random Interfaces and Pinning Models*, 4 March 2026, Theorem 3.16; used before (2.2). | Exact law satisfies its renewal-asymptotic hypotheses. |
| Public quantitative estimate needed at the second-moment boundary | Alexander–Berger, [arXiv:1608.03265v2](https://arxiv.org/abs/1608.03265v2), (4.12), Lemma 4.2 and (4.22); stated as Proposition 5.1. Both renewal exponents are 1/4; the moment exponent is 3/4 and the block-gap exponent 3/2. | The arbitrary-small coefficient in (4.12) is used. Equation (5.1) retains the fixed endpoint factor 1-exp(-lambda); the manuscript explicitly discusses this normalization. |

Sections 2–4 supply the age-process estimate, large constrained weights, planted-renewal endpoint bound, summable fractional moments, and the positive field margin. Section 5 converts the cited restricted-partition estimate into a finite random infinite-spine partition and uniform integrability. These arguments are included in the manuscript.

Berger's Conjecture 4.9 is broader than this fixed problem. Junk–Lacoin's bulk directed-polymer work is credited as methodological inspiration; its theorem is not applied directly to the contact-only model. Lacoin and Toninelli supply the neighboring small- and large-disorder benchmarks described in the introduction.

Evidence type: analytic theorem. No numerical experiment, computer-assisted certificate, or formal proof is claimed. The complete fixed-target result is submitted for independent review; catalogue classification and acceptance remain with the maintainers.
