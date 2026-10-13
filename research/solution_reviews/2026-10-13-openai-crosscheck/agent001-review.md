# Independent family001–124 target comparison

Systematic catalogue screen of every displayed OpenAI result family numbered001–124 against all665 AIM titles; full exact AIM target and actual primary theorem/source comparison for18 candidate overlaps. This is not an independent audit/reproof of all719 manuscripts. No repository edits or PDF uploads. Upstream TeX and Lean sources stored only in external scratch directory.

Pinned AIM `c9929805cece044705abaaebe1cebddac1ba11a6`; OpenAI `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

Screened 120 displayed families against 665 AIM titles. The pinned Contents catalogue has no entries numbered045,061,070,123. Identified14 full overlaps and4 substantive partial overlaps.

Lean documentation links are availability evidence. ComparatorChallenges contain placeholders; actual OAI endpoint source files were separately read where indicated. No local Lean-verified status is recommended without successful pinned replay and permitted-axiom output.

## AIM028 / OpenAI107: partial

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\028-matrix-multiplication-exponent.md`.
PDF: [preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf).
Locator: Theorem thm:main (section 1).

Exact complex arithmetic and arbitrary exponent slack match AIM. The theorem proves omega<=9/4, improving the previous upper bound; it does not prove omega=2 or omega>2. Rectangular exponent-two bounds do not establish the square exponent.

Outcome: Affirmative proof; recommended catalogue treatment: partial.

Lean: Actual endpoint complex_omega_le_nine_quarters is implemented; the comparator is a sorry-containing target file, not the certificate. This formalizes partial progress only; no replay/axiom log inspected.

Known cases/progress: The square exponent over C is at most 9/4, with O_epsilon(n^(9/4+epsilon)) exact arithmetic algorithms.
Remaining target: Determine whether omega=2; the new upper bound remains above two.

## AIM086 / OpenAI087: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\086-mahler-symmetric-four-dimensions.md`.
PDF: [preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf).
Locator: Theorem thm:main; equation eq:main-inequality.

Set n=4 in the unrestricted origin-symmetric convex-body inequality |K||Kpolar|>=4^n/n!. Compactness, nonempty interior, ordinary Euclidean polar and volume are exactly AIM hypotheses. Equality classification is extra, not needed.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: Actual endpoint symmetric_mahler has no external hypothesis beyond compactness/convexity/symmetry/nonempty interior. Set n=4. No successful local replay/axiom audit.

## AIM087 / OpenAI090: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\087-triangular-universal-optimality.md`.
PDF: [preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf).
Locator: Theorems thm:universal and thm:gaussian; transfer eq:gaussian-energy.

Use g(t)=exp(-pi*alpha*t) for every alpha>0. Any AIM periodic union of N translates of a lattice of covolume N is locally finite and has centered-disk density one. Its ordered-pair finite-disk energy per particle converges to the displayed per-cell average: each offset occurs with frequency 1/N, Gaussian tails are summable, and boundary pairs have vanishing normalized contribution. Both sides omit only equal-point self-interactions. The theorem therefore yields the full arbitrary-N periodic bound.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: Actual universal_energy_minimum proves the all-configuration completely-monotone energy statement, and sharp_gaussian_minorants_atomic supplies every Gaussian parameter. Periodic per-cell identification is a mathematical transfer, not a separately replayed AIM adapter. No local verification log.

## AIM092 / OpenAI093: partial

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\092-kls-poincare.md`.
PDF: [preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf).
Locator: Theorem thm:main; subgaussian condition eq:intro-subgaussian.

A dimension-free LSI implies a Poincare bound by linearizing the entropy inequality at a constant. It gives AIM for isotropic log-concave densities whose linear subgaussian parameter a is bounded by a fixed absolute constant; uniform convex-body densities are allowed. General isotropic log-concave measures may have only exponential tails, so the subgaussian assumption is a genuine restriction and cannot be discarded.

Outcome: Affirmative proof; recommended catalogue treatment: partial.

Lean: No matching Lean scope is declared in the family catalogue/docs inspected.

Known cases/progress: Dimension-free Poincare bounds hold for isotropic log-concave densities with a uniformly bounded linear subgaussian parameter; this follows from the stronger LSI with constant O(a^2).
Remaining target: A universal Poincare bound for all isotropic log-concave densities, including those without uniformly subgaussian linear marginals.

## AIM208 / OpenAI077: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\208-sphere-fourier-restriction.md`.
PDF: [preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf).
Locator: Theorem thm:main.

