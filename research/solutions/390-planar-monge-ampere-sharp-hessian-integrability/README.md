# Local Hessian integrability for planar Monge–Ampère inequalities

This package presents a proposed proof of [AIM Problem 390](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/390-planar-monge-ampere-sharp-hessian-integrability.md), at the stated revision.

For every $`0<\lambda<1`$, the manuscript considers every finite convex Alexandrov solution on a bounded convex planar domain satisfying
```math
\lambda|E|\le|\partial u(E)|\le\lambda^{-1}|E|
```
for every Borel set. It proves local strong $`L^{p_\lambda}`$ integrability of the full distributional Hessian, with
```math
p_\lambda=\frac{1+\lambda^2}{1-\lambda^2},
```
and hence the requested all-threshold weak endpoint estimate. Local constants may depend on the fixed solution, parameter, and interior set.

- [Manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Comparison with the original target](TARGET_COMPARISON.md)

The proof credits the calibration and scalar projection ideas in Agazzi et al., arXiv:2609.28311v2, and the transformation geometry in De Philippis–Guerra–Tione. The original Alexandrov measure argument and local weighted estimate are included in the manuscript. The package makes no claim of optimality or priority.

The argument is analytic. No numerical experiment, proof-critical computation, or formal proof is used. The editable source is self-contained apart from ordinary LaTeX packages and its cited public mathematical dependencies.

## Build and verify the files

With a TeX installation providing latexmk, pdflatex, the AMS packages, lmodern, geometry, microtype, and hyperref, run from this package directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
    shasum -a 256 -c SHA256SUMS

The supplied PDF is built from the included source. The reference build used pdfTeX 1.40.27 (TeX Live 2025) and latexmk 4.86a. Compilation and file checks establish artifact consistency; independent mathematical review is requested.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

The manuscript contains a factual statement of substantial OpenAI Codex assistance in developing the argument and exposition. One AI reader and one AI referee, each in a fresh context, reviewed the same initial anonymous draft; one author revision followed with AI assistance. Their reports concern the initial draft. Independent mathematical review is requested.
