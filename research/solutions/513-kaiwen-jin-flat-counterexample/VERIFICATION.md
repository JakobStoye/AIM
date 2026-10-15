# Document validation

Checked on 13 October 2026. The selected source is standalone `paper/main.tex`,
with its bibliography included and no external figures or data inputs.

* Local build: `latexmk` 4.86a with pdfTeX 1.40.27, TeX Live 2025.
* Build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex`.
* Result: a three-page PDF; no unresolved citations, references or labels, and
  no overfull boxes in the final build. A harmless underfull bibliography line
  has no clipping or missing content.
* All three pages were read and visually checked for equations, matrix entries,
  author/contact, citations, margins, page breaks and glyphs.
* Typed-reference preflight: nine source targets, seven typed references,
  zero mismatches and zero unresolved references. Visible reference wording
  and destinations were checked against the source.

These are document checks. The mathematical justification is the complete
analytic argument in the manuscript and its cited primary results. The
manuscript presents the fixed cup-product calculation explicitly; its truth
does not rely on a search program, numerical experiment or hidden certificate.
Independent mathematical review is requested.
