# Independent family 249–377 comparison

Screened 129 result families at pinned OpenAI revision 1581d4cbdd69a0faf34b2089614fe2a814316a6a against all 665 AIM titles, including 14 retained resolved catalogue entries at AIM c9929805cece044705abaaebe1cebddac1ba11a6.

Recommendations: {'solved': 29, 'partial': 3, 'no_match': 10}. The systematic screen covers every assigned family. Candidate comparisons inspect actual TeX theorem statements, definitions, normalizations and Lean scope documentation. Noncandidate families were screened from the catalogue descriptions and constituent abstracts; this is not an independent audit of every complete paper proof. No repository files were edited. Public source downloads and this report live outside AIM.

Lean availability is kept distinct from Lean verified status. No fresh successful kernel log, complete transitive axiom output, or full proof reproduction was inspected by this agent. Full development links require root follow-up.

## Candidate outcomes

### AIM 038 — OpenAI 251 — solved

The theorem proves amenability iff unitarizability for all discrete groups, including the exact countable target. Uniform boundedness and arbitrary complex Hilbert spaces agree.

Locator: build/sections/introduction.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf
Lean: docs/251 covers full equivalence; DixmierAllDiscrete and Dixmier comparators. Available formalization, not locally kernel verified.

### AIM 015 — OpenAI 261 — solved

For d=3 the theorem gives a fixed I=(-6+e2/2,-6+e2) inside (-6,6), a positive disorder threshold, I contained in spectrum and pure absolute continuity almost surely for each fixed coupling. A stated parity unitary flips the hopping sign to the target convention.

Locator: build/01-introduction.tex, thm:main and eq:energy-windows
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf
Lean: docs/261 only proves the planar spectral set; it covers neither the 3D absolute-continuity target nor planar pure-point type.

### AIM 016 — OpenAI 261 — partial

Same uniform law and every fixed positive disorder. The theorem supplies pure-point type and a complete orthonormal eigenbasis but explicitly does not assert exponential eigenfunction decay.

Locator: build/sections/introduction.tex, main:theorem and scope paragraph at line 95
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf
Lean: docs/261 establishes only spectrum [-4-h,4+h], not pure-point type or exponential decay.

Known cases: At every fixed positive disorder, almost surely the planar operator has pure-point spectrum and a complete orthonormal eigenbasis.
Remaining target: Prove that a complete orthonormal eigenbasis can be chosen with exponentially decaying eigenfunctions as required in the original target.

### AIM 098 — OpenAI 263 — partial

Same full fermionic Coulomb Hamiltonian with kinetic term -Delta/2 and two spin states. The theorem proves n<=Z+CM under strict binding E_n<E_(n-1), for real charges at least one and all distinct positions. It expressly leaves threshold eigenstates outside its assertion, while the AIM Nmax includes them.

Locator: build/sections/01-introduction.tex, thm:main and following threshold caveat
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf
Lean: docs/263 formalizes generalized large-ionization asymptotics and radii, not this strict-binding excess-charge bound.

Known cases: Every strictly bound molecular electron sector satisfies N<=Z+CM with a universal constant independent of charges and nuclear positions.
Remaining target: Bound ground-state eigenvalues at the ionization threshold as well, so that Nmax defined using any ground-state eigenvalue satisfies the same universal excess-charge estimate.

### AIM 099 — OpenAI 263 — solved

The first-ionization corollary proves universal two-sided positive bounds for neutral integer-Z atoms with exactly the target kinetic and spin normalization. Its upper bound settles the whole supremum question.

Locator: build/sections/01-introduction.tex, cor:first-ionization
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf
Lean: docs/263 explicitly excludes fixed-m convergence; the selected comparators do not establish the first-ionization bound.

### AIM 199 — OpenAI 265 — solved

Set interaction range R=1 and strength J=1. Rectangles and all nearest-neighbor/on-site terms are admitted, with only a unique ground state and a full-system gap. The vertical-cut edge boundary has exactly M edges, yielding C(q,1,1,Delta)M uniformly over L,M,ell and the interactions.

Locator: build/sections/00-introduction.tex, thm:area and cor:rectangles
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf
Lean: No Lean document is linked for this family.

### AIM 031 — OpenAI 266 — solved

The stated computer-assisted theorem excludes four arbitrary complex orthonormal bases in C6, without restricting the second Hadamard matrix to a known family, and concludes N(6)=3. It depends on the published binary64 arithmetic/compiler and complete-execution certificate conditions; no execution was reproduced by this agent.

