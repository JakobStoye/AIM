# Sequentially private spectral density estimation

Proposed resolution of [AIM problem 507](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/507-interactive-private-spectral-density.md), at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

[The manuscript](paper/main.pdf) proves, in Theorem 1, the proposed joint minimax rate

```math
\mathcal R^{\mathrm{seq}}_{n,\alpha}\asymp
1\wedge(n\alpha^4)^{-2s/(2s+1)},\qquad n\ge2,\quad0<\alpha\le1.
```

The constants depend only on the fixed known parameters $`C_0>1,C_1>0,s>1/2`$. The data are consecutive observations of a centered real stationary Gaussian process in the original variance-bounded class with a Sobolev bound on normalized covariances. A release uses its current raw observation and earlier private outputs, into any standard Borel output space. Thus the proposed result includes privacy parameters that shrink with the sample size. Consistency holds exactly when $`n\alpha^4\to\infty`$; no logarithmic loss is required.

The new lower bound applies to every sequential mechanism in that model. It controls the posterior of a Gaussian innovation through the entire past output history, then combines fresh Gaussian smoothing with contraction by the current private channel. A common independent Gaussian background transfers the bound to neighboring spectral alternatives. The matching non-interactive upper bound is credited to [Issartel and Roueff, arXiv:2608.24847v1](https://arxiv.org/abs/2608.24847v1), Theorem 3; that mechanism is admissible in the sequential class.

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Original-target correspondence](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The argument is analytic. The manuscript contains all new proof steps and cites its external inputs. It uses no numerical experiment, computational certificate or formal proof project.

To compile the source with a standard LaTeX installation, run from `paper/`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

These commands check the document build; they do not certify its mathematics. Verify the delivered bytes from this package root with `shasum -a 256 -c SHA256SUMS`.

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com. OpenAI Codex assisted with developing the argument, checking cited sources and preparing the manuscript. Independent human mathematical verification has not been performed. No separate detailed AI report is submitted; independent mathematical review is requested. This is a complete solution claim awaiting review.
