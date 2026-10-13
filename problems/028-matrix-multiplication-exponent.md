# 028. Is the matrix-multiplication exponent two?

**Area:** Numerical linear algebra and algebraic complexity

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-13

## Problem statement

Over $`\mathbb C`$, let $`\omega`$ be the infimum of all real $`\tau`$ for which two arbitrary $`n\times n`$ matrices can be multiplied using $`O(n^\tau)`$ scalar arithmetic operations. Determine whether $`\omega=2`$.

Equivalently, for every $`\varepsilon>0`$, is there an arithmetic algorithm, with constants allowed to depend on $`\varepsilon`$, using $`O(n^{2+\varepsilon})`$ operations for every $`n`$? Arithmetic is exact; bit complexity and numerical stability are separate requirements.

## Application

Matrix multiplication underlies dense factorizations, least squares, eigenvalue algorithms and many scientific computing kernels. Its exponent describes a fundamental asymptotic computational limit.

## References

1. P. Dutta, F. Gesmundo, C. Ikenmeyer et al., [Geometric complexity theory for product-plus-power](https://wrap.warwick.ac.uk/id/eprint/191761/1/1-s2.0-S0747717125000409-main.pdf), Journal of Symbolic Computation 132 (2026), 102458; introduction. Definition and tensor characterization.
2. E. Dupont et al., [Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://arxiv.org/abs/2608.16884), 2026. August upper-bound improvement.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf), result family 107 (2026). Statement locator: `Theorem thm:main (section 1)`.

## Status review

**Known cases:** Over the complex numbers, the square matrix-multiplication exponent is at most $`9/4`$, with exact algorithms using $`O_\varepsilon(n^{9/4+\varepsilon})`$ arithmetic operations.

**Remaining target:** Determine whether the exponent equals two; the improved upper bound remains strictly above two.

**Statement comparison:** Exact complex arithmetic and arbitrary exponent slack match AIM. The theorem proves $`\omega\le9/4`$, improving the previous upper bound; it does not prove $`\omega=2`$ or $`\omega>2`$. Rectangular exponent-two bounds do not establish the square exponent.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-028) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/107.md). Actual endpoint complex_omega_le_nine_quarters is implemented; the comparator is a sorry-containing target file, not the certificate. This formalizes partial progress only; no replay/axiom log inspected. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/028-matrix-multiplication-exponent.md).
