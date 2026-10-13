# Target comparison for AIM 415

Original target: [415. Uniform control of Neumann advection–diffusion for non-gradient flows](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/415-nongradient-neumann-uniform-control.md).

Statement revision: `c9929805cece044705abaaebe1cebddac1ba11a6`.

Submitted result: Theorem 1.1 in [the finished manuscript](paper/main.pdf), *Uniform Neumann control for strictly outward non-gradient flows*. Locations below refer to that manuscript. This comparison uses the public problem and the manuscript, and describes the submitted theorem claim.

| Original requirement | Manuscript location and result | Coverage |
| --- | --- | --- |
| Bounded connected smooth domain in R^d, d >= 2 | Section 1, before (1), and Theorem 1.1 | Same domain and dimension; no simply connected or convex assumption |
| Nonempty open omega compactly contained in Omega | Section 1, before (1), and (3) | Same interior observation/control region |
| Autonomous B in W^{2,infinity}(R^d;R^d) | Section 1 uses its C1,1 representative | Same global regularity; no smoother drift assumption |
| B dot nu >= c0 > 0 on all of the boundary | Equation (1) | Same strict inequality, including all boundary components |
| Global backward flow X' = -B | Section 1 defines F_s; Section 4 identifies the source's flow by Phi(t,t0)=F_(t0-t) | Same sign and time direction |
| Fixed T0,r0 > 0; for each x in the closed domain some sx in (0,T0) carries the entire open r0-ball into omega | Equation (2); Section 4's closed half-radius inclusion | Same quantifier order; the half radius verifies the cited source's convention without strengthening the original premise |
| No scalar potential representation B = grad f | Theorem 1.1; Section 2, (7)--(9) | The scalar Poisson function changes only the boundary normal component and does not assert B is a gradient |
| y_t - epsilon Delta y + B dot grad y = 1_omega h and homogeneous Neumann condition | Equation (3); Section 2's variational realization | Same state equation and boundary condition |
| Every initial y0 in L2(Omega) | Theorem 1.1 and Section 4's dual construction | Same arbitrary data class; Appendix B justifies observation for all L2 adjoint terminal data |
| Finite T_*; every T > T_* | Section 4 selects an integer m and L=mT0+1; Theorem 1.1 sets T_*=L | Proves every T >= T_*, hence the requested strict range |
| For each such T some C_T and epsilon_T independent of epsilon and y0 | Equations (27)--(29) and Theorem 1.1 | Proves a common C_T=C and epsilon_T=1 for all T >= T_*; constants may depend on the fixed geometry and drift/flushing data |
| Every 0 < epsilon < epsilon_T | Theorem 1.1 and (29) | Proves the full interval 0 < epsilon < 1 |
| h in L2((0,T) x omega), y(T)=0, norm bound C_T times norm of y0 | Closing Hilbert-space and weak duality argument in Section 4 | Same control space, nullity in L2 and homogeneous norm bound |

The fixed-time observation calculation in Section 3 gives an exponential loss of order exp(K_o/epsilon). Section 4 applies the general-drift dissipation estimate on one fixed ambient horizon, chooses m so that m delta_d > K_o, and obtains a uniform observation constant. Restricting any longer-horizon adjoint to that fixed interval gives the same bound for all larger control times.

Public dependencies and their roles:

| Source and locator | Use and applicability |
| --- | --- |
| Et-Tahri, Barcena-Petisco, Boutaayamou and Maniar, [arXiv:2412.16660v1](https://arxiv.org/html/2412.16660v1), Proposition 4.7(1), equation (51), and Proposition 4.5 | General-drift dissipation for the original adjoint. Section 4 checks nonnegative boundary flux, global W1,infinity regularity and the exact closed-ball flushing condition. The decay exponent is fixed before the finite ambient horizon; the prefactor can depend on that fixed horizon. No gradient assumption is imported. |
| Same source, equation (64), and Propositions 3.6 and 3.9 | Interior Carleman weight and fixed-viscosity strong-solution regularity. Section 3 and Appendix B state their uses. |
| Nardi, [arXiv:1302.4103v4](https://arxiv.org/abs/1302.4103v4), Theorems 3.1 and 5.2 | Compatible C2,alpha Neumann Poisson solvability in Section 2 and classical -Delta+1 solutions used in Appendix B. The weak H2 estimate and density passage are proved there. |
| Dier, [arXiv:1406.2884v2](https://arxiv.org/abs/1406.2884v2), Theorem 1.1 | Lions' variational existence theorem for bounded coercive forms, after the fixed-viscosity shift in Section 2. It is used for weak well-posedness, rather than a stronger symmetric-form regularity assertion. |
| Et-Tahri et al., [arXiv:2308.07497v1](https://arxiv.org/html/2308.07497v1), Theorem 1.4 and Section 6 | Section 6 supplies the tangential mixed-product lineage. Theorem 1.4's interior flushing premise cannot hold for boundary trajectories of a Lipschitz tangential flow, as explained in the later paper's Remark 1.6. That conditional theorem is not a proof premise here. The manuscript supplies its own potential and Robin boundary calculation. |

The submission claims the full original autonomous, strictly outward target. Merely nonnegative boundary flux, time-dependent drift and an optimal threshold are outside this manuscript's result. The argument is analytic; numerical testing and formal verification are not claimed. Mathematical acceptance remains a matter for independent review.
