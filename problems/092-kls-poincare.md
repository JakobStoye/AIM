# 092. The dimension-free Kannan–Lovász–Simonovits inequality

**Area:** High-dimensional probability and sampling

**Status:** 🟠 SOLUTION CLAIMED

**Last checked:** 2026-10-15

## Problem statement

Does there exist a universal constant $`C<\infty`$ such that, for every $`n\ge1`$, every probability density $`e^{-V}`$ on $`\mathbb R^n`$ with convex extended-real $`V`$, mean zero and covariance $`I_n`$, and every smooth compactly supported $`f:\mathbb R^n\to\mathbb R`$,

```math
\mathop{\mathrm{Var}}\nolimits_\mu(f)
:=\int f^2\,d\mu-\left(\int f\,d\mu\right)^2
\le C\int|\nabla f|^2\,d\mu?
```

Extended-real convex potentials include uniform measures on convex bodies. The same $`C`$ must work in all dimensions and for all such densities and functions. This is the Poincaré formulation of KLS.

## Application

A dimension-free spectral gap would strengthen guarantees for sampling log-concave distributions and for concentration in high-dimensional inference.

## References

- [Boaz Klartag and Joseph Lehec, *Isoperimetric inequalities in high-dimensional convex sets* (Bulletin of the AMS, 2025), KLS survey](https://doi.org/10.1090/bull/1869).
- [Brayden Letwin, *The KLS constant is O(log¹⁄⁴ n)* (July 2026), abstract and main result](https://arxiv.org/abs/2607.24164).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf), result family 093 (2026). Statement locator: `Theorem thm:main; subgaussian condition eq:intro-subgaussian`.

## Status review

Reviewed 15 October 2026 against the original target in [PR #170](https://github.com/MColbrook/AIM/pull/170). Claim: affirmative dimension-free Poincare inequality

[Proof or source](https://arxiv.org/pdf/2610.05474v1) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/170-scope-review_141_169.md#aim-092). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Review boundary:** The public source claims the full target. Its complete argument has not received an independent audit here, and a peer-reviewed published resolution was not established by this review; the source-to-target comparison alone is not full proof verification.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Resolution-source report (2026-10-15):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-15-prior-resolutions.md#aim-092). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-10-13)

**Known cases:** A dimension-free logarithmic Sobolev bound gives the required Poincare bound for isotropic log-concave measures with an absolute bound on their linear subgaussian parameter.

**Remaining target:** Obtain a universal bound for arbitrary isotropic log-concave measures without the additional subgaussian restriction.

**Statement comparison:** A dimension-free LSI implies a Poincare bound by linearizing the entropy inequality at a constant. It gives AIM for isotropic log-concave densities whose linear subgaussian parameter a is bounded by a fixed absolute constant; uniform convex-body densities are allowed. General isotropic log-concave measures may have only exponential tails, so the subgaussian assumption is a genuine restriction and cannot be discarded.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-092) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/092-kls-poincare.md).
