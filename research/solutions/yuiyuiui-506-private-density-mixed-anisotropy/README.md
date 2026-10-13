# Minimax private density estimation with mixed anisotropy

This package contains a complete analytic solution claim for
[AIM Problem 506](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/506-private-density-mixed-anisotropy.md),
at statement revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
The claim is submitted for independent mathematical review.

Let `T = n alpha^2`, `c = beta_m / delta_m`, and `q = sum_m 1/delta_m`.
The manuscript proves matching bounds for the original expected unsquared
adversarial Sobolev loss:

- `T^(-(c+1)/(2(c+q)))` when `q > 1`;
- `log(eT) / sqrt(T)` when `q = 1`;
- `T^(-1/2)` when `q < 1`.

The parameter class keeps positive integer proportional smoothness vectors,
both a coordinate below `d` and a coordinate above `d`, and permits additional
coordinates equal to `d`. The lower bounds cover every sequentially interactive
alpha-private mechanism with its full released history and every measurable
L2-valued estimator. L2 is the estimator value space; it is not the loss.

The noncritical lower bounds are credited to Albert, Chevallier, Laurent and
Sacko, JMLR 27(69), 2026, Theorem 10, p.14. The paper supplies a weighted scalar
Fourier randomized-response upper construction and the critical full-history
information/testing argument that yields the logarithm. These supplementary
arguments are included in full.

- [Manuscript PDF](paper/mixed_private_density.pdf)
- [Editable LaTeX source](paper/mixed_private_density.tex)
- [Original-target correspondence](TARGET_COMPARISON.md)

Author: Kaiwen Jin. Manuscript contact: `yui.ui.siki@gmail.com`.
OpenAI Codex assisted with mathematical exploration, proof drafting, source
checks and manuscript preparation. This package does not claim human peer
review, formal proof-assistant verification, journal publication or AIM
acceptance. Catalogue classification is left to the maintainers.

The result is analytic; it uses no numerical experiment or computational
certificate. The PDF can be rebuilt from the single public source with a
standard LaTeX installation providing `amsmath`, `amsthm`, `mathtools`,
`lmodern`, `geometry` and `hyperref`. One tested environment is pdfTeX 1.40.27,
TeX Live 2025, with latexmk 4.86a.

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/mixed_private_density.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/mixed_private_density.tex
```

`PUBLIC_MANIFEST.json` records the purposes and SHA256 digests of the delivered
mathematical files. `SHA256SUMS` also covers that manifest.
