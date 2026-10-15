# Maximal topological complexity of aspherical connected sums

Kaiwen Jin · [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com)

This package submits a complete solution claim for [AIM 514](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/514-aspherical-connected-sum-complexity.md). Theorem 1.1 asserts that every pair of closed, connected, oriented aspherical manifolds of the same dimension n >= 3 satisfies ordinary unreduced TC(M#N) = 2n+1. The connected sum itself is not assumed aspherical.

- [Complete manuscript](paper/aspherical-connected-sums.pdf)
- [Editable LaTeX source](paper/aspherical-connected-sums.tex)
- [Comparison with the full original target](TARGET_COMPARISON.md)
- [Payload manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The proof uses the diagonal-cover join and a decomposition of its nonfree cells into factor and cyclic coset blocks. The Borel homology of those blocks contributes only the same-factor products in degree 2n. The ordered mixed fundamental-class products survive in orbit homology, contradicting a planner with 2n domains. The paper prints the full argument and credits its cited sources.

To build the manuscript, use latexmk and a LaTeX installation providing the packages declared in the source (including lmodern, geometry, amsmath, amssymb, amsthm, mathtools, tikz-cd, microtype and hyperref):

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/aspherical-connected-sums.tex
shasum -a 256 -c SHA256SUMS
```

The included PDF was compiled and its seven pages were inspected. Compilation and file integrity are artifact checks; the mathematical evidence is the argument printed in the manuscript. This is a theoretical submission with no numerical or Lean component.

AI use: OpenAI Codex assisted with literature retrieval, mathematical development, checking and manuscript preparation. Fresh-context Codex checks covered a complete manuscript draft, its citations, sequential reading and qualitative style. The authoring agent reconciled that feedback, made two exposition repairs and checked the final changes. These checks shared the workspace and were not human review or Lean verification. No separate detailed AI report is submitted. Independent mathematical review is requested. Catalogue classification remains subject to maintainer review.
