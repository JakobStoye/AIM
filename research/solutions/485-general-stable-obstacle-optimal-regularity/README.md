# Stable obstacle regularity with integrable angular densities

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This package presents a complete analytic solution claim for [AIM 485](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/485-general-stable-obstacle-optimal-regularity.md), at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. Theorem 1.1 proves the full global C^{1,s} bound for every nonnegative smooth compactly supported obstacle and every nonnegative even integrable angular density satisfying the stated mass and quadratic moment bounds. The constant depends only on dimension, order, and those two bounds.

The central classification argument compares a convex secant upper bound of order t with a spectral-measure Hopf lower bound of order t^s. Weak spectral compactness gives uniform profile approximation. The final endpoint step uses the density-kernel flatness theorem of Ros-Oton and Weidner. The endpoint theorem is stated for angular densities; no endpoint obstacle theorem for all singular spectral measures is claimed.

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [Public file manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

## Reproduce the PDF

From this package directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The source is standalone, with its bibliography included. It uses standard LaTeX packages and has no external images, private proof supplements, numerical data, or code dependencies. The distributed PDF was built with TeX Live 2025, pdfTeX 1.40.27, and latexmk 4.86a. Compilation and file-integrity checks establish artifact consistency; they do not certify the theorem.

## AI use and review

AI assistance was used in literature retrieval, mathematical exploration, preparation and checking of the natural-language argument, and exposition. The manuscript records the actual review assistance. No separate detailed AI report is submitted. Independent mathematical review is requested; this package is a solution claim, and catalogue classification is left to the maintainers.
