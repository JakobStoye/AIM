# Polynomial decay for KdV at length 14π

Kaiwen Jin — [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)

This package contains a complete analytic solution claim for [AIM problem 396](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/396-critical-kdv-odd-mode-polynomial-decay.md), frozen at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For the real KdV equation with homogeneous Dirichlet boundary conditions and zero right Neumann datum on (0,14π), Theorem 1.1 proves a common bound

```math
\|y(t)\|_{L^2(0,14\pi)}\le C(1+t)^{-1/2}\qquad(t\ge0)
```

for every sufficiently small real L² datum in the usual energy class. The manuscript allows all stable/undamped mixtures and phases. Its key step is a uniform quadratic boundary observation while retaining resonant motion in the unobserved subspace.

- [Manuscript PDF](paper/manuscript.pdf)
- [Self-contained LaTeX source](paper/manuscript.tex)
- [Comparison with the full original target](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

The proof and bibliography are contained in the TeX file. Build it with a standard LaTeX installation containing the AMS, geometry, lmodern, microtype and hyperref packages:

```sh
cd paper
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

Substantial AI assistance was used in the mathematics, source checks and writing, as disclosed in the paper. Independent mathematical review is requested. This package presents a complete solution claim; repository classification and mathematical acceptance are left to maintainers and reviewers.
