# 090. Cardy's crossing formula for square-lattice bond percolation

**Area:** Random media and conformal invariance

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`D\subset\mathbb C`$ be a bounded simply connected smooth domain with four distinct boundary points $`a,b,c,d`$ in counterclockwise cyclic order. On the induced nearest-neighbor graph $`D\cap\delta\mathbb Z^2`$, declare each edge open independently with probability $`1/2`$. Let $`P_\delta`$ be the probability of an open path connecting the lattice approximations of boundary arcs $`ab`$ and $`cd`$; use vertices within $`2\delta`$ of those arcs. Choose a conformal map to the upper half-plane sending $`(a,b,c,d)`$ to $`(0,\eta,1,\infty)`$, with $`0<\eta<1`$. Prove or disprove

```math
\lim_{\delta\downarrow0}P_\delta
=\frac{\Gamma(2/3)}{\Gamma(1/3)\Gamma(4/3)}
\eta^{1/3}\,{}_2F_1(1/3,2/3;4/3;\eta).
```

Here $`\Gamma`$ is the gamma function and $`\,{}_2F_1`$ the Gauss hypergeometric function.

## Application

In a planar random network, the crossing probability measures the chance that two boundary regions remain connected through open bonds. The formula would predict that probability from the large-scale shape alone in the fine-mesh limit, giving an explicit benchmark for connectivity simulations.

## References

- [Vincent Tassion, *Rotation invariance of critical planar percolation* (Séminaire Bourbaki, June 2023, exposé 1210), Conjecture 3.1](https://www.bourbaki.fr/TEXTES/Exp1210-Tassion.pdf).
- [Mikhail Khristoforov, Mikhail Skopenkov and Stanislav Smirnov, *A Generalization of Cardy's and Schramm's Formulae* (Communications in Mathematical Physics, 2025), triangular-lattice setting and references](https://doi.org/10.1007/s00220-025-05255-z).

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/paper.pdf), result family 223 (2026). Statement locator: `Theorem 1.2, PDF page 6; Introduction theorem Cardy's formula, label intro:cardy, lines 235-245; free-boundary definitions lines 222-234 and boundary-transfer discussion immediately after.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The Cardy theorem directly proves actual free-boundary square-lattice bond crossing probabilities with all edges independent at p=1/2, including boundary edges. Uniform marked Jordan approximation includes smooth AIM domains; the buffered boundary comparison transfers between lattice boundary arcs and the AIM O(mesh) boundary-vertex convention. Its beta-integral ratio equals the hypergeometric formula in AIM by the incomplete beta identity with a=b=1/3. This is an explicit crossing theorem, not an inference from the SLE abstract. The Jordan-quad transfer proof (chordal.tex, Proposition jordan:transfer and Corollary jordan:cardy) sandwiches actual edge crossings on a common primal grid between fixed-margin easier/harder quads. The same fixed-margin comparison applies to the smooth-domain induced graph and vertices within2delta of its designated arcs; this last reduction is the reviewer's geometric scope inference from that proof.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-090) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/090-square-bond-cardy-formula.md).
