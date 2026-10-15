# AIM 411: continuity of states for bounded admissible inputs

Author: Kaiwen Jin  
Contact: yui.ui.siki@gmail.com

This package submits a complete analytic solution claim for
[AIM 411 at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/411-bounded-input-state-continuity.md).
Independent mathematical review is requested.

[Read the manuscript](paper/continuity.pdf) ·
[Editable LaTeX source](paper/continuity.tex) ·
[Full target comparison](TARGET_COMPARISON.md)

Theorem 1 covers arbitrary real or complex Banach state and input spaces.
Under the stated admissibility assumption for every strongly measurable
essentially bounded input, the finite-time control operator norms tend to zero
as the time horizon decreases to zero. Every original convolution state is
therefore continuous in the state-space norm on the whole closed interval.
No geometric or separability assumption is imposed on either Banach space.

The proof fixes one input and varies its scalar multiplier. A resolvent
construction places the resulting operator's range in a separable invariant
subspace of the actual state space. The scalar Grothendieck theorem gives
weak compactness, and Orlicz--Pettis gives norm countable additivity of the
associated vector measure. Pasting inputs on disjoint intervals then proves
the uniform small-time estimate. The manuscript credits the external
Banach-space theorems and the previous geometric continuity results.

The assertion concerns the given extrapolation-space Bochner convolution
with a bounded control operator into that extrapolation space. It does not
claim a result for input maps without this representation.

## Build

From this directory, with a LaTeX installation containing the standard
packages listed in the source:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=paper/build paper/continuity.tex
```

The rebuilt PDF is `paper/build/continuity.pdf`. The supplied five-page PDF
was built with pdfTeX 1.40.27 and latexmk 4.86a from TeX Live 2025.
This is an analytic proof; no numerical experiments or computational
certificates are used.

## AI use and review

OpenAI Codex was used to develop the argument, check mathematical and
bibliographic details, and prepare the text. An initial manuscript was read
in separate fresh AI contexts by a reader and a referee, followed by one
revision and author checks of the final source and all rendered pages.
These are AI checks, not human peer review or formal proof verification.
No separate detailed AI review report is submitted. The package and its
posting do not establish maintainer acceptance or a novelty certificate.
