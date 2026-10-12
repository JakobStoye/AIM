# AIM 451: target comparison

Original target: [A mixed Sobolev estimate for reconstructing a scalar potential](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/451-bourgain-brezis-mixed-sobolev-gradient-estimate.md),
revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
Submitted manuscript: [Failure of a mixed Sobolev estimate for scalar potentials](paper/main.pdf).

| Original requirement | Result and location in the manuscript | Scope |
|---|---|---|
| For every integer dimension d >= 2 | Section 1, Theorem 1, constructs a counterexample sequence in the allowed fixed dimension 2 | Refutes the complete universal assertion; proving failure separately in every dimension is unnecessary. |
| Real smooth mean-zero scalar on the unit torus | Section 5 defines the Poisson-smoothed real potentials, prescribes the zero Fourier mode and selects a positive smoothing scale for each M | Same admissible input class. The auxiliary sheet in Section 4 is replaced before applying the estimate. |
| Exact inhomogeneous H^(1/2) and H^(-1/2) weights | Section 1 defines (1+4pi^2|k|^2)^s; Lemma 2 and Section 5 retain these weights | No homogeneous replacement. |
| Euclidean vector L1 and Fourier energy norms | Section 1 conventions, field bound (7), and Section 5 projection calculation | Same vector conventions. |
| Full W^(1,1) norm and infimum sum norms | Section 1 definitions; Section 5 pairs against every distributional scalar decomposition, then takes its infimum | Full norm is controlled; component-sum conventions change only dimension constants. |
| One finite constant depending only on d | Theorem 1 and estimates (16)--(17): right cost bounded independently of M, left cost at least c sqrt(M)-C | Contradicts every finite C2. |
| A proof or counterexample covering the full statement | Theorem 1, with the closing argument of Section 5 | Complete analytic counterexample claim, awaiting independent mathematical review. |
| Public mathematical dependencies | Section 1 cites normalized Fourier theory and Fubini; Section 5 cites local weak-derivative mollification and explains the periodic domain passage | Guillemin, Section 4; Tao, Theorem 1.7.21; Hunter, Theorem 3.19. The remaining estimates are proved in the manuscript. |

Bourgain--Brezis (2003), equation (1.16), and Brezis (2023), Open Problem 7.1,
are the cited source questions. Their positive divergence and phase results
are not assumed as a proof of the disputed mixed-gradient estimate.

The submission is AI-assisted. Compilation and document checks verify the
artifact, not a universal theorem; independent mathematical review is requested.
