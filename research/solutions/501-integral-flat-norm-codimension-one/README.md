# Integral optimal flat-norm decompositions in codimension one

This package contains Kaiwen Jin's proposed complete resolution of
[AIM problem 501](https://github.com/MColbrook/AIM/blob/1b7c7fd251c1643bb41f0e3cef38704bcef410fd/problems/501-integral-flat-norm-codimension-one.md)
at revision `1b7c7fd251c1643bb41f0e3cef38704bcef410fd`.

[The manuscript](paper/integral_flat_norm.pdf) proves that every compactly
supported integral d-current in R^(d+1), d>=1, admits a compactly supported
integral optimum for the real flat norm. Nonzero input boundary is allowed.
The [target comparison](TARGET_COMPARISON.md) maps each original requirement
to the finished paper. Catalogue classification is left to maintainer review.

The main argument rounds the scalar BV filling with one common shift. The
coarea formula bounds variation away from the input surface; one-sided traces
and integer multiplicities preserve the mean residual mass on it. BV
compactness gives attainment. The proof uses no subdivision conjecture.

## Files and validation

- `paper/integral_flat_norm.pdf`: complete mathematical note.
- `paper/integral_flat_norm.tex`: standalone editable source, including references.
- `TARGET_COMPARISON.md`: original-target coverage.
- `PUBLIC_MANIFEST.json` and `SHA256SUMS`: package content hashes.

The source builds with TeX Live 2025 and latexmk 4.86a:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/integral_flat_norm.tex
shasum -a 256 -c SHA256SUMS
```

The paper is purely analytic. It does not depend on numerical experiments,
software, computational certificates or formal proof artifacts.

## AI use and review

OpenAI Codex assisted with proof development, source checking and writing.
These are AI-assisted checks. No separate detailed AI review report is
submitted; independent mathematical review is requested. This package is a
solution claim, not a statement of upstream acceptance or human certification.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.
