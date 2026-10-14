# A counterexample to a universal error bound for small-BV conservation laws

Kaiwen Jin — [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)

This package presents a proposed analytic counterexample to [Problem 367](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/367-universal-hyperbolic-error-rate.md) at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For one fixed smooth, strictly hyperbolic two-component system with genuinely nonlinear fields and a uniformly strictly convex entropy, Theorem 1.1 constructs one fixed small-BV initial datum and a sequence of approximate flows. They have exact initial agreement and conservation, fixed compact support, a uniform time modulus and the prescribed one-entropy residual bound on every time strip. Their uniform-in-time L1 error divided by the proposed square-root logarithmic scale tends to infinity.

The mechanism is cancellation between opposite entropy defects at the two ends of a translating Burgers pulse. Countably many disjoint pulse families fix the initial datum once for the entire sequence. The conclusion concerns the residual class and rate in the linked statement; it does not determine an optimal replacement rate or a convergence rate for a particular numerical scheme.

- [Complete manuscript (PDF)](paper/paper.pdf)
- [Editable LaTeX source](paper/paper.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

From this package directory, rebuild the manuscript with TeX Live and latexmk:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/paper.tex
```

The manuscript uses standard LaTeX packages and has no external mathematical input files or numerical dependency. The supplied PDF was built with TeX Live 2025, pdfTeX 1.40.27 and latexmk 4.86a; all six pages were inspected after revision.

OpenAI Codex contributed to the construction, proof and manuscript. Two further Codex contexts reviewed an earlier draft for readability and mathematical objections, followed by revision with Codex assistance. These were AI reviews; independent mathematical review is requested. No detailed review report is submitted. This package is a complete counterexample claim, with catalogue classification left to maintainer review.

`PUBLIC_MANIFEST.json` lists the four substantive files. `SHA256SUMS` also covers that manifest; it omits itself to avoid a circular checksum.
