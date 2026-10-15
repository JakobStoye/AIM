# 340. The modern integer 3SUM conjecture

**Area:** Exact algorithms and computational complexity

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

For each integer $`n\geq3`$, the input is an explicitly listed set

```math
S\subseteq\{-n^3,-n^3+1,\ldots,n^3\},\qquad |S|=n.
```

The decision problem is whether there exist three **pairwise distinct** elements $`a,b,c\in S`$ such that $`a+b=c`$. Integers are encoded in binary. Use the classical word-RAM model with word size $`w=\Theta(\log n)`$, large enough to store an input integer and an address. Standard arithmetic and bit operations on words, comparisons and indexed memory accesses have unit cost.

An algorithm must be uniform: a single finite program works for every input size. It may use randomness, but for every valid input its yes/no answer must be correct with probability at least $`2/3`$. All computation, including preprocessing depending on the input, contributes to its running time. There is no free advice or supplied data structure.

For such an algorithm $`A`$, let

```math
T_A(n)=\max_{\substack{S\subseteq\{-n^3,\ldots,n^3\}\\|S|=n}}
\mathbb E[\text{number of word-RAM steps used by }A(S)],
```

where the expectation is over its random choices. **Conjecture:** There are no fixed $`\varepsilon>0`$ and such algorithm $`A`$ satisfying

```math
T_A(n)=O(n^{2-\varepsilon})\qquad(n\to\infty).
```

The exponent improvement must remain positive as $`n`$ grows. The finite-input problem and bounded-error convention follow [1, §§1.1–2.1]. Pătraşcu's original expected-time statement uses zero-error algorithms [9, §1.3]; the bounded-error convention here is explicitly supplied by [1]. Within bounded-error algorithms, a constant-factor timeout and amplification preserve the existence of a fixed-power speedup, so using expected time does not change that target. The standard three-set and zero-sum formulations are discussed in [2, §2.1] and are treated as one problem here. Logarithmic savings are compatible with this conjecture.

## Application

Integer 3SUM is a reference problem for the limits of exact combinatorial algorithms. Reductions transfer its conjectured running-time barrier to graph-triangle reporting, some dynamic reachability tasks and geometric degeneracy tests [2, §§1 and 6; 4, §1.1; 9, Theorems 3–5]. These connections help determine whether a slow step in a larger computation reflects a common unresolved algorithmic barrier. Its applied relevance is foundational: it organizes worst-case limits across these algorithmic tasks.

## References

