# 064 — Global Birkhoff billiard integrability conjecture

**Area:** Hamiltonian dynamics and ray optics

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`D\subset\mathbb R^2`$ be a bounded strictly convex domain with a single $`C^\infty`$ boundary curve and everywhere positive curvature. Its billiard map sends a boundary impact with inward direction to the next impact, using specular reflection. Parameterize the phase annulus by boundary arclength $`s`$ and angle $`\varphi\in(0,\pi)`$ from the positive tangent.

Suppose an open annular neighborhood of the grazing boundary $`\varphi=0`$ is foliated by smooth invariant essential graphs $`\varphi=\varphi_c(s)`$; thus a full neighborhood, including its rational rotation levels, is integrable. Prove that $`\partial D`$ is an ellipse. No assumption that $`D`$ is close to an ellipse or centrally symmetric is allowed.

## Application

This identifies the optical cavities whose near-grazing rays possess a complete family of caustics and avoid chaotic ray transport.

## References

1. Vadim Kaloshin, Comlan Edmond Koudjinan and Ke Zhang, *Birkhoff Conjecture for Nearly Centrally Symmetric Domains*, Geometric and Functional Analysis **34** (2024), 1973–2007. [DOI](https://doi.org/10.1007/s00039-024-00695-6).
2. Illya Koval, *Local Strong Birkhoff Conjecture and Local Spectral Uniqueness of Almost Every Ellipse*, Inventiones Mathematicae **244** (2026), 221–298; online December 2025. [DOI](https://doi.org/10.1007/s00222-025-01397-y).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/paper.pdf), result family 147 (2026). Statement locator: `Theorem 1.1, PDF page 1; Phase-foliation rigidity theorem, introduction.tex lines 17-33, label thm:main; companion Physical-collar rigidity theorem cited as Definition 1.1/Theorem 1.2.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The AIM target assumes a smooth complete foliation of a full grazing annulus, including rational rotation levels. Phase-foliation rigidity permits merely continuous essential individually invariant leaves, for an arbitrary bounded C-infinity strictly convex positive-curvature planar table, and concludes ellipse. The smooth AIM foliation supplies the homeomorphism in the theorem. No closeness or symmetry is added. The physical-collar companion supplies the stated analytic input.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-064) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/064-birkhoff-billiard-integrability.md).
