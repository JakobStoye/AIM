# Building and checking the manuscript

The LaTeX source is self-contained: its bibliography is included, and no figures, external bibliography database or local mathematical supplement is needed.

Use a TeX distribution providing pdfLaTeX and the packages `fontenc`, `lmodern`, `geometry`, `amsmath`, `amssymb`, `amsthm`, `aliascnt`, `microtype`, `needspace`, `hyperref` and `cleveref`. The supplied PDF was built with pdfTeX 1.40.27 (TeX Live 2025).

From this package directory:

```sh
mkdir -p build
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build paper/manuscript.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build paper/manuscript.tex
```

The rebuilt document is `build/manuscript.pdf` (eight pages). The second pass should report no unresolved references or citations. Compilation checks document integrity; it does not establish the mathematical theorem. PDF timestamps can differ between builds.

Verify the supplied files before rebuilding them:

```sh
shasum -a 256 -c SHA256SUMS
```

The integrity list covers every supplied file except itself, including the public manifest. The manifest records the five payload files. No numerical or formal-proof execution is required by this analytic note.
