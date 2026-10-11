# Exactly trackable boundary heat fluxes

This package contains a complete analytic solution claim for [AIM problem 139, “Sharp characterization of exactly trackable boundary heat fluxes”](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/139-sharp-heat-tracking-range.md), at repository revision c9929805cece044705abaaebe1cebddac1ba11a6. It awaits maintainer and independent mathematical review.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.

- [Complete manuscript](paper/heat_tracking.pdf)
- [Editable LaTeX source](paper/heat_tracking.tex)
- [Original-target comparison](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

Theorem 2.1 characterizes the entire tracking range for every bounded connected smooth Euclidean domain in dimension at least two, every positive finite horizon, and every pair of nonempty relatively open control and observation patches with disjoint closures. It retains arbitrary square-integrable Dirichlet controls and the original zero-initial transposition solution.

The tests use only the target flux and fixed geometry: a Gaussian surface potential, recursively translated Taylor coefficients, absolute weighted sums and overlap equalities, then volume integrability, strong parallel boundary traces, exact input support and full observation compatibility. No control or freely chosen caloric extension is an unknown in the tests. The recovered boundary limit gives the unique control and its exact causal norm.

Theorem 6.1 gives the exact geometry-dependent norm of point evaluation from the separated forward heat-flux kernel. Every fixed target is little-o of that scale at the initial time, and no prescribed further factor tending to zero works for every target. The full tests retain temporal and spatial compatibility; the pointwise bound alone is not a sufficient range criterion.

This is an infinite regularity and compatibility characterization. It does not assert a finite decision procedure, a universal named Sobolev/Gevrey class or a closed distance-and-power asymptotic for arbitrary domains. The proof is analytic and uses no numerical experiments or computer-assisted certificates.

## Build and integrity

The source is standalone, with an inline bibliography. It uses standard LaTeX packages: geometry, amsmath, amssymb, amsthm, microtype, enumitem and hyperref. With TeX Live and latexmk installed, run from this package directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/heat_tracking.tex
    shasum -a 256 -c SHA256SUMS

The supplied PDF has 13 pages. The final source compiled successfully; its references, PDF links, complete page content and every rendered page were inspected. Recompilation may change PDF metadata and bytes. Compilation and checksum verification establish artifact integrity, not mathematical correctness.

The manifest records the four mathematical/documentation payload files. The checksum file also covers the manifest and omits itself to avoid a circular digest.

## AI use and review

OpenAI Codex assisted with literature retrieval, mathematical exploration, proof development, checking and manuscript preparation. A separate Codex session with a fresh context reviewed a frozen preliminary 13-page manuscript and its five cited sources. Its local zero-extension wording objection was corrected. The final version received scoped mathematical, source and rendered-artifact checks, including the additional interval-tracking reference. These are AI checks; no human or formal proof certification is claimed. No separate detailed AI review report is submitted. Independent mathematical review is requested.
