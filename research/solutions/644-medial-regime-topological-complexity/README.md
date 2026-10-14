# Topological complexity two in the homogeneous lower model

This package contains a proposed complete analytic resolution of
[AIM Problem 644](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/644-medial-regime-topological-complexity.md).
For every fixed $`p\in(0,1)`$, including random vertices, the lower-model
complex is path-connected and has reduced topological complexity two with
probability tending to one along all positive integer sample sizes.

The new argument shows that the Euler characteristic has no point mass
of asymptotically positive size. A large class of faces with the same vertex
sum modulo the ambient sample size permits many independent simplex trials
to remain unexposed while their cofaces are blocked. Their conditional
contribution is a shifted binomial variable. The connectivity and upper
complexity bound are credited to Barmak and Farber, arXiv:2608.07969v1.

Materials:

- [Complete manuscript](paper/main.pdf).
- [Editable LaTeX source](paper/main.tex).
- [Target correspondence](TARGET_COMPARISON.md).
- [Content manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

The proof is analytic and does not depend on numerical experiments,
computer-assisted certificates or a formal proof project. No numerical code
is required to reproduce the mathematical argument. To rebuild the manuscript,
use a LaTeX installation with the standard AMS packages, Latin Modern,
geometry, microtype and hyperref:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex

The manuscript was developed with OpenAI Codex assistance, as disclosed at
its end. No separate detailed AI-review report is submitted. Independent
mathematical review is requested; the package is a solution claim and does
not establish catalogue acceptance.
