# Proposed solution to AIM problem 193

This package contains an analytic proof of the full Gaussian three-dimensional
moment-spectrum statement in [AIM problem 193](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/193-directed-polymer-moment-spectrum.md).
It is submitted as a proposed solution for independent mathematical review.

For simple random walk from zero on Z^3 with iid standard Gaussian disorder,
the paper proves that the exponent of moments bounded uniformly in the polymer
length is a continuous strictly decreasing bijection from (0, beta_c] onto
[5/3, infinity), using the original weak-disorder critical point. Continuity
at beta_c is from the left. No boundedness at the threshold moment order is
asserted.

- [Manuscript](paper.pdf)
- [Editable LaTeX source](paper.tex)
- [Original-target comparison](TARGET_COMPARISON.md)

The high-moment argument uses the joint terminal partition-function field and
a concave power of its p-moment. Its Jensen deficit and its Gaussian variance
perturbation contain the same endpoint overlap, giving one moment bound for
all lengths. The Gaussian comparison and the critical/one-sided continuity
results are credited to their precise sources in the paper.

The result is purely analytic and uses no numerical or proof-critical
computation. To compile the standalone source, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
```

The source requires a standard LaTeX distribution with AMS, geometry,
lmodern, microtype and hyperref packages. Build checks and rendered-page checks
establish document consistency; they are not mathematical certification.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.
OpenAI Codex was used extensively in developing the argument, checking sources,
preparing the manuscript and providing internal reader and referee feedback. Independent mathematical review is requested;
no separate detailed AI review report is included in this package.
