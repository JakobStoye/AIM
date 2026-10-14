# Correspondence with AIM 645

Original target:
[645: A finite three-ample complex with nontrivial fundamental group](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/645-finite-three-ample-nonsimply-connected.md),
revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The manuscript establishes the finite-existence alternative.

| Original requirement | Manuscript location | Coverage |
| --- | --- | --- |
| A nonempty finite simplicial complex | Theorem 1; Section 2, permitted faces and mark rule (2) | Exactly 32,768 vertices, dimension at most three; face closure is proved. |
| Every vertex set U with at most three vertices | Section 2, missing label q and t=q+2; union bound (5) | Arbitrary U; the empty set is handled separately. Repeated labels are included. |
| Every subcomplex A of X[U] | Section 1, definition (1); Section 2, event (3) and conditional union over the fixed K | All subcomplexes are included, without an inducedness restriction. |
| A may be empty or have smaller vertex support | Discussion following (1) and face-by-face verification following (4) | All corresponding nonempty cone faces are included or excluded exactly. |
| Witness vertex outside U | Section 2, the set W | At least m-4 eligible vertices, all outside U and the designated cycle vertices. |
| Exact restricted-link equality | Section 2, proof after (4) using mark rule (2) | Inclusion uses every lower face; exclusion uses the relevant zero cone mark. |
| One finite complex serves every request | Bound (5) and the exact estimate below it | Failure probability is strictly less than 2^-9, hence some finite outcome succeeds. |
| Nontrivial fundamental group | Fixed maps p,s in Section 2 and its closing paragraph | The cycle is a simplicial retract; its infinite cyclic group injects into the fundamental group of X. Path connectedness is proved. |
| No flag hypothesis | Definition and mark model in Sections 1–2 | Missing edges and triangles in subcomplex requests are allowed. |

The only imported topological facts are the circle fundamental group and
functoriality, cited to Hatcher, Theorem 1.7 and printed page 34. The fixed
section and the application of those facts are proved in the manuscript.
Farber, Example 2.5, supplies the finite question; Barmak's Theorem 1 and
Example 6 in arXiv:2103.03952v1 supply the infinite example and the four-cycle
starting model. A finite conic
example is not treated as already three-ample.

The manuscript gives an analytic probabilistic existence construction.
No actual sampled face list, minimum vertex count, efficient algorithm,
formal verification or independent human review is claimed.
