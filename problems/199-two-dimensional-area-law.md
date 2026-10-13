# 199. An area law for general gapped two-dimensional spin systems

**Area:** Quantum many-body theory; entanglement

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Fix an integer $`q\ge2`$ and $`\Delta>0`$. On $`\Lambda=\{1,\ldots,L\}\times\{1,\ldots,M\}`$ put a copy of $`\mathbb C^q`$ at each vertex. Let $`H=\sum_x h_x+\sum_{\{x,y\}\text{ nearest neighbors}}h_{xy}`$ be self-adjoint, with each term supported on its indicated sites and of operator norm at most $`1`$. Assume a unique normalized ground state $`\psi`$ and spectral gap at least $`\Delta`$. For $`1\le\ell<L`$, let $`A=\{1,\ldots,\ell\}\times\{1,\ldots,M\}`$ and $`\rho_A=\mathop{\mathrm{Tr}}\nolimits_{\Lambda\setminus A}|\psi\rangle\langle\psi|`$.

Does a constant $`C(q,\Delta)`$, independent of $`L,M,\ell`$ and the interaction, always satisfy

```math
-\mathop{\mathrm{Tr}}\nolimits(\rho_A\log\rho_A)\le C(q,\Delta)M?
```

## Application

This would justify boundary-sized entanglement as a general structural principle for insulating quantum matter and tensor-network representations of its ground states.

## References

1. Matthew B. Hastings, [An area law for one dimensional quantum systems](https://arxiv.org/abs/0705.2024), *J. Stat. Mech.* (2007), P08024. The main theorem establishes the one-dimensional precedent.
2. Anurag Anshu, Itai Arad, and David Gosset, [An area law for 2D frustration-free spin systems](https://arxiv.org/abs/2103.02492), STOC (2022), preprint revised 2023. Introduction and main-result discussion explicitly distinguish the general open area law from their locally gapped, frustration-free theorem.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf), result family 265 (2026). Statement locator: `build/sections/00-introduction.tex, thm:area and cor:rectangles`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** Set interaction range R=1 and strength J=1. Rectangles and all nearest-neighbor/on-site terms are admitted, with only a unique ground state and a full-system gap. The vertical-cut edge boundary has exactly M edges, yielding C(q,1,1,Delta)M uniformly over L,M,ell and the interactions.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-199) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** No corresponding complete Lean development was identified in the linked family record; no Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/199-two-dimensional-area-law.md).
