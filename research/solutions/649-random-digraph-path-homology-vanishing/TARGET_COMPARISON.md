# Correspondence with AIM 649

[Original statement](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/649-random-digraph-path-homology-vanishing.md),
revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.
The comparison below uses that public statement and the finished manuscript.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Digraph on [n], no loops; every ordered arc independent with common probability; reciprocal arcs allowed | Section 1 defines G(n,p), A_aa=0 and independence of A_ab and A_ba | Same model |
| All vertex sequences and alternating deletion boundary; repeated-consecutive-vertex terms retained | Section 1 defines Lambda, A and Omega under this convention; Section 2 verifies the literal diamond boundary | Same non-regular convention |
| First path homology over Q | Theorem 1.1 and Section 5: valid integer boundary rows span the rational edge-cycle space, using equal real/rational ranks | Same coefficient field and conclusion |
| Each fixed -2/3 < alpha <= 0, p_n=n^alpha | Corollary 1.2: n^2p_n^3=n^(2+3alpha) dominates log^4(2n) | Entire requested exponent range |
| Remaining interval -2/3 < alpha <= -1/3 | Included in Corollary 1.2 without an extra graph hypothesis | Entire remaining interval, including -1/3 |
| Probability of zero first non-regular Betti number tends to one | Theorem 1.1 and Section 5 | Same probabilistic limit |
| Critical alpha=-2/3 excluded | Section 1 explicitly excludes it; the sufficient condition does not hold there for p=n^(-2/3) | No endpoint claim |
| No requirement of convergence uniform in alpha or absence of integral torsion | Section 1 separates both from the rational conclusion | Neither stronger conclusion is asserted |
| Public external concentration input | Section 3 states the self-adjoint and rectangular matrix Bernstein signatures; Tropp author preprint, Theorems 1.4 and 1.6 | Finite independent centered matrices with displayed norm/variance conditions |

The sufficient theorem applies more generally to every deterministic probability
sequence with `n^2p_n^3/log^4(2n) -> infinity`. It is an upper vanishing condition,
not a claim of the sharp logarithmic threshold.
