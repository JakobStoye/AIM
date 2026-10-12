# Comparison with the complete AIM 516 target

Target: [AIM 516: Tail bounds for causal equivalence classes of uniform random DAGs](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/516-random-dag-equivalence-class-tails.md),
at repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

The submission is a complete analytic solution claim. Theorem 1.1 proves a
stronger estimate, and Corollary 1.2 is the statement asked for.

| Original requirement | Manuscript location and coverage |
|---|---|
| Simple directed acyclic graphs on the labeled set [n] | Section 1 defines precisely this finite set. |
| Uniform over labeled DAGs | Sections 1 and 3 use that measure. The independent-forward-edge measure Q is introduced only for comparison in Lemma 3.4. |
| Same skeleton and v-structures | Section 1 defines M using these two conditions. Section 2 cites the matching essential-graph characterization. |
| Every epsilon in (0,1) | Corollary 1.2 and its proof in Section 5. |
| Finite C_epsilon and t_epsilon>1 | Section 5 chooses t_epsilon=e^(X_epsilon), with X_epsilon large enough, and C_epsilon=C from Theorem 1.1. |
| Simultaneously every integer n>=1 | Theorem 1.3 and all probability comparisons are uniform in n. The case n<m is empty; n<L uses the terminal boundary in Lemma 3.4. |
| Every real t>=t_epsilon | Section 5 uses x=log t and an integer factorial threshold m; no integrality of t is assumed. |
| Exponent 2-epsilon with coefficient one in the exponent | Theorem 1.1 has the stronger scale c(log t/log log t)^2. The final inequality in Section 5 absorbs c and the two log-log factors by choosing X_epsilon. |
| Constants independent of n and t | All constants through Theorem 1.1 are universal; only X_epsilon depends on epsilon. |

The proof does not assert the same result for sparse priors, uniform sampling
of equivalence classes, or random-order forward-edge sampling. Proposition 5.1
shows why the fixed endpoint C exp[-c(log t)^2] is impossible under the stated
uniform-DAG prior.

The existing benchmark and near-two question are Schmid--Sly,
[arXiv:2209.04395v2](https://arxiv.org/abs/2209.04395v2), Theorem 1.1 and the
following paragraph on printed page 2. Their source-layer/tower ingredients
are credited and proved here with sufficient, nonoptimized constants. The
essential-graph characterization is imported from Andersson--Madigan--Perlman;
the subsequent quadratic component estimate is supplied by the manuscript.

Finite enumeration supports only the four-vertex identities it checks. The
universal theorem rests on the complete analytic argument. Successful
submission does not establish acceptance, independent human review, or formal
verification.
