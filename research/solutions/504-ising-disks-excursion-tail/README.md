# Exponential excursion tails for planar Ising disks

This package contains a proposed complete analytic resolution of [AIM problem 504](https://github.com/MColbrook/AIM/blob/1b7c7fd251c1643bb41f0e3cef38704bcef410fd/problems/504-ising-disks-excursion-tail.md).

For the pinned-origin topology-preserving square-clump dynamics, with legal addition rate beta and deletion rate 1, Theorem 1 proves

    lim_{T -> infinity, T integer} P(excursion maximum >= T)^(1/T) = kappa beta

for every fixed 0 < beta < 1/kappa. Here kappa is the area growth constant of square-lattice self-avoiding polygons up to translation. The equivalent rare-event normalization limit is also proved.

The new lower bound uses arbitrary fixed-area polygon blocks joined by a single square. Recovering completed prefixes from cumulative column areas bounds the energy of a unit flow. The proof retains Baryshnikov and Onaran's planar indentability and clump-counting results, with exact source citations.

- [Complete manuscript](paper/ising_disks_excursion.pdf)
- [Editable LaTeX source](paper/ising_disks_excursion.tex)
- [Original-target comparison](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA256 checksums](SHA256SUMS)

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.

## Rebuilding

From this package directory, run twice:

    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/ising_disks_excursion.tex

The manuscript uses standard LaTeX packages: fontenc, lmodern, amsmath, amssymb, amsthm, geometry and hyperref. No code, numerical data or computational certificate is required for the proof.

## AI assistance and review

OpenAI Codex assisted with the mathematical argument, source checking and manuscript preparation. No detailed AI review report is submitted. Independent mathematical review is requested; filing this package does not establish acceptance or formal verification. This contribution adds mathematical materials only and leaves catalogue classification to maintainer review.
