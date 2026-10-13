# Rational approximation of fractional inverse powers

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This package submits a complete analytic solution claim for [AIM 554](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/554-stieltjes-rational-asymptotic-constant.md) at target revision `c9929805cece044705abaaebe1cebddac1ba11a6`. For every fixed positive finite interval `[a,b]` and fixed `0 < gamma < 1`, Theorem 1 proves the proposed leading constant for best absolute uniform approximation of `x^(-gamma)` by the full real rational class of type `(n-1,n)`. Poles outside the interval are unrestricted.

The [manuscript](paper/main.pdf) contains the full argument. Its [editable source](paper/main.tex) is standalone. The [target comparison](TARGET_COMPARISON.md) gives theorem, section and equation locations.

The proof combines the Jacobi-weight multipoint Pade theorem of Baratchart and Yattselev with a weighted finite-Blaschke construction on a slit disk. The construction supplies normalized node measures and alternating absolute errors. A degree count gives the lower bound for every admissible rational function. The relative square-root result of Braess and Hackbusch fixes the elliptic normalization. The cited approximation papers are credited in the manuscript.

## Build

A standard LaTeX installation with `pdflatex`, Latin Modern, AMS packages, `geometry` and `hyperref` suffices. From this package directory run:

```sh
make -C paper
```

The supplied PDF was compiled with pdfTeX from TeX Live 2025 and inspected on all pages. Rebuilding requires only the supplied TeX source and ordinary LaTeX packages. `PUBLIC_MANIFEST.json` and `SHA256SUMS` pin the submitted files; PDF build metadata can vary on recompilation.

## Evidence and review

This is an analytic proof; it uses no numerical experiment, proof-critical computation or formal verification. OpenAI Codex assisted with source retrieval, mathematical derivation, checking and writing. AI checks included the constructing context and a fresh context on a frozen manuscript; those contexts share a vendor and host. Independent mathematical review is requested. No detailed AI review report is included.

The claim covers the entire fixed-parameter target. It makes no uniform assertion at endpoint exponents, at the branch point, or for unbounded intervals. This package-only submission leaves catalogue classification to maintainer review.
