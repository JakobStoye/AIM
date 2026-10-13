# 323. Strong thin-tree conjecture

**Area:** Network design and combinatorial optimization

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`G=(V,E)`$ be a finite undirected loopless multigraph with at least two vertices. Parallel edges are counted separately. For a nonempty proper set $`S\subsetneq V`$, write $`\delta_G(S)`$ for the edges with exactly one endpoint in $`S`$. For an integer $`k\ge1`$, call $`G`$ $`k`$-edge-connected if $`|\delta_G(S)|\ge k`$ for every such $`S`$.

Does there exist an absolute constant $`C>0`$ such that every $`k`$-edge-connected $`G`$, for every $`k\ge1`$, has a spanning tree $`T\subseteq E`$ satisfying

```math
|T\cap\delta_G(S)|\le\frac{C}{k}\,|\delta_G(S)|
\qquad\text{for every }\varnothing\ne S\subsetneq V?
```

The same tree must satisfy every cut inequality, and $`C`$ must be independent of $`k`$, $`G`$ and $`|V|`$. Edges are unweighted. This is the strong thin-tree conjecture; the question requires existence, without an efficient construction or verification algorithm. Goddyn's weaker version permits an arbitrary thinness bound tending to zero with connectivity. It is included here as context, without a separate count or a claim of equivalence. [1, 2]

## Application

A spanning tree supplies a connected backbone in a communication or transport network. Thinness limits the fraction of available links that this backbone uses across every partition of the network. A positive answer would also guarantee that, when $`k>C`$, removing the tree leaves edge connectivity at least $`k-C`$: every remaining cut has at least $`(1-C/k)|\delta_G(S)|`$ edges. This connects the conjecture to preserving network redundancy while reserving a connected subnetwork. [1]

Thin trees also support rounding arguments for asymmetric routing. An existence theorem would provide a constant integrality bound for the directed traveling-salesman relaxation; a corresponding efficient construction would yield an approximation algorithm. Constant bounds for that routing problem already exist by other methods. This connection does not establish the sharp factor two asked for in [entry 313](312-asymmetric-tsp-integrality-gap.md). [1, 2]

## References

1. Nathan Klein, Neil Olver and Zi Song Yeoh, *Thin Trees for near Minimum Cuts*, ICALP 2026, LIPIcs 374, 129:1–129:18, published July 1, 2026, [DOI and publication record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2026.129). [Full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.129/LIPIcs.ICALP.2026.129.html), §1, Theorems 1–2 and §2.1.
2. Nima Anari and Shayan Oveis Gharan, *Effective-Resistance-Reducing Flows, Spectrally Thin Trees, and Asymmetric TSP*, FOCS 2015, 20–39. Accessible [arXiv:1411.4613v4](https://arxiv.org/html/1411.4613v4), revised September 1, 2015: Definition 1.1, Theorem 1.2, discussion after Conjecture 1.3, §1.1 and Corollary 1.8.
3. Alice Moayyedi, *Thin Tree Verification is coNP-Complete*, [arXiv:2512.25043v1](https://arxiv.org/html/2512.25043v1), December 31, 2025, preprint, §1 Conjecture 1, Theorem 1 and Remark 1.
4. Mohit Daga, *Thin Trees via k-Respecting Cut Identities*, [arXiv:2510.12050v1](https://arxiv.org/html/2510.12050v1), October 14, 2025, preprint, §1.3 and Theorems 2.1–2.5.
5. Alireza Haqi and Shayan Oveis Gharan, *On Thin Perfect Matchings up to Polylogarithmic Factors*, [arXiv:2606.01330v2](https://arxiv.org/html/2606.01330v2), revised July 1, 2026, preprint, Lemma 1.2 and Theorems 1.3–1.4.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf), result family 174 (2026). Statement locator: `Theorem 1.1, PDF page 1; Main theorem label thm:main, source/sections/introduction.tex lines 17-28.`.

## Status review

**Resolution:** The linked OpenAI manuscript reports a complete affirmative resolution of the original target.

**Statement comparison:** The theorem quantifies one absolute C>0 over every integer k>=1 and every finite loopless k-edge-connected multigraph with >=2 vertices, counts parallel edges separately, and selects one spanning tree satisfying every nontrivial cut inequality C/k simultaneously. The efficient companion exceeds AIM's existence requirement.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-323) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/174.md). StrongThinTree comparator models edges by separate labels and states exactly the all-cut universal-constant result; declaration uses sorry. AlgorithmicThinTrees is additional. No local verification claimed. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/323-strong-thin-tree.md).
