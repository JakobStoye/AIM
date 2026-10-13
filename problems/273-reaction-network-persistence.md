# 273. No asymptotic extinction in bounded weakly reversible mass-action kinetics

**Area:** Deterministic chemical reaction networks

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`\mathcal R`$ be a finite set of reactions $`y\to y'`$ in $`\mathbb N_0^d`$, each lying on a directed cycle of the complex graph, and fix positive reaction constants $`\kappa_{y\to y'}`$. Consider $`\dot x=\sum_{y\to y'\in\mathcal R}\kappa_{y\to y'}x^y(y'-y)`$ with $`x(0)\in(0,\infty)^d`$ and $`x^y=\prod_i x_i^{y_i}`$. For every solution defined and bounded on $`[0,\infty)`$, must $`\liminf_{t\to\infty}x_i(t)>0`$ for every species $`i`$? No complex-balance assumption is permitted.

## Application

A proof would rule out eventual loss of a chemical species solely from the network’s cycle structure, within bounded concentration regimes.

## References

- [Manoj Gopalkrishnan, Ezra Miller and Anne Shiu, *A geometric approach to the Global Attractor Conjecture* (2014)](https://people.tamu.edu/~annejls/geometricGAC.pdf), Conjecture 4.4.
- [Gheorghe Craciun, *Polynomial Dynamical Systems, Reaction Networks, and Toric Differential Inclusions*, SIAM Journal on Applied Algebra and Geometry (2019)](https://people.math.wisc.edu/~craciun/PAPERS_NEW/1_SIAG_Feb_2018_Revision_3.pdf), §2.2, persistence and permanence questions.
- [Praneet Nandan, Philippe Nghe and Jérémie Unterberger, *Autocatalytic cores in the diluted regime: classification and properties*, Journal of Mathematical Biology (2026)](https://link.springer.com/article/10.1007/s00285-026-02357-7), §4.2.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/permanence.pdf), result family 149 (2026). Statement locator: `Theorem 1.1, PDF page 2; Main theorem label thm:main, introduction.tex lines 43-60; epsilon_P bounds in equation eq:uniform-bounds.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Uniform permanence holds for every finite weakly reversible mass-action network with fixed positive reaction rates and every positive initial state, with a classwise compact absorbing set contained in the strictly positive orthant. The eventual positive lower bound implies each AIM bounded global trajectory has positive liminf for every species; complex balance is not imposed. The theorem is stronger than the target because it also ensures global bounded positive solutions.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-273) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/149.md). Family149 Lean docs concern the September boundedness/persistence article, giving initial-state-dependent all-time bounds rather than classwise uniform October permanence. This is nevertheless sufficient for AIM273. MassAction comparator main statement uses sorry; no local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/273-reaction-network-persistence.md).
