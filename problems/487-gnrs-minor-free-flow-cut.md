# 487. The GNRS conjecture for minor-free network flow

**Area:** Network routing, metric geometry and combinatorial optimization

**Status:** 🟡 PARTIAL

**Last checked:** 2026-10-13

## Problem statement

A graph contains $`H`$ as a *minor* if a sequence of edge contractions and edge or vertex deletions produces $`H`$. Fix any finite simple graph $`H`$. Let $`G=(V,E)`$ range over finite connected undirected simple graphs that contain no $`H`$ minor. Give its edges arbitrary nonnegative lengths $`\ell:E\to[0,\infty)`$, and let $`d_\ell(u,v)`$ be shortest-path distance. Distinct vertices may have distance zero.

Does there exist a finite constant $`C_H\ge1`$, depending only on $`H`$, such that for every such $`(G,\ell)`$ there are an integer $`m\ge1`$ and a map $`f:V\to\mathbb R^m`$ satisfying

```math
d_\ell(u,v)\le\|f(u)-f(v)\|_1\le C_Hd_\ell(u,v)
\qquad\text{for every }u,v\in V,
```

where $`\|z\|_1=\sum_{j=1}^m|z_j|`$? The dimension and map may depend on the weighted graph. The constant must be independent of its size and length assignment. Zero-distance vertices may share an image. This is the Gupta–Newman–Rabinovich–Sinclair (GNRS) conjecture. [1, 2]

An equivalent formulation concerns fractional network routing. On such a supply graph $`G`$, choose finite nonnegative capacities $`c_e`$ and demands $`D_{uv}`$ for unordered pairs $`\{u,v\}\in\binom{V}{2}`$, with at least one positive demand. Let $`\mathcal P_{uv}`$ be the set of simple paths joining $`u`$ and $`v`$. Define $`\lambda^*`$ as the maximum $`\lambda\ge0`$ for which nonnegative real path weights $`x_{uv,P}`$ satisfy

```math
\begin{aligned}
\sum_{P\in\mathcal P_{uv}}x_{uv,P}&\ge\lambda D_{uv}
&&\text{for every }\{u,v\}\in\binom{V}{2},\\
\sum_{\{u,v\}\in\binom{V}{2}}\ \sum_{\substack{P\in\mathcal P_{uv}\\e\in P}}x_{uv,P}&\le c_e
&&\text{for every }e\in E.
\end{aligned}
```

Thus every demand receives the same multiplier, and traffic may split across paths. For a vertex set $`S`$, let $`\delta_G(S)`$ be the edges with exactly one endpoint in $`S`$, and set

```math
D(S)=\sum_{\substack{\{u,v\}\in\binom{V}{2}\\|\{u,v\}\cap S|=1}}D_{uv},
\qquad
\Phi=\min_{\substack{S\subseteq V\\D(S)>0}}
\frac{\sum_{e\in\delta_G(S)}c_e}{D(S)}.
```

Every cut bounds the routable multiplier from above. The equivalent conjecture asks for

```math
\frac{\Phi}{C_H}\le\lambda^*\le\Phi
```

for every capacity and demand assignment. This formulation also covers $`\Phi=0`$ without dividing by $`\lambda^*`$. The demand pairs are arbitrary; only the supply graph excludes $`H`$. No integral or single-path routing is required. The equivalence holds after taking the worst case over length assignments and, respectively, capacity and demand assignments on the same graph. [1, Theorem 3.2; 2, Theorem 1.1; 3, §19.1]

## Application

In a communication network, edge capacities limit link traffic while many source–destination pairs compete for those links. A cut gives a necessary bottleneck bound: traffic crossing a partition cannot exceed its total link capacity. GNRS asks whether network topology alone makes these bounds sufficient up to a constant loss in every demanded transfer rate. It would provide a uniform comparison between bottleneck certificates and achievable fractional throughput for planar networks and other networks excluding a fixed minor. [1–3]

The associated sparsest-cut relaxation is used to find network partitions and analyze routing and layout algorithms. The constant is uniform as a network grows within the chosen graph class; an arbitrary size-dependent bound would not give that guarantee. This is an idealized capacitated-flow model and does not include interference, packet deadlines or queueing delay. [1, 2]

## References

