# Exterior observability with slower surface dispersion

This submission proposes a negative answer to [AIM Problem 386](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/386-slow-surface-schrodinger-observability.md), at repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

For the annulus with radii 1 and 2, bulk dispersion coefficient 1, inner surface coefficient 1/2, and outer Dirichlet condition, Theorem 1 constructs smooth compatible solutions with initial energy one and outer Neumann observation tending to zero for every fixed positive time. It therefore contradicts a solution-independent exterior observability constant at every positive observation time.

- [Complete manuscript (PDF)](paper/exterior_observability.pdf)
- [Editable LaTeX source](paper/exterior_observability.tex)
- [Comparison with the complete target](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

The argument is analytic. No numerical experiments, computer-assisted certificate, or Lean formalization are used.

To rebuild with a standard TeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/exterior_observability.tex
```

The source is self-contained and uses standard LaTeX packages. Successful compilation checks the document build, not mathematical correctness.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

AI use and review: OpenAI Codex (gpt-6.1-sol) contributed to proof construction, literature verification and manuscript preparation. Preparation included AI checks and fresh-context AI feedback, without independent human or formal verification. No separate detailed AI review report is submitted. Independent mathematical review is requested. This is a complete counterexample claim; catalogue classification is left to maintainer review.
