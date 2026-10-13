# AIM 507: independent review of PR #74

Reviewed 13 October 2026 at head `1986a0aaa93ef42709e196bfa9c4746fab250351`. Verdict: **Solved** following a complete independent AI audit. This is not human review or Lean verification. The submission's AI-use disclosure is retained.

[Proof](../../solutions/507-sequential-private-spectral-density/paper/main.pdf), [source](../../solutions/507-sequential-private-spectral-density/paper/main.tex).

## Target and result

The original Gaussian spectral-density class, its variance bounds and Sobolev radius, $`s>1/2`$, $`n\ge2`$ and $`0<\alpha\le1`$ are kept. Each release accesses its own raw observation and the private history only. The theorem supplies the matching squared $`L^2`$ minimax rate $`1\wedge(n\alpha^4)^{-2s/(2s+1)}`$ under sequential interaction, and the exact consistency boundary $`n\alpha^4\to\infty`$. No remaining target is identified.

## Independent audit of the private-history argument

The whole-prefix privacy lemma is valid under the precise access rule. If one coordinate of a fixed raw prefix changes, earlier releases coincide, the changed release is dominated by the factor $`e^\alpha`$, and all later releases apply identical transition kernels given their private histories. Kernel integration preserves domination. When a latent variable influences just one earlier raw coordinate and the other raw inputs are generated from independent nuisance variables, averaging over that nuisance law preserves this property. This establishes privacy for the **entire prefix**, rather than just the one release.

I reconstructed the posterior and Gaussian-smoothing estimates. The bounded posterior likelihood ratio relative to the latent prior yields chi-square at most $`(e^\alpha-1)^2`$. The smoothing kernel for $`tU+\sqrt{1-t^2}W`$ has centered square integral $`t^2/(1-t^2)`$. This follows by direct Gaussian integration: the two covariance eigenvalue factors in the square-density calculation are reciprocal and the resulting determinant is one. Cauchy–Schwarz gives the claimed contraction of posterior chi-square. The positivity bounds survive integration, so all KL comparisons have a valid lower density bound.

For the pure-lag spectral pair, the moving-average representation has coefficients satisfying $`A^2+B^2=1`$, $`AB=\delta/4`$, $`B^2\le\delta^2/8`$ and $`A^2\ge7/8`$. At time $`i`$, the relevant innovation $`\varepsilon_{i-h}`$ appears in exactly one raw coordinate of the earlier prefix, whereas $`\varepsilon_i`$ is fresh. Thus the preceding lemma applies without treating correlated Gaussian observations as independent. Each model's predictive density is close to the same Gaussian density; their separation has one privacy-squared factor. The current locally private channel contributes the second factor by the imported strong data-processing inequality. Gaussian raw-prefix covariance matrices are positive definite, so the common-history null-set comparisons used in the chain rule are valid. The explicit constants give the stated upper bound $`128(n-h)_+\alpha^4\delta^2`$, and the first $`h`$ releases carry no separation.

For a neighboring general spectral pair, subtraction of the common pure-lag part leaves a nonnegative Gaussian spectral background. Condition on that entire common background vector. The translated kernels still access only the current raw input plus released history and have the same privacy parameter. The uniform pure-lag bound therefore holds for every background realization. The common-mixture entropy inequality allows averaging this bound. This neither conditions on a model-dependent background nor assumes the conditioned outputs are independent. I checked positive definiteness and the lower spectral bound used for this decomposition.

## Minimax conclusion checked

The cosine hypercube uses $`m=\lceil\max(1,n\alpha^4)^{1/(2s+1)}\rceil`$ and amplitudes $`\theta=\kappa m^{-s-1/2}`$. For the proposed small fixed $`\kappa`$, every density is positive, has variance one, and satisfies the Sobolev constraint. Neighboring alternatives satisfy the general pair hypotheses with the specified scaling; their KL is at most one eighth. Orthogonal projection onto the cosine coefficients reduces squared $`L^2`$ risk to weighted sign errors. Assouad and Pinsker then give the desired lower bound uniformly, including bounded $`n\alpha^4`$. The cited noninteractive upper mechanism is sequentially admissible, and its two jointly released statistics have total sensitivity at most three. Its exact log-free upper theorem matches this class. The lower bound on every bounded subsequence proves the necessity part of the consistency boundary.

## References, including exact imported hypotheses

[Butucea–Klockmann–Krivobokova](https://www.jmlr.org/papers/volume27/25-0680/25-0680.pdf), JMLR 27(168) (2026), 1–49, has matching metadata and problem context. The manuscript's clipping observation agrees with Appendix A.3's exponential expression; this is explanatory background, not an assumption in the new lower bound.

[Issartel–Roueff, version 1](https://arxiv.org/html/2608.24847v1), dated 25 August 2026, is correctly identified. Lemma 3 applies the strong data-processing inequality to arbitrary measurable outputs; Lemma 7 supplies Assouad, Lemma 14 supplies the kernel entropy chain rule on the standard Borel spaces used here, and Lemma 15 supplies the common-mixture bound. Theorem 3 gives the quoted all-sample-size upper rate on exactly the stated class, including privacy dependence. These statements and hypotheses were checked in the primary text.

[Durrett's fifth-edition author text, 11 January 2019](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf), Section 3.10 (printed pages 196–203), contains the Gaussian covariance/density facts used in the moving-average realization and null-set comparison. Its Theorem A.3.1, printed page 464, supplies extension of the consistent real-valued Gaussian laws. The complete valid 490-page author PDF was obtained and these locators inspected. [Van Handel's 29 May 2007 lecture notes](https://web.math.princeton.edu/~rvan/acm217/ACM217.pdf), Theorems 1.6.6 and 1.6.12, supply the product-measure/Fubini and Radon–Nikodym facts, respectively. All four bibliography entries and the proof-critical imported results were checked. The novel prefix and smoothing arguments are supplied and reconstructed above.

## Presentation and verification limits

The complete source and accompanying explanations were read. All eight PDF pages were visually inspected: the theorem, equations, proof structure and bibliography agree with the source; no clipping or unresolved references were found. There is no executable or numerical dependency. This is a full mathematical audit by an AI reviewer; rendering and citation checks are supplementary evidence, and no independent human or formal verification is claimed.
