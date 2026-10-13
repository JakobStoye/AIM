# Independent matching review: OpenAI families125–248

All extant OpenAI families125–248 and all665 AIM catalogue titles, including retired/resolved records; detailed source theorem/definition comparisons for plausible overlaps. This is not an independent complete proof audit of hundreds of manuscripts and no Lean build was performed.

Pinned OpenAI revision: 1581d4cbdd69a0faf34b2089614fe2a814316a6a. AIM comparison revision: c9929805cece044705abaaebe1cebddac1ba11a6.

Extant families screened: 123. Family163 is absent in the pinned CONTENTS. Full/negative target matches:13; substantive partial target matches:3; related analogue:1. No local Lean verification is claimed.

## AIM 064 / OpenAI 147 — full

The AIM target assumes a smooth complete foliation of a full grazing annulus, including rational rotation levels. Phase-foliation rigidity permits merely continuous essential individually invariant leaves, for an arbitrary bounded C-infinity strictly convex positive-curvature planar table, and concludes ellipse. The smooth AIM foliation supplies the homeomorphism in the theorem. No closeness or symmetry is added. The physical-collar companion supplies the stated analytic input.

Theorem: Phase-foliation rigidity theorem, introduction.tex lines 17-33, label thm:main; companion Physical-collar rigidity theorem cited as Definition 1.1/Theorem 1.2.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/paper.pdf

Source: preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/build/sections/introduction.tex

Lean scope: No family Lean documentation linked; no complete-target verification evidence inspected.

## AIM 065 / OpenAI 146 — full

For the unit torus source map f_k(x,y)=(x+y+k sin(2 pi x), y+k sin(2 pi x)), every k above a positive threshold has positive entropy for normalized area. Coordinate scaling X=2 pi x,Y=2 pi y gives the exact AIM map with K=2 pi k, preserving normalized probability and entropy. Hence an admissible nonzero K exists.

Theorem: Introduction, theorem label main:entropy (first theorem).

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/paper.pdf

Source: preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/build/sections/introduction.tex

Lean scope: StandardMapEntropy comparator defines the actual sine map and finite-partition entropy and the full parameter-tail statement. The comparator theorem ends in sorry; upstream proof-module and reproduction/axiom evidence must be evaluated separately. No local verification claimed.

## AIM 088 / OpenAI 213 — full

The theorem explicitly treats independent nearest-neighbor Bernoulli bond percolation on the ordinary cubic lattice Z^3 at its separately defined bond critical parameter. Almost surely no infinite cluster implies theta(p_c)=0. The additional site result is unnecessary for AIM coverage.

Theorem: Introduction theorem label thm:main, introduction.tex lines 17-22.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf

Source: preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/build/introduction.tex

Lean scope: CriticalZ3 comparator defines the cubic nearest-neighbor bonds and product Bernoulli law and states all critical clusters finite. Main comparator declaration uses sorry; no local verification claimed.

## AIM 090 / OpenAI 223 — full

The Cardy theorem directly proves actual free-boundary square-lattice bond crossing probabilities with all edges independent at p=1/2, including boundary edges. Uniform marked Jordan approximation includes smooth AIM domains; the buffered boundary comparison transfers between lattice boundary arcs and the AIM O(mesh) boundary-vertex convention. Its beta-integral ratio equals the hypergeometric formula in AIM by the incomplete beta identity with a=b=1/3. This is an explicit crossing theorem, not an inference from the SLE abstract.

Theorem: Introduction theorem Cardy's formula, label intro:cardy, lines 235-245; free-boundary definitions lines 222-234 and boundary-transfer discussion immediately after.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/paper.pdf

Source: preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/build/sections/introduction.tex

Lean scope: No family Lean documentation linked; no complete-target local verification evidence inspected.

## AIM 164 / OpenAI 143 — full

Uniform boundedness states that every real planar polynomial vector field of degree at most d has at most the finite integer B(d) isolated geometric periodic-orbit images in the whole plane, independent of coefficients. Specializing d=2 supplies H_2. Definitions match AIM without multiplicity.

Theorem: Uniform boundedness theorem, label thm:uniform, 01-introduction.tex lines 12-16.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf

