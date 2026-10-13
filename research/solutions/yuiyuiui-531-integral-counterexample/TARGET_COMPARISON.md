# Target comparison

Target: [531. Homology at the second transition of torus-grid Rips complexes](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/531-torus-grid-transition-homology.md),
revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The paper's Theorem 1 proves the fourth integral free rank is two for
`K_13(5)`. This is the disproof alternative in the original target: one
admissible parameter violates a required conclusion of the universal statement.

| Original requirement | Manuscript location and result | Scope |
| --- | --- | --- |
| Every integer `k>=5` | Theorem 1 uses the admissible witness `k=5` | Refutes the universal conjunction |
| Side length `n=3k-2` | `n=13=3*5-2`, sections 1--2 | Exact |
| Periodic Manhattan distance | Explicit sum of two shortest cyclic coordinate distances, section 1 | Exact |
| Subsets of diameter at most `k` | Closed Rips convention with `<=5`, section 1 and graph reconstruction | Exact, including equality |
| Integral reduced homology outside degrees 3,4 vanishes | No separate determination needed for a disproof once the rank conclusion fails | No additional claim |
| Integral rank H3 `6k-2+(-1)^k` | No separate determination | No additional claim |
| Integral rank H4 `6k-3+(-1)^k` | Required value is26 at k=5; Lemma 2, Proposition 4 and Theorem 1 prove rank2 | Contradicted |
| No included assertion of torsion-freeness in degrees 3,4 | Proof uses the integral free rank and exact integer operations | Preserved |
| Public proof dependencies | Open-cover nerve theorem in Adams et al. v2, Theorem 3.1; Hatcher Corollary 2.11 and Theorems 2.27,2.35 | Hypotheses are verified in Lemma 2 |

The finite certificate completely enumerates relative simplices with no
degree truncation. It verifies signed boundaries, integer unit cancellations
and the residual rank. The manuscript proves the torus-core and
relative-to-absolute homology steps. The primary paper's mod-two table is
consistent with the even residual boundary; it is not the integer-rank input
to the proof. This submission does not compute an unbounded family of
homology groups or claim a resolution of a separate mod-two conjecture.
