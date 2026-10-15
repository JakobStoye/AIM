# Two Fisher--KPP equilibria on a uniformly smooth unbounded domain

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com. Date: 15 October 2026.

This is a complete analytic counterexample claim for [AIM 379](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/379-strong-kpp-unbounded-uniqueness.md), submitted for independent mathematical review.

Theorem 1 constructs a connected unbounded domain in R^21 with uniformly C^{2,1/2} boundary and two distinct bounded positive classical Dirichlet equilibria. The reaction agrees with u-u^2 on [0,1] and is continued above 1 to satisfy the stated global regularity and sign conditions. The two boundary components are smooth global graphs. A corrected transverse mode supplies one solution with a lower bound of order |x|^{-2}; a compact enlargement and an exterior supersolution give another with an upper bound of order |x|^{-4}.

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Comparison with every requirement of the target](TARGET_COMPARISON.md)
- [Content manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

The admissible choice beta=0 and one dimension suffice to refute the target's universal uniqueness assertion. No optimal dimension or Robin classification is asserted. Rossi and Tough's [related preprint, v1](https://arxiv.org/abs/2610.17121v1) gives quadratic uniqueness through dimension 6 and homogeneous counterexamples from dimension 7 on locally analytic domains. The construction here checks uniform boundary charts through two global graphs; it does not transfer their shrinking-obstacle domains into that class. No exhaustive novelty or priority conclusion is claimed.

## Build

The source is self-contained apart from standard LaTeX packages. It was built with TeX Live 2025, pdfTeX 1.40.27 and latexmk 4.86a. From this directory:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final six-page PDF was checked for content, references and layout. Compilation is an artifact check. The mathematical evidence is the analytic argument in the paper; no numerical experiment, computer-assisted certificate or formal proof is used.

## AI use and review

OpenAI Codex assisted with the mathematical development, source verification and writing. Two fresh Codex contexts supplied a reader simulation and a mathematical referee review of an earlier draft; the author made one revision and checked the final artifact. The reviewers share the same model vendor as the development tool. These were AI reviews, and independent mathematical review is requested. The author remains responsible for the manuscript. No separate detailed review report is submitted.

This package supplies the paper and target correspondence. Catalogue classification is left to maintainer review.
