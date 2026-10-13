# Comparison with AIM Problem 386

Target: [Boundary observation of a Schrödinger field with slower surface dispersion](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/386-slow-surface-schrodinger-observability.md).
Pinned repository revision: `c9929805cece044705abaaebe1cebddac1ba11a6`.
Submitted argument: Theorem 1 of [the manuscript](paper/exterior_observability.pdf).

The source asks whether, for every positive time, a finite constant bounds the initial bulk-plus-surface gradient energy of every smooth compatible solution by its full outer Neumann observation. The submitted theorem gives a negative answer for each positive time.

| Source requirement | Manuscript location and correspondence |
| --- | --- |
| Planar annulus with radii 1 and 2; inner and outer circles | Section 1 defines exactly this domain and both boundary components. |
| Bulk Schrödinger equation with coefficient 1 | Equation (1); the radial realization is equation (5). |
| Outer Dirichlet condition | Equations (1) and (5); the operator domain requires the radial function to vanish at radius 2. |
| Inner trace equals the bulk boundary value | Equation (1); the surface coordinate is the trace in Section 2. |
| Surface coefficient 1/2 and outward normal from the annulus | Equation (1); Section 2 derives the inner equation with the sign from the inward radial normal. |
| Exact bulk-plus-surface gradient energy | Equation (2); equation (6) identifies it with the angular-mode quadratic form. |
| Full outer boundary observation with surface measure | Equation (6) gives the exact factor 2 from the outer radius, used in Section 4. |
| Public functional-analysis inputs | Sections 2–3 use Teschl, second edition, Theorems 2.14 and 5.1 and Lemmas 1.12–1.13. The manuscript verifies the dense closed form, self-adjoint realization and bounded derivative hypotheses before applying these results. |
| Smooth compatible solutions | Section 4 constructs exact unitary evolutions from data in every operator-power domain and verifies smoothness and all boundary compatibility identities. |
| Every fixed positive observation time | Theorem 1 provides one sequence with energy one and observation at most a time-dependent constant times `n^6 exp(-2 c n)`, for every positive time; the sequence and positive decay constant do not depend on time. |
| Constant independent of the particular solution | The observation tends to zero along that sequence while its energy remains one. No finite solution-independent constant can satisfy the proposed inequality. |

The collar eigenfunction is an auxiliary construction on a shorter annulus. The final counterexamples are exact solutions on the full prescribed annulus, rather than solutions on the collar or approximate solutions. The graph norm comparison in Section 4 controls the observed derivative, and energy normalization completes the contradiction.

The full pinned target is addressed. The manuscript makes no claim about other surface coefficients, other geometries, nonlinear models, or a uniform estimate as time tends to infinity. There is no remaining case of the pinned question asserted open within this submission.

Evidence status: complete analytic counterexample claim, developed and checked with AI assistance. No independent human review, formal proof, or upstream acceptance is claimed. A detailed AI review report is not included; independent mathematical review is requested.
