# 328. Accuracy of parsimony reconstruction under a molecular clock

**Area:** Mathematical phylogenetics and ancestral-state inference

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`r\ge5`$ be an integer and let $`T`$ be a finite rooted tree with at least two leaves, in which every internal vertex has exactly two children. Write $`\rho`$ for its root and $`X`$ for its leaf set. Assign each edge $`e`$ a finite length $`\ell_e\ge0`$, and require every path from $`\rho`$ to a leaf to have the same total length $`H`$. This is the molecular-clock, or ultrametric, assumption.

Generate states $`\sigma_v\in\{1,\ldots,r\}`$ on the vertices as follows. Choose $`\sigma_\rho`$ uniformly. Along an edge of length $`\ell`$, evolve a continuous-time Markov chain for time $`\ell`$ with generator

```math
Q_{ij}=\begin{cases}
-1,&i=j,\\
1/(r-1),&i\ne j.
\end{cases}
```

Branches evolve independently conditional on their parent states. This is the symmetric Neyman $`r`$-state model, with expected substitution rate one. In particular, the probability that any specified leaf has the root's state is

```math
q_r(H)=\frac1r+\frac{r-1}{r}\exp\!\left(-\frac{rH}{r-1}\right).
```

Observe the states at all leaves of the known tree. The Fitch parsimony estimator constructs a set $`S_v`$ at each vertex: $`S_x=\{\sigma_x\}`$ at a leaf, and, for children $`u,w`$ of an internal vertex $`v`$,

```math
S_v=\begin{cases}
S_u\cap S_w,&S_u\cap S_w\ne\varnothing,\\
S_u\cup S_w,&S_u\cap S_w=\varnothing.
\end{cases}
```

Choose $`\widehat\sigma_\rho`$ uniformly from $`S_\rho`$. Its accuracy includes both the random character generated on the tree and this final tie-breaking choice.

**Does every such tree and length assignment satisfy**

```math
\Pr\{\widehat\sigma_\rho=\sigma_\rho\}\ \ge\ q_r(H)?
```

Thus, does using all the leaves with Fitch parsimony perform at least as well as guessing the root state from any one leaf? This is the unresolved $`r>4`$ portion of the Li–Steel–Zhang conjecture. The same inequality is proved for $`r=2,3,4`$. The estimator uses the topology and leaf states; the edge lengths specify the probability model but are not inputs to its recursion. The question concerns one character on each finite tree, rather than an asymptotic sequence-length or tree-estimation guarantee.

## Application

Ancestral-state inference estimates a trait or a sequence position of a common ancestor from present-day species. Parsimony provides a fast estimator without requiring branch-length estimates. The inequality would establish a basic accuracy guarantee for using an entire clock-like phylogeny with a larger character alphabet, including a stylized 20-state model for an amino-acid position. The symmetric model isolates the effect of tree shape and shared ancestry on information use. Actual protein substitutions have unequal rates, so the proposed guarantee would be a theoretical benchmark for that application, not a conclusion for arbitrary evolutionary models.

## References

