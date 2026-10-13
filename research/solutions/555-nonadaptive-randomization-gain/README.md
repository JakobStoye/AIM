# AIM 555: The maximal gain of nonadaptive randomization

Author: Kaiwen Jin · Contact: yui.ui.siki@gmail.com

This package presents a **complete solution claim**, awaiting independent
mathematical review, for [AIM Problem 555](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/555-nonadaptive-randomization-gain.md)
at target revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
The claimed supremum of the randomized polynomial rate minus the deterministic
polynomial rate is **one**, for the stated nonadaptive expected-norm model.

The manuscript constructs a fixed infinite-dimensional operator for each even
integer q >= 4. Each has two finite rates, and its gain is at least
`1 - 3/(2q) + 1/q^2`. These gains tend to one; attainment by a single operator
is not asserted. The measurements are continuous linear functionals, chosen
before input, with at most n measurements for every seed. The error estimate
covers inputs occupying infinitely many blocks.

- [Complete six-page manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Original-target comparison](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA256 checksums](SHA256SUMS)

The argument is analytic. It combines a proved finite-dimensional trace lower
bound, the CountSketch estimate of Kunsch--Wnuk (fixed preprint Proposition 4.1),
and the universal comparison of Krieg--Novak--Ullrich. All dependencies are
identified in the manuscript. No numerical experiments, implementation,
computer-assisted certificate, or formal proof is used as evidence.

## Build and check

With TeX Live and latexmk installed, run from this package directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
shasum -a 256 -c SHA256SUMS
```

The PDF in `paper/` is the submitted artifact; compilation produces a separate
`build/main.pdf`. PDF creation timestamps may differ between builds. The
source needs only standard LaTeX packages listed in `paper/main.tex`.
Compilation and checksums validate delivery, not the mathematical theorem.

## AI use and review

OpenAI Codex assisted in exploring the construction, drafting and checking the
argument, verifying cited sources, and preparing the manuscript. A fresh Codex
context was used for a separate pre-submission manuscript/source review, within
the same vendor and shared workspace. These are AI-assisted checks; no human
or formal proof certification is asserted. No separate detailed AI review
report is submitted. Independent mathematical review is requested.

This package adds mathematical materials only. Catalogue classification is
left to the AIM maintainers.