The theorem states precisely the same S2 extension, phase 2*pi*i*x.omega, surface area measure, complex bounded measurable inputs, and every p>3 with a constant depending only on p. It reaches all remaining exponents. The diagonal positively-curved-surface companion also implies this on S2 by finite-measure embedding.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: No matching Lean scope is declared in the family catalogue/docs inspected.

## AIM209 / OpenAI078: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\209-bochner-riesz-three-dimensions.md`.
PDF: [preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf).
Locator: Theorem thm:bochner-riesz; Corollary cor:full-bochner-riesz.

The primary L3 estimate holds for every positive order; the explicitly read analytic-interpolation and duality corollary gives all 1<=p<=infinity under delta>max(3|1/p-1/2|-1/2,0). Restricting to AIM 1<p<infinity gives exactly its multiplier and full strict range. No equality endpoint is needed.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: No matching Lean scope is declared in the family catalogue/docs inspected.

## AIM210 / OpenAI079: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\210-euclidean-wave-local-smoothing.md`.
PDF: [preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf).
Locator: Theorem thm:main; Corollary cor:full-range, eq:phys-full-range and its annular interpolation proof.

The half-wave and time interval [1,2] agree. The critical p=3 estimate permits every positive Sobolev loss; the read corollary/interpolation proof covers all p>2. For AIM p>=3 choose alpha=1-3/p+epsilon and localize to lambda<=|xi|<=2lambda; the annular multiplier bound gives lambda^alpha times the Lp input norm, uniformly in lambda>=1.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: No matching Lean scope is declared in the family catalogue/docs inspected.

## AIM234 / OpenAI090: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\234-abrikosov-global-crystallization.md`.
PDF: [preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf).
Locator: Theorem thm:main; definitions eq:cutoffs, eq:admissible, eq:local-energy, eq:whole-energy.

This companion is a separate direct theorem matching the Sandier-Serfaty/Abrikosov target. It uses the same divE=2*pi(sum delta-1), curlE=0, unit background, fixed-width smooth square cutoffs, puncture limit before limsup, self-energy pi*log(eta), normalization 4R^2, and covolume-one triangular field. Its density bound on centered disks is equivalent to AIM square growth bound by disk-square inclusions and local finiteness. The source derives local Lq (q<2) from the equations and permits nonperiodic competitors and infinite energies.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: Family090 Lean docs cover Gaussian minorants/universal nonnegative pair energies and circle packing, not this renormalized Coulomb field theorem; no full AIM234 Lean certificate established.

## AIM293 / OpenAI102: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\293-unique-games.md`.
PDF: [preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf).
Locator: Theorem thm:ugc.

Take the theorem errors epsilon=delta equal to AIM epsilon. The fixed alphabet F2^s depends only on the errors; translations are permutations. Output graphs are nonempty explicit unweighted simple bipartite instances, and value is ordinary classical fraction of satisfied edges. The deterministic polynomial reduction from 3SAT supplies exactly the NP-hard promise gap.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: Actual theorem11 returns BinaryGapReduction with a fixed alphabet/program before inputs, simple bipartite outputs, translations, completeness and soundness. No local replay/axiom log.

## AIM301 / OpenAI124: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\301-three-processor-unit-scheduling.md`.
PDF: [preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf).
Locator: Theorem thm:main; deterministic multitape time O((L+2)^150020).

Arbitrary explicitly listed DAG, nonpreemptive unit-length jobs and exactly three identical machines agree. Its slot values 1..T equal AIM start times plus one. The theorem treats n>=1 and 1<=T<=n: AIM extra cases are immediate in polynomial time (n=0 feasible, T=0 with n>0 infeasible, T>=n feasible by topological sequential schedule). Thus binary arbitrary deadline and empty input add no unresolved case.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: Actual main_theorem proves one finite machine and binary-input polynomial bound for nonempty n and normalized deadlines; the trivial edge-case adapter is not a separately replayed AIM theorem. No local verification record.

