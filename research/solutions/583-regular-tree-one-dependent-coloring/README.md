# Symmetric one-dependent colorings of regular trees

This package submits a complete analytic solution claim for [AIM Problem 583](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/583-regular-tree-one-dependent-coloring.md), at target revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

For every integer degree d >= 3, Theorem 1.1 constructs one probability law on the full infinite d-regular tree using the finite palette

```math
q(d)=2^{2d+16}d^2(2^d-1)9^{d-1}.
```

The coloring is proper almost surely. Complete restrictions to any two finite vertex sets at distance greater than one are independent. The law is invariant under every tree automorphism and every permutation of the colors. The palette depends only on the degree; its bound is not optimized.

The construction uses symmetric Hilbert-space tensors. Orthogonal projection ranges exclude equal adjacent colors; summing a vertex tensor permits arbitrary vertex deletion; a uniform estimate on rooted branches proves positivity for every finite size. Projective finite laws then give the infinite field. The Introduction credits the line and star literature, the neighboring two-dependent result, and the projection/positive-cone path method of Flin, Li and Suomela.

## Materials

- [Complete six-page manuscript](paper/main.pdf) and [editable LaTeX source](paper/main.tex).
- [Comparison with every original target requirement](TARGET_COMPARISON.md).
- [AI-use and review disclosure](AI_USE.md).
- [Payload manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.

## Rebuild

From this package directory, use a LaTeX distribution with the AMS packages, `lmodern`, `geometry`, `microtype`, `hyperref`, and `latexmk`:

```sh
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The bibliography is embedded in the source; no additional manuscript inputs are needed. The argument is analytic and uses no proof-critical numerical computation or executable verifier. Building the document checks its presentation, not the mathematical theorem.

To check the distributed files:

```sh
shasum -a 256 -c SHA256SUMS
```

This is a solution claim submitted for review. A separate fresh-context AI reader checked the manuscript and its cited source uses; independent mathematical review is requested. Catalogue classification and acceptance are left to the maintainers.
