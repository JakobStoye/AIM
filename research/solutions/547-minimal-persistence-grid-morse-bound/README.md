# Minimal persistence grids and homological Morse bounds

This package proposes an affirmative resolution of [AIM problem 547](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/547-minimal-persistence-grid-morse-bound.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

[The manuscript](paper/grid_morse_bound.pdf), by Kaiwen Jin, proves in Theorem 2 that each coordinate set of the canonical minimal persistence grid has cardinality at most the exact homological Morse lower bound. It covers every finite nonempty simplicial complex, every coefficient field and number of parameters, and all face-monotone filters, including coordinate coincidences. Homology is ordinary unreduced homology of one common filter. The prescribed higher-syzygy subtraction is retained.

For each essential coordinate value, the proof chooses a minimal presentation degree on that slice. The resulting coordinate maps away from that grade are isomorphisms, so the local Koszul complex has no higher homology there. Injectivity of top-dimensional homology excludes a relation outside the degree range summed in the bound. Each coordinate value therefore supplies a distinct positive contribution.

- [Complete manuscript](paper/grid_morse_bound.pdf)
- [Editable LaTeX source](paper/grid_morse_bound.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The argument is analytic and does not depend on a computational certificate. The existing grid definitions and Morse lower-bound quantity are credited to Harrington, Tillmann and Torras-Perez and to Guidolin and Landi in the manuscript.

To rebuild the PDF, use a LaTeX distribution with AMS packages, `lmodern`, `geometry`, `microtype` and `hyperref`:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error grid_morse_bound.tex
pdflatex -interaction=nonstopmode -halt-on-error grid_morse_bound.tex
```

AI use and review: OpenAI Codex assisted with proof development, source checking and manuscript preparation, and checked the mathematical argument and cited source statements. No separate detailed AI review report is submitted. Independent mathematical review is requested; this package is a complete solution claim awaiting that review.