## AIM321 / OpenAI122: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\321-polynomial-trace-reconstruction.md`.
PDF: [preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf).
Locator: Theorem thm:main and thm:tv.

Definitions match known length n, fixed known deletion probability q in (0,1), independent complete deletion traces (including length), randomized decoder common to all binary strings, unrestricted computation and exact recovery. Set success s=2/3. For each fixed q, n^(c*log(q^3*log n)) eventually exceeds Cq*n^kq for every constants Cq,kq. Hence the requested polynomial-sample assertion is false at every fixed channel.

Outcome: Counterexample; recommended catalogue treatment: solved.

Lean: Actual superpolynomial_sample_complexity and quantitative_sample_lower_bound agree with the unrestricted complete-trace target; inspected estimator definitions include decoder randomization. No successful local replay/axiom log.

## AIM341 / OpenAI118: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\341-modified-integer-round-up.md`.
PDF: [preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf).
Locator: Theorem thm:unbounded-gap; Definition def:configuration-lp.

The source explicitly uses unrestricted numerical-size type patterns, whose multiplicities are limited by capacity rather than input demand; this is the exact nonproper-pattern LP in AIM. Set c=1: LP=B integer and OPT>B+1 refutes MIRUP without a ceiling ambiguity. Convert rational sizes to integer item lengths using a common denominator W; positive integer type demands are multiplicities. Removing excess items identifies integer covering optimum with packing optimum. This is an unconditional structural counterexample, independent of NP!=P.

Outcome: Counterexample; recommended catalogue treatment: solved.

Lean: Actual main_results proves unbounded gaps with both typeLP and individualLP equal integer B. The relevant typeLP preserves unrestricted patterns. Integer-length scaling is a mathematical adapter. No local replay/axiom log.

## AIM447 / OpenAI082: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\447-triangular-hilbert-transform-l3.md`.
PDF: [preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf).
Locator: Theorem thm:main.

The operator is literally AIM integral F(x+t,y)G(x,y+t)dt/t with both finite hard truncation endpoints. An absolute bound for the pointwise supremum over epsilon,R in L^(3/2), for arbitrary complex L3 inputs, dominates every individual truncation. This is a full resolution, stronger than AIM; it is not merely the dyadic companion.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: Actual main_estimate formalizes the maximal estimate and full-measure/measurability conditions with genuine hard integrals. No local replay/axiom log.

## AIM448 / OpenAI075: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\448-fourier-l-log-l-pointwise-convergence.md`.
PDF: [preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf).
Locator: Theorem thm:main.

Source torus R/(2*pi*Z) with normalized measure and e^(ikx) is AIM unit torus after x=2*pi*y. Integrability with log(2+|f|) is equivalent to log(e+|f|), with bounded ratio and finite measure. Both state complex measurable data and a single null set outside which the entire sequence of ordinary symmetric partial sums converges to f.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: Actual paperMain establishes full symmetric sums for measurable complex LlogL data on the normalized 2*pi torus; coordinate rescaling identifies AIM. No local reproduction/axiom log.

## AIM450 / OpenAI083: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\450-stein-lipschitz-direction-hilbert-bound.md`.
PDF: [preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf).
Locator: Theorem thm:main.

The theorem assumes all 1-Lipschitz unit fields on R2, allows both coordinates, holds at absolute outer scale a*>0, and proves a strong L2 principal-value bound and the exact weak-(2,2) inequality for Schwartz data. Choose AIM K=1/a* (>=1) and C=C*^2. Symmetric principal values exist pointwise on Schwartz inputs.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: Actual main provides principal-value and weak-(2,2) at an existential short scale; uniform_truncation additionally gives the reciprocal-Lipschitz bound. It discharges laceyLiInput through a proved import, not an external assumption in the endpoint. No local replay/axiom audit.

