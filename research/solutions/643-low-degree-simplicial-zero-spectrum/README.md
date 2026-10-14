# A degree-three counterexample for the normalized upper Laplacian

This package presents an analytic counterexample to both assertions in [AIM Problem 643](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/643-low-degree-simplicial-zero-spectrum.md).

Theorem 1 constructs a countable pure three-dimensional complex with maximum triangle degree three. On its full degree-weighted triangle cochain space, the normalized upper Laplacian has spectrum contained in `[1/C,4]` for an explicit positive constant `C`, and its kernel is zero. Every edge has infinite triangle incidence. One admissible dimension-three example disproves each all-dimensions assertion separately.

- [Complete manuscript](paper/degree_three_counterexample.pdf) and [editable source](paper/degree_three_counterexample.tex).
- [Comparison with the original target](TARGET_COMPARISON.md).
- [New manuscript-only AI review](AI_REVIEW.md).
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

In the review, `manuscript.tex` locators refer to the included editable source.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.

The construction, proof development, manuscript preparation and natural-language checking used OpenAI Codex. The review records its own preparation relationship and limitations. Independent mathematical review is requested; repository classification remains subject to maintainer assessment.

## Rebuilding the manuscript

From this package directory, with a standard TeX Live installation and latexmk:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/degree_three_counterexample.tex
```

The source is standalone and uses standard article, AMS, Latin Modern, geometry and hyperlink packages. The distributed PDF was built using TeX Live 2025. To reproduce its fixed creation timestamp, prefix the command with `SOURCE_DATE_EPOCH=1791936000 FORCE_SOURCE_DATE=1`. Successful compilation checks the artifact; the mathematical conclusion rests on the analytic argument in the manuscript.

Verify distributed file contents with:

```sh
shasum -a 256 -c SHA256SUMS
```

The argument requires no numerical experiment, certificate input or external proof-development supplement. The references identify the pinned AIM statement and the actual arXiv v1 of Rosenthal's paper. No priority or exhaustive literature claim is made.
