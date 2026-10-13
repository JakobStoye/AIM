# Comparison with the original target

Original statement: [417. Polynomial growth of reachable neighborhoods for analytic control systems](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/417-analytic-reachable-set-polynomial-growth.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted result: Theorem 1 of [the manuscript](paper/main.pdf), *Small-time controllability without polynomial reachable neighborhoods*.

| Original requirement | Manuscript result and location | Scope |
| --- | --- | --- |
| Analytic control-affine fields near the origin in dimension `n >= 3` | Equation (2) and Theorem 1 give a polynomial system on all of `R^5`, with constant input fields in coordinates 1 and 5. | An admissible `n=5`, `m=2` system suffices to refute the universal implication. |
| Equilibrium drift `X_0(0)=0` | Every drift component in equation (2) vanishes at zero. | Exact. |
| All measurable controls in the cube `[-1,1]^m` | Theorem 1 uses the entire two-input cube; Section 2 proves the negative-axis bound for every such control. | No restriction on switching or control smoothness. |
| Endpoints in time at most `t`, with trajectories in the fields' domain | Section 2 constructs unique global trajectories by successive integration. The monotone bound applies to every duration at most `t`. | The domain is all of `R^5`. |
| The origin is interior to the reachable set for all sufficiently small positive `t` | Theorem 1, equation (3), and its Section 3 proof reach a full Euclidean ball for every `t>0`; the loop and steering use at most `5t/8`. | Stronger time range, same full-dimensional premise. |
| Some system-dependent `C,T>0` and integer `N>=1` provide a polynomial inner ball at all `0<t<T` | Equation (4) bounds every negative fourth-axis endpoint by `t^11 exp(-1/(6t))/4`. The last paragraph of the proof excludes `-(C/2)t^N e_4` for sufficiently small `t<T`, for every proposed triple `C,T,N`. | Complete negation of the asserted conclusion for this one system. |
| Public mathematical dependencies | Absolute-continuity integration and integration by parts are used on finite intervals; the cited Hunter Appendix 3.A gives Theorems 3.60 and 3.62. The quartic identity, concentration family and controllability argument are proved in the paper. | No external controllability theorem or computational certificate is assumed. |

The comparison is between the finished manuscript and the original statement. It makes no separate claim about dimensions three or four, a sharp attainable radius, human verification or formal verification. The proposed counterexample is submitted for independent mathematical assessment.

Jafarpour's Conjecture 1.2 (PDF p.3) in arXiv:1604.02432v7 supplies the growth question. Beauchard--Marbach, arXiv:2608.28582v1, Section 6 supplies the quartic-system motivation; its Lemma 6.1 and Remark 6.2 are described at their stated scope. Neither source is cited as having proved the counterexample.
