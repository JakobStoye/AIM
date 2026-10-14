# Target comparison for AIM 610

Original target: [610. Nill's facet bound for reflexive lattice polytopes](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/610-reflexive-polytope-facet-bound.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted result: Theorem 1 of [the manuscript](paper/manuscript.pdf), proved in Section 3. The permitted alternative is **disproof** by one admissible counterexample.

| Original requirement | Manuscript evidence | Scope |
| --- | --- | --- |
| Full-dimensional lattice polytope in the standard integer lattice | Section 3 sets `P = Q_5^*`, with `Q_0 = R_(40,32)` and `Q_j = T(Q_(j-1))`. Lemmas 2 and 3 and Proposition 4 give dimension 45 and integral primal and polar generators. | All premises satisfied by the witness. |
| Origin in ordinary interior | Lemma 2 proves this for the base; Lemma 3 preserves it under each pyramid. The elementary polar argument at the start of Section 2 supplies it for the polar. | Ordinary Euclidean interior on both sides. |
| Polar convention `P^* = {y : <x,y> <= 1 for all x in P}` | Section 1 fixes this convention; Lemmas 2 and 3 compute the polar with it. Section 3 uses bipolarity to give `P^* = Q_5`. | Identical normalization. |
| Polar also a lattice polytope | Proposition 4 lists every family of integral generators of `Q_5^*`; the vertices of `Q_5` are integral. | Both lattice requirements verified. |
| Remaining dimensions `d >= 5` | Theorem 1 and its proof use `d = 45`. | One dimension in the unresolved range suffices for disproof. |
| No simplicity, simpliciality or symmetry assumption | The construction and proofs use only their displayed inequalities, integrality, full dimension and interior conditions. | No additional structural hypothesis. |
| Facet bound `f_(d-1)(P) <= 6^(d/2)` | The proof of Theorem 1 establishes the vertex/facet bijection and the exact count `F = 2^32 binom(40,8) + 5`. It displays `F^2 - 6^45 = 5154504949354948553223060244660249 > 0`. | Strict violation; negates the universal statement. |
| Public mathematical dependencies | The construction, polar transformation, integrality, facet count and integer comparison are proved in Sections 2 and 3. Citations identify Nill's conjecture, the restricted twinned-chain result, and prior reflexive embeddings. | No omitted private proof supplement or computation is required. |

The statement is a full-target existential disproof. It does not identify the smallest possible dimension, classify all counterexamples, or claim independent novelty certification. The package requests independent review and does not itself change the repository's problem status.