Locator: build/sections/introduction.tex, thm:main; manuscript Section 7 and Appendix A
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf
Lean: docs/266 only proves at most five bases and supporting Fourier cancellation. It does not prove N(6)=3 or exclude four.

### AIM 196 — OpenAI 267 — solved

The density-uniform theorem covers every fixed bounded measurable nonzero nonnegative radial finite-range potential, so includes every target Cc-infinity potential. At T=0 its exact canonical ground state has occupation at least c*(V)>0 at every sufficiently dilute fixed density along all thermodynamic sequences, with trace-N density matrix and constant orbital.

Locator: build/sections/introduction.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf
Lean: docs/267 covers only the hard-sphere ground-state model. The target requires smooth finite-range potentials; that formalization does not cover it.

### AIM 194 — OpenAI 268 — solved

Identical pure spin-one antiferromagnetic coupling-one Hamiltonian on even periodic rings and next distinct eigenvalue convention. The positive bound holds for every even N>=60. Taking the minimum with the finitely many positive finite-dimensional gaps N=4,...,58 gives the required all-N uniform positive gap.

Locator: build/introduction.tex, thm:main and immediately following small-chain paragraph
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf
Lean: No Lean document is linked for this family; numerical/interval verification files are separate from Lean kernel verification.

### AIM 206 — OpenAI 272 — solved

The manuscript constructs a trace-preserving PPT channel Theta on M21 whose square is not entanglement breaking. Taking Phi=Psi=Theta directly disproves the all-dimension all-channel target. The separate two non-trace-preserving maps would not by themselves be enough.

Locator: build/source/sections/introduction.tex, thm:main-channel
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf
Lean: docs/272 covers the dimension-21 trace-preserving PPT channel counterexample via DimensionTenChannel; the zero-secret-key statement is outside the comparators. No local kernel log inspected.

### AIM 590 — OpenAI 272 — partial

An explicit PPT entangled state on C10 tensor C10 has zero distillable secret key for arbitrary admitted completed protocols; PPT ensures bound entanglement. A positive device-independent key protocol would give a positive trusted-device key protocol, so this supplies a substantive affirmative case of the target, not its universal conclusion.

Locator: build/source/sections/introduction.tex, thm:main-state and operational-extension paragraph
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf
Lean: docs/272 explicitly excludes the zero-distillable-secret-key statement; only PPT-composition consequences are formalized.

Known cases: For the explicit dimension-10 PPT bound-entangled state in the manuscript, copies cannot generate positive asymptotic secret-key rate even with trusted devices, and therefore cannot do so device independently.
Remaining target: Decide the device-independent secret-key prohibition for every finite-dimensional bound-entangled state and arbitrary protocols.

### AIM 205 — OpenAI 273 — solved

The exact displayed g-inverse entropy photon-number inequality is proved for any finite number of modes, any transmissivity in [0,1], finite photon energy, product inputs, and arbitrary correlations within either port. Entropy uses natural logarithms as in the target.

Locator: build/sections/00-introduction.tex, thm:epni
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-entropy-photon-number-inequality-September-24-2026/paper.pdf
Lean: docs/273 describes the full EPnI target via EntropyPhotonNumber; only channel-capacity consequences are outside it. No local kernel log inspected.

### AIM 207 — OpenAI 276 — solved

The theorem establishes unrestricted tensor-power Holevo additivity for all generalized amplitude-damping parameters. At stationary excited population nu=0 the Kraus channel is the target ordinary amplitude-damping channel. Entropy and capacity are in bits, and arbitrary entangled block inputs are included.

Locator: build/paper.tex, thm:main and generalized-channel definition
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf
Lean: docs/276 covers tensor-power additivity for all parameters via AmplitudeDamping. No local kernel log inspected.

### AIM 037 — OpenAI 288 — solved

Exactly arbitrary unital complex C*-algebras, arbitrary complex Hilbert spaces and bounded unital algebra homomorphisms, without complete-boundedness assumption. The manuscript uses S*pi*S^-1 rather than S^-1*pi*S; replacing S by its inverse reconciles the conventions.

Locator: build/sections/introduction.tex, thm:similarity
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/paper.pdf
Lean: docs/288 describes the full unrestricted similarity theorem via KadisonSimilarity. No local kernel log inspected.

### AIM 034 — OpenAI 289 — solved

The two-sided norm-unit-ball distance and the epsilon/delta quantifiers agree exactly for von Neumann algebras sharing identity I_H, the standard convention for the target. The separate one-sided near-inclusion and C*-algebra counterexamples do not refute this target.

