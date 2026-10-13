# 208. Sharp Fourier extension from the sphere in three dimensions

**Area:** Harmonic analysis; monochromatic wave concentration

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\sigma`$ be surface area measure on $`S^2=\{\omega\in\mathbb R^3:|\omega|=1\}`$ and define

```math
Eg(x)=\int_{S^2}e^{2\pi i x\cdot\omega}g(\omega)\,d\sigma(\omega).
```

Is it true that for every $`p>3`$ there exists $`C_p<\infty`$ such that

```math
\|Eg\|_{L^p(\mathbb R^3)}\le C_p\|g\|_{L^\infty(S^2,\sigma)}
```

for every bounded measurable $`g:S^2\to\mathbb C`$? The constant must be independent of the angular amplitude $`g`$.

## Application

The extension operator superposes plane waves at a fixed frequency. The estimate limits how strongly such waves can concentrate throughout three-dimensional space.

## References

1. Shaoming Guo, Changkeun Oh, Hong Wang, Shukun Wu, and Ruixiang Zhang, [The Bochner–Riesz problem: an old approach revisited](https://arxiv.org/abs/2104.11188), *Peking Math. J.* 8 (2025), 201–270. Section 1, Conjecture 1.2, equations (1.4)–(1.5), states this dual restriction formulation.
2. Hong Wang and Shukun Wu, [Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities](https://arxiv.org/abs/2411.08871), preprint (2024). Abstract and principal restriction estimate establish the partial range $`p>22/7`$.
3. Eric T. Sawyer, [A comparison of trilinear testing conditions for the paraboloid Fourier extension and Kakeya conjectures in three dimensions](https://arxiv.org/abs/2411.18457v8), revised 8 February 2026. Current abstract and version history clarify a search result that still displays an earlier full-proof title.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf), result family 077 (2026). Statement locator: `Theorem thm:main`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem states precisely the same S2 extension, phase 2*pi*i*x.omega, surface area measure, complex bounded measurable inputs, and every p>3 with a constant depending only on p. It reaches all remaining exponents. The diagonal positively-curved-surface companion also implies this on S2 by finite-measure embedding.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-208) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/208-sphere-fourier-restriction.md).
