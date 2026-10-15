# Proposed counterexample for Problem 463

Kaiwen Jin — yui.ui.siki@gmail.com — 15 October 2026.

[Manuscript](paper/manuscript.pdf) · [Editable LaTeX](paper/manuscript.tex) · [Target comparison](TARGET_COMPARISON.md).

This package proposes a negative answer to the general kernel-uniform full-order Sobolev estimate in [Problem 463](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/463-concave-nonlocal-calderon-zygmund.md). Write `sigma = 2s`. For every dimension `n >= 2`, order `0 < sigma < 2`, strict ellipticity pair `0 < lambda < Lambda`, and finite `p > max(2,n/sigma)`, the manuscript constructs admissible families that violate any bound with a constant depending only on these parameters. The solutions and forcing are smooth and bounded; each kernel is even, translation invariant, and smooth away from the origin. At order one the space is ordinary `W^(1,p)`; otherwise it is the Slobodeckij space.

The kernel family is permitted to vary while the ellipticity pair stays fixed. The result concerns a uniform estimate over the whole kernel class. It does not assert failure for the equal-constant isotropic class or for every individual fixed operator, and it makes no endpoint claim.

Independent choices of the kernel on disjoint jump annuli produce a prescribed nonlinear average from vanishing oscillations. Their linear averages tend to zero in every finite `Lp`. The resulting approximation would force an impossible Sobolev bound for concentrated negative Riesz potentials. The full analytic argument is in the eight-page manuscript. No computation or data is needed.

## Rebuild

The source is standalone and uses standard LaTeX packages. From this package directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/manuscript.tex
```

The supplied PDF is built from the supplied source. The package manifest and `SHA256SUMS` identify the delivered bytes. Compilation checks the artifact, not the correctness of its theorem.

## AI use and review status

OpenAI Codex assisted with proof development, mathematical checking, exposition, and manuscript feedback. A fresh-context reader and a fresh-context referee examined the same initial draft within Codex, followed by an author revision. These were AI feedback runs using a shared file system. No separate detailed review report is submitted. Independent mathematical review is requested; no human review, formal verification, novelty certification, or maintainer acceptance is claimed. Catalogue classification is left to maintainer review.
