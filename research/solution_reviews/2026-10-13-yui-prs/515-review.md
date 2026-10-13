# Independent review of AIM 515: Greedy Sparsest Poset counterexample

**Date:** 2026-10-13  
**Submission:** [PR #73](https://github.com/MColbrook/AIM/pull/73), Kaiwen Jin  
**Reviewed head:** `6c47f2a0345e5b51292a7ff5b7590a7c7be5ecac`  
**AIM statement:** problem 515 at `c9929805cece044705abaaebe1cebddac1ba11a6`  
**Reviewer:** independent Codex AI review in the maintainer's session. The reviewer did not develop this submission. No human review or Lean verification is claimed.  
**Decision:** **Solved by counterexample**, for the stated restricted-faithfulness oracle search.

[Manuscript](../../solutions/515-gspo-counterexample/paper/counterexample.pdf) · [Source](../../solutions/515-gspo-counterexample/paper/counterexample.tex)

## Target comparison

The counterexample uses a nondegenerate Gaussian distribution on six observed variables. It is Markov and restricted-faithful to the stated true DMAG. The starting poset maps, through both applications of the adjacency construction and maximal ancestral closure, to an eight-edge graph. Every legitimate single mark change followed by the required reconstruction remains among three eight-edge graphs. A six-edge graph is in the same original search space and no image has fewer edges. Thus the every-start nonincreasing-reachability assertion is false. The result does not assert failure under full faithfulness, different moves, or generic coefficients.

## Complete argument audit

The displayed noise matrix is triangular with diagonal one. Multiplying it by its transpose gives exactly the displayed covariance; all leading principal minors are positive. For a Gaussian vector, the almost-principal minor divided by the positive conditioning principal minor is the conditional covariance. All 240 pair/conditioning queries were recomputed in exact rational arithmetic, not estimated from samples.

The true skeleton is a six-cycle. Its two simple paths between each pair have only noncolliders internally except for vertex 6, which is a sink collider. This supplies the separation table directly. Comparing the separation table with the exact Gaussian minors leaves precisely one additional independence: variables 1 and 6 are marginally independent. These endpoints have skeleton distance three. They are neither adjacent, nor endpoints of a length-two path. Endpoints of any discriminating path share its first internal vertex as a skeleton neighbor, since that vertex is a parent of the last endpoint. The exceptional pair is therefore outside all three restricted-faithfulness protections. All protected m-connected queries remain dependent.

The proposed three graphs are ancestral. The listed separators establish maximality of the central graph; equivalence-preserving changes of the two root edges establish it for the other two. Direct exact reconstruction gives the claimed four fixed points, including the true six-edge graph. Every true adjacent pair is dependent given every conditioning set, so each application of the adjacency map retains all six true adjacencies and the closure cannot remove them. This proves the global minimum is exactly six without needing an enumeration of all posets.

All proposed mark changes were independently checked in two ways. The manuscript's parent/spouse obstruction is the correctly quoted necessary condition of Zhang--Spirtes Lemma 1; the two allowed root changes satisfy all its sufficient conditions. The inspected checker instead exhaustively enumerates simple paths and all conditioning sets, comparing complete separation signatures together with ancestry and maximality. It returns exactly the four transitions between the three graphs. Reconstruction fixes their endpoints. No reachable state leaves this component, regardless of allowed search depth or whether increasing edge counts would otherwise be permitted.

The finite checker has no unproved graphical shortcut in its legitimacy test. Its ancestor transitive closure, endpoint arrowhead interpretation, collider activation by ancestors of the conditioning set, rational determinant elimination, two adjacency passes, and maximal closure were reviewed against the definitions. The discriminating-path clause omitted from the checker's protected-pair shortcut is justified separately by the skeleton-distance argument above, so it is not an omitted assumption.

## Reproduction and ancillary material

After source inspection, in the submitted package at the reviewed head, with bundled Python 3.12.14 and without optimization:

```text
python -B scripts/verify_certificate.py
python -B -m unittest discover -s test -v
```

The verifier returned `PASS`, 240 exact Gaussian queries, one extra marginal independence, three eight-edge component graphs, a six-edge minimum, and the stated exact successors. All six tests passed, including collider descendants, nonmaximal closure, rational determinant controls, and changed-covariance rejection. The certificate is small exact input data, not an empirical simulation. The proof also gives all tables and the analytic obstruction, so the conclusion is not based on a heuristic discovery search.

## Reference audit

All three cited references are real, accurately attributed, and relevant. [Bernstein, Saeed, Squires and Uhler, PMLR 108 (2020), 4098--4108](https://proceedings.mlr.press/v108/bernstein20a/bernstein20a.pdf) contains the Gaussian example in Figure 1, the two-pass poset construction, and Conjecture 1; the submission credits the original model. [Squires and Uhler, Foundations of Computational Mathematics 23 (2023), 1781--1815](https://doi.org/10.1007/s10208-022-09581-9) retains the GSPO consistency question in Section 4.4. [Zhang and Spirtes, UAI (2005), Section 2.2, Lemma 1](https://arxiv.org/pdf/1207.1419v1) gives exactly the no-other-directed-path, parent/spouse, and discriminating-path conditions used. No necessary reference is missing from this argument.

## Conclusion and scope

The complete counterexample, assumptions, original search map, closure, reachable-component exhaustion, and smaller global minimum were independently audited. This supports `Solved` under the repository's documented independent-audit rule. This is an AI mathematical audit with exact computational support, not a claim of peer review or formal proof-assistant verification.

## Rendered PDF check

All 7 pages of the supplied main PDF were visually inspected against the source presentation. Titles, theorem statements, mathematical tables/equations, proof structure and bibliography agree; no clipped content or unresolved references were found. Root package checks separately parsed all pages and checked payload and archive hashes. Rendering is supplementary artifact evidence, not mathematical or formal verification.
