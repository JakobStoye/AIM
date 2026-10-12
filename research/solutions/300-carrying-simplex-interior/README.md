# Interior smoothness of carrying simplices

Author: Kaiwen Jin ([yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)).

This package proposes an affirmative resolution of [AIM problem 300](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/300-carrying-simplex-interior.md) at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
Theorem 1 proves that the entire positive interior of the carrying simplex is a C1 embedded hypersurface for every dimension d >= 3 under the problem's exact per-capita competition and closed-box spectral assumptions. Equivalently, its radial function is C1 on the relative interior of the probability simplex. The statement is limited to interior regularity.

Read the [complete manuscript](paper/interior_smoothness.pdf), its [editable source](paper/interior_smoothness.tex), and the [target comparison](TARGET_COMPARISON.md). The proof uses a uniform contraction of weighted logarithmic inverse derivatives, constructs a continuous covector, and shows that its kernel contains every contingent direction of the logarithmic carrying simplex.

## Build and integrity

The source is standalone LaTeX and uses standard packages included in TeX Live. From this directory run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/interior_smoothness.tex
```

The resulting file is `build/interior_smoothness.pdf`. The supplied PDF has seven pages. The proof is analytic; no numerical or formal-proof runtime is required. Compilation checks document generation.

`PUBLIC_MANIFEST.json` gives the purposes and SHA256 hashes of the four payload files. `SHA256SUMS` additionally covers the manifest. On a system with `sha256sum`, run `sha256sum -c SHA256SUMS`; on macOS run `shasum -a 256 -c SHA256SUMS`.

## AI use and review

OpenAI Codex assisted with literature retrieval, development of the argument, proof checking, and manuscript preparation, as disclosed in the paper. A pre-publication version was read by fresh-context AI evaluators for mathematical objections and comprehension; the final version incorporates local exposition clarifications and exact source-version links. Independent mathematical review is requested. No separate detailed AI report is submitted. This package presents a complete solution claim; acceptance and catalogue classification are for the receiving repository's maintainers.
