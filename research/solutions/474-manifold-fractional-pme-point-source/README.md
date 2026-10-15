# Point-source fractional porous medium diffusion on manifolds

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This is a complete analytic solution claim for
[AIM 474](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/474-manifold-fractional-pme-point-source.md).
Independent mathematical review is requested.

For every complete connected noncompact manifold of dimension at least two
with a lower Ricci bound and a uniform Euclidean Faber–Krahn inequality,
Theorem 1.1 constructs a nonnegative distributional solution of the spectral
fractional porous medium equation from any positive point mass, for every
exponent m > 1 and fractional order 0 < s < 1. It has strong positive-time
L1 continuity, local boundedness and the prescribed initial trace against
every bounded continuous function. Uniqueness and large-time asymptotics
are separate questions.

- [Complete manuscript](paper/manuscript.pdf)
- [Editable LaTeX source](paper/manuscript.tex)
- [Requirement-by-requirement comparison](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json)
- [SHA256 checksums](SHA256SUMS)

The bounded-data semigroup and smoothing estimate are those of Berchio,
Bonforte, Grillo and Muratori, cited in the manuscript. The additional
argument uses averages of the linear heat semigroup to control spatial
tails, then compactness and nonlinear contraction to pass to a point source.
The Euclidean measure-data work of Grillo, Muratori and Punzo is credited
as background. No numerical or formal proof is asserted.

To build from this directory with a standard TeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/manuscript.tex
```

The source is standalone and requires no supplementary files. The supplied
PDF has seven pages. The source was compiled with TeX Live 2025; all pages,
cross-references and bibliography were inspected. Compilation and layout
checks do not certify the mathematical theorem.

OpenAI Codex assisted proof development, source checks, writing and internal
AI review. One fresh-context AI reader and one fresh-context AI referee
examined the same draft. The final revision clarifies three notation points.
These reviews do not constitute independent human or formal certification.
No separate detailed AI review report is submitted.

This package adds the manuscript and comparison. Catalogue classification
is left to maintainer review; submission does not establish acceptance.
