# A counterexample to degree-zero universality

Kaiwen Jin, 13 October 2026.

For every field, the paper constructs a bounded pseudometric on all
four-parameter persistence-module isomorphism classes that is stable under
uniform perturbations of ordinary degree-zero sublevel homology. A pair
realized on a three-point discrete space has interleaving distance 1 and
the constructed stable distance 3.

The finite free-module example and its inverse matrices are due to
H. B. Bjerkevik, arXiv:1609.02086v3, Examples 5.2--5.3. The supplement proves
that eventual-component supports are intrinsic and uses them to define the
required stable distance for all inputs. The arbitrary-field positive-degree
universality question remains outside this result.

- [Complete paper (PDF)](paper/interleaving_counterexample.pdf)
- [Editable LaTeX source](paper/interleaving_counterexample.tex)
- [Comparison with the exact AIM 494 target](TARGET_COMPARISON.md)

This is a proposed counterexample awaiting independent mathematical review.
The paper states the actual AI assistance and review scope.

## Reproduction

The proof is self-contained symbolic linear algebra and a set-colimit
argument. The birth vectors, matrices, and distance tables are all printed
in Section 4. A LaTeX installation with `latexmk`, `amsmath`, `amssymb`,
`amsthm`, `geometry`, `lmodern`, `microtype`, and `hyperref` builds the paper:

```sh
mkdir -p build
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/interleaving_counterexample.tex
```

The supplied PDF was built with pdfTeX 1.40.27 (TeX Live 2025), using
latexmk 4.86a. The document uses an embedded bibliography and needs no
external data or supplementary proof files.

`PUBLIC_MANIFEST.json` records the four content files and their SHA-256
hashes. `SHA256SUMS` covers those files and the manifest, excluding itself:

```sh
shasum -a 256 -c SHA256SUMS
```
