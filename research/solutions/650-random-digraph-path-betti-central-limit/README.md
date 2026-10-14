# Central limit theorem for the first path Betti number

A complete analytic solution claim for [AIM problem 650](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/650-random-digraph-path-betti-central-limit.md).

The manuscript proves the central limit theorem for the rational non-regular first path Betti number of a loop-free random digraph with independent ordered edges, allowing reciprocal pairs, for every sequence with `n p_n -> infinity` and `n^(2/3) p_n -> 0`. It also proves that the variance is asymptotic to `n(n-1)p_n(1-p_n)`. The theorem uses the actual expectation and variance, and does not assume graph connectivity.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

- [Manuscript PDF](manuscript.pdf): complete six-page argument.
- [Editable LaTeX source](manuscript.tex): self-contained source with inline bibliography.
- [Target comparison](TARGET_COMPARISON.md): original clauses and their manuscript locations.
- [AI use and review](AI_USE.md): factual assistance and review limits.
- [References](REFERENCES.md): public source versions and exact cited locations.

The proof bounds squared single-edge changes of the boundary rank using an overcomplete family of triangles, diamonds and paired reciprocal paths, then controls weak-component changes by a fixed-vertex component estimate. The resulting centered correction is negligible relative to the edge-count standard deviation. No numerical data or code is required for the proof.

To rebuild with TeX Live and latexmk:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
```

This package presents a solution claim for independent mathematical review. Catalogue classification is left to the receiving maintainers.

## File integrity

This embedded public manifest lists the five payload files. This README is the manifest container; the fixed Git commit also identifies its bytes. All paths below are relative to this package.

| File | Purpose | SHA-256 |
|---|---|---|
| `AI_USE.md` | AI assistance and review limits | `c7c4f70a216f0a4da276b0e82041c3f3b511f0a1e2a0c19d7d72942393745ce4` |
| `REFERENCES.md` | Public sources and cited locations | `d66d867f69d2531728b6d504b44f81d0d7f62bf0a3b8bf9146c7f358061f9c10` |
| `TARGET_COMPARISON.md` | Full original-target clause map | `e57ced307c181c634e6d54d3d0012619f63f32ae5086f5398dda49d94a353b07` |
| `manuscript.pdf` | Complete six-page manuscript | `ce52cc648f45029a679613290ae0313e1eadf77462fe8ae433852dbe0d0978ac` |
| `manuscript.tex` | Self-contained editable source | `861c49ebe4b27ac26edce06200ab32ca8064a395186fe621212cdfb5760c32f1` |
