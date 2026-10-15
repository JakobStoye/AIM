# AIM 540: quadratic barrier growth on a hyperbolic ball

**PR:** [119](https://github.com/MColbrook/AIM/pull/119). **Head:** `de7478fb7a79bf2b815e447c7aa60e645a8f4630`. **Date:** 2026-10-15. **Decision:** Solved.

Independent Codex AI review in the maintainer's session, without preparation of the submission. No human or Lean verification is claimed. The entire five-page source/PDF, README and target comparison were examined against the pinned/current target, particularly its arbitrary-triple third-derivative inequality.

[Proof](../../solutions/540-hyperbolic-ball-barrier-parameter/paper/hyperbolic_ball_barriers.pdf).

At a circle maximum the positive tangential Hessian is at most the outward derivative times coth(r), forcing that derivative positive. The covector curvature commutator with the stated curvature convention has magnitude exactly the radial derivative. Both mixed self-concordance bounds therefore imply the radial Hessian lower bound tanh(r) squared divided by 16. A diagonal-only definition would not justify this step, but the AIM target explicitly supplies the two mixed instances.

I checked the nonsmooth maximum-profile step independently: subtracting the specified quadratic and an offending chord would produce an interior positive annular maximum, contradicting the radial second derivative bound. This proves scalar strong convexity without differentiating a moving maximizer. Even convexity gives the initial nonnegative slope, then a linear lower slope. The gradient inequality along every full radial geodesic gives reciprocal-derivative decay and the opposing slope bound theta/(R-r). Taking the middle radius yields the claimed uniform quadratic lower bound for every nonsymmetric barrier. Neither existence of an optimal barrier nor a shared choice across radii is assumed.

The upper construction is genuinely imported from [Hirai--Nieuwboer--Walter v2](https://arxiv.org/pdf/2303.04771v2): Theorem 5.16(i) is the mixed-slot bound for squared distance with constant eight at curvature minus one, and Theorem 1.6 gives the printed epigraph function and pointwise Newton bound. Polarization in the last two slots loses no constant. Restriction to the totally geodesic constant-S slice preserves the covariant tensors, supplies the exact function used, and bounds the parameter by 1+2R squared. Its displayed Hessian is positive also at the center, and boundary divergence gives ambient closedness of the epigraph.

All three bibliography entries were examined. [Criscitiello--Nieuwboer--Walter v1](https://arxiv.org/pdf/2604.07319v1), Corollary 1.4 and its following paragraph, give the benchmark and distinguish weaker geodesic self-concordance; [Hirai v2](https://arxiv.org/pdf/2212.10981v2) is accurately credited as construction context. The source versions and cited theorem content are consistent; no proof-critical reference is missing. All five rendered PDF pages are legible and consistent with the source; build/integrity receipts are handled separately in integration.

No unresolved gap was identified for the exact full-tensor definition. The distinct diagonal-only optimization question remains separate and is not the AIM target being marked solved.
