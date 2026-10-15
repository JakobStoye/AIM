# A lower bound for fast Schrödinger boundary control

**Problem 403 — Solution claimed; independent mathematical review requested.**

For the complex one-dimensional Schrödinger equation on an interval of length L, with an L2 Dirichlet control at the left endpoint and initial data measured in H^-1, the accompanying note proves

```math
C_S(T,L) \ge c_L T^{7/2}\exp\!\left(\frac{L^2}{\pi T}\right),
\qquad 0<T\le \frac{L^2}{2\pi},
```

where c_L is positive and independent of T. Therefore

```math
\liminf_{T\downarrow0} T\log C_S(T,L)\ge L^2/\pi>L^2/4.
```

This gives a negative answer to the proposed coefficient in the [original problem at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/403-schrodinger-sharp-fast-control-exponent.md). It leaves the sharp coefficient and existence of a limit open. The proof uses the necessary moments of one normalized sine state, a centered entire transform, Jensen's formula and an exact finite product.

- [Complete paper](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

## Build

Use a LaTeX distribution with latexmk, pdfLaTeX, amsmath, amssymb, amsthm, lmodern, geometry and hyperref. From this package directory:

```sh
mkdir -p paper/build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=paper/build paper/main.tex
```

The supplied four-page PDF was built from this source, with all pages and reference destinations inspected. The argument is analytic. PUBLIC_MANIFEST.json lists the selected payloads and their hashes; SHA256SUMS also covers that manifest.

## AI assistance and review

OpenAI Codex assisted with literature searches, proof development, calculation checks and drafting. Separate fresh AI contexts checked the complete argument and reviewed the manuscript, including a source-order reader review and a referee review of the same frozen draft. These were same-vendor reviews on a shared host, with no verified operating-system isolation. Independent human mathematical review is requested. The author is responsible for the submitted claims.
