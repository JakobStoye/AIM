# AIM 398: a counterexample to finite-time exact boundary control

This package submits a complete negative answer to the universal question in
[Problem 398](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/398-parabolic-obstacle-boundary-control.md),
at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
It is a solution claim submitted for independent mathematical review.

The obstacle and initial state are

```math
\psi(x)=1-81(x-1/3)^2(x-2/3)^2,\qquad y_0(x)=9x(1-x).
```

They satisfy every data assumption in the question. The stationary minimizer
is equal to one on `[1/3,2/3]`. For every finite `T > 0` and every admissible
pair of endpoint controls, Theorem 1 proves

```math
\|y(T)-\bar y\|_{L^2(0,1)}
\ge \frac{2\sqrt{6}}{3\pi}e^{-9\pi^2T}>0.
```

Thus this single smooth data pair disproves the assertion for arbitrary smooth
obstacles. The result does not decide approximate or asymptotic steering, or
control questions with additional restrictions on the obstacle.

## Materials

- [Complete manuscript](paper/obstacle_control_counterexample.pdf).
- [Editable LaTeX source](paper/obstacle_control_counterexample.tex).
- [Comparison with the original target](TARGET_COMPARISON.md).
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

The manuscript contains the full analytic proof and its public source
citations. No numerical experiment, computer-assisted certificate or Lean
proof is used.

## Build and validation

The submitted PDF was built with pdfTeX 1.40.27, TeX Live 2025. It uses standard
LaTeX packages: `fontenc`, `lmodern`, `geometry`, `amsmath`, `amssymb`, `amsthm`
and `hyperref`. All bibliography entries are in the single source file.
From this package directory, run:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error obstacle_control_counterexample.tex
pdflatex -interaction=nonstopmode -halt-on-error obstacle_control_counterexample.tex
```

Compilation, references, source-to-PDF agreement and all four rendered pages
were checked. These artifact checks do not constitute mathematical
certification. A later build may differ in PDF timestamps and other metadata.

## Author and AI use

Manuscript author: Kaiwen Jin, `yui.ui.siki@gmail.com`.
OpenAI Codex helped develop the counterexample and proof, check cited source
passages and prepare the manuscript. The argument received AI review during
preparation; no human or formal verification is claimed. No separate detailed
AI review report is submitted. Independent mathematical review is requested.
Catalogue classification is left to the maintainers.
