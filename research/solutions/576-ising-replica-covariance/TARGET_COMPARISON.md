# Target comparison for AIM 576

Target: [Uniform covariance bounds for constrained Ising replicas](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/576-ising-replica-covariance.md),
repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
Result: Theorem 1.1 of the accompanying manuscript, proved in Sections 2--3.

| Original requirement | Result and location in the manuscript | Coverage |
|---|---|---|
| Every fixed integer n >= 1 and real symmetric J | Theorem 1.1; equations (4)--(6) have delta = exp(-4 sum of absolute off-diagonal interactions) > 0 | All finite interactions; no sign or spectral-smallness assumption |
| Every partition of [n] | Conserved parts in the original law (1), block sums in Section 2 and the two-copy constraints in Section 3 | All partitions, including one part and all singleton parts |
| Every replica count N >= 2 | Theorem 1.1; Lemma 2.2 leaves at most 2^n unpaired subset types; Lemma 2.3 has a count-independent constant | Uniform in N, without normalization by N |
| Every feasible integer magnetization vector M | Original constrained set in Section 1; Section 3 converts both copies' constraints into zero disagreement totals | All feasible totals, including extremes and sparse disagreement counts |
| Every real field array v in R^(Nn) | Equation (1); pair-energy identity in Section 3 cancels the field exactly after fixing the coordinatewise sum | Arbitrary heterogeneous replica/site fields; no bounded-field assumption |
| Ordinary Euclidean covariance of all Nn spins | Equations (2)--(3); final Cauchy--Schwarz argument in Section 3 | Exactly the required full-spin operator norm |
| Finite C(J,A), independent of N,M,v | Lemmas 2.2--2.3 give L > 0 and U < infinity; Proposition 2.1 gives U/L; Section 3 gives C = 2U/L | Full simultaneous uniformity; explicit unoptimized constant |

The original measure is identical to equation (1). Its density convention in
Caputo--Morellini Definition 1.9, equations (1.23)--(1.24) of the v1 PDF is related to the integer totals by
rho(A) = (1 + M_A/(N |A|))/2, as stated in the manuscript. Since a fixed finite
set has finitely many partitions, their constants can also be maximized to
obtain a bound depending only on J.

Caputo and Morellini, arXiv:2511.05223v1, Section 4.5, is the source of the
covariance conjecture. The manuscript cites Proposition 3.6 and Section 3.4
for the restricted high-temperature benchmark. Its proof of the new bound
uses no imported analytic theorem, numerical certificate or hidden supplement.

This is a complete analytic solution claim. It does not assert an optimal
constant, a separately proved entropy-decay theorem, formal verification,
independent human review, or upstream acceptance.
