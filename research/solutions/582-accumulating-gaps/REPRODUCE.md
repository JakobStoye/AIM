# Build and verify the manuscript

The submitted result is analytic. Its complete proof and exact public dependencies are in `paper/main.tex` and `paper/main.pdf`. No numerical result, formal proof, or computational certificate is required for the claim.

## Build

From the package directory, use a TeX installation containing pdfLaTeX and latexmk:

```sh
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The source uses standard packages: fontenc, lmodern, amsmath, amssymb, amsthm, geometry, microtype, tikz, xurl and hyperref. The screen schematic is inline TikZ; the bibliography is inline. No external source file or image is needed.

The supplied PDF was built with pdfTeX 1.40.27 (TeX Live 2025) and latexmk 4.86a. It has 8 pages. PDF timestamps and TeX versions can change its bytes without changing the source or mathematical content; the supplied file is identified by its exact hash.

## Package integrity and checks

On macOS:

```sh
shasum -a 256 -c SHA256SUMS
```

On systems with GNU coreutils:

```sh
sha256sum -c SHA256SUMS
```

The source was compiled successfully and all rendered pages inspected. The checks covered displayed equations, theorem references, the figure, author/contact, bibliography and end AI-use disclosure. They check the artifact and source-to-target correspondence; independent mathematical review remains requested.

The complete theorem is Theorem 1.1, with its closing proof in Section 4. Its admissible geometry is Lemma 1.2; the harmonic mode is in Lemmas 2.1–2.3; charge regularity is in Lemmas 3.1–3.2; equation (20) identifies the original Helmholtz operator.
