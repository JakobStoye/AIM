# Target comparison for AIM 574

Target: [574. Draws in the undirected trapping game on percolation clusters](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/574-trap-draws-percolation.md).

Statement revision: c9929805cece044705abaaebe1cebddac1ba11a6. Manuscript: *Draws in the undirected trapping game on site-percolated lattices*, Kaiwen Jin, 13 October 2026.

| Original requirement | Manuscript location and conclusion |
| --- | --- |
| Nearest-neighbor graph on the entire integer lattice, independently deleting each site with probability p in (0,1) | Introduction defines the original board and the deletion convention. Section 2 uses the open indicator q=1-p. |
| Both players know the board; alternating undirected moves to unvisited undeleted vertices; no legal move loses | Introduction states these rules. Section 2 relates finite exit games to the original infinite game without changing its legal moves. |
| A deleted origin is a first-player win and never a draw | Introduction states the convention. Lemma 2.2, equation (2.3), includes the open-origin factor q; Section 5.4 retains that event in the limiting draw probability. |
| Draw means neither player can force a win against every opposing strategy | Introduction defines the outcome. Lemma 2.2 proves the equivalence with disagreement of the two limiting boundary outcomes, using finite branching to identify every forcing win. |
| D_2(p)=0 for every p in (0,1) | Theorem 1.1 and Proposition 3.3. The surface bound of Lemma 3.1 and the nonzero-fluctuation implication of Lemma 3.2 yield the contradiction for every such p. |
| For every integer d at least three, some p in (0,1) has D_d(p)>0 | Theorem 1.1 and Sections 4–5. Lemma 4.3 gives the contour comparison; Lemma 5.1 and equations (5.5)–(5.8) bound all fixed admissible permutations before random contour selection. Section 5.4 chooses strictly positive p and passes to the original infinite board. |
| Full infinite target, rather than only finite boxes or a directed game | Lemma 2.2 proves exhaustion independence and the exact game correspondence. Section 5.4 uses decreasing cardinality-increment events and continuity from above. The final proof combines both original clauses. |

The submitted claim covers the entire proposed dimension-dependent picture. It does not claim an explicit critical deletion probability or a classification of every p with draws in higher dimensions.

The finite graph criterion from Basu, Holroyd, Martin and Wästlund and the boundary-connectivity result of Timár are cited with the arXiv versions used. Finite-activity Gibbs uniqueness and low-temperature disorder arguments are background and method comparisons; their conclusions are not substituted for game outcomes.

The proof is analytic. No numerical calculation or finite certificate is needed to reproduce a premise. AI assistance is disclosed at the end of the manuscript. Independent mathematical review is requested.
