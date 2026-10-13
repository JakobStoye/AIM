# Integration under uniform derivative bounds

This package submits an affirmative solution claim for
[AIM problem 556](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/556-smooth-integration-dimensional-curse.md).

Theorem 1 of the [manuscript](paper/uniform_derivative_integration.pdf)
proves, for every dimension `d >= 1` and every `0 < epsilon < 1`,

```math
n(\varepsilon,d)\ge (1-\varepsilon)
 \left(\tfrac12+\sin\tfrac12\right)^{-d}.
```


The function class and information model are those of the linked problem:
every mixed partial derivative of every order, including the function itself,
has supremum at most one. The lower bound permits adaptive sampling,
nonlinear reconstruction, and arbitrary quadrature weights. It therefore
gives the dimensional curse at a fixed absolute error tolerance.

The proof constructs a quadratic function from a sample-span complement
projection and a tensor product of unit vectors. It proves the full
all-order derivative inclusion and computes the exact product moment
matrix. Related squared-kernel work is credited in the paper; no priority
claim is made.

Files:

- [Complete manuscript](paper/uniform_derivative_integration.pdf).
- [Editable LaTeX source](paper/uniform_derivative_integration.tex).
- [Target comparison](TARGET_COMPARISON.md).
- [Content manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

The result is an analytic proof and does not depend on numerical
experiments or a computation certificate. The four-page manuscript was
compiled and read in full; its bibliography was checked against primary
sources. OpenAI Codex assisted in developing and checking the argument and
preparing the manuscript. Independent mathematical review is requested.
Catalogue classification remains with the maintainer.

To rebuild with a standard LaTeX installation:

```sh
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error uniform_derivative_integration.tex
```

The source is standalone and needs only standard LaTeX packages. The
manifest covers the authored mathematical files; `SHA256SUMS` also records
the manifest's hash and excludes its own hash.
