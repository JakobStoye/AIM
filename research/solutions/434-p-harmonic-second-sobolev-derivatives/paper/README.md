# Manuscript

`main.tex` is a self-contained LaTeX article; `main.pdf` is the submitted compiled version. Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

Theorem 1.1 is the full unweighted local second-derivative statement for every finite p >= 5 in R^3. Lemma 2.1 passes through critical points. Section 3 gives signed curvature coercivity and the boundary estimate. Proposition 4.1 gives the epsilon-independent inverse-gradient Hessian estimate, followed by the proof identifying all weak second derivatives. Appendix A proves the smooth critical-value and coarea facts. All nine references are given with public source links and cited locators.

Build from the package root with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex`. No extra manuscript files are required.
