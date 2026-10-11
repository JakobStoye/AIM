# AIM 067: exact uniform control time near a viscous Burgers shock

This package submits a complete analytic solution claim for
[AIM problem 067](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/067-burgers-shock-uniform-control-time.md)
at statement revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
The manuscript is by Kaiwen Jin.

For the exact centered shock `U^epsilon(x) = -tanh(x/(2 epsilon))` on
`(-L,L)`, Theorem 1.1 gives `T_unif/L = 4 sqrt(2)`. The worst-case L2
control cost stays bounded as viscosity tends to zero for every
`T > 4 sqrt(2)L` and diverges for every `0 < T < 4 sqrt(2)L`.
The cost at the critical time itself is left open; both strict sides suffice
to determine the requested infimum.

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [Package manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The proof is analytic. Sections 2--4 and Appendix A contain the entire
argument and its cited public dependencies; no separate computational
certificate or numerical experiment is used.

To build the source with a standard TeX installation, run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

AI assistance was used for literature retrieval, developing and checking the
argument, and preparing the manuscript. No separate detailed AI report is
submitted. Independent mathematical review is requested. This package presents
a solution claim; catalogue classification is left to maintainer review.
