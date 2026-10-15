# AIM 416: positive equilibrium attraction

This package proposes an affirmative resolution of [AIM Problem 416](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/416-catalytic-reaction-diffusion-positive-attractor.md) at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.

Theorem 1.1 proves uniform convergence of all three concentrations to the positive equilibrium for every dimension, bounded connected smooth domain of volume one, positive diffusion coefficients, and strictly positive C2 Neumann-compatible initial data in the mass regime M2 <= M1 < 2 M2.

- [Complete manuscript](paper/manuscript.pdf)
- [Editable standalone LaTeX source](paper/manuscript.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [AI use and review disclosure](AI_DISCLOSURE.md)
- [Public file manifest](PUBLIC_MANIFEST.json)
- [SHA-256 checksums](SHA256SUMS)

The quadratic energy for the first and third concentrations is credited to Nguyen and Tang. The additional global argument combines uniform spatial homogenization, a scalar logistic equation for the total catalyst mass with a vanishing relative error, and a final zero-mean heat estimate. Standard Neumann spectral and kernel facts are attributed to the specified author version of Baudoin's book; the consequences needed for this proof are derived in Section 2.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

## Build the manuscript

With a standard LaTeX installation containing the packages declared in the source, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/manuscript.tex
```

The supplied PDF was built with pdfTeX from TeX Live 2025 and checked page by page. The evidence is an analytical proof; document compilation is a reproducibility check on the manuscript.

This is a complete solution claim submitted for independent mathematical review. Catalogue classification is left to the maintainers.