## AIM487 / OpenAI089: partial

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\487-gnrs-minor-free-flow-cut.md`.
PDF: [preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf).
Locator: Theorem thm:main in each manuscript.

The results establish constant distortion for all planar graphs and every fixed treewidth bound, with arbitrary positive real lengths and arbitrary demands. They do not cover every fixed excluded minor: minor-free classes can include nonplanar graphs of unbounded treewidth. Finite L1 metrics are finite nonnegative sums of cut metrics, giving AIM finite-dimensional real ell1. Nonnegative edge lengths are obtained by adding epsilon to each edge then taking a limit in the finite-dimensional cut cone (or contracting zero components); distortion constant is preserved.

Outcome: Affirmative proof; recommended catalogue treatment: partial.

Lean: Actual endpoints cover positive-length planar and fixed-treewidth metrics only. They do not formalize the full arbitrary-excluded-minor target or the zero-length transfer. No local verification record.

Known cases/progress: The GNRS embedding and equivalent arbitrary-demand concurrent-flow/cut bound hold for all planar graphs and for each fixed treewidth bound; constants are independent of graph size and edge-length ratios.
Remaining target: A constant depending only on every prescribed excluded minor H, including classes of nonplanar graphs of unbounded treewidth.

## AIM491 / OpenAI104: partial

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\491-simple-stochastic-games-polynomial-time.md`.
PDF: [preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf).
Locator: Theorem thm:main and explicit simple-stochastic-game reduction in section 1.

The deterministic algorithm has bit time 2^O((log(L+2))^2), which is quasipolynomial, not a fixed polynomial. The source explicitly reduces reachability >=1/2 to nonnegative expectation-of-liminf mean payoff with absorbing rewards +/-1, including nonabsorbing plays. AIM strict >1/2 is also obtainable: pure positional SSG values are rational with denominator at most 3^n by integer linear systems and Hadamard; positive 2v-1 is >=3^-n. Multiply all +/-1 rewards by 2*3^n and subtract 1 from every edge, so nonnegative mean payoff holds iff v>1/2. This has polynomial encoding length and preserves the quasipolynomial bound.

Outcome: Affirmative proof; recommended catalogue treatment: partial.

Lean: Docs104 formalize only randomized ordinary mean-payoff and a finite Truffet counterexample. They do not declare a formalization of this deterministic stochastic algorithm or AIM491.

Known cases/progress: The strict-threshold decision for arbitrary explicitly encoded simple stochastic games admits a uniform deterministic quasipolynomial bit-time algorithm, via the stochastic mean-payoff theorem and rational-gap threshold adjustment.
Remaining target: A uniform deterministic polynomial bound in binary input length, with equality v=1/2 rejected and no stopping or structural promise.

## AIM543 / OpenAI101: full

AIM: `C:\Users\MatthewColbrook\Documents\git_repos\AIM\problems\543-simplex-maximal-isotropic-constant.md`.
PDF: [preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf).
Locator: Theorem intro:simplex; equation intro:simplex-bound.

The source definition of L_K is exactly (det covariance/volume^2)^(1/(2n)), and its all-dimensional arbitrary-convex-body inequality has precisely AIM simplex constant. No symmetry/polytope restriction appears. Equality uniqueness is extra. This resolves the sharp target, not merely the weaker uniform slicing constant.

Outcome: Affirmative proof; recommended catalogue treatment: solved.

Lean: No matching Lean scope is declared in the family catalogue/docs inspected.

## Closest excluded targets

