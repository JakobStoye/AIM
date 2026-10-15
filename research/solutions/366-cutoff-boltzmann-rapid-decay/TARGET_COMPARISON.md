# Target comparison: AIM 366

Original: [Continuation of the cutoff Boltzmann flow from macroscopic bounds](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/366-cutoff-boltzmann-continuation.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted result: Theorem 1.1 and Corollary 5.1 of *Loss of rapid velocity decay in a broad smooth class for the cutoff Boltzmann equation*.

| Original requirement | Result and manuscript location | Scope |
| --- | --- | --- |
| Hard-sphere kernel, full sphere and specified post-collision velocities | Equation (1.1), Section 1; radial normalization in (2.2)–(2.4) | Same model and sphere measure of total area `4 pi` |
| Domain `[0,T) x T^3 x R^3` for finite `T` | Theorem 1.1, Corollary 5.1; restrict a homogeneous radial solution to any `0<T<t_*` | An admissible special case suffices for a counterexample to a universal assertion |
| Nonnegative smooth solution | Sections 4–5; Propositions 4.1–4.2 and compact maximum argument | Joint pointwise smoothness up to time zero and at all finite velocities, including zero |
| Initially rapidly decreasing datum with rapidly decreasing derivatives | Equation (1.3) and Section 5: Gaussian datum | All spatial and velocity derivatives are Schwartz; correction time jets vanish initially |
| Uniform positive lower and finite upper local mass | Equation (1.3), Section 5 | Mass is identically one, so `m_0=M_0=1` |
| Uniform local energy upper bound | Equation (1.4), final part of Section 5 | Finite bound from a uniform `X_6` norm; no energy conservation or energy inequality is asserted |
| Uniform local entropy upper bound | Equation (1.4), final part of Section 5 | Positive and negative entropy parts are finite; upper bound follows from mass and a uniform pointwise bound |
| Extension with rapid velocity decay | Equation (1.5), Corollary 5.1 | Every continuous endpoint extension has a positive `r^-6` tail, which excludes rapid decay |
| Quantifiers and constants | Theorem 1.1, final part of Section 5 | One fixed positive `epsilon` and short interval suffice; all macroscopic bounds are uniform in time and space |
| Imported kinetic existence theorem | None | The construction is proved in the manuscript. The three references are contextual; the exact theorem comparison with Lu–Wennberg remains unverified |

The result is a proposed negative answer to the literal rapid-decay conclusion when “smooth” means joint pointwise smoothness and no energy-admissibility or positive-time Schwartz condition is included in the solution class. The example already continues smoothly in `X_6` across every chosen endpoint `T<t_*`. It therefore does not establish local derivative blowup, failure of critical-weight smooth continuation, or resolution of a conservative/energy-admissible continuation formulation.

Related weak energy-increasing solutions are credited in Section 1. This package makes no novelty or priority claim and does not assert that the literal interpretation settles every conventional conditional-regularity question.
