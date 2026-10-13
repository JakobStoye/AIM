# Building the manuscript

The editable source is a standalone LaTeX article. It has no local inputs, external figures or bibliography database. A TeX distribution containing `lmodern`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `geometry`, `microtype` and `hyperref` is sufficient.

From this package directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/jack_normal.tex
```

Alternatively:

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/jack_normal.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/jack_normal.tex
```

The supplied PDF was built with pdfLaTeX from TeX Live 2025 (pdfTeX 1.40.27) and checked page by page. Hyperlinks and citations should be resolved after the final pass. TeX metadata and compression may make a rebuilt PDF bytewise different; this does not alter the source argument.

From this package directory, the supplied payload and manifest can be checked with:

```sh
shasum -a 256 -c SHA256SUMS
```

No experimental program is required to apply the theorem. All mathematical assumptions, imported results and derivations are stated in the manuscript.
