# Uniqueness of nonnegative heat controls at the minimum time

This package proposes a complete resolution of [AIM Problem 138](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/138-unique-minimum-time-positive-heat-control.md). For every pair of distinct positive constant states on the unit rod, the nonnegative finite Radon boundary-control pair satisfying all terminal sine moments at the original minimum time is unique. Its two components coincide. The formulation includes the closed time interval and possible endpoint atoms.

**Status: complete solution claim awaiting independent mathematical review.** The package is an analytic argument; the claim has not been accepted by the problem repository or independently verified by a human.

## Read the argument

- [Complete manuscript, PDF](paper/manuscript.pdf), 11 pages.
- [Editable LaTeX source](paper/manuscript.tex).
- [Comparison with every clause of the pinned target](TARGET_COMPARISON.md).
- [Payload manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

Theorem 1.1 states the full result. Lemma 2.1 identifies the measure moment time with the infimum over bounded nonnegative controls and proves attainment. Finite critical moment cones then produce nonnegative tests of vanishing cost. Exponential interpolation and a determinant estimate retain those tests' domination and a nonvanishing coefficient after an exponent is inserted. Proposition 4.5 determines both the positive average and the dominated signed boundary difference. The final proof returns to the original pair.

The Introduction distinguishes earlier waiting-time and attainment results, a later single-controlled-end result restricted to purely impulsive controls, and finite-dimensional uniqueness. All mathematical arguments needed for the present theorem are included in the manuscript, together with the precise cited source interfaces. The result supplies no explicit minimum-time formula or extension to nonconstant profiles.

## Build and integrity

The standalone source was compiled with TeX Live 2025 (pdfTeX 1.40.27) and latexmk 4.86a. With a TeX installation providing the standard packages named in the source, run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/manuscript.tex
shasum -a 256 -c SHA256SUMS
```

The supplied PDF is the inspected final artifact. A rebuild can differ in PDF timestamps or document identifiers. The proof is analytic and does not depend on numerical experiments, software certificates, or a formal proof project.

## Authorship and AI use

Manuscript author: Kaiwen Jin. Contact: [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com).

OpenAI Codex assisted with exploration, proof drafting, source checks, and editing. A separate fresh Codex context conducted a bounded review of the complete argument and cited interfaces, finding no surviving major objection and one minor literature-positioning issue. The final revision added a source-checked comparison and reference; the mathematical proof was unchanged. That editorial delta was checked in the preparation context. No detailed AI report is submitted. The AI review is not human or formal verification; independent mathematical review is requested.
