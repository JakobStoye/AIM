# Failure of joint continuity for fractional-pressure porous-medium flow

Kaiwen Jin · yui.ui.siki@gmail.com

This package submits an analytic counterexample to [AIM problem 467](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/467-fractional-pressure-superquadratic-continuity.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

For every N ≥ 2, m > 2 and 1/2 < s < 1, the manuscript proves that a global bounded energy weak solution with nonzero, nonnegative, bounded integrable compactly supported initial data cannot admit a representative jointly continuous on all of R^N × (0,∞). The equation is

```math
u_t=\nabla\cdot(u^{m-1}\nabla p),\qquad p=(-\Delta)^{-s}u,\qquad \widehat p(\xi)=|\xi|^{-2s}\widehat u(\xi).
```

Existing global existence results supply a solution in the exact energy class. In particular, N = 2, m = 3, s = 3/4 and the indicator of the unit ball give an admissible counterexample to the universal continuity assertion. No claim is made about the complementary range s ≤ 1/2, or the location or type of a discontinuity.

The pressure gradient is bounded in the proved range. A weak moving-halfspace argument shows that joint continuity would prevent the support from expanding after any positive time, because the transport velocity vanishes with the density at vacuum. Positive conserved mass in a fixed bounded support then forces a positive lower bound for the fractional L² dissipation, contradicting its finite integral over all time. Appendix A verifies weak L¹ time continuity and all required energy endpoints for the same constructed global solution.

- [Complete six-page manuscript](paper/main.pdf)
- [Editable, self-contained LaTeX source](paper/main.tex)
- [Comparison with every original requirement](TARGET_COMPARISON.md)
- [Public file manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

From this package directory, build with a standard TeX Live installation and latexmk:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
shasum -a256 -c SHA256SUMS
```

The source needs only the standard LaTeX packages named in its preamble. There are no external figures, bibliography files, private supplements or proof-critical computations. The submitted source was compiled, all six rendered pages were checked, and the bibliographic identities and cited passages were verified. These artifact checks do not constitute formal verification.

OpenAI Codex developed the argument, checked sources and prepared the manuscript. Two fresh Codex contexts separately performed a reader pass and a referee review of the draft; the subsequent revision corrected a citation locator. No separate detailed AI report is submitted. Independent human mathematical review is requested. This package does not change catalogue status or claim upstream acceptance or certified novelty.