Source: preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/build/sections/01-introduction.tex

Lean scope: Family143 Lean docs link only QuinticLienard: degree<=5 classical Lienard systems, not arbitrary quadratic planar vector fields. Thus complete AIM164 is not covered by the selected formal statement; no Lean verified status.

## AIM 169 / OpenAI 212 — full

The exponential limit-shape theorem covers undirected nearest-neighbor Z^2 FPP with independent exponential weights of any positive rate, including rate1. It explicitly gives strict convexity and the strict interpolation inequality for every pair of distinct boundary points, with no assumed curvature or geodesic hypothesis.

Theorem: The exponential limit shape theorem, label thm:exponential-shape, introduction.tex lines 21-32.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf

Source: preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/build/sections/introduction.tex

Lean scope: Family212 docs explicitly say strict convexity is outside its selected differentiability comparators. A C1 boundary or unique supporting line does not imply strict convexity. No complete AIM169 formalization/verification supported by these links.

## AIM 171 / OpenAI 212 — full

The no-bigeodesics theorem rules out all injective doubly infinite nearest-neighbor minimizing paths simultaneously for every nonnegative nonatomic iid weight law satisfying E[min(X1,X2,X3,X4)^2]<infinity. Mean-one exponential weights satisfy this hypothesis (their minimum has rate4 and finite second moment). No direction restriction or shape assumption occurs.

Theorem: Introduction theorem label thm:main, 01-introduction.tex lines 24-37.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf

Source: preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/build/sections/01-introduction.tex

Lean scope: Family212 selected Lean docs only cover differentiability of limit shapes; no bigeodesic comparator is linked. No full AIM171 formalization/verification supported.

## AIM 176 / OpenAI 214 — full

The theorem applies to every infinite connected locally finite nonamenable quasi-transitive graph and gives pc<p_(2to2)<=pu. Vertex-transitive AIM graphs are included. Its vertex-boundary nonamenability is equivalent to the AIM edge-boundary form on these uniformly bounded-degree graphs. Definitions of pc/pu agree.

Theorem: Introduction theorem label thm:main, introduction.tex lines 58-69; definitions/nonamenability preceding.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf

Source: preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/build/sections/introduction.tex

Lean scope: Family214 docs link BenjaminiSchramm/CayleyPercolation statements for the relevant full graph class. Comparator templates alone are not reproduction evidence; no local verification claimed.

## AIM 178 / OpenAI 220 — full

Directional transience implies ballisticity is stated for every d>=2, iid nearest-neighbor transition rows with a common positive lower bound, every fixed unit direction, and annealed almost-sure escape. It gives a deterministic vector limit X_n/n and strictly positive projection in the same direction, exactly including AIM d=3.

Theorem: Directional transience implies ballisticity theorem, label thm:main, 01-introduction.tex lines 50-61.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf

Source: preprints/Directional-transience-implies-ballisticity-September-23-2026/build/01-introduction.tex

Lean scope: DirectionalBallisticity comparator constructs an environment sampled once and retained along the walk, annealed path law, uniform ellipticity, and the exact vector limit. The declaration uses sorry; no local verification claimed.

## AIM 179 / OpenAI 220 — full

The zero-one theorem covers every d>=3, iid nearest-neighbor transition rows, every fixed nonzero real direction, and merely strict positivity. Uniform ellipticity of the AIM Z^3 model is stronger and hence sufficient. Its escape event and annealed law from the origin agree exactly.

Theorem: Introduction theorem label thm:main, 01-introduction.tex lines 61-69, strict-ellipticity equation and path-law definitions preceding.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf

Source: preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/build/01-introduction.tex

Lean scope: DirectionalWalk comparator gives the iid product environment and annealed origin escape event; main declaration uses sorry. No local verification claimed.

## AIM 273 / OpenAI 149 — full

Uniform permanence holds for every finite weakly reversible mass-action network with fixed positive reaction rates and every positive initial state, with a classwise compact absorbing set contained in the strictly positive orthant. The eventual positive lower bound implies each AIM bounded global trajectory has positive liminf for every species; complex balance is not imposed. The theorem is stronger than the target because it also ensures global bounded positive solutions.