Locator: build/sections/01-introduction.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf
Lean: docs/289 covers the universal near-identity unitary conjugacy statement via StrongKadisonKastler. No local kernel log inspected.

### AIM 023 — OpenAI 325 — solved

All n,m, all degrees, arbitrary complex coefficient matrices and constant two match. The manuscript orders tensors A^j tensor C_j and AIM orders C_j tensor A^j; the tensor-factor flip is unitary and preserves the operator norm.

Locator: build/main.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf
Lean: docs/325 covers the full finite-matrix target via DirectCrouzeix/CompleteCrouzeix, plus arbitrary-Hilbert and structural extensions. No local kernel log inspected.

### AIM 127 — OpenAI 337 — solved

The theorem includes all smooth complete simply connected n>=2 manifolds with Sec<=0 and every finite-volume finite-perimeter set. For the target smooth relatively compact domain, perimeter is boundary area; the coefficient is exactly n*omega_n^(1/n). This includes n>=5 with no additional geometric restriction.

Locator: build/sections/01-introduction.tex, thm:main with kappa=0
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf
Lean: docs/337 links the related sharp integral-current CAT(0) filling theorem rather than the manuscript smooth-perimeter theorem. A conversion to the target requires an additional geometric-current comparison; no local kernel verification was made.

### AIM 011 — OpenAI 350 — solved

One fixed smooth metric on the closed connected three-sphere has exact nonzero real Laplace eigenfunctions with positive eigenvalues tending to infinity and nodal two-measure/sqrt(lambda) tending to infinity. This refutes the universal target; the smooth-surface upper bound is an additional positive subcase.

Locator: build/sections/introduction.tex, thm:main (S3 fixed-metric counterexample)
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/paper.pdf
Lean: docs/350 describes fixed-metric counterexamples via SmoothYau (and a separate dimension-five YauCounterexample), as well as the surface theorem. No local kernel log inspected.

### AIM 391 — OpenAI 353 — solved

For n=3,...,9 the theorem classifies smooth positive-Hessian affine maximal graphs complete in induced Euclidean metric. An entire graph is Euclidean-complete because its metric dominates Euclidean distance and the graph is closed. The C4 target bootstraps locally to smoothness: the positive cofactor matrix makes the w equation elliptic on compact subsets, and det(D2u)=w^(-(n+2)/(n+1)) plus local Monge-Ampere regularity iterates Schauder regularity. No growth or affine completeness is needed.

Locator: build/main.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf
Lean: docs/353 covers the smooth Euclidean-complete graph theorem via AffineBernstein. The C4 bootstrap and target comparison are mathematical implications, not a locally checked Lean theorem. No local kernel log inspected.

### AIM 401 — OpenAI 360 — solved

Same squared-distance cost and weak MTW formula. The theorem gives an almost-everywhere unique optimal map with a global bi-Holder homeomorphic representative for measurable probability densities between fixed positive finite bounds on compact connected smooth manifolds. It does not require convex injectivity domains in advance, so covers the target assumptions.

Locator: build/sections/introduction.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf
Lean: docs/360 covers full bi-Holder transport via BiholderTransport. Supporting finite-family geometric statements have narrower scope. No local kernel log inspected.

### AIM 073 — OpenAI 362 — solved

Exact one-species R3 relativistic Vlasov-Maxwell normalization, compact nonnegative smooth particle data, Cb-infinity finite-L2-energy fields and Gauss constraints. The global solution has compact phase-space support on each finite interval, so in particular bounded momentum support, preserves Gauss constraints and finite field energy; no size/symmetry restriction.

Locator: build/sections/introduction.tex, thm:global and eq:data
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf
Lean: docs/362 describes the full target via VlasovMaxwell. No local kernel log inspected.

### AIM 227 — OpenAI 363 — solved

Two distinct global solutions have the same datum, exact target hard-sphere |(v-v*) dot omega| normalization, all weighted Q+ and Q- locally integrable, strong L1 initial traces, all five local conservation laws and entropy dissipation. The paper renormalizes F/M for a fixed Maxwellian. Locally integrable unrenormalized transport/collision equation gives the beta(F) chain rule along characteristics; conserved mass and kinetic energy turn relative entropy into the target absolute entropy inequality. The datum is rough, so this does not resolve smooth-data AIM074.

Locator: build/paper/01-introduction.tex, thm:main and def:admissible
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf
Lean: docs/363 covers the earlier periodic renormalized nonuniqueness theorem, not the later full local-conservation refinement. Comparator BoltzmannNonuniqueness; no local kernel log inspected.

