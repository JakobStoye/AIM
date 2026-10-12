# Holomorphy of the Dirichlet-to-Neumann semigroup on continuous boundary functions

This package submits a proposed affirmative resolution of [AIM 431](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/431-dtn-analyticity-continuous-boundary.md), at target revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Theorem 1.1 proves holomorphy of angle pi/2 on C(boundary Omega) for every bounded connected Lipschitz domain in dimension d >= 2 and every real symmetric uniformly elliptic coefficient matrix with Lipschitz entries on the closure. It uses the weak outward Dirichlet-to-Neumann operator, surface measure, and the supremum norm. Operator norms are bounded for all nonzero times in every strictly smaller sector. Constants may depend on the fixed domain and coefficient field.

The argument proves a complex Robin uniqueness theorem on a half-space, using vertical L2 Dirichlet control and an iteration of large-ball boundary mass estimates. A boundary rescaling argument then gives the required supremum norm resolvent estimate. A positive bounded weak-star limit of the graph area densities is retained in the limiting Robin condition.

## Materials

- [Complete nine-page manuscript](paper/dtn_analyticity.pdf).
- [Editable standalone LaTeX source](paper/dtn_analyticity.tex).
- [Target comparison and public theorem dependencies](TARGET_COMPARISON.md).
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

## Build and validation

From this package directory, with a standard TeX Live installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/dtn_analyticity.tex
shasum -a 256 -c SHA256SUMS
```

The proof is analytic and uses no numerical experiment, computer-assisted certificate, or Lean project. Compilation checks the document, not the mathematical theorem. The source is self-contained apart from standard LaTeX packages; its mathematical dependencies are cited in the manuscript.

## AI assistance and review status

OpenAI Codex assisted with proof exploration, checking cited source statements, and preparing the manuscript. No separate detailed AI review report is submitted. The result is a complete solution claim awaiting independent mathematical review. It has not been formally verified or independently certified by a human referee.
