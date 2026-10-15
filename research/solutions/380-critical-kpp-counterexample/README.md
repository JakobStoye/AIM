# A positive equilibrium at the critical Dirichlet eigenvalue

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This package submits a counterexample to [AIM 380, Extinction at the critical Dirichlet eigenvalue for strong-KPP reactions](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/380-strong-kpp-critical-extinction.md), at the pinned statement revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Read the [complete manuscript](paper/main.pdf), its [editable LaTeX source](paper/main.tex), and the [clause-by-clause target comparison](TARGET_COMPARISON.md).

For `x` in twenty-dimensional Euclidean space, set `t = 1000 + |x|^2`, `b = 50/t`, and `h = arccos(-b)`. The domain is the region `|z| < h(x)` in dimension 21. It is connected, unbounded and uniformly smooth. The manuscript proves that its compact-test Dirichlet spectral infimum equals 1 and constructs a bounded positive classical solution of the logistic equation with zero values at every boundary point. A bounded globally regular extension of the reaction above 1 satisfies the original reaction hypotheses. Thus the universal critical nonexistence assertion fails; no optimal dimension or dimension classification is claimed.

The proof combines the horizontal Hardy inequality with a bound on the vertical spectral deficit, an explicit strict subsolution, an ordered iteration on bounded domains, and a uniform boundary comparison function. The argument is analytical and uses no numerical experiment, proof-critical computation or formal proof. Related work and the exact analytical sources are cited in the manuscript.

To rebuild the PDF with a LaTeX distribution, run from this package:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

Alternatively run `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build paper/main.tex` twice after creating `build/`. No external figures or bibliography files are needed. `PUBLIC_MANIFEST.json` lists the four payload files and their hashes; `SHA256SUMS` additionally covers that manifest.

OpenAI Codex developed and checked the construction and prepared the exposition. One separate fresh-context AI reader and one fresh-context AI referee reviewed a frozen draft, followed by one author revision. These were same-vendor AI evaluations on a shared host; they were not human peer review or formal verification. No detailed review report is submitted. Independent mathematical review is requested. This is a solution claim awaiting maintainer assessment.
