# Correspondence with AIM problem 067

Original problem:
[067 -- Exact uniform control time near a viscous Burgers shock](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/067-burgers-shock-uniform-control-time.md),
revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted manuscript: [Exact uniform control time for a centered viscous
Burgers shock](paper/main.pdf), by Kaiwen Jin.

| Original requirement | Manuscript result and retrieval point | Coverage |
| --- | --- | --- |
| Every fixed L>0; interval (-L,L) | Introduction and Theorem 1.1; exact norm-preserving scaling at the end of Appendix A | Identical parameter and domain class |
| Exact coefficient -tanh(x/(2 epsilon)) and linearized equation | Introduction, equation (1.1); adjoint and conjugation in Section 2 | Identical coefficient and normalization |
| One left Dirichlet boundary control h in L2(0,T), with u(t,L)=0 | Equation (1.1), equations (2.2)--(2.3), Appendix A | Identical actuator, endpoint and control norm |
| Supremum over the entire unit sphere of L2 initial data | Equation (1.2), Theorem 1.1(1), graph-domain density in Section 2.3 and control construction in Appendix A | All initial data; exact terminal zero in the usual transposition solution |
| Finite viscosity limsup of the worst-case cost | Theorem 1.1(1) and equation (3.18) | Uniform bound for every sufficiently small positive viscosity whenever T>4 sqrt(2)L |
| Exclusion of all smaller positive times | Theorem 1.1(2), equation (1.5), and Section 4 | Cost diverges for every 0<T<4 sqrt(2)L, with admissible viscosity-dependent adverse data |
| Exact dimensionless infimum T_unif/L, closing the stated interval | Theorem 1.1 and the last paragraph of Section 4.2 | Complete solution claim: T_unif/L=4 sqrt(2) |

The upper bound controls the full spectrum: the determinant estimate in
Section 3.1 bounds every fast index, Section 3.3 compares finite-time and
half-line observations uniformly in truncation, and Section 3.4 separates
the near-zero mode. Section 2.3 and Appendix A extend the estimate to the
original full L2 control problem. In the lower bound, Section 4.1 uses one
common layer for all retained indices, and Section 4.2 explicitly controls
the omitted product tail. Thus a finite spectral construction is used as
an admissible test, rather than substituted for the full target.

The external analytic inputs are regular separated Sturm--Liouville theory,
Hadamard factorization, Laplace/Hardy unitarity, the constant-one model-space
Bernstein inequality, and convergent analytic products. They are stated or
specialized at their use and cited to public sources in the manuscript.
In particular the Bernstein input is Baranov, Jaming, Kellay and Speckbacher,
Theorem 5.2, with the half-plane and norm translations given in Section 3.3.

Boundedness of the cost exactly at T=4 sqrt(2)L is not asserted. This does not
remove a case from the original infimum question. The manuscript makes no
claim for off-center shocks or the nonlinear equation.

The submission is an analytic solution claim awaiting independent mathematical
review. AI assistance is disclosed in the manuscript. No detailed AI review
report or formal-verification claim is included.