Theorem: Main theorem label thm:main, introduction.tex lines 43-60; epsilon_P bounds in equation eq:uniform-bounds.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/permanence.pdf

Source: preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/build/sections/introduction.tex

Lean scope: Family149 Lean docs concern the September boundedness/persistence article, giving initial-state-dependent all-time bounds rather than classwise uniform October permanence. This is nevertheless sufficient for AIM273. MassAction comparator main statement uses sorry; no local verification claimed.

## AIM 323 / OpenAI 174 — full

The theorem quantifies one absolute C>0 over every integer k>=1 and every finite loopless k-edge-connected multigraph with >=2 vertices, counts parallel edges separately, and selects one spanning tree satisfying every nontrivial cut inequality C/k simultaneously. The efficient companion exceeds AIM's existence requirement.

Theorem: Main theorem label thm:main, source/sections/introduction.tex lines 17-28.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf

Source: preprints/The-strong-thin-tree-conjecture-September-23-2026/build/source/sections/introduction.tex

Lean scope: StrongThinTree comparator models edges by separate labels and states exactly the all-cut universal-constant result; declaration uses sorry. AlgorithmicThinTrees is additional. No local verification claimed.

## AIM 585 / OpenAI 161 — counterexample

Main theorem explicitly produces a finite simple unweighted host G with at least one edge and a fixed finite simple bipartite incidence graph H with35 vertices and66 edges for which t(H,G)<p(G)^66. Definitions t=hom/n^v and p=2|E|/n^2 match AIM, including noninjective maps. Thus this is a complete negative resolution, not only a weighted or graphon counterexample.

Theorem: Main theorem label thm:main, introduction.tex lines18-26; definitions lines1-15.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf

Source: preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/build/sections/introduction.tex

Lean scope: SidorenkoCounterexample comparator explicitly defines the22 triples, incidence graph, all homomorphisms and finite simple host deficit. Main declaration uses sorry; forcing consequence is outside selected Lean statement and irrelevant to AIM585. No local verification claimed.

## AIM 142 / OpenAI 150 — partial

The weak-mixing theorem applies to every nondegenerate irrational-angle Euclidean triangle under precisely normalized position-times-uniform-direction Liouville measure, excluding the same null vertex-hit trajectories. Weak mixing implies ergodicity, so every three-side instance of the requested irrational polygon example is impossible; the existential question for larger polygons remains open.

Theorem: Introduction theorem label thm:main, normalized measure immediately preceding.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/weak-mixing-triangular-billiards.pdf

Source: preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/build/sections/introduction.tex

Lean scope: Family150 selected Lean docs formalize ergodicity of irrational triangles, which suffices for this partial exclusion; weak mixing is not the selected comparator claim. Comparator presence is not local verification.

Known cases: Every nondegenerate triangle with at least one angle irrational relative to pi has ergodic, indeed weakly mixing, unit-speed billiard flow for normalized Liouville measure. Such a triangle cannot supply the requested nonergodic example.

Remaining target: Determine whether a bounded simple irrational polygon with at least four sides has nonergodic full Liouville billiard flow, or prove that every such polygon is ergodic.

## AIM 337 / OpenAI 184 — partial

For each fixed integer r>=4, correspondence coloring of every K_r-free simple graph is at most ceil(C_r Delta/log Delta) for sufficiently large Delta. Since ordinary chi<=chi_DP, taking Delta sufficiently large that C_r/log Delta<=1/2 implies the exact Reed inequality for this bounded-clique subcase. The constants and threshold depend on the fixed clique cap; this does not handle arbitrary graph-dependent clique number or all degrees. This is a derived subset consequence rather than a manuscript theorem named Reed.

Theorem: Correspondence-coloring main theorem label thm:main, introduction.tex lines24-33; chi<=chi_list<=chi_DP preceding.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf

Source: preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/build/sections/introduction.tex

Lean scope: Family184 selected Lean docs only formalize the logarithmic independence lower bound (CliqueFreeLog), not the correspondence-coloring theorem used here; no full or direct partial Reed verification claimed.

