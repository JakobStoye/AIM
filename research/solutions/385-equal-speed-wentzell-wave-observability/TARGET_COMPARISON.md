# Target comparison: AIM 385

Original target: [Observability of an acoustic shell at equal bulk and surface speeds](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/385-equal-speed-wentzell-wave-observability.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted result: Theorem 1 of [the complete manuscript](paper/equal_speed_observability.pdf), an analytic counterexample for the full prescribed model.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Planar annulus with radii one and two; inner and outer circles as stated | Section 1 defines the same domain and boundary components | Exact match |
| Bulk wave speed one, outer Dirichlet condition, inner trace identity and dynamic wave equation with surface speed one | Equation (1); Sections 2 and 3 verify each identity for the separated modes | Exact match |
| Outward annular normal and the circle Laplacian | Section 1 states the normal signs and unit-circle tangential operator; equation (7) derives the exact inner boundary determinant | Exact match |
| Full bulk-plus-surface energy, including both velocity and spatial terms | Equation (2) matches the original energy. Equation (14) evaluates it at zero displacement; equation (15) bounds its surface kinetic term from below | Exact match |
| Exterior squared normal derivative integrated with outer arclength and time | Equation (3) defines the same observation; equation (16) includes the radius-two arclength factor | Exact match |
| Every smooth compatible solution | Theorem 1 and its proof supply an infinite family of real solutions smooth up to both boundaries for all time, satisfying the equations exactly | Admissible counterexample family |
| A finite threshold time, followed by every larger time and a finite solution-independent constant | Theorem 1 and the final proof show failure for every finite positive time. The normalized observation is bounded by $`C T m^{-1/3}\to0`$, where $`C`$ is independent of time and order | Full negative answer |
| No extra geometric, spectral or initial-data assumption | The modes use zero initial displacement and their exact compatible velocity; any universal inequality must cover them | No added target assumption |
| Imported mathematical facts | Section 2 cites the conventional Bessel equation, Wronskian, fixed-angle Debye expansions, turning-point Airy expansions and Airy values in DLMF; Lemma 1 proves moving-argument uniformity rather than assuming it | Public cited inputs and proved specializations |

The 2022 annular paper is cited for its model and the strict inequalities between propagation speeds. The 2025 review is cited for its statement that equality remains open there. Neither contextual reference is used as a premise of the counterexample.

This submission claims a complete analytic negative answer for the stated annulus. It does not claim a sharp weaker-observability loss, a stabilization rate, or a result for arbitrary domains. Catalogue classification remains for maintainer review.
