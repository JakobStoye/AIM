# Correspondence with AIM Problem 258

Original target: [Global constrained null control of a two-phase Stefan interface](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/258-global-two-phase-stefan-control.md), revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

The comparison uses the public problem and the accompanying complete manuscript. The contribution is an affirmative analytic solution claim awaiting mathematical review.

| Original requirement | Manuscript result and location | Scope |
|---|---|---|
| All L,d_l,d_r,lambda,T strictly positive | Theorem 1; Section 2 exact normalization | Full parameter range; constants may depend on all data |
| L0 and LT strictly between 0 and L | Theorem 1; Section 5, equation (11) | Full interior range; convex interpolation preserves strict interiority |
| Arbitrary real y0,z0 in the stated compactly supported smooth phase classes | Theorem 1; Lemma 3 | All signs and amplitudes; no extra initial sign or smallness condition |
| Heat equations with the two physical diffusivities | Section 2; equations (3), (8), (12); closing proof | Exact physical coefficient restoration |
| Two exterior Dirichlet controls in L-infinity(0,T) | Theorem 1; Lemma 7, exterior trace construction | Continuous, hence bounded, controls; no common amplitude ceiling |
| Both interface temperatures zero | Lemma 3 homogeneous interface traces; Lemma 5 beta0=0; equation (12) | Pointwise throughout the constructed solution |
| d_l y_x(ell^-)-d_r z_x(ell^+)=-lambda ell' | Section 2, equation (1); p_plus=p_minus-f in equation (10) | Exact sign and length/latent-heat factors |
| Initial profiles and ell(0)=L0 | Lemma 3; Lemma 6 and the open overlap (a/2,a) in Lemma 7 | Initial evolution retained without modification |
| Whole-time C1 interface with 0<ell<L | Lemma 3 at t=0; equation (11), flat cutoff jets and open-overlap join | All t in [0,T] |
| Terminal y=z=0 and ell(T)=LT | Lemma 7; vanishing jets after 2a<T | Exact terminal state, reached before T |
| Zero extensions continuous into L2(0,L) | Final paragraph of Lemma 7 and Section 2 scaling | Strong continuity including initial time and moving-interface crossings |
| No positive minimum control time | a=min(delta,T)/4, Lemma 7 | Every T>0; costs are not estimated uniformly |
| Applicability of imported flatness results | Lemma 5 and its proof; Colle--Loheac--Takahashi Proposition 3.4 and Corollary 3.6, HAL-03721544v1 | Global Gevrey outputs with order less than 2; coefficient result has no sign or smallness requirement |
| Analytic initial-data bridge | Lemmas 2--4 and 6 | Proved in the manuscript; not borrowed from the source's sign-restricted main theorem |

No claim is made about sign-preserving controlled paths, rougher initial data, higher dimensions, a shared bound on control amplitudes, or independent human/formal verification.