Known cases: For every fixed clique cap r-1 (r>=4), the manuscript gives chi_DP(G)<=ceil(C_r Delta/log Delta) for K_r-free graphs at sufficiently large Delta, implying Reed's bound in that subcase. Previously documented claw-free and other cases remain applicable.

Remaining target: Prove or refute the displayed one-half Reed bound uniformly over all finite simple graphs, including unrestricted clique number and the remaining finite-degree regimes.

## AIM 346 / OpenAI 183 — partial

The halving-power theorem counts exactly unordered pairs determining balanced straight lines of arbitrary even planar n-point sets with no three collinear. It gives an absolute fixed positive saving epsilon from4/3 for all sufficiently large even n; enlarging C covers finite smaller n. It neither supplies exponents1+eta for every eta>0 nor gives a disproof of that near-linear target.

Theorem: Power-saving halving theorem label thm:halving-power, introduction.tex lines9-16.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf

Source: preprints/A-power-saving-for-planar-halving-lines-September-25-2026/build/sections/introduction.tex

Lean scope: HalvingLines comparator states the same fixed power saving for general-position sets, and a separate all-level bound for a stronger generic condition. Main declaration uses sorry; no local verification claimed.

Known cases: For absolute epsilon>0 and C, every even general-position planar n-point set has at most C n^(4/3-epsilon) halving lines. This improves the previous4/3 upper exponent; the saving and constants are nonquantitative.

Remaining target: Establish h(n)<=C_eta n^(1+eta) for every eta>0, or disprove that assertion. A single fixed saving from4/3 leaves a gap to the required near-linear exponent.

## AIM 091 / OpenAI 237 — related

The main fixed-length theorem and gyration corollary concern uniformly sampled honeycomb walks, diameter and radius-of-gyration moments. AIM fixes Z^2 square-lattice walks and endpoint mean-square displacement. A lattice-universality transfer and endpoint-versus-diameter lower-moment comparison are absent. This is a substantive analogue, not a solved subcase of the exact target.

Theorem: Fixed-length mass and covering theorem label thm:main, 00_introduction.tex lines17-27; radius-of-gyration and moment corollary lines50-61.

PDF: https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Mass-and-covering-exponents-for-fixed-length-honeycomb-walks-September-26-2026/main.pdf

Source: preprints/Mass-and-covering-exponents-for-fixed-length-honeycomb-walks-September-26-2026/build/sections/00_introduction.tex

Lean scope: Family237 docs explicitly exclude spatial3/4 and moment laws from its supporting bridge/free-energy comparator statements. No full-target Lean coverage.

Known cases: The honeycomb analogue has diameter and radius-of-gyration moments of order n^(3p/4+o(1)); it does not establish a square-lattice endpoint-displacement case.

Remaining target: The exact square-lattice uniform-walk endpoint mean-square displacement exponent remains the complete AIM091 target.

## Screening exclusions

