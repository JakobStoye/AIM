# Relative density under fixed-parameter extrapolation

This note claims a complete affirmative answer to [AIM problem 630](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/630-extrapolation-relative-density.md).

Starting from 0 and 1, let $`Q_\lambda`$ contain exactly the points obtainable by finitely many applications of $`(a,b)\mapsto(1-\lambda)a+\lambda b`$. Theorem 1 proves that $`Q_\lambda`$ is relatively dense in the real line for every real $`\lambda\notin[0,1]`$, and in the complex plane for every nonreal $`\lambda`$. The covering radius may depend on $`\lambda`$; no topological closure is taken.

- [Complete manuscript, PDF](paper/relative_density.pdf)
- [Editable LaTeX source](paper/relative_density.tex)
- [Comparison with every requirement of the problem](TARGET_COMPARISON.md)

The proof combines an integer polynomial small on the unit interval and expanding at the chosen parameter with a finite digit construction of a relatively dense set. A uniform bound on all digit polynomials gives one affine image of that entire set inside $`Q_\lambda`$. The imported polynomial characterization and the bounded-family embedding idea are credited to Fenner, Green and Homer, [*Fixed-Parameter Extrapolation and Aperiodic Order*](https://doi.org/10.1007/s00454-025-00816-4), especially Theorem 3.6, Fact 3.3, Corollary 3.8 and Lemma 6.19.

## Build

With a standard LaTeX installation providing `latexmk`, pdfLaTeX, AMS packages, `lmodern`, `geometry`, `microtype` and `hyperref`, run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/relative_density.tex
```

The supplied PDF has three pages. The proof is analytic and uses no numerical experiments or proof-critical computation. `PUBLIC_MANIFEST.json` records the selected files and their hashes; `SHA256SUMS` also covers that manifest.

## Authorship and review

Author: Kaiwen Jin; manuscript contact: yui.ui.siki@gmail.com.

OpenAI Codex was used to develop the argument, check the cited source and prepare the manuscript. A separate fresh context of the same AI assistant read the complete manuscript, checked its cited primary source and found no surviving objection within that bounded review. The contexts shared a filesystem; this was neither human review nor formal verification. No detailed AI review report is distributed. Independent mathematical review is requested, and catalogue classification is left to the maintainers.