- OpenAI071 / AIM651: Circle-domain existence does not prove convergence of the CRDT conformal-map iteration.
- OpenAI081 / AIM426: Riesz-transform rectifiability concerns measures and singular-integral L2 boundedness, not the vector potential mixed-Sobolev inequality.
- OpenAI086 / AIM447: One-dimensional trilinear Hilbert shifts differ from the two-dimensional triangular bilinear operator; use family082 for AIM447.
- OpenAI090 / AIM449: Gaussian Gabor frame condition number depends on operator lower/upper spectral bounds, not simply pair energy; triangular energy minimality does not establish it.
- OpenAI092 / AIM349: Covering density and least packing density are different quantities.
- OpenAI096 / AIM294: Gaussian first-moment partition maximization (propeller) is not positive-correlation balanced simplex noise stability for q>=4.
- OpenAI097 / AIM564: Partial-sum rearrangement/signing bounds are not selecting <=2d points whose convex hull retains radius c/sqrt(d).
- OpenAI103 / AIM490: L=RL derandomizes logarithmic-space machines, and does not directly give deterministic polylog-depth circuits for general matching.
- OpenAI108 / AIM024: Permanent-vs-determinant complexity lower bounds are not a permanental dominance inequality.
- OpenAI111 / AIM330: Independent random values with one sample and ratio 2^-310 do not imply adversarial fixed weights in random order with sharp secretary ratio 1/e.
- OpenAI113 / AIM490: Randomized approximate counting, even with zero detection, is not deterministic uniform NC search.
- OpenAI116 / AIM310: Noncommutative matrix hitting for formulas does not decide arbitrary commutative circuits; even a commutative identity can have a nonzero free noncommutative lift.
- OpenAI118 / AIM315: Offline additive configuration-LP gaps do not determine optimal asymptotic competitive ratio of deterministic online bin packing.
- OpenAI119 / AIM327: Binary mutual-information contraction does not directly settle the influential-variable bound for bounded-degree real polynomials.
- OpenAI120 / AIM490: Randomized almost-linear sequential maximum matching does not establish deterministic NC depth/uniformity.
- OpenAI121 / AIM277: Almost-linear edit-distance approximation does not determine the exact asymptotic longest common-subsequence match fraction.

## Family-by-family screen

