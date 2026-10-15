# Strong disorder and critical-point shift for a Gaussian pinning model

Kaiwen Jin — contact: yui.ui.siki@gmail.com

This package proposes a complete analytic resolution of [AIM problem 191](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/191-pinning-strong-disorder-critical-shift.md). For the exact renewal law $`K(n)=n^{-5/4}/\zeta(5/4)`$ and independent standard Gaussian disorder, Theorem 1.1 proves, for every inverse temperature $`β>0`$, that almost-sure extinction of the annealed-normalized free partition function implies a strictly positive critical-field shift.

The conclusion concerns this exact normalized gap law. It does not claim the general renewal-law conjecture or a shift uniform in the inverse temperature.

- [Complete manuscript](paper/manuscript.pdf) (11 pages).
- [Editable standalone LaTeX source](paper/manuscript.tex).
- [Target comparison and imported results](TARGET_COMPARISON.md).
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

To build, install a standard TeX distribution with latexmk and run `make` from this directory. The output is `build/manuscript.pdf`. The supplied source was built with TeX Live 2025 and latexmk 4.86a. No custom class, external bibliography database, numerical code, or computational certificate is required. PDF timestamps can differ on a fresh build.

The argument uses the quantitative restricted-partition estimate in Alexander and Berger, arXiv:1608.03265v2, with its endpoint normalization written explicitly. The manuscript credits the other background and methodological sources.

OpenAI Codex contributed substantially to the mathematical argument, source checks, and writing; AI reader and referee-style feedback informed the revision. No separate detailed AI review is submitted. Independent mathematical review is requested. This is a proposed solution, with no claim of formal verification or maintainer acceptance.
