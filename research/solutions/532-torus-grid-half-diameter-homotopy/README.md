# Torus-grid Rips complexes at half the diameter

This submission addresses [AIM problem 532](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/532-torus-grid-half-diameter-homotopy.md), at statement revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For every integer k >= 3, the closed Vietoris–Rips complex of the 2k by 2k periodic Manhattan grid at radius k is claimed to be homotopy equivalent to a wedge of one three-sphere and 4k spheres of dimension 2k−1. The manuscript gives an analytic proof for the entire parameter range.

- [Complete manuscript](paper/torus-grid-half-diameter.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [Content manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

Adjacent pairs of rows and columns provide the high-dimensional spheres. After removing one facet from each, a cover by coordinate semicircles compares the remaining complex with the band union. A uniform cylinder calculation, integral homology comparison, simple connectivity and the homology Whitehead theorem identify the remaining three-sphere.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.

OpenAI Codex was used for proof exploration, drafting, source checking and manuscript preparation. AI checks are not human review or formal verification. No separate detailed AI review report is submitted. Independent human mathematical review is requested; the submission is a complete solution claim awaiting that review.

## Building the manuscript

The source is standalone and uses standard TeX Live packages. From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The exported source has been compiled, its typed references checked, and all six PDF pages read and visually inspected. Compilation verifies the document build. The mathematical claim rests on the written analytic argument and its cited public dependencies. No numerical computation, certificate or Lean proof is used in the manuscript.
