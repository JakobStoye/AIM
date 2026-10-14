# Bounded flat transversals for fat convex bodies

A proposed proof for [AIM problem 596](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/596-fat-convex-transversal-pq.md), supplied for independent mathematical review.

For fixed integers d >= 3, 1 <= k <= d - 2, p >= k + 2 and fatness rho >= 1, the manuscript proves a bound C(d,k,p,rho) on the number of affine k-flats needed to hit any finite family of compact rho-fat convex bodies satisfying the (p,k+2) transversal condition. Body sizes, locations and convex boundaries may vary freely.

The new step rounds a fractional transversal uniformly across arbitrary body sizes. Groups formed around a minimum-radius member admit a common absolute error scale; a spherical dimension induction then produces approximate probes that a finite perturbation family turns into exact transversals. The manuscript credits the published fractional Helly and fractional transversal results it uses. The bound is not optimized.

- [Complete manuscript (PDF)](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Comparison with the frozen target](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com. OpenAI Codex substantially assisted proof exploration, source checking and drafting; the manuscript includes an AI-use statement. Independent mathematical review is requested.

## Building the paper

Use a LaTeX installation providing pdfLaTeX, Latin Modern, geometry, amsmath, amssymb, amsthm, microtype and hyperref:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The complete argument and its references are in the manuscript; the package has no additional proof supplement.
