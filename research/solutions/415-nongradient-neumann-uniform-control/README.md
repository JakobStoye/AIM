# AIM 415 — proposed affirmative resolution

Author: Kaiwen Jin · [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)

This package submits an analytic proof for [AIM Problem 415](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/415-nongradient-neumann-uniform-control.md), at the displayed immutable revision. It is a complete solution claim submitted for mathematical review.

Theorem 1.1 of the [manuscript](paper/main.pdf) treats every bounded connected smooth domain in dimension at least two, every interior open control region and every autonomous global W^{2,infinity} drift satisfying the strict outward boundary inequality and the original neighborhood flushing condition. It imposes no gradient representation. A finite threshold T_* and a constant C give, for all T >= T_* and 0 < epsilon < 1, an L2 control driving each L2 initial datum to zero, with norm at most C times the initial norm. C is independent of epsilon and T in this range. No optimal control-time threshold is claimed.

The proof prescribes the normal derivative of a scalar conjugating function through a compatible Neumann Poisson equation. The remaining drift is tangential at the boundary, and the transformed Robin coefficient is positive. Two Carleman weights cancel the uncontrolled tangential boundary terms. A fixed-time exponential observation bound then combines with the cited general-drift flushing dissipation estimate. Both the full mixed-product calculation and the rough-data justification are included in the manuscript.

Files:

- [Complete manuscript](paper/main.pdf)
- [Editable standalone LaTeX source](paper/main.tex)
- [Requirement-by-requirement target comparison](TARGET_COMPARISON.md)
- [Content manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

To compile from this directory with a TeX Live installation containing latexmk:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

On macOS, verify the delivered file checksums with `shasum -a 256 -c SHA256SUMS`; on Linux use `sha256sum -c SHA256SUMS`. The argument is analytic and has no proof-critical computer calculation or numerical experiment. Compilation and checksums verify the delivered artifacts, rather than the mathematical conclusion.

OpenAI Codex provided substantial assistance with the argument, calculation checking, cited-source comparison, manuscript and submission preparation. No separate detailed AI report is submitted. No human or formal proof certification is claimed; independent mathematical review is requested. Catalogue classification is left to maintainer review.