1. Marshall Ball, Alon Rosen, Manuel Sabin and Prashant Nalini Vasudevan, *Average-Case Fine-Grained Hardness*, ECCC TR17-039 (2017), [author manuscript](https://msabin.github.io/files/papers/BRSV17.pdf), dated February 27, 2017. §1.1 gives the finite-integer problem; §2 and §2.1 specify randomized word-RAM computation, the success probability and the conjecture.
2. Ce Jin and Yinzhan Xu, *Removing Additive Structure in 3SUM-Based Reductions*, [arXiv:2211.07048v2](https://arxiv.org/pdf/2211.07048v2), revised March 16, 2023, cited preprint. §2.1, Definition 2.1 and Hypothesis 2.2; §1.1, Theorem 1.1; §3, Theorem 3.1. The served manuscript has a March 20 title-page date.
3. Yael Kirkpatrick, John Kuszmaul, Surya Mathialagan and Virginia Vassilevska Williams, *Preprocessed 3SUM for Unknown Universes with Subquadratic Space*, ICALP 2026, LIPIcs 374, Article 126, [published full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.126/LIPIcs.ICALP.2026.126.html), July 1, 2026. §1, the hypothesis, known general bound and Theorem 1.
4. Allan Grønlund and Seth Pettie, *Threesomes, Degenerates, and Love Triangles*, [arXiv:1404.0799v3](https://arxiv.org/html/1404.0799v3), May 30, 2014, cited preprint. §§1.1–1.3 and Theorem 1.1 distinguish integer algorithms, real-input algorithms and linear decision trees.
5. Timothy M. Chan and Moshe Lewenstein, *Clustered Integer 3SUM via Additive Combinatorics*, [arXiv:1502.05204v1](https://arxiv.org/pdf/1502.05204v1), February 18, 2015, cited preprint. §4 defines clustered sets; Theorem 4.1, Corollary 4.3 and §4.2 give the restricted-input guarantees.
6. Amir Carmel, Yakov Kosoburd and Robert Krauthgamer, *Recovery Beats Storage: Improved Space for Preprocessed 3SUM*, [arXiv:2608.22355v1](https://arxiv.org/html/2608.22355v1), August 23, 2026, preprint. §1 and Theorem 1.1 retain the general hypothesis while improving a preprocessing space/query-time trade-off.
7. Itai Dinur and Alexander Golovnev, *Improved Time-Space Tradeoffs for 3SUM-Indexing*, ICALP 2026, LIPIcs 374, Article 78, [published full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.78/LIPIcs.ICALP.2026.78.html). §1, the indexing model, Theorem 4 and the following preprocessing-time statement.
8. Neha Pant and Ryan Williams, *Beating Trivial Time for Tricky Triangle Tasks*, [arXiv:2606.27727v1](https://arxiv.org/html/2606.27727v1), June 26, 2026, preprint. §1, Theorems 1–2, 4 and 7, with the word-size convention.
9. Mihai Pătraşcu, *Towards Polynomial Lower Bounds for Dynamic Problems*, STOC 2010, pp. 603–610, [author manuscript](https://people.csail.mit.edu/mip/papers/mp-3sum/paper.pdf). §1.3, Conjecture 6 and its preceding zero-error convention; Theorems 3–5.
10. Timothy M. Chan, *More Logarithmic-factor Speedups for 3SUM, (median,+)-convolution, and Some Geometric 3SUM-hard Problems*, ACM Transactions on Algorithms 16(1), Article 7, published November 2019, [published full text](https://people.csail.mit.edu/virgi/6.1420/papers/real3sum.pdf), DOI 10.1145/3363541. §1, §2 and Corollary 3.12.
11. Valerii Sopin, *A new algorithm for solving the rSUM problem*, arXiv:1407.4640v5, February 9, 2015, [manuscript served by IACR 2022/1113](https://eprint.iacr.org/2022/1113.pdf). §3, Theorem 2 and its proof give the input-dependent runtime condition.
12. Luis Barba, Jean Cardinal, John Iacono, Stefan Langerman, Aurélien Ooms and Noam Solomon, *Subquadratic Algorithms for Algebraic Generalizations of 3SUM*, SoCG 2017, LIPIcs 77, Article 13, [published full text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol077-socg2017/LIPIcs.SoCG.2017.13/LIPIcs.SoCG.2017.13.pdf). §1.2 defines the models; Theorems 8, 13, 15 and 16 separate their guarantees.

## Status review

**Resolution-source report (2026-10-16):** [Primary proof, full-target comparison and evidence limits](../research/literature_reports/2026-10-16-prior-resolutions.md#aim-340). This AI-prepared report identifies a later resolution source or a direct application of an existing proof for maintainer review under the catalogue evidence policy.

### Earlier status review (2026-09-19)

**Literature check:** Open in cited literature; no later resolution located as of 2026-09-19.

The current July and August 2026 sources [3, 6] independently retain the general fixed-power hypothesis. The July account gives the best general integer running time as $`n^2\mathop{\mathrm{poly}}\nolimits(\log\log n)/(\log n)^2`$. It remains $`n^{2-o(1)}`$. The original strict-quadratic real-input conjecture was refuted in [4]; its Theorem 1.1 provides logarithmic algorithmic savings and a much smaller decision-tree depth. Counting comparisons in a decision tree does not supply a uniform machine implementation with that total running time.

Chan's Corollary 3.12 also retains exponent two at logarithmic word size [10]. Its §1 restates the logarithmic improvements by Freund and Gold–Sharir. Freund's publisher abstract was accessible, but the original subscription-restricted proof was not read; the exact bound was checked in Chan's full text. Algebraic 3SUM similarly has a fixed-power saving in decision-tree depth and only a logarithmic saving in its uniform algorithm [12]. Sopin's full runtime analysis requires sufficiently few surviving tuples after filtering, an additional condition not guaranteed for every input [11].

Theorem 1 of [3], Theorem 1.1 of [6] and Theorem 4 of [7] give improved space or query costs after preprocessing whose stated time remains $`\widetilde O(n^2)`$. Here $`\widetilde O`$ suppresses logarithmic factors. The current problem counts preprocessing and the decision together, so these are not the required general algorithms. The August result strengthens the guarantee to adaptive queries without removing this preprocessing cost.

Chan–Lewenstein's truly subquadratic result assumes that an input set can be covered by fewer than linearly many short intervals, with a fixed power saving in the number of intervals [5, Corollary 4.3]. An arbitrary set in the cubic universe need not satisfy that promise. Likewise, direct convolution is fast for sufficiently small universes; its dependence on the universe size matters here. Jin–Xu's reductions and hardness on Sidon sets are conditional on 3SUM, rather than proofs of the base hypothesis.

The 2026 triangle algorithms [8] save factors depending on the word size. At $`w=\Theta(\log n)`$ their relevant guarantees supply logarithmic savings, preserving the polynomial exponents. Their four-cycle result allowing larger words and their dense-graph special case do not establish the displayed general 3SUM speedup.

The September 18–19, 2026 searches covered the integer and modern 3SUM names, proof and refutation claims, unrestricted dates, 2025–2026 results, author corrections and version histories. The [evidence ledger](../research/expansion-2026-09/candidates/integer-three-sum-hardness.json) records exact scopes and the separated review. Supporting proofs were inspected as needed for scope, not independently certified in full.

[Matrix multiplication](028-matrix-multiplication-exponent.md) asks about a different operation in an exact scalar-arithmetic model. [Log-rank](290-log-rank.md) counts communication with unrestricted local computation. [Polynomial identity testing](310-deterministic-polynomial-identity-testing.md) asks for deterministic polynomial time on a compact circuit representation. None is the same assertion as this bounded-word, randomized exponent lower bound.