- 001: Milne’s rationality conjecture and algebraic specialization: no matching AIM target located
- 002: The full BSD formula from low Selmer corank: no matching AIM target located
- 003: The quasi-Riemann hypothesis: no matching AIM target located
- 004: Hilbert’s tenth problem over ℚ: no matching AIM target located
- 005: Irrationality of Catalan’s constant: no matching AIM target located
- 006: Goldfeld’s conjecture: densities and mean analytic rank: no matching AIM target located
- 007: Ordinary two-point correlations and the corrected Elliott conjecture: no matching AIM target located
- 008: The Deligne–Drinfeld conjecture: no matching AIM target located
- 009: Function-field reconstruction from Milnor K-theory and Galois data: no matching AIM target located
- 010: Unrestricted pro-modularity at the prime two: no matching AIM target located
- 011: Prime-factor statistics of $`p-1`$: no matching AIM target located
- 012: Independent largest prime factors of consecutive integers: no matching AIM target located
- 013: Ostmann’s inverse Goldbach conjecture: no matching AIM target located
- 014: Restricted geometric Langlands, global Arthur enhancements, and generic Ramanujan: no matching AIM target located
- 015: Torus-packet equidistribution in prime, quartic, and sextic degrees: no matching AIM target located
- 016: Zilber–Pink in abelian varieties and the Siegel threefold: no matching AIM target located
- 017: The irrationality exponent of <i>π</i> is 2: no matching AIM target located
- 018: The Margulis–Platonov conjecture over global fields: no matching AIM target located
- 019: The local <i>p</i>-adic section conjecture and global consequences: no matching AIM target located
- 020: Squarefree quartics and power-free polynomial values: no matching AIM target located
- 021: A quadratic bound for Jacobsthal’s function: no matching AIM target located
- 022: The weak inhomogeneous Duffin–Schaeffer conjecture: no matching AIM target located
- 023: Patterson's first moment for cubic Gauss sums: no matching AIM target located
- 024: An asymptotic formula for the number of totients: no matching AIM target located
- 025: Short Egyptian fractions: no matching AIM target located
- 026: Positive lower density of large prime gaps: no matching AIM target located
- 027: Potential integral density on curve character varieties: no matching AIM target located
- 028: Uniformly bounded components of Gaussian-prime graphs: no matching AIM target located
- 029: Primitive roots for every admissible integer base: no matching AIM target located
- 030: Modularity of elliptic curves over imaginary quadratic fields: no matching AIM target located
- 031: Uchida’s conjecture for open homomorphisms of Galois groups: no matching AIM target located
- 032: The rational Hodge conjecture for CM abelian varieties: no matching AIM target located
- 033: Iitaka subadditivity, variation, and logarithmic additivity: no matching AIM target located
- 034: Log abundance for compact Kähler spaces under logarithmic Iitaka subadditivity: no matching AIM target located
- 035: Log-canonical threefold abundance in numerical dimension one: no matching AIM target located
- 036: Numerical semiampleness and generalized minimal models: no matching AIM target located
- 037: The ordinary-double-point volume gap: no matching AIM target located
- 038: Fujita’s freeness conjecture: no matching AIM target located
- 039: Nagata’s conjecture and maximal Seshadri constants: no matching AIM target located
- 040: Bloch’s conjecture for complex surfaces: no matching AIM target located
- 041: Hyperkähler SYZ and projective-space bases: no matching AIM target located
- 042: Oka classification for minimal compact complex surfaces: Kodaira dimension zero and class VII: no matching AIM target located
- 043: <i>P</i> = <i>W</i> for fixed-determinant SL<sub><i>n</i></sub> moduli spaces: no matching AIM target located
- 044: The equivariant cohomological Hikita conjecture: no matching AIM target located
- 046: Shafarevich counterexamples in dimension two and with large fundamental group: no matching AIM target located
- 047: Zariski cancellation and affine fibrations over the complex numbers: no matching AIM target located
- 048: A characteristic-zero counterexample to Lipman–Zariski: no matching AIM target located
- 049: A stable-coordinate counterexample in four variables: no matching AIM target located
- 050: A counterexample to Griffiths’ positivity conjecture: no matching AIM target located
- 051: Kobayashi’s canonical-ampleness conjecture: no matching AIM target located
- 052: Tangent splittings and product decompositions: no matching AIM target located
- 053: A counterexample to Pixton completeness in Chow: no matching AIM target located
- 054: Irrational cubic fourfolds with Hodge-theoretic and categorical K3 associations: no matching AIM target located
- 055: Gepner symmetry and large-volume stability on threefolds: no matching AIM target located
- 056: Termination of projective and Kähler fourfold minimal model programs: no matching AIM target located
- 057: Fundamental groups of special complex varieties and root orbifolds: no matching AIM target located
- 058: Semialgebraic universal covers and bounded domains: no matching AIM target located
- 059: Counterexamples to Zariski’s multiplicity conjecture: no matching AIM target located
- 060: The Global Spherical Shell conjecture: no matching AIM target located
- 062: Projective contact classification and the LeBrun–Salamon conjecture: no matching AIM target located
- 063: The generalized Mukai conjecture: no matching AIM target located
- 064: Topological triviality of <i>μ</i>-constant surface singularities: no matching AIM target located
- 065: Virasoro constraints for complete intersections and projective-bundle towers: no matching AIM target located
- 066: Bounded klt complements for Fano contractions: no matching AIM target located
- 067: The Campana–Peternell conjecture in dimension six: no matching AIM target located
- 068: Anticanonical nonvanishing in every dimension: no matching AIM target located
- 069: Global quantum geometric Langlands at irrational level: no matching AIM target located
- 071: Koebe’s circle-domain conjecture: no matching AIM target located
- 072: Brennan's conjecture and the integral-means spectrum: no matching AIM target located
- 073: The Falconer distance conjecture: no matching AIM target located
- 074: Kakeya in three and four dimensions: no matching AIM target located
- 075: The $`L\log L`$ Fourier-convergence conjecture: candidate overlaps AIM 448
- 076: Real ultraflat Littlewood polynomials and unbounded binary merit factors: no matching AIM target located
- 077: Fourier restriction for positively curved surfaces: candidate overlaps AIM 208
- 078: The three-dimensional Bochner–Riesz conjecture: candidate overlaps AIM 209
- 079: Local smoothing in three dimensions: candidate overlaps AIM 210
- 080: The exact Sobolev endpoint for Schrödinger convergence: no matching AIM target located
- 081: Riesz transforms and rectifiability in higher codimension: no matching AIM target located
- 082: Annular variation and dyadic absolute bounds for the triangular Hilbert transform: candidate overlaps AIM 447
- 083: Hilbert transforms along Lipschitz directions: candidate overlaps AIM 450
- 084: The geometric case of the Erdős similarity conjecture: no matching AIM target located
- 085: Endpoint Sobolev regularity of centered disk averages: no matching AIM target located
- 086: An <i>L</i><sup>3</sup> bound for the trilinear Hilbert transform: no matching AIM target located
- 087: The Mahler conjectures, functional inequalities and polar-product symplectic width: candidate overlaps AIM 086
- 088: Sharp projection-body inequalities and a counterexample to simplex maximization: no matching AIM target located
- 089: Bounded-distortion <i>L</i><sub>1</sub> embeddings of planar and bounded-treewidth graphs: candidate overlaps AIM 487
- 090: Triangular-lattice optimality, long-range Riesz and Coulomb energies, and spherical logarithmic energy: candidate overlaps AIM 087, 234
- 091: Logarithmic and <i>L</i><sub><i>p</i></sub> Brunn–Minkowski inequalities and the B-conjecture: no matching AIM target located
- 092: The optimal order of convex-body covering density: no matching AIM target located
- 093: Dimension-free logarithmic Sobolev inequality for subgaussian log-concave measures: candidate overlaps AIM 092
- 094: Subpolynomial dimension reduction in <i>L</i><sub><i>p</i></sub>: no matching AIM target located
- 095: Hyperbolicity cones without semidefinite lifts: no matching AIM target located
- 096: The Gaussian propeller conjecture in every dimension: no matching AIM target located
- 097: The Euclidean Steinitz–Bergström bound: no matching AIM target located
- 098: Compact counterexamples to bi-Lipschitz dimension reduction: no matching AIM target located
- 099: The sharp exponential scale of edit-distance distortion: no matching AIM target located
- 100: Cylinder coverings below the half-area bound: no matching AIM target located
- 101: The sharp simplex conjecture for isotropic constants: candidate overlaps AIM 543
- 102: The Unique Games Conjecture and optimal approximation thresholds: candidate overlaps AIM 293
- 103: Exact derandomization of logarithmic space: $`\mathsf L=\mathsf{RL}=\mathsf{BPL}`$: no matching AIM target located
- 104: Quasipolynomial algorithms for mean-payoff, stochastic and parity games: candidate overlaps AIM 491
- 105: Perfect completeness for 2-to-1 games: no matching AIM target located
- 106: Hardness of coloring three-colorable graphs: no matching AIM target located
- 107: Matrix multiplication with exponent at most 9/4: candidate overlaps AIM 028
- 108: A cubic permanent–determinant lower bound: no matching AIM target located
- 109: Integer multiplication below $`n\log n`$: no matching AIM target located
- 110: Optimal-order randomized <i>k</i>-server on arbitrary metrics: no matching AIM target located
- 111: One-sample matroid prophet inequalities against an almighty adversary: no matching AIM target located
- 112: Beyond the square-root exponent for depth-three circuits: no matching AIM target located
- 113: Approximate counting and entropy of perfect matchings: no matching AIM target located
- 114: Approximate counting of common integer polymatroid bases: no matching AIM target located
- 115: Sampling and counting contingency tables with arbitrary margins: no matching AIM target located
- 116: Uniform black-box noncommutative identity testing across characteristics: no matching AIM target located
- 117: Uniform sparsest cut: hardness and semidefinite gaps: no matching AIM target located
- 118: Bin packing and unbounded configuration-LP gaps: candidate overlaps AIM 341
- 119: The Courtade–Kumar and Hellinger conjectures: no matching AIM target located
- 120: Almost-linear-time exact matching and prescribed-degree factors in general graphs: no matching AIM target located
- 121: Almost-linear approximation of edit distance: no matching AIM target located
- 122: Quantitative trace-reconstruction bounds with a uniform decoder: candidate overlaps AIM 321
- 124: Polynomial-time scheduling on three identical machines: candidate overlaps AIM 301