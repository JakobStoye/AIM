# Fourth-order diffusion approximation for three-player gambler's ruin

This is a complete analytic solution claim for [AIM 615](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/615-gambler-scaling.md), submitted for review.

For every fixed positive integer triple A, B, C and every elimination order, the manuscript proves that multiplying all capitals by n gives an error of O((n(A+B+C))^-4) from the Brownian limit. The proof uses loser-swap antisymmetry, a sixth-order angular defect and an explicit discrete superharmonic barrier.

- [Complete manuscript](paper/gambler_scaling.pdf)
- [Editable LaTeX source](paper/gambler_scaling.tex)
- [Target correspondence](TARGET_COMPARISON.md)

The manuscript author is Kaiwen Jin, with contact yui.ui.siki@gmail.com.

Build with a standard TeX Live installation containing amsmath, amsthm, lmodern, geometry and hyperref:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/gambler_scaling.tex
```

The paper contains the complete argument and cites public sources for the harmonic-function facts and the Brownian limit. No numerical computation or finite certificate is used as a proof premise. PUBLIC_MANIFEST.json lists the four payload files and their SHA256 hashes; SHA256SUMS also covers that manifest.

AI use and review: OpenAI Codex assisted with proof development, drafting and algebraic checks. No human referee certification, Lean verification or maintainer acceptance is asserted. A separate fresh-context Codex referee examined the complete five-page draft and all cited source interfaces; separate reader and qualitative style passes were also completed. Local notation and abstract comments were corrected by the drafting agent. The AI contexts shared a local filesystem and supply no independent human or formal certification. Detailed review reports are not part of this package.
