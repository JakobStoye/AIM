# Connectivity when isolated vertices disappear in a convex polytope

Kaiwen Jin · yui.ui.siki@gmail.com

This package presents a complete analytic solution claim for [AIM 647: Connectivity when the last isolated point disappears in a polytope](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/647-polytopal-connectivity-last-isolated-point.md), at statement revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For every fixed integer d ≥ 3 and every fixed compact convex polytope A in R^d with nonempty interior, take independent uniform sample points. Let L_n be the largest nearest-neighbour distance and M_n the radius at which their closed Euclidean random geometric graph becomes connected. Theorem 1.1 of the manuscript establishes

```math
\lim_{n\to\infty}\Pr(L_n=M_n)=1.
```

The proof uses face territories, cone-ball volume gains and empty collars. A fixed spatial net controls large components simultaneously at all radii above a deterministic lower level. The four probability estimates and the final hitting-time argument are included in the manuscript.

## Materials

- [Complete manuscript](paper/connectivity-polytope.pdf), nine pages.
- [Editable LaTeX source](paper/connectivity-polytope.tex).
- [Target comparison](TARGET_COMPARISON.md), with precise manuscript locations and imported-source scope.
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

## Build and integrity checks

The manuscript is a standalone LaTeX file with an inline bibliography. With a standard TeX installation containing latexmk and the listed standard packages, run from this package directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -no-shell-escape -outdir=build paper/connectivity-polytope.tex
shasum -a 256 -c SHA256SUMS
```

The supplied PDF was built with pdfTeX 1.40.27 (TeX Live 2025) and latexmk 4.86a. Source compilation, resolved references and all PDF pages were checked. Rebuilt PDF bytes may differ because PDF timestamps and TeX versions vary. The checksums bind the supplied files.

## AI use and review

OpenAI Codex assisted in developing and writing the argument and in checking mathematical and bibliographic dependencies. The manuscript contains an AI use statement. No separate detailed AI review report is included in this package. Independent mathematical review is requested; compilation and file integrity checks do not certify the theorem. Catalogue classification remains for the receiving maintainers.
