# Problem 478: critical stochastic SQG with nonlinear noise

This package claims an affirmative resolution of [Problem 478](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/478-critical-stochastic-sqg-global-regularity.md) at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. It is submitted for independent mathematical review.

**Author:** Kaiwen Jin. **Contact:** yui.ui.siki@gmail.com.

Theorem 1.1 of [the manuscript](paper/manuscript.pdf) treats the full stated class: arbitrary deterministic smooth data on the two-dimensional torus and every finite smooth spatial/state-dependent coefficient family satisfying the stated global derivative and Lipschitz bounds. It gives an adapted, pathwise unique global solution continuous in H3 on every finite horizon, with the requested integral identity in H1. The constant mode is retained, and no smallness, affine, additive or zero-mean restriction is added. The [target comparison](TARGET_COMPARISON.md) maps each original requirement to the proof.

The argument combines a fractional stochastic truncation estimate for amplitude, an integrated finite-power spatial-increment estimate, and a dyadic H3 continuation bound. A power-linear convexity remainder allows the spatial exponent to be fixed before the finite power is chosen.

## Files and reproduction

- [Manuscript PDF](paper/manuscript.pdf): complete theorem, proof and references.
- [Standalone LaTeX source](paper/manuscript.tex).
- [Target comparison](TARGET_COMPARISON.md).
- [Public file manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

From `paper/`, build with a standard TeX installation containing `amsart`, `geometry`, `amssymb`, `mathtools`, `microtype` and `hyperref`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
```

The source has no private file inputs. The supplied PDF has 11 pages. Source references and internal PDF destinations were checked, and the rendered pages were inspected. There is no numerical evidence or software theorem claim in this submission.

## Review scope

OpenAI Codex assisted the literature work, mathematical development and checking, and manuscript preparation. The complete draft argument underwent an AI check in the author context, followed by one fresh-context AI reader review and one fresh-context AI referee review of the same frozen manuscript. Both found the same local punctuation defect; it was corrected in the single author revision and verified in the final source and PDF. The referee checked all seven references and their attributed uses and retained no major objection or mathematical gap within its review scope.

These were AI assessments on a shared host, with no physically enforced filesystem isolation. They do not establish human independent review, formal verification, exhaustive novelty, or acceptance by the catalogue maintainers. The author is responsible for the claims and citations. The appropriate submission status is **Solution claimed**, pending independent mathematical review; this package does not change the catalogue status.
