# The homology of a persistence fiber without finite bars

Kaiwen Jin - yui.ui.siki@gmail.com

This package proposes a complete affirmative answer to [AIM 537](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/537-persistence-fiber-betti-numbers.md), at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For every finite connected simplicial complex K and every q>=0, Theorem 1 proves that the ordinary F2 homology of the prescribed all-simplex persistence fiber F_K is isomorphic to H_q(K;F2). It includes the exact interval normalization, both m=1 and m=2, and all homological degrees. The [target comparison](TARGET_COMPARISON.md) gives the statement-to-proof map.

Read the [four-page manuscript](paper/persistence_fiber.pdf) or its [standalone LaTeX source](paper/persistence_fiber.tex). The fiber has a deformation retract identified with the order complex of nonempty F2-acyclic subcomplexes. A homological poset comparison then gives the conclusion. The poset method is credited to existing work, and the needed special case is proved in the manuscript.

## Reproduction

The argument is an analytic proof. It requires no numerical experiment or computation-dependent certificate. To rebuild the manuscript from these public inputs, use a TeX distribution with `latexmk` and the standard packages listed in the source:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/persistence_fiber.tex
shasum -a256 -c SHA256SUMS
```

The source was built with TeX Live 2025 and latexmk 4.86a. The complete rendered PDF and its internal references were inspected. The manifest and checksum file describe the submitted bytes.

## AI use and review

OpenAI Codex was used to develop the argument, check the proof and references, and prepare the note. No separate detailed AI review report is submitted. Independent mathematical review is requested; catalogue classification is left to maintainer review.
