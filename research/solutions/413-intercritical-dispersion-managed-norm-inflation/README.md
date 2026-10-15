# AIM 413: norm inflation for the defocusing quintic averaged equation

**Author:** Kaiwen Jin. **Contact:** yui.ui.siki@gmail.com.

This note gives an affirmative solution claim for [AIM 413](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/413-intercritical-dispersion-managed-norm-inflation.md), at statement revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For every positive epsilon, Theorem 1.1 constructs Schwartz data on R3 with homogeneous H^(1/4) norm below epsilon and a global smooth solution whose norm exceeds epsilon^(-1) at a nonzero negative time of absolute value below epsilon. The equation has exactly the defocusing sign and the averaging interval [0,1] in the problem statement. Corollary 3.1 gives the explicit concentrated Gaussian family and quantitative norm and time bounds.

- [Paper (PDF)](paper/main.pdf)
- [Editable standalone LaTeX source](paper/main.tex)
- [Comparison with the complete original target](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

Build the source with `latexmk -pdf main.tex` from the `paper` directory. The delivered PDF was built with pdfTeX1.40.27 (TeX Live2025) and latexmk4.86a. The proof is analytical and does not rely on numerical experiments or a formal proof project.

OpenAI Codex assisted the exploration, algebraic checks, writing and review. The argument was checked in the authoring context, followed by one separate fresh Codex reader and one separate fresh Codex referee on the same frozen draft. Reviews covered the mathematical argument before one local terminology revision. The final source and PDF were checked again. These were AI reviews; no independent human review is represented. No separate detailed AI report is submitted, and independent mathematical review is requested. Public submission is a solution claim, not evidence of maintainer acceptance.