1. Guoliang Li, Mike Steel and Louxin Zhang, *More Taxa Are Not Necessarily Better for the Reconstruction of Ancestral Character States*, Systematic Biology 57(4) (2008), 647–653, [published paper](https://doi.org/10.1080/10635150802203898); [accessible published PDF](https://www2.gwu.edu/~clade/bisc%20207/LiEtAl2008.pdf). The final paragraph before the acknowledgments on p. 652 states the conjecture.
2. Mareike Fischer and Bhalchandra D. Thatte, *Maximum Parsimony on Subsets of Taxa*, Journal of Theoretical Biology 260(2) (2009), 290–293, [DOI](https://doi.org/10.1016/j.jtbi.2009.06.010); [author manuscript v2](https://arxiv.org/pdf/0809.3653v2), 6 July 2009. Theorem 2, manuscript p. 9, proves the two-state case; Theorem 1 concerns a non-clock counterexample.
3. Lina Herbst and Mareike Fischer, *On the Accuracy of Ancestral Sequence Reconstruction for Ultrametric Trees with Parsimony*, Bulletin of Mathematical Biology 80 (2018), 864–879, [DOI](https://doi.org/10.1007/s11538-018-0407-5); [author manuscript](https://arxiv.org/abs/1706.06085). Theorems 1–2 prove the four- and three-state cases. Section 5, manuscript p. 18, explicitly leaves $`r>4`$ open.
4. Lina Herbst, Heyang Li and Mike Steel, *Quantifying the accuracy of ancestral state prediction in a phylogenetic tree under maximum parsimony*, Journal of Mathematical Biology 78 (2019), 1953–1979, [published PDF](https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/lina.pdf). Section 1.1 gives the model and length normalization; Theorem 2, Theorem 4, Corollary 3 and Conjecture 1 distinguish the available bounds from a stronger conjecture.
5. Sebastien Roch and Kun-Chieh Wang, *Sufficient condition for root reconstruction by parsimony on binary trees with general weights*, Electronic Communications in Probability 26 (2021), article 55, 1–13, [DOI](https://doi.org/10.1214/21-ECP423); [published PDF](https://par.nsf.gov/servlets/purl/10342268). Section 1, Theorems 1.2 and 1.5, treats two-state reconstruction uniformly over tree depths.

## Status review

Reviewed 15 October 2026 against the original target in [PR #145](https://github.com/MColbrook/AIM/pull/145). An exact positive-edge ultrametric three-leaf example for the symmetric twenty-state model violates the proposed Fitch accuracy inequality.

[Proof or source](../research/solutions/fitch-ultrametric-counterexample/paper/main.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/328-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Full negative answer to the assertion over all alphabet sizes r>=5; strict deficit 171/400000.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Literature check:** Open in cited literature; no later resolution located.

Open in cited literature; no later resolution located as of 2026-09-18.

The September 18, 2026 search covered the conjecture's authors, Fitch/Neyman and molecular-clock terminology, general-state accuracy inequalities, proof and counterexample terms, 2025–2026 work, unrestricted dates, corrections and manuscript histories. Herbst–Fischer supplies a specialist assessment with authors disjoint from the original paper. Its publisher text was subscription-only; the relevant author-manuscript sections were read. The [evidence record](../research/expansion-2026-09/candidates/fitch-ultrametric-ancestral-accuracy.json) records access and version differences and the full scope comparisons.

Herbst–Li–Steel proves the general bound $`\Pr\{\widehat\sigma_\rho=\sigma_\rho\}\ge1/r`$. For finite $`H`$, the requested $`q_r(H)`$ is larger. Its comparison with a recursive coin-toss estimator is proved for two states and conjectured for general $`r`$; Theorem 2 identifies the coin-toss benchmark with $`q_r(H)`$ under the clock assumption. Roch–Wang also treats two states, with a branching condition and an infinite-depth benchmark.

The non-clock counterexamples in Li–Steel–Zhang and Fischer–Thatte do not satisfy the equal-height hypothesis. Counterexamples to improvement over arbitrary subsets do not refute comparison with a single leaf. Other checked results concern prescribed leaf patterns, reconstruction of tree topology, or special tree shapes, rather than the asserted probability bound for all finite clock-like trees. No matching later resolution was located.

This is one problem across alphabet sizes. Unequal substitution rates, arbitrary subsets, and the stronger non-clock coin-toss conjecture are not separate additions. It differs from [selected-population genealogy](318-selected-brownian-population-genealogy.md), which asks for a random ancestry process, and [trace reconstruction](321-polynomial-trace-reconstruction.md), which asks how many deletion-channel observations identify an unknown string.

Review was a separated adversarial self-pass after drafting. No independent agent or human review is claimed.

A publication refresh on September 18, 2026 rechecked status and upstream duplicates; see the [batch 4 audit](../research/expansion-2026-09/batch-04-review.md). No matching later resolution was located.
