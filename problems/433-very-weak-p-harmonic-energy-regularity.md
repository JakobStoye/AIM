# 433. A nonlinear Weyl lemma at the minimal p-harmonic integrability threshold

**Area:** Degenerate elliptic PDEs and nonlinear potential theory

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16
## Problem statement

Let $`d\ge3`$, $`p>2`$, and $`\Omega\subset\mathbb R^d`$ be open. If $`u\in W^{1,p-1}_{\mathrm{loc}}(\Omega)`$ satisfies

```math
\int_\Omega |\nabla u|^{p-2}\nabla u\cdot\nabla\varphi\,dx=0\qquad(\varphi\in C_c^\infty(\Omega)),
```

must $`u\in W^{1,p}_{\mathrm{loc}}(\Omega)`$? Equivalently, must this distributional solution have a representative that is an ordinary weak p-harmonic function? The endpoint assumption ensures integrability of the flux but does not assume finite p-energy.

## Application

Nonlinear conduction laws naturally provide flux information before energy bounds. This question determines whether distributional stationary states automatically enter the usual finite-energy theory.

## References

1. P. Lindqvist, [Notes on the p-Laplace Equation](https://jyx.jyu.fi/bitstreams/2a8cbc94-58e9-4e75-94d6-0f1f5bc22ac1/download), second edition, University of Jyväskylä Report 161 (2017), §11, p. 93, “Very Weak Solutions.”
2. J. L. Lewis, [On very weak solutions of certain elliptic systems](https://doi.org/10.1080/03605309308820984), *Communications in PDE* **18** (1993), 1515–1537, higher-integrability results.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-433). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-22)

**Literature check:** Open in cited literature; no later resolution located.

Lindqvist distinguishes the endpoint p−1 from the known p−epsilon theory. Searches for endpoint very weak p-harmonic regularity and 2025–2026 higher-integrability results found no theorem reaching this endpoint for all p and dimensions. Results for general elliptic systems with additional integrability do not settle the scalar endpoint.
