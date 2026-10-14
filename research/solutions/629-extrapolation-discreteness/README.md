# Discreteness of fixed-parameter extrapolation sets

This package contains Kaiwen Jin's proposed resolution of [AIM problem 629](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/629-extrapolation-discreteness.md), at statement revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Starting from 0 and 1, let Qλ contain exactly the points obtained by finitely many applications of `(a,b) ↦ (1−λ)a + λb`. The manuscript proves, for every complex λ, that Qλ is discrete if and only if λ is an algebraic integer whose other Galois conjugates, apart from λ and its complex conjugate, are real and belong to (0,1). In this case distinct generated points are at least distance 1 apart.

The converse combines integer-polynomial approximation, adjustment within a prescribed residue class, and density of a proper projection of the field embeddings. Fenner, Green and Homer's polynomial characterization and algebraic-integrality theorem are cited dependencies. Campbell's prior result for totally real parameters is credited explicitly.

- [Complete manuscript](paper/extrapolation_discreteness.pdf)
- [Editable LaTeX source](paper/extrapolation_discreteness.tex)
- [Target comparison and dependency locators](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The contribution is an analytic proof. It uses no proof-critical computation, numerical experiment or Lean formalization. Independent mathematical review of the full solution claim is requested; repository classification remains subject to maintainer review.

The manuscript was developed with assistance from OpenAI Codex, including source retrieval and checks of the argument. No separate detailed AI review report is submitted, and no independent human review is claimed. The manuscript contains the AI-use statement and the contact address `yui.ui.siki@gmail.com`.

To compile the editable source, install a LaTeX distribution providing the packages listed in its preamble, then run from the package directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/extrapolation_discreteness.tex
sha256sum -c SHA256SUMS
```

On macOS, `shasum -a 256 -c SHA256SUMS` can be used for checksum verification. The source is self-contained and requires no additional local manuscript files. The delivered PDF was compiled and all five pages, reference destinations and bibliography links were checked. Compilation and layout checks are distinct from mathematical review.
