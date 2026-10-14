# AIM 648: the most isolated point in a polyhedral sample

This package presents an analytic proof claim for the two noncritical spatial
limits in [AIM 648](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/648-polyhedral-most-isolated-point-location.md).
Independent mathematical review is requested.

- [Complete manuscript](paper/polyhedral_isolation.pdf) (8 pages).
- [Standalone LaTeX source](paper/polyhedral_isolation.tex).
- [Target comparison](TARGET_COMPARISON.md).

For every fixed compact convex polyhedron in three dimensions, Theorem 1
claims that the most isolated iid uniform sample point tends to normalized
boundary surface area when the minimum interior dihedral angle exceeds pi/2,
and to normalized length on all minimum-angle edges when that angle is below
pi/2. The original smallest-index tie rule is retained. The critical equality
is outside the claim.

The proof computes spatial empty-ball intensities, bounds compatible nearby
isolation events and derives joint no-exceedance probabilities directly for
the fixed-size sample. The original conjecture is credited to Penrose, Yang
and Higgs. The source papers and basic probability/measure tools are cited
in the manuscript.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.
The mathematical argument, source checks and manuscript were prepared with
OpenAI Codex. No detailed AI review report is included in this package.

## Build

The source is self-contained and uses standard LaTeX packages. From paper/:

```sh
pdflatex -interaction=nonstopmode -halt-on-error polyhedral_isolation.tex
pdflatex -interaction=nonstopmode -halt-on-error polyhedral_isolation.tex
```

The delivered PDF was compiled successfully and its eight pages were checked
for content and layout. Compilation checks document integrity; mathematical
verification requires review of the proof and its cited dependencies.

PUBLIC_MANIFEST.json identifies the four content files and their SHA-256
hashes. SHA256SUMS also covers the manifest and can be checked with
`shasum -a 256 -c SHA256SUMS`.
