# Concentric balls for radiative thermal insulation

This package contains the manuscript **Concentric balls for thermal insulation with a radiative boundary law**, by Kaiwen Jin ([contact](mailto:yui.ui.siki@gmail.com)).

Theorem 1.1 presents an affirmative proof of the complete inequality in [AIM problem 400](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/400-radiative-insulation-concentric-balls.md). It covers every stated dimension and parameter, measurable heated sets, bounded Lipschitz outer sets, the upper bound on total volume, and the bare-ball endpoint.

- [Read the complete manuscript](paper/main.pdf).
- [Read or edit the LaTeX source](paper/main.tex).
- [Compare the theorem with the exact target](TARGET_COMPARISON.md).
- [Inspect the package manifest](PUBLIC_MANIFEST.json) and [file checksums](SHA256SUMS).

The argument rearranges the boundary potential with its singular variation retained, approximates the resulting one-dimensional cost by finitely many jumps, and removes the jumps by concavity under multiplication of the whole tail potential. The proof is analytic and uses no numerical experiment or computational certificate.

To build the manuscript with a standard TeX installation including `latexmk`, `pdflatex`, `amsmath`, `amssymb`, `amsthm`, `geometry`, `lmodern`, `microtype` and `hyperref`, run from this package directory:

```sh
latexmk -pdf -cd -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The generated PDF is `paper/build/main.pdf`. The supplied PDF was built with TeX Live 2025 and latexmk 4.86a. Only the included TeX files are needed. All references are listed in `paper/references.tex` with primary-source links.

AI use: OpenAI Codex assisted with developing and checking the argument, algebra, references and drafting. One AI reader and one AI referee reviewed an anonymized earlier draft in fresh contexts on a shared host; no detailed internal reports are included. This package presents a complete solution claim for independent mathematical review. It does not assert maintainer acceptance, human verification or formal verification.
