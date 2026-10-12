# Smooth real potential uniqueness on a known manifold

Author: **Kaiwen Jin** · [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)

This package presents a complete solution claim for [AIM 051](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/051-potential-on-general-manifold.md), at repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Theorem 1.1 of the [manuscript](paper/main.pdf) states that, on every known compact connected smooth Riemannian manifold of dimension at least three with smooth nonempty boundary, equality of the full ordinary Dirichlet-to-Neumann maps at energy zero determines an arbitrary smooth real potential. Zero must lie outside both Dirichlet spectra. Negative eigenvalues, multiple boundary components and nonorientable manifolds are allowed.

The mixed Green kernel, product continuation, shrinking-sphere transfer and uniform density/coercivity mechanism are adapted from the [OpenAI September 24 preprint](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026) and its [October 5 metric/connection treatment](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026). The scalar application uses nonresonant signed cap gluing, local positive source solutions, the resulting drift equation, and a common-neighborhood argument for all exterior sources. The manuscript proves the auxiliary steps it uses. No claim of a new core continuation method is made.

## Materials

- [Complete manuscript](paper/main.pdf) and [editable LaTeX source](paper/main.tex).
- [Target comparison](TARGET_COMPARISON.md), including theorem and section locations.
- [Public manifest](PUBLIC_MANIFEST.json) and content checksums in `SHA256SUMS`.

## Build and review

The proof is analytic. Its conclusion does not depend on numerical experiments, certificates or a formal proof project.

With a standard TeX installation including `latexmk`, run from this package directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory=build paper/main.tex
```

The source is standalone and contains its bibliography. The supplied PDF has been compiled and inspected page by page. Compilation and checksums validate the artifact, and do not certify the mathematical theorem.

OpenAI Codex assisted with candidate arguments, mathematical and source checks, and exposition. No human or Lean verification is claimed. No separate detailed AI review report is submitted; independent mathematical review is requested. The main theorem is a solution claim awaiting review. Catalogue classification is left to the maintainers.
