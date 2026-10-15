# AIM 402: two coupled subdiffusion orders

This package proposes an affirmative resolution of [AIM Problem 402](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/402-mixed-order-fractional-logarithmic-convexity.md), at statement revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 1 proves the stated product-L2 interpolation inequality for every bounded smooth domain, every pair of distinct orders between zero and one, every positive final time, and every L2 initial pair. Its constant depends only on the domain, orders and final time. The proof treats the potentially growing low modes, the critical Dirichlet eigenvalue 2, and all high frequencies analytically.

- [Complete manuscript](manuscript.pdf)
- [Editable LaTeX source](manuscript.tex)
- [Comparison with the original target](TARGET_COMPARISON.md)

The manuscript contains the complete analytic argument. To rebuild it with a standard TeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
```

Author: Kaiwen Jin. Manuscript contact: `yui.ui.siki@gmail.com`.

The literature search, mathematical development and manuscript preparation used substantial OpenAI Codex assistance. One reader and one referee examined the same frozen draft in fresh Codex contexts sharing a workspace, followed by one author revision. This is AI feedback; independent human review has not occurred. No separate detailed AI report is submitted. Independent mathematical review is requested, and catalogue classification is left to the maintainers.
