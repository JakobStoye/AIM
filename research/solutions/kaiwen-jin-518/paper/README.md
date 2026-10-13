# Manuscript

`main.pdf` is the complete 15-page article by Kaiwen Jin
(<yui.ui.siki@gmail.com>). `main.tex` is its editable standalone source.
The bibliography, numerical table and the coordinates for all three plots
are embedded in the source. The AI use declaration follows the bibliography.

Theorem 1 addresses the full time-semidiscrete target. Sections 2-4 contain
the analytic proof; Section 5 contains finite numerical experiments.
The [target comparison](../TARGET_COMPARISON.md) locates the requirements
of the pinned public problem.

The three vector PDFs in `figures/`, `numerical_table.tex` and
`numerical_summary.json` can be regenerated with
`python numerical_case/make_figures.py` from the package root. They are
convenient separate outputs; `main.tex` does not read these files.

For a conventional TeX installation:

```bash
cd paper
pdflatex -halt-on-error -interaction=nonstopmode main.tex
pdflatex -halt-on-error -interaction=nonstopmode main.tex
```

The submitted source was also compiled successfully with the Codex desktop
editor's compiler. See the [reproduction report](../REPRODUCTION_REPORT.md)
for artifact and software checks. These checks are not mathematical certification.