### AIM 046 — OpenAI 365 — solved

Uniformly positive bounded real scalar conductivities on the smooth ball B(0,3) differ on positive volume and have exactly the same full weak H1/2-to-H-1/2 DN operator. This directly refutes the all-pairs target and even keeps both conductivities equal to one near the boundary.

Locator: build/paper.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf
Lean: docs/365 covers this full rough scalar-conductivity counterexample via Conductivity. It does not cover the separate smooth anisotropic papers. No local kernel log inspected.

### AIM 047 — OpenAI 365 — solved

The explicit full-boundary corollary recovers arbitrary smooth metrics on any compact connected smooth n>=3 manifold by a diffeomorphism fixing every boundary point. Equal target pointwise normal-DN operators with the same boundary metric yield equal density-valued energy maps, so the corollary applies.

Locator: build/sections/01-introduction.tex, main:full corollary
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf
Lean: docs/365 links only the bounded-measurable scalar counterexample. No Lean formalization of this smooth anisotropic target is provided in the family document.

### AIM 048 — OpenAI 365 — solved

The explicit scalar corollary proves equality throughout the closed domain for strictly positive smooth scalar conductivities from identical arbitrary same-patch voltage/flux measurements, all n>=3, with no inaccessible-boundary agreement assumption.

Locator: build/sections/01-introduction.tex, main:scalar corollary
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf
Lean: docs/365 links only the rough scalar nonuniqueness comparator, not the smooth same-patch uniqueness result.

### AIM 157 — OpenAI 367 — solved

Exactly J=integral(|grad u|^2+indicator(u>0)), one-homogeneous nonnegative global minimizers with arbitrary nonnegative Sobolev same-trace competitors. Every cone through dimension six is flat and a nonflat cone exists in dimension seven, so the target critical dimension is seven. Standard minimizer regularity supplies continuity for the existence example.

Locator: build/paper.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf
Lean: docs/367 covers only existence of a nonflat cone in dimension seven via BernoulliNonflatInSeven; flatness in dimensions at most six is outside it, so it does not determine the full critical dimension.

### AIM 153 — OpenAI 368 — solved

The first manuscript covers 1<=p<=2 and the second covers 2<p<infinity. Together they prove strong W1p approximation by smooth diffeomorphisms onto the same target for any bounded 3D domains and any Sobolev homeomorphism. No boundary smoothness or boundary equality is required; orientation-preserving maps are included.

Locator: both manuscripts build/sections/01-introduction.tex, main:theorem
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf
Lean: No Lean document is linked for this family.

### AIM 003 — OpenAI 369 — solved

Every nonzero real eigenfunction in the first positive Neumann eigenspace on every smooth bounded simply connected planar domain has no interior critical point and obeys strict interior inequalities against boundary extrema. Every convex target domain is simply connected; multiplicities and every vector in the eigenspace are explicitly included.

Locator: build/sections/01-introduction.tex, thm:main and eq:hotspots
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/main.pdf
Lean: docs/369 covers the full strict hot-spots conclusion via HotSpots. No local kernel log inspected.

### AIM 350 — OpenAI 370 — solved

The unweighted corollary covers n>=3 and all p,q>0 under exactly 1/(p+1)+1/(q+1)>(n-2)/n, excluding strictly positive entire C2 solutions without symmetry, decay, integrability, stability or energy assumptions. This includes every n>=5 target case.

Locator: build/sections/01-introduction.tex, cor:lane-emden
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/paper.pdf
Lean: docs/370 covers the complete unweighted target as a specialization of HenonEmden. No local kernel log inspected.

### AIM 050 — OpenAI 372 — solved

Exactly bounded connected smooth 3D domains, arbitrary smooth real lambda/mu, mu>0 and 3lambda+2mu>0, static zero-frequency displacement-to-traction map and recovery of both coefficients. No near-boundary or near-constant condition is added.

Locator: build/sections/introduction.tex, thm:main
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/article.pdf
Lean: docs/372 covers the full uniqueness target via ElasticityUniqueness. No local kernel log inspected.

### AIM 089 — OpenAI 375 — solved

The unrestricted monotone Allen-Cahn rigidity theorem is stated in dimension eight with no directional limits, energy growth or minimization hypothesis. Embed the target by U(x1,...,x8)=u(x1,...,x4,x8). The extra-coordinate independence forces their components of the resulting unit direction to vanish, giving exactly the dimension-five tanh profile with positive fifth component.

