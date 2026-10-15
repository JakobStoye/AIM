# Comparison with AIM 640

Original target:
[640-random-balanced-cayley-expansion.md at a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/640-random-balanced-cayley-expansion.md).

Result: a negative answer for every fixed integer k>=2. The paper's
Theorem 1 gives a deterministic cohomology lower bound on the admissible
groups G_d=(F2)^d. Corollary 2 shows that every subset of the prescribed
logarithmic size has zero expansion for all sufficiently large d.

| Original requirement | Result and location in the manuscript | Scope |
| --- | --- | --- |
| Every fixed k>=2 | Theorem 1 and Corollary 2 | Every such fixed dimension |
| Constants C_k,epsilon_k>0 | Corollary 2 fixes arbitrary positive C and epsilon before d grows | Refutes every proposed pair of constants |
| Constants work along every diverging finite-group sequence | Corollary 2 uses G_d=(F2)^d with orders 2^d tending to infinity | One admissible sequence refutes the required universal guarantee for each k |
| D(G)=sum of irreducible complex representation dimensions | Proof of Corollary 2 counts the 2^d one-dimensional sign characters | Exact D(G_d)=2^d |
| k+1 disjoint vertex parts, full (k-1)-skeleton | Section 1, and the common-skeleton argument in the proof of Theorem 1 | Same complex and preceding coboundary space |
| Top simplex iff the ordered group product belongs to A | Section 1 uses additive notation for the product on G_d | Exact translation of the original selection rule |
| Binary cochains and B=im delta_{k-2} | Section 1 and equations (4)-(6) in the proof of Theorem 1 | Same F2 coefficient field and quotient |
| Uniform subset of size ceil(C_k log D(G)) | Corollary 2 and its eventual ceiling inequality | Sample is admissible; every subset of that exact size fails |
| Unnormalized numerator and distance-to-B denominator | Equation (1) and the last paragraph of the proof of Theorem 1 | Nonzero cohomology class has zero numerator and finite strictly positive denominator |
| Success probability tends to one | Corollary 2 | Success probability is exactly zero for all sufficiently large d |

The construction and conjecture are those of Meshulam, *Random Balanced
Cayley Complexes*, arXiv:2211.02085v1, pp. 2–4 and 17.
The source's real-coefficient spectral result is background; the counterexample
concerns the explicitly requested binary cochain bound.
No imported mathematical theorem or numerical evidence is needed for the proof.

