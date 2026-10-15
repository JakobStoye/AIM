# Rebuild the paper

Use a LaTeX distribution providing pdfLaTeX, `lmodern`, `amsmath`, `amssymb`,
`amsthm`, `geometry`, and `hyperref`. From this package directory, run:

```sh
mkdir -p build
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build paper/main.tex
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build paper/main.tex
```

The rebuilt PDF is `build/main.pdf`. Two passes resolve the theorem,
equation and bibliography references. The supplied PDF was built with
pdfTeX 1.40.27 from TeX Live 2025. All manuscript inputs are included;
the cited primary papers are mathematical references rather than build inputs.

The proof requires no numerical script, data file, network call, or private
supplement. PDF byte identity after rebuilding is not required because creation
timestamps and distribution metadata can differ.
