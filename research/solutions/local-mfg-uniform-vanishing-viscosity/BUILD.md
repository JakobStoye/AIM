# Build and integrity checks

The manuscript is a standalone LaTeX document. A standard TeX installation with `latexmk` and `pdflatex` is sufficient. It uses the article class and the geometry, fontenc, lmodern, amsmath, amssymb, amsthm, microtype and hyperref packages; there are no external source files, images or bibliography database.

From this package's root:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The rebuilt PDF is `build/main.pdf`. The supplied reviewed document is `paper/main.pdf`, twelve pages. The source was compiled with TeX Live 2025, pdfTeX 1.40.27 and latexmk 4.86a. Its final log has no unresolved references, duplicate labels, missing assets or material box warnings. All twelve rendered pages were read and visually inspected after the final revision.

To check the supplied file bytes on macOS:

```sh
shasum -a 256 -c SHA256SUMS
```

On a platform providing `sha256sum`:

```sh
sha256sum -c SHA256SUMS
```

`SHA256SUMS` covers the manuscript, documentation and `PUBLIC_MANIFEST.json`; it excludes itself to avoid a circular digest. The public manifest lists the five content files and their purposes. A rebuild can change PDF creation metadata and byte hashes while preserving content, so these checksums identify the supplied snapshot rather than every future compilation.

These are document and package integrity checks. The analytic proof is in the manuscript and its cited public dependencies; mathematical acceptance requires review of that argument.
