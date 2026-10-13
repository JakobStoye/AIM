# Unnormalized univariate trace inequalities

This package submits a proposed full undecidability resolution of [AIM 559](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/559-univariate-trace-decidability.md).

[The manuscript](paper/trace_decidability.pdf) proves that no always-terminating exact algorithm decides nonnegativity of a rational polynomial in the ordinary traces of powers of one real symmetric matrix, uniformly over all finite matrix sizes. [Editable source](paper/trace_decidability.tex) and a [target comparison](TARGET_COMPARISON.md) are included.

The proof encodes arbitrary nonnegative integer tuples as multiplicities at fixed spectral nodes. Stationary interpolation supplies an error bound independent of the number of eigenvalues. A polynomial penalty controls every off-node spectrum and gives an exact reduction from discrete polynomial sign undecidability. Each polynomial summed over eigenvalues has zero constant coefficient, so no dimension trace is used.

The discrete undecidability input is credited to Hatami and Norine, Section 5 of arXiv:1005.2382v3, as a consequence of Matiyasevich's theorem. The manuscript supplies the full additional spectral argument.

## Rebuild

With a standard LaTeX installation and latexmk, run from this package directory:

```sh
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/trace_decidability.tex
```

The argument is analytic and uses no computational certificate. Compilation checks the document; its mathematical claim remains available for independent review.

## Authorship and AI use

Author: Kaiwen Jin, yui.ui.siki@gmail.com. OpenAI Codex contributed to developing the argument, source checking and drafting. The manuscript includes this disclosure. Independent human mathematical review is requested; no human or formal verification is claimed.

This PR adds the mathematical package and leaves catalogue classification to maintainer review.
