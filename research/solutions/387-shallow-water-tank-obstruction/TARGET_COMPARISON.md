# AIM 387: target correspondence

Target: [387. The sharp local maneuvering time for a shallow-water tank](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/387-shallow-water-tank-sharp-control-time.md),
at repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted result: Theorem 1 of *Failure of local controllability at time 21/10
for a shallow-water tank*, by Kaiwen Jin. The manuscript is a proposed complete
negative resolution of the stated universal sufficiency question.

| Original requirement | Manuscript location and result | Coverage |
|---|---|---|
| Normalized Saint--Venant equations on 0 < x < 1, tank acceleration as the continuous scalar control, velocity walls, s'=a and D'=s | Section 1, equations (1)--(2); Section 2 unfolds this exact system | Same model and normalization |
| Positive C1 depth of mass one, C1 velocity zero at the walls, equal wall depth derivatives | Section 1 defines the same state space; equations (4)--(5) construct the terminal family; the proof of Theorem 1 checks all conditions | All counterexample states are admissible |
| Equilibrium (1,0,0,0), arbitrary small endpoint neighborhoods | Initial state is exactly equilibrium; terminal states (1+h_rho,v_rho,0,0) are O(rho) in C1 and tend to equilibrium | For every eta > 0, a member lies inside the required neighborhood |
| Sufficiency for every T > 2 | Theorem 1 fixes T=21/10 > 2 | One time above two disproves the universal statement; no assertion at T=2 is needed |
| For every trajectory tolerance epsilon, some endpoint neighborhood admits all transfers with a uniformly small classical trajectory and control | Theorem 1 fixes epsilon=1e-8; Section 4 derives a contradiction for every allowed trajectory to each sufficiently small nonzero terminal state | Exact quantifier negation: fixed epsilon, every eta, an unreachable pair |
| Tank position and velocity are part of the state | Both are zero at both endpoints; equation (23) derives U(T)=0 and integral U=0 | An allowed endpoint subfamily; zero displacement is used in the proof |
| Complete analytic proof of the negative alternative | Lemma 2 gives uniform nonlinear estimates; Proposition 3 computes the complete quadratic primitive; Lemma 4 proves separation; Section 4 projects the control primitive and closes the nonlinear contradiction | Complete manuscript argument; no numerical or hidden supplementary premise |
| Published dependencies and citations | References [1]--[3] locate the large-time result, original conjecture and below-two obstruction; the new proof is derived directly | Historical source claims have exact theorem/page locators; no control theorem is imported into the counterexample proof |

The remaining broader question is the least eventual local controllability
time. This manuscript only disproves sufficiency at every time above two.
Independent review of this claim is requested.
