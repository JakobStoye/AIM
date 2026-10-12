# Target comparison for AIM 562

Original entry: [562 — Sharp least-singular-value bounds for independent random
tensor columns](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/562-tensor-singular-value.md),
at repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted manuscript: Kaiwen Jin, *Least singular values of independent random
tensor columns*. Theorem 1 and its proof in Section 3.2 claim the complete
affirmative conclusion. This comparison is based on the public target and
the manuscript. Independent mathematical review is requested.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Real factor vectors in dimension n; column i is a product of d independent factors | Section 1 defines x_i,l, X_i, A and N=n^d before Theorem 1 | Same model |
| All scalar coordinates mutually independent, mean zero, variance one, psi_2 at most K under the exponential-square convention | Section 1 gives that exact convention and assumptions; Lemmas 2-3 use independent centered laws; Proposition 5 verifies tensor isotropy | All permitted laws, including distinct and discrete laws; no symmetry or density premise |
| Fixed epsilon in (0,1/2] | Theorem 1; Proposition 5; closing limit in Section 3.2 | Every fixed epsilon in that interval; no assertion for epsilon tending to zero |
| Integer d=d(n)>=1 with d=o(sqrt(n/log n)) | Theorem 1 uses the equivalent condition d^2 log(n)/n -> 0; the failure terms in equation (17) vanish in exactly this regime | Growing order allowed |
| d=1 | Proposition 5 treats the empty first-factor tensor as b_i=1 and all its auxiliary events deterministically | Included |
| N=n^d, m=floor((1-epsilon)N) | Section 1 and Theorem 1; Proposition 5 sets h=N-m and k=floor(delta_K h), checking k>=delta_K h/2 eventually | Floors retained |
| Natural ambient scale and linear aspect-ratio gap: s_min(A)>=c_K epsilon n^(d/2) with probability tending to one | Theorem 1; Proposition 5 gives a sqrt(epsilon N/8) projected-block bound; equation (18) and Section 3.2 lift it to the full matrix | Complete stated lower bound |
| Constant independent of n,d,epsilon and permitted law sequence | Equation (14) chooses delta_K using K alone; Section 3.2 sets c_K=sqrt(delta_K)/8; equation (17) is uniform in fixed block and laws | K-only constant; convergence thresholds may depend on the fixed epsilon |
| No additional assumption about ranks of outside columns or random subspace geometry | Proposition 5 uses a measurable projection, rank >=N-(m-k), with no rank equality; all estimates are uniform in that projection | No genericity or subspace-distribution premise |
| A proof for all coefficient vectors | Section 3.2 proves a deterministic fraction-of-bad-subsets implication for each matrix before integration | No numerical surrogate or union bound over all subsets |

## Public sources and supplementary argument

Vershynin's [updated author manuscript](https://arxiv.org/abs/1905.00802v5),
Theorem 1.4, supplies the tensor Euclidean concentration bound displayed as
equation (6). Its Corollary 6.2 is the weaker benchmark discussed in Section 1,
not the conclusion used to obtain the new ambient scale.

Tropp's [revised author preprint](https://tropp.caltech.edu/books/Tro14-Introduction-Matrix-preprint.pdf),
Theorem 5.1.1, supplies the positive-semidefinite matrix Chernoff upper tail in
equation (7). The truncation, covariance normalization and threshold conversion
are proved in Proposition 5.

The Hermite-operator calculation credits
[Bandeira, Kunisky, Nizic-Nikolac, Pesenti and Wang](https://arxiv.org/abs/2610.01982v1),
Section 2, for its method. Lemma 4 proves the two coefficient-block norm bounds
and every polynomial-operator identity used here.
[van Handel](https://arxiv.org/abs/2512.18588v2) is cited for broader convex-order
context; the scalar comparison needed here is proved in Lemma 2.

The added argument consists of the conditional quadratic Gram estimate for
projected tensor blocks, its uniform growing-order application, and the
deterministic random-subset lifting to all coefficients. A direct invocation
of the two concentration theorems does not supply the claimed least-singular-value
scale. No priority claim is inferred from a bounded literature search.

The manuscript is analytic. It uses no numerical experiment, certificate,
code premise, or formal proof. Compilation checks the document artifact; it
does not certify the mathematical theorem.