1. Anupam Gupta, Ilan Newman, Yuri Rabinovich and Alistair Sinclair, *Cuts, Trees and ℓ1-Embeddings of Graphs*, Combinatorica **24** (2004), 233–269, [publisher record](https://link.springer.com/article/10.1007/s00493-004-0015-x). The accessible [author manuscript](https://people.eecs.berkeley.edu/~sinclair/cuts.pdf), dated October 22, 2002, gives the definitions in §2, Theorem 3.2 and the unnumbered conjecture in §3, internal pp.7–8; restricted results in Theorems 4.1 and 4.8.
2. James R. Lee and Anastasios Sidiropoulos, *On the Geometry of Graphs with a Forbidden Minor*, STOC 2009, 245–254. [Author-hosted proceedings text](https://people.csail.mit.edu/tasos/papers/geoforbid_stoc2009.pdf), §1, Theorem 1.1, Conjectures 1–3 and Theorems 1.4 and 1.8.
3. Chandra Chekuri, *CS 583: Approximation Algorithms*, [lecture notes](https://courses.grainger.illinois.edu/CS583/sp2026/approx-algorithms-lecture-notes.pdf), May 4, 2026; Chapter 19, pp.248–252 and bibliographic notes p.267.
4. Arnold Filtser, *A Face Cover Perspective to ℓ1 Embeddings of Planar Graphs*. [Revised author manuscript, arXiv:1903.02758v4](https://arxiv.org/html/1903.02758v4), July 28, 2024; preliminary version SODA 2020. §1, Theorem 1 and Corollaries 1–2; §2 definitions. Journal DOI 10.1145/3686800; the inspected full text is the arXiv version.
5. Nikhil Kumar, *An Approximate Generalization of the Okamura–Seymour Theorem*, FOCS 2022, 1093–1101. [Revised author manuscript, arXiv:2208.00795v3](https://arxiv.org/pdf/2208.00795v3), January 10, 2025, §§2–3, Theorems 5–6, internal pp.5–6.
6. David Alemán Espinosa and Niklas Schlomberg, *Pinning on Tight Cuts: Improved Algorithm and Bounds for Unsplittable Multicommodity Flows in Outerplanar Graphs*, ICALP 2026, LIPIcs **374**, Article 11. [Full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.11/LIPIcs.ICALP.2026.11.html), §§1.1–1.3 and 2.1, Theorems 1–2.
7. Chandra Chekuri, Guyslain Naves, Joseph Poremba and F. Bruce Shepherd, *Uncrossed Multiflows and Applications to Disjoint Paths*, APPROX/RANDOM 2026, LIPIcs **392**, 12:1–12:23, published September 9, 2026. [Full proceedings text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol392-approx-random2026/LIPIcs.APPROX-RANDOM.2026.12/LIPIcs.APPROX-RANDOM.2026.12.pdf), Theorems 1–3, Corollaries 4–5 and §§2.4–3.
8. Daniel Agassy, Dani Dorfman and Haim Kaplan, *Improved Tree Sparsifiers in Near-Linear Time*, ICALP 2026, LIPIcs **374**, Article 7. [Full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.7/LIPIcs.ICALP.2026.7.html), §2, Claim 2.7 and Theorem 2.8.

- OpenAI, [manuscript PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf), result family 089 (2026). Statement locator: `Theorem thm:main in each manuscript`.

## Status review

**Known cases:** Universal distortion holds for planar graph metrics, and distortion depending only on the treewidth bound holds for every fixed bounded-treewidth class. The comparison explains the finite-dimensional cut-metric and zero-length-edge reductions.

**Remaining target:** Cover every fixed excluded-minor class; nonplanar minor-free classes may have unbounded treewidth.

**Statement comparison:** The results establish constant distortion for all planar graphs and every fixed treewidth bound, with arbitrary positive real lengths and arbitrary demands. They do not cover every fixed excluded minor: minor-free classes can include nonplanar graphs of unbounded treewidth. Finite L1 metrics are finite nonnegative sums of cut metrics, giving AIM finite-dimensional real ell1. Nonnegative edge lengths are obtained by adding epsilon to each edge then taking a limit in the finite-dimensional cut cone (or contracting zero components); distortion constant is preserved.

**Review scope:** The [dated source comparison](../research/solution_reviews/2026-10-13-openai-crosscheck/README.md#aim-487) checked the actual theorem, hypotheses, quantifiers and required reductions against the unchanged AIM statement. This is an AI statement-level review of a published manuscript, not a fresh independent audit of its complete proof or a Lean kernel replay.

**Lean scope:** [Upstream scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/089.md). Actual endpoints cover positive-length planar and fixed-treewidth metrics only. They do not formalize the full arbitrary-excluded-minor target or the zero-length transfer. No local verification record. No AIM Lean-verified status is asserted.

**Source check:** Reviewed OpenAI commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a` on 2026-10-13, including its current manuscript map, history and available formalization scope. Earlier AIM literature notes remain accessible at [the previous revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/487-gnrs-minor-free-flow-cut.md).
