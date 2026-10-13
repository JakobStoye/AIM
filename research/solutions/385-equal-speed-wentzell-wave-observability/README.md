# AIM 385: equal-speed wave observability in an annulus

This package submits an analytic counterexample to [AIM problem 385](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/385-equal-speed-wentzell-wave-observability.md), at the cited immutable problem revision.

[Read the complete manuscript](paper/equal_speed_observability.pdf) or [its editable LaTeX source](paper/equal_speed_observability.tex). [The target comparison](TARGET_COMPARISON.md) maps each requirement to the manuscript.

Theorem 1 constructs smooth real compatible solutions of the prescribed unit-speed system on $`1<|x|<2`$. Their initial bulk-plus-surface energy is one, while their outer normal-derivative observation is at most $`C T m^{-1/3}`$ along an infinite sequence, for every finite $`T>0`$. Thus the proposed energy observability inequality fails for every finite positive observation time.

The proof uses exact Bessel modes, a uniform short-interval estimate from the Bessel equation, an adjacent-phase subsequence, exact frequency roots, and the Bessel Wronskian. The manuscript contains the complete analytic proof.

To rebuild the manuscript with a standard TeX installation providing `latexmk`, run from this package directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/equal_speed_observability.tex
```

The paper uses ordinary LaTeX packages (`geometry`, `amsmath`, `amssymb`, `amsthm`, `fontenc`, `lmodern`, `microtype`, and `hyperref`). The supplied PDF was compiled with TeX Live 2025. A successful compilation checks the document, not the mathematical theorem.

OpenAI Codex assisted with literature retrieval, the spectral construction, checking the argument, and writing. The paper contains the AI-use statement. No separate detailed AI review is submitted. Independent mathematical review is requested; this package is a solution claim awaiting review.

`PUBLIC_MANIFEST.json` lists the selected files and their hashes; `SHA256SUMS` also covers the manifest. The scope is the exact annular model and energy in the problem, without a claim about optimal weaker norms or other geometries.
