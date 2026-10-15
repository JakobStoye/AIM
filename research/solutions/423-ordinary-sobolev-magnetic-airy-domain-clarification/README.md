# An ordinary Sobolev domain correction for a magnetic Airy expression

This package explains why the ordinary Sobolev restriction printed in the
[2015 magnetic Schrödinger problem](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-02/2015-02_AIM_Almog_2.pdf)
is nonclosed. It is a domain clarification, and does not establish spectral
nonemptiness or eigenvalues for the natural closed magnetic Dirichlet
realization at every nonzero parameter.

- [Read the note](paper/domain-correction.pdf).
- [Editable LaTeX source](paper/domain-correction.tex).
- [Target and scope comparison](TARGET_COMPARISON.md).

For every fixed real parameter, the note constructs finite smooth functions
whose values and operator images converge strongly in the original L2 space,
while the limit fails ordinary H1 membership. Under the stated convention
that a resolvent point requires a bounded everywhere-defined inverse of a
bijective shift, the spectrum of this nonclosed restriction is all of the
complex plane. If spectrum is reserved for closed operators, the displayed
domain fails the prerequisite. Neither conclusion supplies a spectral
threshold for the distinct closed magnetic realization.

The author is Kaiwen Jin; contact: yui.ui.siki@gmail.com. The note contains
an AI-assistance disclosure. Internal AI evaluations do not constitute
independent human peer review.

## Build

The source is a standalone LaTeX article with its bibliography included.
From the package directory, run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/domain-correction.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/domain-correction.tex
```

The delivered PDF was built with pdfTeX from TeX Live 2025. The source uses
the standard geometry, amsmath, amssymb, amsthm, microtype and hyperref packages.
The argument is analytic and does not depend on numerical data or a solver.

`PUBLIC_MANIFEST.json` identifies the mathematical payload and its hashes.
`SHA256SUMS` covers that payload and the manifest; the integrity files do not
attempt to contain their own hashes.
