# Comparison with the pinned target

Target: [Boundary control to equilibrium for a parabolic obstacle problem,
Problem 398](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/398-parabolic-obstacle-boundary-control.md),
revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
Result: Theorem 1 in the [complete manuscript](paper/obstacle_control_counterexample.pdf)
gives a counterexample to the entire universal assertion as written.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Interval `(0,1)`, smooth real obstacle, negative endpoint values and positive maximum | Equation (3) gives a polynomial obstacle with endpoint values `-3` and maximum `1`; data verification in the proof of Theorem 1 | All obstacle premises met by one fixed example |
| Unique stationary minimizer of the Dirichlet energy above the obstacle with zero endpoint values | The same minimizer is defined in Section 1; Lemma 1 proves it equals `1` on `[1/3,2/3]` | The original target state, with no replacement target |
| Initial datum in `H^1_0(0,1)` above the obstacle | `y_0=9x(1-x)` in equation (3); proof gives `y_0-psi=81(x(1-x)-1/6)^2+3/4>0` | Smooth initial datum satisfies every premise |
| Some finite time `T > 0` and endpoint controls in `H^1(0,T)` | Theorem 1 quantifies over every finite `T > 0` and every such pair of admissible controls | Excludes all permitted times and controls for the fixed data |
| Controls start and end at zero and stay above the obstacle's endpoint values | Equation (2), retained in Theorem 1 | Includes all stated compatibility and lower-bound restrictions |
| Dynamics interpreted by the associated parabolic variational inequality | Equations (5)-(6), the affine boundary lift and the admissible upward variation in the proof | Uses only energy-space regularity and a necessary consequence of that same inequality |
| Terminal equality with the stationary minimizer in `L^2(0,1)` | Equation (4) gives a strictly positive norm bound; the final part of the proof passes the scalar distributional estimate to the terminal `L^2` trace | The requested exact equality fails for every finite time |

The question is universal over admissible obstacles and initial states.
One admissible pair with no successful finite-time control is therefore a
complete negative answer. The proof does not claim failure for every obstacle,
and its bound tends to zero as time tends to infinity. Approximate or
asymptotic steering and restricted contact geometries are outside the conclusion.

The evidence is an analytic proof. No numerical case, finite enumeration,
computer-assisted certificate or formal proof is used. This package is a
solution claim awaiting independent mathematical review.