125: Metric k-median threshold is a different optimization problem from AIM routing/scheduling/allocation targets.
126: PSD extension complexity does not solve deterministic NC perfect matching (AIM490).
127: Sensitivity upper bounds for polynomial threshold functions do not establish Fourier entropy/influence (488) or influential-variable lower bounds (327).
128: Shortest common superstring approximation is not the LCS mean match fraction or variance (277/286).
129: The quantified claim and model described for Exponential state costs for two-way automata do not match any AIM target in the complete665-title inventory.
130: Exact complex Fourier circuits are not the matrix multiplication exponent or the numerical bit/precision targets.
131: Switch-chain graph sampling does not cover the reflected Burnside partition chain (535) or proper-coloring Glauber chain (269).
132: The quantified claim and model described for A superquadratic separation of sensitivity and block sensitivity do not match any AIM target in the complete665-title inventory.
133: The quantified claim and model described for The computational complexity of Weisfeiler–Leman refinement do not match any AIM target in the complete665-title inventory.
134: The quantified claim and model described for Generalized star height at most three do not match any AIM target in the complete665-title inventory.
135: The quantified claim and model described for Homogeneous depth-five lower bounds for iterated matrix multiplication do not match any AIM target in the complete665-title inventory.
136: The quantified claim and model described for A quasilinear PCP theorem for PPAD do not match any AIM target in the complete665-title inventory.
137: The quantified claim and model described for One-tape time simulation in two-fifths-power space do not match any AIM target in the complete665-title inventory.
138: Subset Sum decision time does not prove the support-concentration inequality (345).
139: First-order query sampling for strong well-conditioned potentials does not prove KLS for arbitrary isotropic log-concave laws (092).
140: The quantified claim and model described for Memory–sample lower bounds for noiseless Gaussian regression do not match any AIM target in the complete665-title inventory.
141: Finite real-polynomial sentence complexity does not decide the transcendental/infinite-time dynamical targets.
142: The quantified claim and model described for Deterministic polynomial factorization over prime fields do not match any AIM target in the complete665-title inventory.
144: The quantified claim and model described for Banach’s simple Lebesgue-spectrum problem do not match any AIM target in the complete665-title inventory.
145: The quantified claim and model described for Rokhlin’s multiple-mixing problem do not match any AIM target in the complete665-title inventory.
148: The quantified claim and model described for The entropy-rate dimension formula for self-similar measures do not match any AIM target in the complete665-title inventory.
151: The quantified claim and model described for A <i>C</i><sup>1</sup> counterexample to the entropy conjecture do not match any AIM target in the complete665-title inventory.
152: The quantified claim and model described for Zero entropy does not guarantee a smooth positive-volume model do not match any AIM target in the complete665-title inventory.
153: The quantified claim and model described for Arithmetic classification and non-Pisot singularity for Bernoulli convolutions do not match any AIM target in the complete665-title inventory.
154: The quantified claim and model described for Pointwise multiple ergodic averages for mixing transformations do not match any AIM target in the complete665-title inventory.
155: The quantified claim and model described for A counterexample to periodic tiling in dimension three do not match any AIM target in the complete665-title inventory.
156: Borsuk smaller-diameter covering is different from convex-body illumination (486).
157: Hadwiger minor counterexamples and linear list Hadwiger bounds do not refute or prove the Reed bound (337).
158: The quantified claim and model described for The Euclidean plane cannot be colored with five colors do not match any AIM target in the complete665-title inventory.
159: The quantified claim and model described for Erdős’s reciprocal-sum conjecture and quasipolynomial Szemerédi bounds do not match any AIM target in the complete665-title inventory.
160: The quantified claim and model described for Superexponential van der Waerden numbers do not match any AIM target in the complete665-title inventory.
162: The quantified claim and model described for Counterexamples to Ryser’s covering conjecture do not match any AIM target in the complete665-title inventory.
164: The quantified claim and model described for Hindman’s finite sums and products conjecture do not match any AIM target in the complete665-title inventory.
165: The quantified claim and model described for The Harary–Hill and Zarankiewicz crossing-number formulas do not match any AIM target in the complete665-title inventory.
166: The quantified claim and model described for The higher-dimensional Erdős distinct-distances conjecture do not match any AIM target in the complete665-title inventory.
167: The quantified claim and model described for Planar distinct distances and unit-distance bounds do not match any AIM target in the complete665-title inventory.
168: The quantified claim and model described for Combinatorial invariance of Kazhdan–Lusztig polynomials do not match any AIM target in the complete665-title inventory.
169: The quantified claim and model described for Shareshian–Wachs elementary positivity do not match any AIM target in the complete665-title inventory.
170: The quantified claim and model described for Sharp logarithmic exponents for off-diagonal Ramsey numbers do not match any AIM target in the complete665-title inventory.
171: The quantified claim and model described for The hypercube Ramsey conjecture do not match any AIM target in the complete665-title inventory.
172: The quantified claim and model described for Classification of finite Euclidean Ramsey configurations do not match any AIM target in the complete665-title inventory.
173: The quantified claim and model described for Seymour’s second-neighborhood conjecture do not match any AIM target in the complete665-title inventory.
175: The quantified claim and model described for Talagrand’s expectation thresholds, discrete convexity, and graph decompositions do not match any AIM target in the complete665-title inventory.
176: The quantified claim and model described for The second Kahn–Kalai conjecture with an edge-count bound do not match any AIM target in the complete665-title inventory.
177: Existence of some bounded-degree coboundary expanders does not prove high-probability expansion of the specified random balanced Cayley model (640), nor the exact low-degree spectrum condition (643).
178: Constructing some Ramanujan graphs does not sign every prescribed regular graph (214).
179: Nonexistence of circulant Hadamard matrices beyond4 neither proves nor refutes existence of unrestricted Hadamard matrices at every multiple of4 (026).
180: Barnette's planar cubic bipartite Hamiltonicity excludes the nonbipartite snark/cycle-permutation targets.
181: The quantified claim and model described for The Erdős–Gallai cycle-decomposition conjecture do not match any AIM target in the complete665-title inventory.
182: The quantified claim and model described for Power savings for intersective polynomial differences and prime arguments do not match any AIM target in the complete665-title inventory.
185: The quantified claim and model described for Counterexamples to infinite matroid intersection and packing/covering do not match any AIM target in the complete665-title inventory.
186: The quantified claim and model described for Uniform influence and sharp thresholds for graph and hypergraph properties do not match any AIM target in the complete665-title inventory.
187: The quantified claim and model described for Snaky in 21 Maker moves do not match any AIM target in the complete665-title inventory.
188: Random triangle-removal terminal asymptotics do not give the universal triangle packing-covering factor2 (335).
189: The quantified claim and model described for Cycle–clique Ramsey numbers do not match any AIM target in the complete665-title inventory.
190: The quantified claim and model described for Polynomial removal fails for ordered binary matrices do not match any AIM target in the complete665-title inventory.
191: An n^(-2+c) minimum triangle lower bound still vanishes and does not refute AIM635's vanishing-area assertion for any nonzero mod-two cycle.
192: Square-root degree/correlation counterexample is not a Fourier entropy-influence counterexample (488).
193: The quantified claim and model described for Serre’s intersection-multiplicity conjecture do not match any AIM target in the complete665-title inventory.
194: The quantified claim and model described for Lech’s multiplicity conjecture do not match any AIM target in the complete665-title inventory.
195: The quantified claim and model described for A counterexample to the small Cohen–Macaulay module conjecture do not match any AIM target in the complete665-title inventory.
196: The quantified claim and model described for A counterexample to Kaplansky’s zero-divisor conjecture do not match any AIM target in the complete665-title inventory.
197: The quantified claim and model described for A torsion-free group algebra that is not directly finite do not match any AIM target in the complete665-title inventory.
198: The quantified claim and model described for A counterexample to finitistic-dimension finiteness do not match any AIM target in the complete665-title inventory.
199: The quantified claim and model described for Counterexamples to Auslander–Reiten, Tachikawa and related homological conjectures do not match any AIM target in the complete665-title inventory.
200: The quantified claim and model described for Eisenbud–Green–Harris and lex-plus-powers do not match any AIM target in the complete665-title inventory.
201: The quantified claim and model described for A counterexample to Kurosh’s division-ring problem do not match any AIM target in the complete665-title inventory.
202: The quantified claim and model described for The blockwise Alperin weight conjecture do not match any AIM target in the complete665-title inventory.
203: The quantified claim and model described for Donovan's conjecture over fields and complete mixed-characteristic DVRs do not match any AIM target in the complete665-title inventory.
204: The quantified claim and model described for Tensor saturation for even spin groups do not match any AIM target in the complete665-title inventory.
205: The quantified claim and model described for Saxl’s conjecture and universal tensor squares do not match any AIM target in the complete665-title inventory.
206: The quantified claim and model described for Finite lattice representation and undecidability do not match any AIM target in the complete665-title inventory.
207: Group-ring traces/idempotents do not settle unitarizability of all countable groups (038).
208: The quantified claim and model described for Finite symmetric tensor categories and the Verlinde tower do not match any AIM target in the complete665-title inventory.
209: The quantified claim and model described for Integral counterexamples to Gersten’s conjecture do not match any AIM target in the complete665-title inventory.
210: The quantified claim and model described for Foulkes' conjecture for sixth powers and quadratic stabilization do not match any AIM target in the complete665-title inventory.
211: The quantified claim and model described for The geometric phase diagram, diffusion, and spectra of random planar maps do not match any AIM target in the complete665-title inventory.
215: Classical2D O(n) mass generation is different from the fixed quantum spin-chain and Hubbard/Néel models (194/203/204).
216: XY/BKT2D roughening is not the3D Ising-interface roughening target (188).
217: Mean-field SK free-energy fluctuations are not planar/3D Edwards-Anderson spin glass targets.
218: Static Ising correlation/interface universality does not prove the specified Ising mixing/topology-preserving dynamics targets.
219: Random-regular-graph Anderson/GOE laws are not the Z^3 lattice Anderson extended-state target (015/303) or Sinai billiard GOE (211).
221: The quantified claim and model described for The Mézard–Parisi formula for diluted spin glasses do not match any AIM target in the complete665-title inventory.
222: Ising/spherical perceptron free energies are not the unregularized quadratic-network recovery target (550).
224: The quantified claim and model described for Critical and quenched near-critical universality for Poisson–Voronoi percolation do not match any AIM target in the complete665-title inventory.
225: The quantified claim and model described for Gaussian free field limits throughout the balanced six-vertex regime do not match any AIM target in the complete665-title inventory.
226: The quantified claim and model described for The double-dimer loop ensemble converges to CLE<sub>4</sub> do not match any AIM target in the complete665-title inventory.
227: Gaussian mean-field SK dynamics do not cover the deterministic ferromagnetic planar Ising mixing/scan-comparison targets.
228: Existence of selected3D radial potentials with temperature jumps is not the fixed2D hard-disk model (187).
229: Symmetric3/4-state broadcasting threshold is not the requested parsimony reconstruction comparison (328).
230: The quantified claim and model described for Exact Hausdorff gauges for SLE do not match any AIM target in the complete665-title inventory.
231: Free uniform spanning forest factor-IID is not3D minimal spanning forest connectivity (174).
232: The quantified claim and model described for Gaussian fields and interfaces for triangular-lattice Lipschitz heights do not match any AIM target in the complete665-title inventory.
233: The quantified claim and model described for The joint critical Ashkin–Teller current limit do not match any AIM target in the complete665-title inventory.
234: The quantified claim and model described for All-temperature pressure of orthogonally invariant Ising spin glasses do not match any AIM target in the complete665-title inventory.
235: The quantified claim and model described for Limiting random SAT thresholds, sharp variance and computability do not match any AIM target in the complete665-title inventory.
236: Ising spin factors on trees do not give invariant one-dependent proper colorings (583).
238: Thorp shuffle mixing is not the hypergraph one-particle spectral-gap comparison (607/609) or partition Burnside chain (535).
239: Symmetric random sign singularity rate is not the independent random tensor-column least-singular-value target (562).
240: The quantified claim and model described for Shelah's eventual categoricity and the prescribed-threshold obstruction do not match any AIM target in the complete665-title inventory.
241: The quantified claim and model described for Rigidity of the Turing degrees do not match any AIM target in the complete665-title inventory.
242: The quantified claim and model described for Single-fold Diophantine representations and undecidability under an at-most-one-solution promise do not match any AIM target in the complete665-title inventory.
243: The quantified claim and model described for Separating choiceless counting from polynomial time and witnessed choice do not match any AIM target in the complete665-title inventory.
244: The quantified claim and model described for The Partition Principle does not imply Choice do not match any AIM target in the complete665-title inventory.
245: The quantified claim and model described for Weak normalization implies strong normalization in pure type systems do not match any AIM target in the complete665-title inventory.
246: The quantified claim and model described for Cannon's conjecture do not match any AIM target in the complete665-title inventory.
247: The quantified claim and model described for An infinite finitely presented residually finite 2-group and a finitely presented nil algebra do not match any AIM target in the complete665-title inventory.
248: Nonamenability of one named group does not resolve the general countable-group unitarizability converse (038).

## PDF/source follow-up

All17 linked candidate/partial/related PDFs were also downloaded and text-inspected outside AIM. The exact main theorem number and PDF page are recorded in matches.json. The Birkhoff physical-collar companion theorem was read directly. The Cardy common-primal-edge Jordan-quad sandwich proof was inspected; its application to the smooth induced-domain/2delta electrode convention is an explicit scope inference. The honeycomb manuscript explicitly excludes lattice universality and a fixed-length endpoint lower bound. Verdicts remain unchanged.
