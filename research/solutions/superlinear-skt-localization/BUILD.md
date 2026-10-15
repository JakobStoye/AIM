# Rebuilding the manuscript

The manuscript is a standalone LaTeX article with its bibliography included. From the package directory, run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/localization.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/localization.tex
```

The two passes resolve equation, theorem and bibliography references. Standard packages are geometry, fontenc, lmodern, amsmath, amssymb, amsthm, mathtools, microtype and hyperref. The submitted PDF was built with pdfTeX 1.40.27 (TeX Live 2025). No external TeX inputs, bibliography files, figures, numerical code or private supplements are needed.

Checksums identify submitted bytes; a local rebuild can differ in PDF timestamps and metadata. Compilation and checksum validation do not certify the mathematical proof.
