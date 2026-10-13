# A square-pyramid counterexample for Problem 565

This package proposes a complete counterexample for [Problem 565, Asymmetry at the Macbeath point of a convex body](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/565-macbeath-center-asymmetry.md).

The body is the square pyramid

```math
K=\{(u,v,z):0\leq z\leq1,\ |u|\leq1-z,\ |v|\leq1-z\}\subset\mathbb R^3.
```

Its unique center maximizing the symmetric-intersection volume is
$`p=(0,0,(3-\sqrt2)/7)`$. For the apex $`y=(0,0,1)`$, the required point $`p-(y-p)/3`$ has height $`(5-4\sqrt2)/21<0`$, and so is outside the pyramid. The manuscript proves global uniqueness, including all nonaxial centers.

- [Complete manuscript](paper/macbeath_counterexample.pdf).
- [Editable LaTeX source](paper/macbeath_counterexample.tex).
- [Target comparison](TARGET_COMPARISON.md).
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

The proof is analytic; no numerical optimizer or computational certificate is required. To rebuild the PDF with a standard TeX distribution and the packages listed in the source, run from this package directory:

```sh
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/macbeath_counterexample.tex
```

The supplied PDF was compiled with TeX Live 2025, and both pages were checked for content, references and rendering.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.
OpenAI Codex derived the construction and proof draft and assisted with symbolic checks and exposition. No separate detailed AI review is submitted, and no independent mathematical review has yet been performed. Independent review is requested. Catalogue classification is left to maintainer review.
