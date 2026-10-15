# 111. Unbounded first Steklov multiplicity with fixed boundary count

**Area:** Boundary-mode degeneracy

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

Does there exist a fixed integer $`b\ge1`$ and a sequence of smooth compact connected orientable Riemannian surfaces $`(M_j,g_j)`$, each with exactly $`b`$ boundary components, such that

```math
\dim\{u:\Delta_{g_j}u=0,\ \partial_\nu u=\sigma_1(M_j,g_j)u\}\longrightarrow\infty?
```

Here $`\sigma_1`$ is the first positive eigenvalue of the ordinary, unweighted Steklov problem. The genus and metric may vary; $`b`$ must not vary. Boundary length may be normalized to one by scaling.

## Application

This asks whether arbitrarily many lowest boundary-vibration modes can coincide while the number of boundary components stays fixed, by increasing interior topology.

## References

1. S. Audet-Beaumont, [Constructing surfaces with first Steklov eigenvalue of arbitrarily large multiplicity](https://doi.org/10.4153/S0008439525101288), Canadian Mathematical Bulletin 69 (2026), Remark 1.3: explicit fixed-boundary-count question in the journal version.
2. M. Karpukhin, G. Kokarev and I. Polterovich, [Multiplicity bounds for Steklov eigenvalues on Riemannian surfaces](https://doi.org/10.5802/aif.2918), Annales de l’Institut Fourier 64 (2014), Theorem 1: topological upper bounds.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-111). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-08)

**Literature check:** Open in cited literature; no later resolution located.

Audet-Beaumont proves arbitrarily large first multiplicity when the number of boundary components also grows. Remark 1.3 separates the still-open fixed-count question. Fixed-genus upper bounds explain why the allowed genus must grow, and do not rule out the sequence asked for here.

**Search audit:** “Steklov arbitrarily large multiplicity fixed number boundary components”; “Audet Beaumont Remark 1.3 2026”. Searches included proof, counterexample, and 2025–2026 updates. No later resolution of the stated problem was located; this is a literature review, not a proof of openness.
