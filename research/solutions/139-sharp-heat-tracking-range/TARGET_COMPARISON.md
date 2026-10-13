# AIM 139: comparison with the original target

Original statement: [problem 139 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/139-sharp-heat-tracking-range.md).

Submitted argument: [A constructive characterization of exactly trackable heat fluxes](paper/heat_tracking.pdf), by Kaiwen Jin; [standalone source](paper/heat_tracking.tex). Theorem 2.1 gives the necessary and sufficient target class; Theorem 6.1 gives the sharp initial-time evaluation restrictions. This is a complete solution claim awaiting mathematical and maintainer review.

| Original requirement | Result and location in the manuscript | Scope |
| --- | --- | --- |
| Every bounded connected smooth domain in Euclidean dimension at least two | Section 1 and Theorem 2.1; Lemma 2.2 constructs all auxiliary objects | Same hypotheses; no analytic boundary, special geometry or dimension upper bound |
| Every positive finite horizon | Sections 1–2; all coefficient and trace tests use the original interval | Every T > 0; no small-time restriction |
| Nonempty relatively open control and observation patches with disjoint closures | Section 1, tests D–E and Theorem 2.1 | Exact original patches; no smooth-edge assumption |
| Arbitrary square-integrable Dirichlet controls on the control patch | Section 3, especially Lemma 3.2 | Full boundary-time L2 class; smooth data are used for density only |
| Zero initial transposition solution of the heat equation | Equation (16), Lemma 3.2 and Section 5 | The reconstructed state satisfies the original transposition identity |
| Outward normal flux on the observation patch | Sections 1 and 6, equations (2), (17) and (29) | Original outward-normal convention, with the separated flux kernel K < 0 |
| Regularity conditions on the target itself | Test A and test B, equations (5)–(8) | Causal local smoothness, initial flatness, explicit coefficient summability, heat recurrence and overlaps |
| Necessary and sufficient compatibility | Tests C–E and Theorem 2.1, proved in Section 5 | Volume L2, strong parallel traces, support and observed normal trace are necessary and sufficient together |
| No existential control or extension restatement, abstract dual inequality or singular-system membership | Root derivatives and fixed binomial translations in test B; explicit functions in equation (9) | Every continuation coefficient is computed from the target; subsequent conditions test these computed quantities |
| Compatibility with the actual control support | Test D, equation (12) | Literal complement of the control patch, including edges of positive surface measure |
| Compatibility on the entire observation patch | Test E, equation (13) | All compact coordinate subsets and all components; the seed is only a reconstruction device |
| Sharp quantitative restrictions near initial time | Theorem 6.1, equations (29)–(31) | Exact point-evaluation norm, optimal constant one, fixed-target little-o and no universal prescribed extra decay factor |
| Quantifiers in the no-extra-rate assertion | Proof of Theorem 6.1, pp.12–13 | For each positive factor tending to zero, one fixed L2 input and target defeat that factor along times tending to zero |
| All geometric continuation choices valid | Lemmas 2.2 and 4.1–4.2; Theorem 2.1 | Radii fixed by geometry; finite tree paths; every time derivative uniform through the one-sided terminal endpoint |
| Uniformity and constants | Sections 3–4 and Theorems 2.1, 6.1 | Trace bounds depend on the fixed domain and horizon; Taylor radii are fixed independently of data; coefficient bounds may depend on the local function and derivative order |
| Concrete function-space structure | Theorem 2.1 and equation (14) | Exact causal input norm, unique recovered control, Hilbert range isometric to the original L2 control space and independence from auxiliary choices |

The squared evaluation scale is the integral of the squared separated forward kernel over the control patch and elapsed time. It is smooth and flat at zero; no smoothness claim for derivatives of its square root at zero is needed. The scalar pointwise restriction is not a sufficient condition by itself: the full target class retains continuation, time dependence and patch support.

The characterization is an infinite family of explicit regularity and compatibility tests. It does not claim a finite membership algorithm, a universal named Sobolev/Gevrey space or a closed geometric short-time asymptotic. These limits are stated in the manuscript.

## Public dependencies and comparison

Grieser's *Notes on Heat Kernel Asymptotics*, Theorems 3.1 and 3.12 and Definitions 2.1 and 3.3, supply the forward Dirichlet heat kernel, its precise smoothness and off-diagonal properties. Hunter's *Measure Theory*, Theorems 4.6, 4.24, 5.18, 7.7 and 7.10, and *Notes on Partial Differential Equations*, Sections 1.9–1.12 and 5.A–5.B, supply the stated elementary integration, mollification and Fourier conventions. The complete manuscript derives its trace bridge, source cancellation, continuation estimates, strict signs and range equivalence.

Bárcena-Petisco–Zuazua provides tracking background; Davron–Lissy gives the exact interval criteria and finite-time compatibility discussed in the Introduction. Puzyrev–Shlapunov, Theorem 2, is the classical heat-potential continuation antecedent. Their restricted or existential criteria are not imported as a theorem for the present full L2 multidimensional target. Every reference is linked in the manuscript, with the inspected arXiv versions pinned where applicable.

The argument and reference uses have received AI checks described in the [package README](README.md). No human/formal certification or upstream acceptance is asserted; catalogue classification is left to the maintainer.