Locator: build/sections/00-introduction.tex, thm:monotone
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/article.pdf
Lean: No Lean document is linked for this family.

### AIM 419 — OpenAI 377 — solved

The theorem gives interior C1,alpha in every dimension d>=3 for continuous viscosity infinity-harmonic functions, including zero-gradient tests. The corollary explicitly localizes by bounded compact balls, so the target arbitrary continuous 3D solution has continuous gradient locally. Connectedness is handled componentwise.

Locator: build/manuscript/sections/01-introduction.tex, thm:main and cor:interior-c1
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/interior-c1-infinity-harmonic.pdf
Lean: No Lean document is linked for this family.

### AIM 303 — OpenAI 261 — no_match

A purely absolutely continuous spectral interval does not imply the fixed-disorder all-large-time two-sided diffusive mean-square displacement rate requested by AIM303.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 018 — OpenAI 262 — no_match

The theorem is one-dimensional, finite matrix-valued and has the scalar one-bound-state coefficient. AIM018 fixes the three-dimensional scalar gamma=1 semiclassical coefficient 1/(15*pi^2). Neither the dimension nor sharp coefficient matches; no target subclass resolution follows.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/sharp-matrix-lieb-thirring.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 195 — OpenAI 269 — no_match

The theorem is the fermionic spherical V1 projector at filling 1/3 with cubic Laughlin polynomial. AIM195 is bosonic planar Bargmann contact interaction at filling 1/2 with a total-degree cutoff and squared Laughlin polynomial. These are different Hamiltonians, statistics and geometries, not a subset of the target.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 197 — OpenAI 267 — no_match

Quantum depletion and condensation bounds do not establish the thermodynamic Wu logarithmic energy coefficient with an error little-o of rho*a^3*abs(log(rho*a^3)).

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/fixed-repulsion-quantum-depletion.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 100 — OpenAI 263 — no_match

Ionization asymptotics in the limit m->infinity and Z/m->infinity do not prove convexity of E(N,Z) at every N and integer Z, or give a counterexample.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/paper.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 032 — OpenAI 272 — no_match

The constructed states come from PPT maps and have positive partial transpose. They do not give the negative-partial-transpose all-copy nondistillability required by AIM032.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 051 — OpenAI 365 — no_match

The theorem recovers a metric and a unitary rank-two connection. It does not recover an arbitrary real scalar Schrodinger potential on a fixed general manifold from one zero-frequency DN map.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/paper.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 055 — OpenAI 365 — no_match

Metric recovery from an elliptic DN map does not by itself give recovery from the boundary-distance function of smooth simple manifolds; no conversion between these data is proved here.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 452 — OpenAI 353 — no_match

Affine maximal surfaces solve a specific fourth-order cofactor equation. AIM452 concerns arbitrary smooth uniformly elliptic second-order F(D2u)=0 with bounded Hessian in dimensions three and four. The objects and equations differ.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf
Lean: Formalization availability does not change this scope mismatch.

### AIM 154 — OpenAI 368 — no_match

Strong forward W1p diffeomorphic approximation alone does not guarantee convergence of an elastic energy with singular determinant/compression penalties. The high-p manuscript explicitly distinguishes this question.

Locator: Main theorem scope and definitions in the listed sources
PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf
Lean: Formalization availability does not change this scope mismatch.

## Screen ledger

See screened-families.json for all assigned family IDs, titles, candidate crosswalks and nonmatch notes. Family IDs are OpenAI collection identifiers and are never copied as AIM problem IDs.

## Important limitations

The MUB paper uses a computer-assisted complete-execution certificate under stated arithmetic/compiler conditions; this agent checked its theorem and scope, not the full computation. The C4 affine-Bernstein target requires standard local elliptic bootstrap to use the smooth manuscript theorem. The Boltzmann comparison requires the ordinary renormalization chain rule along characteristics and conversion from relative to absolute entropy by the conserved quantities. These mathematical reductions are stated in the comparisons and must not be described as Lean kernel checks.

## Final supplemental checks on 13 October 2026

MUB execution source Section 7 reports a completed 4 October 2026 run, all 100 invocations accounted, and no final unresolved records. Its binary64/compiler semantics remain explicit assumptions, and no independent execution was performed. Referenced native-code and numerical-archive verification directories are absent from this manuscript folder in the pinned public tree, so archive availability and its contents were not certified.

The previously omitted CAT(0) companion to family337 has now been inspected: its cor:cartan-hadamard independently gives the smooth-domain inequality matching AIM127 in every d>=3. It supplies no additional AIM target.
