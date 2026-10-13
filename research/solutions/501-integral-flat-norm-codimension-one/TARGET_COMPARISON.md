# Target comparison for AIM 501

Original source: [pinned problem statement](https://github.com/MColbrook/AIM/blob/1b7c7fd251c1643bb41f0e3cef38704bcef410fd/problems/501-integral-flat-norm-codimension-one.md).
Revision: `1b7c7fd251c1643bb41f0e3cef38704bcef410fd`.
Result: [finished manuscript](paper/integral_flat_norm.pdf), Theorem 1.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Every d>=1, ambient R^(d+1) | Theorem 1; n=d+1 in Section 2 | Full |
| Compactly supported integral input T with finite mass and boundary mass | Section 1 and Theorem 1 | Same data class |
| Real flat norm over compactly supported real normal currents | Equation (1); Lemma 2 covers arbitrary normal top-dimensional fillings | Exact real competitor class |
| Objective M(X)+M(S), coefficient one | Equations (1), (9), (10), (13); final proof | Exact normalization |
| Current identity T=X_I+boundary S_I | Theorem 1 and final construction in Section 4 | Exact current identity |
| Both outputs compactly supported and integral | Last paragraph of Section 3; Section 4 common-ball argument and integer BV limit | Full |
| Optimum attains the real infimum | Last two paragraphs of Section 4, lower semicontinuity plus real feasibility | Actual equality and attainment |
| Nonzero boundary is permitted | Theorem 1, the rounding proof, and boundary X_I=boundary T at the end | No cycle assumption |
| Existence of at least one integral optimum | Theorem 1 | The requested existential claim |
| Remaining d>=2 scope without the subdivision conjecture | Same proof for every n=d+1>=2 | No subdivision hypothesis |

The prior planar result and the conditional general result are credited to
Ibrahim, Krishnamoorthy and Vixie (2016), Corollary 3.8 and Theorem 3.7.
The additional argument is the shared-shift residual identity (8), its BV
trace justification in Lemma 3, and its compactness lift in Section 4.
Classical coarea, trace, boundary-rectifiability and BV-compactness inputs are
stated where used and cited in the manuscript. No formalization or
computation is needed for the proposed analytic conclusion.
