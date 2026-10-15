# AIM 376: the zero center-of-mass diffusion limit

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This package presents a proposed affirmative resolution of [AIM problem 376](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/376-fene-vanishing-center-of-mass-diffusion.md) at the stated immutable revision. Theorem 1.1 gives the complete claimed result for all viscosity parameters nu > 0, FENE exponents k > 2, and all initial data in the problem's smooth bounded-positive normalized class on the three-dimensional torus and configuration unit ball.

- [Manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Correspondence with the original problem](TARGET_COMPARISON.md)

The argument conditions on a common spatial Brownian motion before applying nonlinear configuration entropy transforms. It then identifies the stress-work covariance, retains configuration Fisher coercivity under averaging, and propagates a zero normalized density defect. The limiting system keeps the full noncorotational configuration drag and all original fluxes.

To compile the self-contained source with a standard TeX installation and `latexmk`, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The resulting PDF is `build/main.pdf`. The source uses standard LaTeX packages listed in its preamble and has an inline bibliography. There is no proof-critical numerical computation or separate code package.

AI use: OpenAI Codex assisted with developing the argument, checking sources, and writing the manuscript. Fresh Codex AI contexts supplied a reader trace and referee report on the preceding draft; this version incorporates the resulting local corrections. Independent mathematical review is requested. No separate detailed AI review report is submitted. A manuscript build checks the document artifact; catalogue classification and mathematical acceptance remain with the receiving maintainers and reviewers.

`PUBLIC_MANIFEST.json` and `SHA256SUMS` identify the exact selected files in this package.
