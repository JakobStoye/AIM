# AIM 424: separated spherical Robin operators

This package contains a proposed complete analytic resolution of [AIM 424](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/424-spherical-pt-robin-real-spectrum.md), at target revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 1.1 of the manuscript proves real spectrum for every half-width `0 < a < pi/2`, real boundary parameter `alpha`, and integer mode `m`, with the exact potential and coordinate Robin conditions in the problem. The assertion is for each separated realization. The proof constructs a bounded inverse at every nonreal spectral parameter.

- [Complete manuscript (PDF)](paper/spherical_robin_real_spectrum.pdf)
- [Editable LaTeX source](paper/spherical_robin_real_spectrum.tex)
- [Target comparison](TARGET_COMPARISON.md)

The comparison of real Robin and Dirichlet eigenvalues is proved at every index. The nonzero modes use a positive Laplace representation for Fourier coefficients of the spherical potential; the zero mode uses actual first-order operator products. The resulting canonical-product ratio has a strict half-plane sign, which excludes nonreal solutions of the complex Robin boundary equation.

This is an analytic proof. No numerical experiment, computer-assisted certificate or formal proof is a premise. No numerical code is needed to reproduce the argument.

## Build

With a standard TeX Live installation including `latexmk`, run from this package:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/spherical_robin_real_spectrum.tex
```

The source is standalone and needs no additional manuscript assets. The supplied PDF was built with pdfTeX 1.40.27 (TeX Live 2025). `PUBLIC_MANIFEST.json` lists the selected content files and their SHA-256 hashes; `SHA256SUMS` also covers that manifest.

## Attribution and review

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

The manuscript credits Siegl's problem note, the partial results of Krejcirik and Siegl, and the standard spectral and complex-analysis sources it uses. OpenAI Codex assisted with exploration, drafting, source checks and revision. One internal AI reader and one internal AI referee examined the same frozen draft; the author then addressed the supported findings. Those reviews are preparation feedback, and no separate detailed AI review report is submitted. Independent mathematical review is requested. Public catalogue classification is left to the maintainers.
