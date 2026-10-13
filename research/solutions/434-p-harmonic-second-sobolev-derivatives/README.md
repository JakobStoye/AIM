# Second-order Sobolev regularity of three-dimensional p-harmonic functions

This package supplies a proposed affirmative resolution of [Problem 434](../../../problems/434-p-harmonic-second-sobolev-derivatives.md) at AIM revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

For every finite real **p >= 5**, every open **Omega subset R^3**, and every real weak **u in W^{1,p}_loc(Omega)** solving **div(|Du|^{p-2} Du) = 0**, the manuscript proves **u in W^{2,2}_loc(Omega)**. All nine unweighted second distributional derivatives are locally square integrable, including every critical-point neighborhood. No sign, symmetry, nonvanishing-gradient or critical-set assumption is added. Constants may depend on fixed p.

The proof controls the inverse-gradient Hessian energy of smooth regularized solutions. A signed Gaussian-curvature correction supplies pointwise coercivity; Gauss--Bonnet and boundary-curve total curvature give an integrated bound, and radial iteration makes it uniform in the regularization parameter. Uniform gradient bounds and distributional testing then give the unweighted conclusion. The manuscript contains the complete argument, including the critical-point passage and smooth coarea facts.

- [Complete manuscript PDF](paper/main.pdf)
- [Standalone LaTeX source](paper/main.tex)
- [Exact target comparison](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json)

## Build and file verification

From this package directory, with a standard TeX distribution containing the listed LaTeX packages:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
shasum -a 256 -c SHA256SUMS
```

The selected source has no external figure, bibliography or private file input. Development used TeX Live 2025 and latexmk 4.86a. Rebuilding reproduces the mathematical document; PDF metadata and bytes can depend on build time and TeX versions. The manifest hashes identify the submitted source and PDF. Hash checks validate file integrity, not mathematical correctness. No numerical computation or formal proof artifact is a premise.

## Authorship, assistance and review

Manuscript author: **Kaiwen Jin**, contact **yui.ui.siki@gmail.com**. AI assistance was used for proof development, source checking, mathematical checking and writing; the manuscript includes an AI-use statement. The submission requests independent mathematical review. No maintainer acceptance or human review is asserted.

The package credits the problem collection [AIM -- Open Applied Problems](https://github.com/MColbrook/AIM), curated by Steve Brunton, Matthew J. Colbrook, Maarten V. de Hoop, George Stepaniants, Alex Townsend and Rachel Ward (2026), and cites the mathematical sources in the manuscript. The source problem is pinned to the revision above so that later catalogue renumbering does not change the target.
