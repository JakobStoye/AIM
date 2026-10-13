# AIM 574: draws in the undirected trapping game

This package contains a proposed affirmative resolution of the full statement of [AIM Problem 574](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/574-trap-draws-percolation.md), at revision c9929805cece044705abaaebe1cebddac1ba11a6.

Theorem 1.1 of the [manuscript](paper/main.pdf) states that the draw probability is zero on the site-deleted nearest-neighbor lattice in dimension two for every deletion probability in (0,1), and is positive for some deletion probability in (0,1) in every integer dimension at least three. The token moves without revisiting vertices, both players know the board, and a deleted origin is excluded from draws.

The [target comparison](TARGET_COMPARISON.md) maps the original model, quantifiers and both conclusions to the paper. The [editable source](paper/main.tex) is a standalone LaTeX document. [Build instructions](paper/README.md) require only a standard TeX installation.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.

Codex supported argument development, finite diagnostic checks, proof and citation checking, and writing. The mathematical proof is analytic and uses no computational certificate or numerical premise. No separate detailed AI review is included. Independent mathematical review is requested; this package is a solution claim awaiting review.

The file manifest gives package-relative paths, purposes and SHA-256 hashes. Check the frozen package with `shasum -a 256 -c SHA256SUMS`.
