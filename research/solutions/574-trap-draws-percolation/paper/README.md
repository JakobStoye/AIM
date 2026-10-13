# Building the manuscript

The manuscript is a single standalone LaTeX file. Its bibliography is included in the source; no additional figures, data files or bibliography database are required.

From the package root, use TeX Live with latexmk:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The output is `build/main.pdf`. The source uses the article class, Latin Modern fonts, geometry, AMS mathematics packages, microtype and hyperref. The included PDF was built with TeX Live 2025 and pdfTeX 1.40.27.

The manuscript contains the complete analytic argument and its external citations. Building the PDF checks the document; it does not certify the mathematical proof.
