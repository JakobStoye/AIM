# Rectangular grids in crossing segment arrangements

This package proposes a complete affirmative solution to [AIM 593, A linear threshold for extracting a segment grid](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/593-red-blue-segment-grid.md), at repository revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.

For every integer $`k\geq1`$, $`3k`$ pairwise disjoint red straight segments and $`3k`$ pairwise disjoint blue straight segments, crossing completely between colors in their relative interiors, contain $`k`$ segments of each color forming a rectangular grid. Theorem 1 preserves the entire colored subdivided graph, vertex cyclic orders and the unbounded face.

Corollary 5 gives the stronger sufficient size $`2k-1`$ of each color. It also gives a rectangular selection of $`p`$ red and $`n-p+1`$ blue segments from $`n`$ of each color, for every $`1\leq p\leq n`$. Optimality of that sufficient size is not asserted.

- [Complete manuscript](paper/segment_grids.pdf), four pages.
- [Editable standalone LaTeX source](paper/segment_grids.tex).
- [Target comparison](TARGET_COMPARISON.md).
- [File purposes and SHA-256 hashes](PUBLIC_MANIFEST.json).

The argument is analytic. Circular averaging selects compatible segment directions; the geometric proof matches crossing orders, rotations, endpoints and the unbounded face. The final remark addresses the resulting conflict with the exclusion stated in Figure 26 of the source paper under its embedded-grid definition.

The source problem and orientation strategy are credited to R. Jain, M. Ricci, J. Rollin and A. Schulz, [On the geometric thickness of 2-degenerate graphs](https://doi.org/10.20382/jocg.v15i2a4), *Journal of Computational Geometry* 15(2), 94–123 (2024 issue, published 10 February 2025), Section 3.1 and Section 4, Question 1.

The argument, cited-source checks and manuscript preparation used OpenAI Codex. Independent mathematical review is requested. No independent human review or formal verification is claimed, and no separate detailed AI referee report is included.

To rebuild the manuscript with a LaTeX installation providing latexmk, amsmath, amssymb, amsthm, geometry and hyperref, run from this package:

    latexmk -norc -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/segment_grids.tex

The source was compiled with TeX Live 2025 and pdfTeX 1.40.27. The four-page PDF was checked for text, formulas, citation/reference destinations and layout. Compilation and these artifact checks do not replace mathematical review.
