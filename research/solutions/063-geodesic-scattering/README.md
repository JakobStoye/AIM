# A variational characterization of geodesic scattering on simple disks

Kaiwen Jin · October 12, 2026 · yui.ui.siki@gmail.com

This package submits a complete analytic solution claim for [AIM 063: Characterizing realizable geodesic scattering data](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/063-range-of-geodesic-scattering.md). Theorem 2.1 gives necessary and sufficient conditions, using only the proposed boundary map and prescribed boundary metric, for realization by a smooth simple Riemannian metric on the fixed disk. It covers the entire open boundary unit cotangent bundle, with no perturbative or genericity assumption.

Boundary action and invariant Fourier traces first determine a normalized conformal boundary coordinate. An always-feasible convex length-majorization problem then selects a unique least-norm density in a strong L2 closure. Smooth positivity, the prescribed boundary trace, explicit geodesic/Jacobi tests and exact area saturation characterize realizability. The proof passes length inequalities through the closure using a family-integrated estimate, then uses strict action-area monotonicity to identify the full scattering map.

The criterion is exact and qualitative. It includes infinitely many curves, smoothness of the selected L2 class and exact ODE and scalar conditions; no finite algorithm or stability estimate is claimed.

## Materials

- [Complete manuscript, 11 pages](paper/geodesic_scattering.pdf)
- [Editable standalone LaTeX source](paper/geodesic_scattering.tex)
- [Comparison with the original target](TARGET_COMPARISON.md)
- [File hashes](SHA256SUMS)

The manuscript contains the complete argument, an exact Euclidean-disk example and five references. Paternain–Salo–Uhlmann supply the geometric and transport results; the variational selection, integrated closure passage, area comparison and fixed-disk transfer are explained in the manuscript. This is a purely analytic contribution; no numerical evidence or formal proof is submitted.

## Build and checks

With a LaTeX distribution providing the packages listed in the source, plus `latexmk` and `make`, run:

```sh
make
make check
```

The rebuilt PDF is `build/geodesic_scattering.pdf`. The supplied PDF was built with pdfTeX 1.40.27 (TeX Live 2025) and latexmk 4.86a. The source is self-contained, including its bibliography, and needs no supplemental files. `make check` verifies the supplied file hashes; it does not verify the theorem. PDF bytes may differ across build dates or TeX installations.

## AI use and review

An OpenAI Codex agent assisted with developing the argument, checking cited source statements and preparing the manuscript. AI-assisted checks and successful typesetting do not establish independent mathematical verification. No separate detailed AI review report is submitted. Independent mathematical review of the complete proof is requested; this package does not assert community acceptance or a formal proof certificate.
