# Independent review of AIM 636: uniform Jack Kolmogorov bound

**Date:** 2026-10-13  
**Submission:** [PR #82](https://github.com/MColbrook/AIM/pull/82), Kaiwen Jin  
**Reviewed head:** `ec73c4f188e85051b8560f41b762835a564e05fa`  
**AIM statement:** problem 636 at `c9929805cece044705abaaebe1cebddac1ba11a6`  
**Reviewer:** independent Codex AI mathematical audit, separate from the submitted proof's development. No human or Lean verification is claimed.  
**Decision:** **Solved**.

[Manuscript](../../solutions/636-uniform-jack-normal/paper/jack_normal.pdf) · [Source](../../solutions/636-uniform-jack-normal/paper/jack_normal.tex)

## Target and exchangeable coupling

The bound uses the original Jack hook probability and transposition statistic, for every integer n at least three and every real alpha at least one. Its constant is the explicit universal value 10; it is independent of both parameters and covers the transition alpha of order n. No fixed-alpha limit, extra logarithm, or parameter-range restriction remains.

I checked Kerov's content convention and transition/cotransition formulas in the primary source. Addable corners use north-west box content, removable corners use the south-east content shifted by alpha minus one; the anisotropic diagram area is alpha times the box count. The positive Pieri multiplicity, hook dimension and harmonic function give normalized upward/downward kernels, and their products with the hook Jack law give detailed balance. Growing two independent children of a common size n-1 parent therefore gives the claimed exchangeable pair, with Jack marginals. This does not assume that upward and downward contents are independent after conditioning on the larger diagram.

## General symbolic argument independently reconstructed

The product formula for the corner resolvent follows by row telescoping. Expanding the logarithm of that finite rational product gives its coefficients through degree five. These yield upward moments and the shifted reciprocal-resolvent downward moments exactly, as finite algebraic identities for arbitrary positive real alpha. Expanding the removed content plus the alpha-minus-one shift recovers all three displayed downward formulas.

The low Jack-character identities were checked against Lassalle Section 15 and converted with the stated content scaling. Fulman's coefficient orthogonality and the constant all-ones coefficient give zero means and pairwise orthogonality for the three nontrivial characters. Their squared norms are independent of alpha in the submitted normalization. This implies the original statistic has mean zero and variance one.

Condition on the removed box before inserting the new box. The inserted content has zero mean and variance alpha times n-1. Its third moment depends on the parent's content sum, which is the larger diagram's sum minus the removed content. Retaining this term gives exactly the conditional cubic expression in the manuscript, with no lost covariance term. In its orthogonal-character form the cubic is:

```math
\frac{H_4+3\delta H_3+(5n-6+\delta^2)H_2}{n\binom n2^{3/2}}.
```

I independently expanded the character combination, the second-moment defect, and both squared norms. In particular the cubic squared norm has no cross terms, and its numerator is exactly the displayed polynomial Q. These are identities for arbitrary n at least five and real alpha, not inferences from finite numerical examples.

Shao--Zhang Corollary 2.2 really does permit the signed conditional third moment used here. Its assumptions are met: the regression coefficient is 2/n in (0,1), the remainder is zero, the statistic has first absolute moment at most one, and the finite partition law has all moments. Passing from conditioning on the diagram to conditioning on the statistic is valid by conditional expectation and Cauchy--Schwarz. The subsequent polynomial bounds use (alpha-1) squared divided by alpha at most alpha and split the normalized parameter below/above one. Recomputing the fourth-root constant gives the stated value strictly below 10 for n at least five. The cases n=3,4 follow from the elementary Kolmogorov distance bound by one. Thus all original quantifiers and the logarithm removal are proved.

## Independent finite checks and their role

As a separate diagnostic, I reconstructed Jack hook masses, upward corner residues and reverse probabilities by detailed balance without using submission code. For n=5 through 10 and alpha=1,2,10,100, all 24 rational cases matched the claimed defect and conditional-cubic squared norms exactly. [Recorded check results](636-independent-moment-checks.json) preserve the ranges and outcomes. These finite cases support the algebra audit but are not its premise and do not establish arbitrary-parameter validity by themselves. The submitted package contains no numerical experiment claimed as a proof certificate.

## Complete reference audit

All six bibliography items have correct authors, titles, dates and identifiers. The four journal metadata records were checked against official DOI records. The proof-relevant primary passages were checked:

- [Fulman, JCTA 108 (2004), 275--296, author manuscript](https://dornsife.usc.edu/jason-fulman/wp-content/uploads/sites/224/2023/06/steinjackfinal6.pdf): Lemmas 3.1--3.2 give the orthogonality and coefficient normalization used; its uniform-parameter conjecture is correctly described.
- [Kerov, arXiv:math/9712267v1 (1997)](https://arxiv.org/html/math/9712267v1): Section 2, Theorem 6.7, Lemma 7.2 and the hook/branching relations give the exact kernels with the stated corner coordinates.
- [Lassalle, Advances in Mathematics 222 (2009), 2227--2269](https://arxiv.org/html/0802.0448v3): Section 15 gives exactly the three low content identities after the explicit scaling/sign substitutions.
- [Shao and Zhang, Annals of Probability 47(1) (2019), 61--108](https://arxiv.org/html/1710.01554v2): Corollary 2.2 has the quoted signed-cubic inequality, not an absolute-third-moment replacement.
- [Chen, Raic and Thanh, Bernoulli 27(1) (2021), 442--468](https://bpb-us-w2.wpmucdn.com/blog.nus.edu.sg/dist/3/10976/files/2020/11/BEJ1245.pdf): Proposition 4.1 gives the stated 8.2 logarithmic bound and the fixed-power large-alpha comparison.
- [Thanh and Tu, Comptes Rendus Mathematique 363 (2025), 757--776](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.711.pdf): Theorem 8 has the stated restricted alpha range.

No required reference or proof assumption was found missing. Standard conditional expectation and finite polynomial operations are justified directly.

## Conclusion

The complete coupling, exact moment calculations, imported identities, Stein hypotheses, numerical constant and all-parameter conclusion were independently audited. This supports `Solved` through a documented independent AI audit. No external human or formal proof-assistant verification is claimed.

## Rendered PDF check

All 6 pages of the supplied main PDF were visually inspected against the source presentation. Titles, theorem statements, mathematical tables/equations, proof structure and bibliography agree; no clipped content or unresolved references were found. Root package checks separately parsed all pages and checked payload and archive hashes. Rendering is supplementary artifact evidence, not mathematical or formal verification.
