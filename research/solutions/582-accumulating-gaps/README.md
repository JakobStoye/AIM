# Failure of Sobolev surjectivity for a screen with accumulating gaps

**Author:** Kaiwen Jin — yui.ui.siki@gmail.com.

This package submits an analytic counterexample to [AIM problem 582](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/582-fractal-screen-sobolev-invertibility.md), at revision `c9929805cece044705abaaebe1cebddac1ba11a6`. The complete argument is in the [manuscript](paper/main.pdf); [editable LaTeX](paper/main.tex), a [target comparison](TARGET_COMPARISON.md), and [build instructions](REPRODUCE.md) are included.

## Result

Set $`q=1/4`$ and

```math
\Gamma=\{0\}\cup\bigcup_{j\ge0}[q^{j+1},2q^{j+1}].
```


This compact subset of the real line is an Ahlfors regular 1-set: for every $`x\in\Gamma`$ and $`0<r\le1`$,

```math
r/16\le\mathcal H^1(\Gamma\cap B_r(x))\le2r.
```


Theorem 1.1 gives an exponent $`\alpha\in(0,1/2)`$ such that, for every Helmholtz wavenumber $`k>0`$ and every $`\alpha<t<1/2`$, the original Hausdorff-measure single-layer operator

```math
\mathbb S_k:\mathbb H^{t-1/2}(\Gamma)\longrightarrow\mathbb H^{t+1/2}(\Gamma)
```


is bounded and fails to be surjective. A fixed energy-space density has an image with an $`H^1(\mathbb R)`$ extension and does not belong to the asserted smoother density space. The positive harmonic function used to construct it comes from a mixed-boundary problem on a periodic cylinder; the strict adjoint boundary term forces its radial exponent below $`1/2`$.

The original problem permits $`n=d=1`$, so this is a disproof of its universal assertion. The argument does not determine the sharp regularity threshold for this screen or settle the assertion restricted to noninteger dimension $`d<n`$. It also does not assert irregularity for any one prescribed incident wave.

## Evidence and AI use

This is a mathematical solution claim submitted for review. OpenAI Codex assisted with the construction, drafting, primary-source checks and mathematical review. The complete public proof is in the manuscript; no proof-critical numerical computation or Lean formalization is asserted. The mathematical review includes an additional AI review that began in a fresh context. Independent human review and formal verification are not claimed. Independent mathematical review is requested. No separate detailed AI review report is submitted.

The geometry figure is a schematic drawn in LaTeX. The package contains no numerical experiment, solver or computational certificate. Its hashes are listed in [SHA256SUMS](SHA256SUMS) and [PUBLIC_MANIFEST.json](PUBLIC_MANIFEST.json).
