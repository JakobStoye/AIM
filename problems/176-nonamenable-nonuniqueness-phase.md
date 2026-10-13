# 176. A nonuniqueness phase on every nonamenable transitive graph

**Area:** Percolation and network resilience

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`G=(V,E)`$ be infinite, connected, locally finite and vertex-transitive. Assume it is nonamenable, meaning

```math
\inf_{\varnothing\ne K\subset V,\ |K|<\infty}\frac{|\partial_E K|}{|K|}>0,
```

where $`\partial_EK`$ consists of edges with exactly one endpoint in $`K`$. For independent bond percolation, set $`p_c=\inf\{p:\mathbb P_p(\text{an infinite open cluster exists})>0\}`$ and $`p_u=\inf\{p:\mathbb P_p(\text{exactly one infinite open cluster exists})=1\}`$. Must $`p_c<p_u`$?

## Application

A strict gap gives a regime with several macroscopic conducting regions before the network forms one global connected phase.

## References

- [Russell Lyons and Yuval Peres, *Probability on Trees and Networks* (Cambridge, 2016; paperback 2021), online revision of 19 August 2026](https://rdlyons.pages.iu.edu/prbtree/book_pb.pdf), §7.7, Conjecture 7.31; this entry uses its transitive case.
- [Tom Hutchcroft, *Percolation on Hyperbolic Graphs* (2019)](https://doi.org/10.1007/s00039-019-00498-0), a substantial class where the gap is known.
- [Tom Hutchcroft and Minghao Pan, *Percolation at the uniqueness threshold via subgroup relativization* (2024 preprint)](https://arxiv.org/abs/2409.12283), later results about particular group structures and behavior at the uniqueness threshold.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf), result family 214 (2026). Statement locator: `Theorem 1.1, PDF page 3; Introduction theorem label thm:main, introduction.tex lines 58-69; definitions/nonamenability preceding.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem applies to every infinite connected locally finite nonamenable quasi-transitive graph and gives pc<p_(2to2)<=pu. Vertex-transitive AIM graphs are included. Its vertex-boundary nonamenability is equivalent to the AIM edge-boundary form on these uniformly bounded-degree graphs. Definitions of pc/pu agree.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-176) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/214.md). Family214 docs link BenjaminiSchramm/CayleyPercolation statements for the relevant full graph class. Comparator templates alone are not reproduction evidence; no local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/176-nonamenable-nonuniqueness-phase.md).
