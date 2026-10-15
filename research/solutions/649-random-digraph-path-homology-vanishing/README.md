# AIM 649: first path homology of a random digraph

The paper claims that the first non-regular path homology over Q of the
independent ordered-edge random digraph vanishes with high probability whenever
`n^2 p^3 / log^4(2n) -> infinity`. In particular this covers `p=n^alpha` for
every fixed `-2/3 < alpha <= 0`.

- [Paper (PDF)](paper/path_homology_vanishing.pdf)
- [Editable LaTeX source](paper/path_homology_vanishing.tex)
- [Comparison with the original problem](TARGET_COMPARISON.md)
- [AI assistance and review disclosure](AI_USE.md)

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.
This is an analytic proof. The argument and external matrix-concentration
input are stated in the paper; no numerical experiment is a proof premise.
Independent mathematical review is requested. A solution claim is not an
upstream acceptance or publication decision.

The critical exponent `alpha=-2/3`, the optimal logarithmic factor, uniform
convergence in alpha, and integral torsion are outside the claim.

## Build

With a LaTeX distribution providing the standard AMS packages, geometry,
microtype and hyperref, run from this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/path_homology_vanishing.tex
```

The source is standalone. The supplied PDF was built with pdfTeX/TeX Live 2025.
`SHA256SUMS` records the supplied files; rebuilding may change PDF metadata
without changing the mathematical text.

## Sources

- [Pinned original AIM statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/649-random-digraph-path-homology-vanishing.md)
- [Chaplin, First Betti number of the path homology of random directed graphs](https://doi.org/10.1007/s41468-022-00108-3)
- [Tropp, User-Friendly Tail Bounds for Sums of Random Matrices](https://doi.org/10.1007/s10208-011-9099-z)
