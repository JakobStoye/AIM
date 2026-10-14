# Target comparison: AIM 602

Original target: [A linear genus–girth bound for facial cycles](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/602-surface-girth-facial-linear-bound.md), repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted manuscript: *A uniform linear bound for facial cycles on surfaces*, Kaiwen Jin, Theorem 1.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Finite simple graph of girth at least ell, maximal for the fixed crossing-free embedding | Theorem 1 and the opening definition; Section 4 derives boundary distances from maximality | Same |
| Connected closed orientable surface with g handles, or nonorientable surface with g crosscaps | Theorem 1; Sections 2 and 4 use Euler genus kappa and preserve kappa <= 2g | Both types |
| Every integer g >= 1 and ell >= 3, with one constant | Theorem 1, Lemma 9 and the final inequality in Section 4 | All stated parameters |
| Noncellular embeddings and graphs that may be disconnected | Section 4 replaces the empty side of a separating facial cycle by a disk, handles the nonseparating case directly, and keeps the component containing the subdivided cycle | Same; no extra assumption |
| A simple cycle forming the entire boundary of one face | Definition in Section 1, Theorem 1 and Section 4 | Same; the proof also handles the point-set one-sided reading |
| Facial-cycle length at most C g ell | Theorem 1 proves C = 100000; the closing estimate gives the stronger bound `|C| < 71684 g ell` | Complete affirmative claim |
| No stipulated numerical algorithm or formal proof | The submitted evidence is a complete analytic manuscript with public dependencies | Analytic argument only |

## Imported results and their use

| Public dependency | Manuscript location | Interface and applicability |
| --- | --- | --- |
| Axenovich et al., *Faces in girth-saturated graphs on surfaces*, arXiv:2410.13481v3, Theorem 2, Question 2 and Lemma 1 | Section 1 and Section 4 | Quadratic benchmark, exact uniform question, and boundary-distance observation; the manuscript also derives the last observation for its full embedding scope |
| Pálvölgyi–Zólomy, *Stabbing non-piercing sets and face lengths in large girth plane graphs*, arXiv:2504.10618v2, Theorem 3 and Section 4 | Section 1 | Fixed orientable-genus linear girth comparison and credit for the ball-piercing/nearest-center strategy; no genus-uniform constant is imported |
| Bousquet et al., *Packing and covering balls in graphs excluding a minor*, arXiv:2001.04517v3, Theorem 4 and page 1 | Proposition 7 and Lemma 9; Section 3 fractional definitions | A ball subfamily on V(J), nu* <= e d nu, and finite LP duality. The graph contains the facial cycle and has an edge; Lemma 6 bounds every simple-minor average degree, and boundary diameter gives nu = 1 |
| Ding–Seymour–Winkler, *Bounding the vertex cover number of a hypergraph*, author-hosted original, (5.4), printed page 10, with (5.1)/(5.3) and Section 5 conventions | Proposition 8 and Lemma 9 | The bound uses primal VC dimension and the original base-two logarithm. The manuscript states the finite integer-copy bridge, accounts for one distinct edge, and explicitly converts both logarithms |
| Erickson, *Surface classification*, lecture 6, Corollary 6.4 and Theorem 6.5 | Section 2 | Closed-surface classification and Euler's formula for both surface types; the manuscript supplies the regular-neighborhood, boundary-capping and facial-walk calculations |

The paper claims the complete original target. It does not claim bounds for nonsimple facial walks, an optimal absolute constant, formal verification or upstream acceptance. The manuscript and its cited public sources constitute the mathematical submission; no private supplement is required.
