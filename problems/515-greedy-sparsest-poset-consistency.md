# 515. Consistency of the Greedy Sparsest Poset algorithm

**Area:** Statistical inference and causal discovery

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`P`$ be a distribution of observed variables $`(X_i)_{i\in V}`$, with $`V`$ finite. A directed maximal ancestral graph (DMAG) on $`V`$ has directed and bidirected edges, at most one edge per pair, no directed cycles, and no directed path between endpoints of a bidirected edge. Maximality means that every nonadjacent pair can be separated as follows. A path is $`m`$-connecting given $`S`$ if each internal noncollider is outside $`S`$ and each internal collider has a directed descendant in $`S`$, allowing itself as a descendant. A collider has two arrowheads pointing into it along the path. Absence of such a path defines $`m`$-separation. Write $`I(H)`$ for the conditional independences encoded by this separation rule; two DMAGs are Markov equivalent when their $`I(H)`$ agree.

Assume $`P`$ is Markov and restricted-faithful to a DMAG $`G^*`$. Markov means every separation in $`I(G^*)`$ is a conditional independence of $`P`$. Restricted faithfulness requires conditional dependence whenever a pair is $`m`$-connected given $`S\subseteq V\setminus\{i,j\}`$ and is either adjacent, the endpoints of a length-two path in the skeleton, or the endpoints of a discriminating path. A discriminating path for $`k`$ has form $`\langle i,\ldots,k,j\rangle`$, at least three edges, nonadjacent endpoints, and every vertex strictly between $`i`$ and $`k`$ is both a collider on the path and a parent of $`j`$.

For a partial order $`\pi`$ on $`V`$, set

```math
D_\pi(i,j)=\{v:v\le_\pi i\text{ or }v\le_\pi j\}\setminus\{i,j\}.
```

Construct $`A(\pi,P)`$ by placing an edge between $`i,j`$ exactly when $`X_i`$ and $`X_j`$ are conditionally dependent given $`X_{D_\pi(i,j)}`$. Orient it from the smaller to the larger vertex if comparable, and bidirect it otherwise. Let $`\mathop{\mathrm{po}}\nolimits(H)`$ be the partial order of directed ancestry, including equality, and define

```math
G_\pi=\mathop{\mathrm{cl}}\nolimits_{\mathrm{ma}}\left(A\bigl(\mathop{\mathrm{po}}\nolimits(A(\pi,P)),P\bigr)\right).
```

The operator $`\mathop{\mathrm{cl}}\nolimits_{\mathrm{ma}}`$ denotes the maximal ancestral closure: add edges between pairs that cannot be $`m`$-separated, preserving the separation model and ancestral orientations. Thus both the second application of $`A`$ and the closure are part of the definition.

Form a directed search graph with vertices the distinct graphs $`G_\pi`$. From $`H`$ allow a move to $`G_{\mathop{\mathrm{po}}\nolimits(H')}`$ whenever $`H'`$ comes from $`H`$ by changing one edge $`i\to j`$ to $`i\leftrightarrow j`$, or conversely, with $`H'`$ still a DMAG Markov equivalent to $`H`$. These are the legitimate mark changes.

Prove or refute that every starting vertex $`H_0`$ has a directed path $`H_0,H_1,\ldots,H_r`$ in this search graph satisfying

```math
|E(H_{t+1})|\le |E(H_t)|,\qquad |E(H_r)|=\min_\pi |E(G_\pi)|.
```

The number being minimized is the number of graph edges. This is the oracle consistency conjecture for Greedy Sparsest Poset (GSPo) with sufficiently large search depth. It does not prescribe a fixed depth or a polynomial running time.

## Application

Unobserved common causes can make ordinary directed acyclic models of measured variables inadequate. DMAGs represent the resulting conditional independence information. This question asks whether a concrete search procedure can reliably recover the identifiable causal equivalence class when exact independence information is available, providing a foundation for its statistical implementation.

## References

1. D. I. Bernstein, B. Saeed, C. Squires and C. Uhler, [Ordering-Based Causal Structure Learning in the Presence of Latent Variables](https://proceedings.mlr.press/v108/bernstein20a.html), PMLR **108**, 4098–4108 (2020), §§2–4, especially Conjecture 1 and Algorithm 2. [Primary PDF](https://proceedings.mlr.press/v108/bernstein20a/bernstein20a.pdf); [arXiv:1910.09014v2](https://arxiv.org/abs/1910.09014v2).
2. C. Squires and C. Uhler, [Causal Structure Learning: A Combinatorial Perspective](https://doi.org/10.1007/s10208-022-09581-9), Foundations of Computational Mathematics **23**, 1781–1815 (2023), §4.4, p.1803.
3. J. Zhang and P. Spirtes, [A transformational characterization of Markov equivalence for directed acyclic graphs with latent variables](https://www.cmu.edu/dietrich/philosophy/docs/spirtes/uai05.pdf), UAI (2005), Lemma 1 and §2.2.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/515-gspo-counterexample/paper/counterexample.pdf) establishes the full original target. Complete counterexample for restricted-faithfulness original GSPO search.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/515-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #73](https://github.com/MColbrook/AIM/pull/73) at `6c47f2a0345e5b51292a7ff5b7590a7c7be5ecac`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
