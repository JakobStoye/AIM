# Repeated GUE interaction on three tensor legs

This package contains Kaiwen Jin's proposed affirmative solution of [AIM 577](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/577-repeated-gue-strong-freeness.md).

For one normalized size-`N^2` GUE matrix `X_N`, the ordered operators `X_N ⊗ I_N` and `I_N ⊗ X_N` reuse the same realization on three tensor factors. The manuscript proves convergence in probability of the operator norm of every fixed complex noncommutative polynomial to its norm in two free variance-one semicircular elements.

- [Complete manuscript](paper/repeated_gue_three_legs.pdf)
- [Editable LaTeX source](paper/repeated_gue_three_legs.tex)
- [Comparison with the original target](TARGET_COMPARISON.md)
- [File manifest](MANIFEST.json) and [checksums](SHA256SUMS)

The proof applies existing results of Bandeira–Boedihardjo–van Handel, Gao–Kunnawalkam Elayavalli, Jekel–Lee–Nelson–Pi, and Haagerup–Thorbjørnsen. Its application checks the shared covariance and uses full self-adjoint matrix pencils; expected traces and a Gaussian variance estimate supply the norm lower bound. The conclusion concerns the stated three-site pair. Larger repeated-interaction families are not treated.

## Build the manuscript

The source is standalone and uses standard LaTeX packages: fontenc, lmodern, amsmath, amssymb, amsthm, mathtools, geometry, microtype, and hyperref. It contains its bibliography and requires no external figure, data, code, or proof supplement.

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/repeated_gue_three_legs.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/repeated_gue_three_legs.tex
```

The supplied PDF and source are bound by the package manifest. Checksums verify file integrity; compilation verifies typesetting. The theorem is supported by the analytic argument in the manuscript, with the stated public theorem dependencies. No numerical or formal-proof certificate is claimed.

## AI use and review

OpenAI Codex assisted with the derivation, source checks, mathematical review, and manuscript preparation. A separate fresh Codex context reviewed the manuscript and cited primary sources. This AI review is not independent human review or formal verification. No detailed AI report is included; independent mathematical review is requested. Catalogue classification and acceptance are left to the receiving maintainers.

Manuscript author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.
