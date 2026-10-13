# OpenAI manuscript cross-reference, 13 October 2026

We screened all 372 current result families and all 719 manuscript links in [OpenAI's mathematics collection](https://github.com/openai/math) against the 665 active and retained AIM entries at `c9929805cece044705abaaebe1cebddac1ba11a6`. Three separate Codex AI reviewers handled families 001–124, 125–248 and 249–377; missing family numbers are not extra manuscripts. Plausible overlaps received actual theorem, definition and hypothesis comparisons, including necessary normalizations and reductions. Noncandidate screening used the family descriptions and constituent abstracts.

The review identifies **56 complete published theorem matches** and **10 substantive partial matches**. Complete matches are recorded as Solved under the repository's published-resolution route; this is not a new independent verification of every manuscript proof. No external human peer review, priority claim or fresh Lean kernel replay is attributed to this comparison. The original problem pages, IDs, statements and applications are preserved. All proof links point to OpenAI; no OpenAI PDF, TeX source or Lean source is uploaded here.

## Sources and verification scope

The [source inventory](source-inventory.json), [complete family screen](family-screen.json), [detailed comparisons](comparisons.json), [inspected source hashes](source-hashes.json) and [page-preservation record](page-preservation.json) pin the review to OpenAI revision `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. Every referenced manuscript/source path was checked against the untruncated upstream preprint tree, and inspected TeX content was checked against its Git blob IDs, normalizing Windows CRLF exports where needed. The source hash record distinguishes inspected from canonical bytes. Current release-history withdrawals and corrections were considered.

Lean scope notes and actual proof-module links are kept distinct from comparator challenge templates, which intentionally contain placeholders. The upstream formalization catalogue records its review status as `unchecked`; no public Actions runs or dated successful kernel/axiom receipts were found. The published toolchain is Lean 4.34.1. Full, partial and supporting formalizations are identified below; the [availability record](lean-availability.json) links their actual upstream proof modules and immutable hashes, but no entry is promoted to AIM Lean verified without the reproduction evidence required by [CONTRIBUTING](../../../CONTRIBUTING.md#status-and-evidence).

AIM 031 is a published computer-assisted resolution. Its paper reports a completed run and states arithmetic/compiler assumptions; the named native archive is absent from the pinned public manuscript directory. We did not reproduce that computation. This limitation is explicit in its page and comparison.

Issue [36](https://github.com/MColbrook/AIM/issues/36) supplied nine useful starting correspondences: its paired numbers mean AIM ID followed by OpenAI family ID, not two AIM IDs. The statement comparison supports eight complete matches and one partial match (AIM 016) from that list, plus 48 further complete matches and nine further partial matches. The two collections use separate numbering; AIM 261, 268, 213 and 325 therefore retain their own unrelated targets. AIM 087's triangular Gaussian-energy target also matches OpenAI family 090.

## Complete matches

| AIM | OpenAI family | Recorded outcome | External proof |
| --- | --- | --- | --- |
| [003](../../../problems/003-planar-convex-hot-spots.md) | 369 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/main.pdf) |
| [011](../../../problems/011-yau-nodal-upper-bound.md) | 350 | Counterexample | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/paper.pdf) |
| [015](../../../problems/015-anderson-extended-states.md) | 261 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf) |
| [023](../../../problems/023-complete-crouzeix.md) | 325 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf) |
| [031](../../../problems/031-mub-dimension-six.md) | 266 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf) |
| [034](../../../problems/034-kadison-kastler.md) | 289 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf) |
| [037](../../../problems/037-kadison-similarity.md) | 288 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/paper.pdf) |
| [038](../../../problems/038-dixmier-unitarizability.md) | 251 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf) |
| [046](../../../problems/046-rough-conductivity-calderon.md) | 365 | Counterexample | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf) |
| [047](../../../problems/047-smooth-anisotropic-calderon.md) | 365 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf) |
| [048](../../../problems/048-arbitrary-local-calderon-data.md) | 365 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf) |
| [050](../../../problems/050-static-lame-uniqueness.md) | 372 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/article.pdf) |
| [064](../../../problems/064-birkhoff-billiard-integrability.md) | 147 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/paper.pdf) |
| [065](../../../problems/065-standard-map-metric-entropy.md) | 146 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/paper.pdf) |
| [073](../../../problems/073-vlasov-maxwell-global-classical.md) | 362 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf) |
| [086](../../../problems/086-mahler-symmetric-four-dimensions.md) | 087 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf) |
| [087](../../../problems/087-triangular-universal-optimality.md) | 090 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf) |
| [088](../../../problems/088-critical-percolation-three-dimensions.md) | 213 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf) |
| [089](../../../problems/089-de-giorgi-dimension-five.md) | 375 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/article.pdf) |
| [090](../../../problems/090-square-bond-cardy-formula.md) | 223 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/paper.pdf) |
| [099](../../../problems/099-uniform-first-ionization.md) | 263 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf) |
| [127](../../../problems/127-cartan-hadamard-isoperimetry.md) | 337 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf) · [PDF 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Sharp-integral-fillings-in-CAT%280%29-spaces-September-23-2026/paper.pdf) |
| [153](../../../problems/153-ball-evans-three-dimensions.md) | 368 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf) · [PDF 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf) |
| [157](../../../problems/157-one-phase-critical-dimension.md) | 367 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf) |
| [164](../../../problems/164-quadratic-hilbert-sixteen.md) | 143 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf) |
| [169](../../../problems/169-strict-convexity-fpp.md) | 212 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf) |
| [171](../../../problems/171-absence-fpp-bigeodesics.md) | 212 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf) |
| [176](../../../problems/176-nonamenable-nonuniqueness-phase.md) | 214 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf) |
| [178](../../../problems/178-rwre-transience-ballisticity.md) | 220 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf) |
| [179](../../../problems/179-rwre-directional-zero-one.md) | 220 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf) |
| [194](../../../problems/194-haldane-gap.md) | 268 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf) |
| [196](../../../problems/196-thermodynamic-bose-condensation.md) | 267 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf) |
| [199](../../../problems/199-two-dimensional-area-law.md) | 265 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf) |
| [205](../../../problems/205-entropy-photon-number.md) | 273 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-entropy-photon-number-inequality-September-24-2026/paper.pdf) |
| [206](../../../problems/206-ppt-squared.md) | 272 | Counterexample | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf) |
| [207](../../../problems/207-amplitude-damping-additivity.md) | 276 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf) |
| [208](../../../problems/208-sphere-fourier-restriction.md) | 077 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf) |
| [209](../../../problems/209-bochner-riesz-three-dimensions.md) | 078 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf) |
| [210](../../../problems/210-euclidean-wave-local-smoothing.md) | 079 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf) |
| [227](../../../problems/227-renormalized-boltzmann-uniqueness.md) | 363 | Counterexample | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf) |
| [234](../../../problems/234-abrikosov-global-crystallization.md) | 090 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf) |
| [273](../../../problems/273-reaction-network-persistence.md) | 149 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/permanence.pdf) |
| [293](../../../problems/293-unique-games.md) | 102 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf) |
| [301](../../../problems/301-three-processor-unit-scheduling.md) | 124 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf) |
| [321](../../../problems/321-polynomial-trace-reconstruction.md) | 122 | Counterexample | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf) |
| [323](../../../problems/323-strong-thin-tree.md) | 174 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf) |
| [341](../../../problems/341-modified-integer-round-up.md) | 118 | Counterexample | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf) |
| [350](../../../problems/350-lane-emden-subcritical-system.md) | 370 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/paper.pdf) |
| [391](../../../problems/391-affine-bernstein-entire-low-dimensions.md) | 353 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf) |
| [401](../../../problems/401-mtw-convex-domains-transport-continuity.md) | 360 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf) |
| [419](../../../problems/419-infinity-harmonic-c1-three-dimensions.md) | 377 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/interior-c1-infinity-harmonic.pdf) |
| [447](../../../problems/447-triangular-hilbert-transform-l3.md) | 082 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf) |
| [448](../../../problems/448-fourier-l-log-l-pointwise-convergence.md) | 075 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf) |
| [450](../../../problems/450-stein-lipschitz-direction-hilbert-bound.md) | 083 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf) |
| [543](../../../problems/543-simplex-maximal-isotropic-constant.md) | 101 | Affirmative proof | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf) |
| [585](../../../problems/585-sidorenko.md) | 161 | Counterexample | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf) |

## Partial progress

| AIM | OpenAI family | What remains | External manuscript |
| --- | --- | --- | --- |
| [016](../../../problems/016-anderson-planar-localization.md) | 261 | Establish exponential decay for an entire orthonormal eigenbasis at every positive disorder, including weak disorder. Pure-point spectral type alone does not provide that decay. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf) |
| [028](../../../problems/028-matrix-multiplication-exponent.md) | 107 | Determine whether the exponent equals two; the improved upper bound remains strictly above two. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf) |
| [092](../../../problems/092-kls-poincare.md) | 093 | Obtain a universal bound for arbitrary isotropic log-concave measures without the additional subgaussian restriction. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf) |
| [098](../../../problems/098-maximal-molecular-ionization.md) | 263 | Control ground-state eigenvalues at the ionization threshold as well. The original definition of maximal charge includes such threshold eigenvalues. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf) |
| [142](../../../problems/142-irrational-nonergodic-polygon.md) | 150 | Decide whether an irrational polygon with four or more sides can be nonergodic, or rule out all such examples. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/weak-mixing-triangular-billiards.pdf) |
| [337](../../../problems/337-reed-colouring.md) | 184 | Prove the stated bound for arbitrary clique numbers and all degrees, or give a counterexample. The fixed-clique asymptotic subcase does not cover that full quantifier. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf) |
| [346](../../../problems/346-planar-halving-lines.md) | 183 | Reach an upper bound of order $`n^{1+\eta}`$ for every $`\eta>0`$, or disprove that near-linear target. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf) |
| [487](../../../problems/487-gnrs-minor-free-flow-cut.md) | 089 | Cover every fixed excluded-minor class; nonplanar minor-free classes may have unbounded treewidth. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf) |
| [491](../../../problems/491-simple-stochastic-games-polynomial-time.md) | 104 | Obtain a fixed polynomial-time algorithm for all encoded inputs. Quasipolynomial running time does not meet that requirement. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf) |
| [590](../../../problems/590-revised-peres.md) | 272 | Decide the prohibition for every finite-dimensional bound-entangled state and arbitrary device-independent protocols. | [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf) |

## Independent comparison reports

- [Families 001–124](agent001-review.md).
- [Families 125–248](agent125-review.md).
- [Families 249–377](agent249-review.md).

The coordinating agent also checked the issue's principal targets, normalized the source records, verified every cited PDF/source path and immutable source bytes, and checked preservation and catalogue integration. The reports distinguish full source reading for candidate statements from the broader topic screen.

## Detailed target comparisons

<a name="aim-003"></a>

### AIM 003 — OpenAI 369

Every nonzero real eigenfunction in the first positive Neumann eigenspace on every smooth bounded simply connected planar domain has no interior critical point and obeys strict interior inequalities against boundary extrema. Every convex target domain is simply connected; multiplicities and every vector in the eigenspace are explicitly included.

**Statement locator:** `build/sections/01-introduction.tex, thm:main and eq:hotspots`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strict-hot-spots-and-absence-of-interior-critical-points-on-smooth-simply-connected-planar-domains-September-24-2026/main.pdf).

**Lean scope:** docs/369 covers the full strict hot-spots conclusion via HotSpots. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/369.md).

<a name="aim-011"></a>

### AIM 011 — OpenAI 350

One fixed smooth metric on the closed connected three-sphere has exact nonzero real Laplace eigenfunctions with positive eigenvalues tending to infinity and nodal area divided by $`\sqrt{\lambda}`$ tending to infinity. This refutes the universal target; the smooth-surface upper bound is an additional positive subcase.

**Statement locator:** `build/sections/introduction.tex, thm:main (S3 fixed-metric counterexample)`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-counterexamples-to-Yaus-nodal-upper-bound-in-dimensions-three-and-four-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Geometry/NodalSets/Main.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Geometry/SmoothYau/ProductMetric/SphereProduct.lean) · [Module 3](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Geometry/SmoothYau/SphereMetric/ThreeSphere.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/350 describes fixed-metric counterexamples via SmoothYau (and a separate dimension-five YauCounterexample), as well as the surface theorem. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/350.md).

<a name="aim-015"></a>

### AIM 015 — OpenAI 261

For d=3 the theorem gives a fixed I=(-6+e2/2,-6+e2) inside (-6,6), a positive disorder threshold, I contained in spectrum and pure absolute continuity almost surely for each fixed coupling. A stated parity unitary flips the hopping sign to the target convention.

**Statement locator:** `build/01-introduction.tex, thm:main and eq:energy-windows`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf).

**Lean scope:** docs/261 only proves the planar spectral set; it covers neither the 3D absolute-continuity target nor planar pure-point type.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/261.md).

<a name="aim-016"></a>

### AIM 016 — OpenAI 261

Same uniform law and every fixed positive disorder. The theorem supplies pure-point type and a complete orthonormal eigenbasis but explicitly does not assert exponential eigenfunction decay.

**Statement locator:** `build/sections/introduction.tex, main:theorem and scope paragraph at line 95`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf).

**Lean scope:** docs/261 establishes only spectrum [-4-h,4+h], not pure-point type or exponential decay.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/261.md).

**Known cases:** The OpenAI manuscript proves pure-point spectrum and a complete orthonormal eigenbasis at every fixed positive disorder. Exponential localization was already known at strong disorder.

**Remaining target:** Establish exponential decay for an entire orthonormal eigenbasis at every positive disorder, including weak disorder. Pure-point spectral type alone does not provide that decay.

<a name="aim-023"></a>

### AIM 023 — OpenAI 325

All n,m, all degrees, arbitrary complex coefficient matrices and constant two match. The manuscript orders tensors A^j tensor C_j and AIM orders C_j tensor A^j; the tensor-factor flip is unitary and preserves the operator norm.

**Statement locator:** `build/main.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-direct-proof-of-the-complete-Crouzeix-inequality-September-26-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/DirectCrouzeix/CompleteBound.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/NumericalRange/Main.lean) · [Module 3](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/StructuralCrouzeix/Endpoint.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/325 covers the full finite-matrix target via DirectCrouzeix/CompleteCrouzeix, plus arbitrary-Hilbert and structural extensions. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/325.md).

<a name="aim-028"></a>

### AIM 028 — OpenAI 107

Exact complex arithmetic and arbitrary exponent slack match AIM. The theorem proves $`\omega\le9/4`$, improving the previous upper bound; it does not prove $`\omega=2`$ or $`\omega>2`$. Rectangular exponent-two bounds do not establish the square exponent.

**Statement locator:** `Theorem thm:main (section 1)`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/LinearAlgebra/MatrixFields/Conclusions/AllFieldsBound.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual endpoint complex_omega_le_nine_quarters is implemented; the comparator is a sorry-containing target file, not the certificate. This formalizes partial progress only; no replay/axiom log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/107.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/LinearAlgebra/MatrixMultiplication/Main.lean).

**Known cases:** Over the complex numbers, the square matrix-multiplication exponent is at most $`9/4`$, with exact algorithms using $`O_\varepsilon(n^{9/4+\varepsilon})`$ arithmetic operations.

**Remaining target:** Determine whether the exponent equals two; the improved upper bound remains strictly above two.

<a name="aim-031"></a>

### AIM 031 — OpenAI 266

The stated computer-assisted theorem excludes four arbitrary complex orthonormal bases in C6, without restricting the second Hadamard matrix to a known family, and concludes N(6)=3. It depends on the published binary64 arithmetic/compiler and complete-execution certificate conditions; no execution was reproduced by this agent. Section 7 reports a completed 4 October 2026 run with all 100 invocations accounted and no final unresolved records. Its native source/archive paths are named but those verification directories are absent from the pinned public preprints tree; the run was not independently reproduced.

**Statement locator:** `build/sections/introduction.tex, thm:main; manuscript Section 7 and Appendix A; build/sections/execution.tex, execute:finite-theorem and execute:observed`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf).

**Lean scope:** docs/266 only proves at most five bases and supporting Fourier cancellation. It does not prove N(6)=3 or exclude four.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/266.md).

**Evidence limitation:** Published observed-execution report checked. Referenced native code and computation archive not present under this folder in the pinned public tree; no independent run or compiler-semantics audit.

<a name="aim-034"></a>

### AIM 034 — OpenAI 289

The two-sided norm-unit-ball distance and the epsilon/delta quantifiers agree exactly for von Neumann algebras sharing identity I_H, the standard convention for the target. The separate one-sided near-inclusion and C*-algebra counterexamples do not refute this target.

**Statement locator:** `build/sections/01-introduction.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026/paper.pdf).

**Lean scope:** docs/289 covers the universal near-identity unitary conjugacy statement via StrongKadisonKastler. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/289.md).

<a name="aim-037"></a>

### AIM 037 — OpenAI 288

Exactly arbitrary unital complex C*-algebras, arbitrary complex Hilbert spaces and bounded unital algebra homomorphisms, without complete-boundedness assumption. The manuscript uses S*pi*S^-1 rather than S^-1*pi*S; replacing S by its inverse reconciles the conventions.

**Statement locator:** `build/sections/introduction.tex, thm:similarity`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/paper.pdf).

**Lean scope:** docs/288 describes the full unrestricted similarity theorem via KadisonSimilarity. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/288.md).

<a name="aim-038"></a>

### AIM 038 — OpenAI 251

The theorem proves amenability iff unitarizability for all discrete groups, including the exact countable target. Uniform boundedness and arbitrary complex Hilbert spaces agree.

**Statement locator:** `build/sections/introduction.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Unitarizability/AllDiscrete.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/251 covers full equivalence; DixmierAllDiscrete and Dixmier comparators. Available formalization, not locally kernel verified.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/251.md).

<a name="aim-046"></a>

### AIM 046 — OpenAI 365

Uniformly positive bounded real scalar conductivities on the smooth ball B(0,3) differ on positive volume and have exactly the same full weak H1/2-to-H-1/2 DN operator. This directly refutes the all-pairs target and even keeps both conductivities equal to one near the boundary.

**Statement locator:** `build/paper.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Conductivity/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/365 covers this full rough scalar-conductivity counterexample via Conductivity. It does not cover the separate smooth anisotropic papers. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/365.md).

<a name="aim-047"></a>

### AIM 047 — OpenAI 365

The explicit full-boundary corollary recovers arbitrary smooth metrics on any compact connected smooth n>=3 manifold by a diffeomorphism fixing every boundary point. Equal target pointwise normal-DN operators with the same boundary metric yield equal density-valued energy maps, so the corollary applies.

**Statement locator:** `build/sections/01-introduction.tex, main:full corollary`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Conductivity/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/365 links only the bounded-measurable scalar counterexample. No Lean formalization of this smooth anisotropic target is provided in the family document.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/365.md).

<a name="aim-048"></a>

### AIM 048 — OpenAI 365

The explicit scalar corollary proves equality throughout the closed domain for strictly positive smooth scalar conductivities from identical arbitrary same-patch voltage/flux measurements, all n>=3, with no inaccessible-boundary agreement assumption.

**Statement locator:** `build/sections/01-introduction.tex, main:scalar corollary`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Conductivity/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/365 links only the rough scalar nonuniqueness comparator, not the smooth same-patch uniqueness result.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/365.md).

<a name="aim-050"></a>

### AIM 050 — OpenAI 372

Exactly bounded connected smooth 3D domains, arbitrary smooth real lambda/mu, mu>0 and 3lambda+2mu>0, static zero-frequency displacement-to-traction map and recovery of both coefficients. No near-boundary or near-constant condition is added.

**Statement locator:** `build/sections/introduction.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Global-Uniqueness-for-the-Smooth-Isotropic-Elasticity-Inverse-Problem-September-24-2026/article.pdf).

**Lean scope:** docs/372 covers the full uniqueness target via ElasticityUniqueness. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/372.md).

<a name="aim-064"></a>

### AIM 064 — OpenAI 147

The AIM target assumes a smooth complete foliation of a full grazing annulus, including rational rotation levels. Phase-foliation rigidity permits merely continuous essential individually invariant leaves, for an arbitrary bounded C-infinity strictly convex positive-curvature planar table, and concludes ellipse. The smooth AIM foliation supplies the homeomorphism in the theorem. No closeness or symmetry is added. The physical-collar companion supplies the stated analytic input.

**Statement locator:** `Theorem 1.1, PDF page 1; Phase-foliation rigidity theorem, introduction.tex lines 17-33, label thm:main; companion Physical-collar rigidity theorem cited as Definition 1.1/Theorem 1.2.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Continuous-Phase-Foliations-Create-Analytic-Caustic-Collars-September-24-2026/paper.pdf).

**Lean scope:** No family Lean documentation linked; no complete-target verification evidence inspected.

<a name="aim-065"></a>

### AIM 065 — OpenAI 146

For the unit torus source map f_k(x,y)=(x+y+k sin(2 pi x), y+k sin(2 pi x)), every k above a positive threshold has positive entropy for normalized area. Coordinate scaling X=2 pi x,Y=2 pi y gives the exact AIM map with K=2 pi k, preserving normalized probability and entropy. Hence an admissible nonzero K exists.

**Statement locator:** `Theorem 1.1, PDF page 2; Introduction, theorem label main:entropy (first theorem).`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Positive-Metric-Entropy-for-the-Standard-Map-at-Large-Parameters-September-23-2026/paper.pdf).

**Lean scope:** StandardMapEntropy comparator defines the actual sine map and finite-partition entropy and the full parameter-tail statement. The comparator theorem ends in sorry; upstream proof-module and reproduction/axiom evidence must be evaluated separately. No local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/146.md).

<a name="aim-073"></a>

### AIM 073 — OpenAI 362

Exact one-species R3 relativistic Vlasov-Maxwell normalization, compact nonnegative smooth particle data, Cb-infinity finite-L2-energy fields and Gauss constraints. The global solution has compact phase-space support on each finite interval, so in particular bounded momentum support, preserves Gauss constraints and finite field energy; no size/symmetry restriction.

**Statement locator:** `build/sections/introduction.tex, thm:global and eq:data`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/VlasovMaxwell/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/362 describes the full target via VlasovMaxwell. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/362.md).

<a name="aim-086"></a>

### AIM 086 — OpenAI 087

Set n=4 in the unrestricted origin-symmetric convex-body inequality |K||Kpolar|>=4^n/n!. Compactness, nonempty interior, ordinary Euclidean polar and volume are exactly AIM hypotheses. Equality classification is extra, not needed.

**Statement locator:** `Theorem thm:main; equation eq:main-inequality`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Mahler/Classification.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Mahler/MainTheorem.lean) · [Module 3](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Geometry/PolarProducts/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual endpoint symmetric_mahler has no external hypothesis beyond compactness/convexity/symmetry/nonempty interior. Set n=4. No successful local replay/axiom audit.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/087.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Mahler/MainTheorem.lean).

<a name="aim-087"></a>

### AIM 087 — OpenAI 090

Use g(t)=exp(-pi*alpha*t) for every alpha>0. Any AIM periodic union of N translates of a lattice of covolume N is locally finite and has centered-disk density one. Its ordered-pair finite-disk energy per particle converges to the displayed per-cell average: each offset occurs with frequency 1/N, Gaussian tails are summable, and boundary pairs have vanishing normalized contribution. Both sides omit only equal-point self-interactions. The theorem therefore yields the full arbitrary-N periodic bound.

**Statement locator:** `Theorems thm:universal and thm:gaussian; transfer eq:gaussian-energy`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Triangular/Energy/Universal.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Triangular/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual universal_energy_minimum proves the all-configuration completely-monotone energy statement, and sharp_gaussian_minorants_atomic supplies every Gaussian parameter. Periodic per-cell identification is a mathematical transfer, not a separately replayed AIM adapter. No local verification log.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/090.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Triangular/Energy/Universal.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/Triangular/Main.lean).

<a name="aim-088"></a>

### AIM 088 — OpenAI 213

The theorem explicitly treats independent nearest-neighbor Bernoulli bond percolation on the ordinary cubic lattice Z^3 at its separately defined bond critical parameter. Almost surely no infinite cluster implies theta(p_c)=0. The additional site result is unnecessary for AIM coverage.

**Statement locator:** `Theorem 1.1, PDF page 1; Introduction theorem label thm:main, introduction.tex lines 17-22.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-bond-and-site-percolation-on-the-cubic-lattice-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Probability/CriticalZ3/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** CriticalZ3 comparator defines the cubic nearest-neighbor bonds and product Bernoulli law and states all critical clusters finite. Main comparator declaration uses sorry; no local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/213.md).

<a name="aim-089"></a>

### AIM 089 — OpenAI 375

The unrestricted monotone Allen-Cahn rigidity theorem is stated in dimension eight with no directional limits, energy growth or minimization hypothesis. Embed the target by U(x1,...,x8)=u(x1,...,x4,x8). The extra-coordinate independence forces their components of the resulting unit direction to vanish, giving exactly the dimension-five tanh profile with positive fifth component.

**Statement locator:** `build/sections/00-introduction.tex, thm:monotone`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/De-Giorgis-conjecture-in-dimension-eight-September-26-2026/article.pdf).

**Lean scope:** No Lean document is linked for this family.

<a name="aim-090"></a>

### AIM 090 — OpenAI 223

The Cardy theorem directly proves actual free-boundary square-lattice bond crossing probabilities with all edges independent at p=1/2, including boundary edges. Uniform marked Jordan approximation includes smooth AIM domains; the buffered boundary comparison transfers between lattice boundary arcs and the AIM O(mesh) boundary-vertex convention. Its beta-integral ratio equals the hypergeometric formula in AIM by the incomplete beta identity with a=b=1/3. This is an explicit crossing theorem, not an inference from the SLE abstract. The Jordan-quad transfer proof (chordal.tex, Proposition jordan:transfer and Corollary jordan:cardy) sandwiches actual edge crossings on a common primal grid between fixed-margin easier/harder quads. The same fixed-margin comparison applies to the smooth-domain induced graph and vertices within2delta of its designated arcs; this last reduction is the reviewer's geometric scope inference from that proof.

**Statement locator:** `Theorem 1.2, PDF page 6; Introduction theorem Cardy's formula, label intro:cardy, lines 235-245; free-boundary definitions lines 222-234 and boundary-transfer discussion immediately after.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Square-lattice-FK-interfaces-and-nested-loops-for-1-leq-q-lt-4-September-23-2026/paper.pdf).

**Lean scope:** No family Lean documentation linked; no complete-target local verification evidence inspected.

<a name="aim-092"></a>

### AIM 092 — OpenAI 093

A dimension-free LSI implies a Poincare bound by linearizing the entropy inequality at a constant. It gives AIM for isotropic log-concave densities whose linear subgaussian parameter a is bounded by a fixed absolute constant; uniform convex-body densities are allowed. General isotropic log-concave measures may have only exponential tails, so the subgaussian assumption is a genuine restriction and cannot be discarded.

**Statement locator:** `Theorem thm:main; subgaussian condition eq:intro-subgaussian`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-dimension-free-logarithmic-Sobolev-inequality-for-subgaussian-log-concave-measures-September-23-2026/paper.pdf).

**Lean scope:** No matching Lean scope is declared in the family catalogue/docs inspected.

**Known cases:** A dimension-free logarithmic Sobolev bound gives the required Poincare bound for isotropic log-concave measures with an absolute bound on their linear subgaussian parameter.

**Remaining target:** Obtain a universal bound for arbitrary isotropic log-concave measures without the additional subgaussian restriction.

<a name="aim-098"></a>

### AIM 098 — OpenAI 263

Same full fermionic Coulomb Hamiltonian with kinetic term $`-\Delta/2`$ and two spin states. The theorem proves $`N\le Z+CM`$ under strict binding $`E_N<E_{N-1}`$, for real charges at least one and all distinct positions. It expressly leaves threshold eigenstates outside its assertion, while the AIM Nmax includes them.

**Statement locator:** `build/sections/01-introduction.tex, thm:main and following threshold caveat`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/CoulombIonization/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/263 formalizes generalized large-ionization asymptotics and radii, not this strict-binding excess-charge bound.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/263.md).

**Known cases:** The stated excess-charge bound holds for strictly bound molecular sectors: $`E_N<E_{N-1}`$ implies $`N\le Z+CM`$ with a universal constant.

**Remaining target:** Control ground-state eigenvalues at the ionization threshold as well. The original definition of maximal charge includes such threshold eigenvalues.

<a name="aim-099"></a>

### AIM 099 — OpenAI 263

The first-ionization corollary proves universal two-sided positive bounds for neutral integer-Z atoms with exactly the target kinetic and spin normalization. Its upper bound settles the whole supremum question.

**Statement locator:** `build/sections/01-introduction.tex, cor:first-ionization`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/CoulombIonization/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/263 explicitly excludes fixed-m convergence; the selected comparators do not establish the first-ionization bound.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/263.md).

<a name="aim-127"></a>

### AIM 127 — OpenAI 337

The theorem includes all smooth complete simply connected n>=2 manifolds with Sec<=0 and every finite-volume finite-perimeter set. For the target smooth relatively compact domain, perimeter is boundary area; the coefficient is exactly n*omega_n^(1/n). This includes n>=5 with no additional geometric restriction. The CAT(0) companion separately states cor:cartan-hadamard with exactly the same smooth-domain inequality in every d>=3.

**Statement locator:** `build/sections/01-introduction.tex, thm:main with kappa=0`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf) · [PDF 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Sharp-integral-fillings-in-CAT%280%29-spaces-September-23-2026/paper.pdf).

**Lean scope:** docs/337 covers sharp integral-current filling in proper CAT(0) spaces via SharpCAT0Filling. The companion explicitly derives the smooth Cartan-Hadamard domain inequality by uniqueness of compactly supported top-dimensional fillings. This is mathematical target coverage with a geometric-current reduction, not a successful local kernel verification.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/337.md).

<a name="aim-142"></a>

### AIM 142 — OpenAI 150

The weak-mixing theorem applies to every nondegenerate irrational-angle Euclidean triangle under precisely normalized position-times-uniform-direction Liouville measure, excluding the same null vertex-hit trajectories. Weak mixing implies ergodicity, so every three-side instance of the requested irrational polygon example is impossible; the existential question for larger polygons remains open.

**Statement locator:** `Theorem 1.1, PDF page 1; Introduction theorem label thm:main, normalized measure immediately preceding.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/weak-mixing-triangular-billiards.pdf).

**Lean scope:** Family150 selected Lean docs formalize ergodicity of irrational triangles, which suffices for this partial exclusion; weak mixing is not the selected comparator claim. Comparator presence is not local verification.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/150.md).

**Known cases:** Every irrational-angle Euclidean triangle is weakly mixing, hence ergodic, for the specified Liouville billiard measure. This rules out a nonergodic example with three sides.

**Remaining target:** Decide whether an irrational polygon with four or more sides can be nonergodic, or rule out all such examples.

<a name="aim-153"></a>

### AIM 153 — OpenAI 368

The first manuscript covers $`1\le p\le2`$ and the second covers $`2<p<\infty`$. Together they prove strong $`W^{1,p}`$ approximation by smooth diffeomorphisms onto the same target for any bounded 3D domains and any Sobolev homeomorphism. No boundary smoothness or boundary equality is required; orientation-preserving maps are included.

**Statement locator:** `both manuscripts build/sections/01-introduction.tex, main:theorem`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-1-le-p-le-2-September-24-2026/main.pdf) · [PDF 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf).

**Lean scope:** No Lean document is linked for this family.

<a name="aim-157"></a>

### AIM 157 — OpenAI 367

Exactly J=integral(|grad u|^2+indicator(u>0)), one-homogeneous nonnegative global minimizers with arbitrary nonnegative Sobolev same-trace competitors. Every cone through dimension six is flat and a nonflat cone exists in dimension seven, so the target critical dimension is seven. Standard minimizer regularity supplies continuity for the existence example.

**Statement locator:** `build/paper.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026/The-critical-dimension-for-one-phase-Bernoulli-minimizers-September-24-2026.pdf).

**Lean scope:** docs/367 covers only existence of a nonflat cone in dimension seven via BernoulliNonflatInSeven; flatness in dimensions at most six is outside it, so it does not determine the full critical dimension.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/367.md).

<a name="aim-164"></a>

### AIM 164 — OpenAI 143

Uniform boundedness states that every real planar polynomial vector field of degree at most d has at most the finite integer B(d) isolated geometric periodic-orbit images in the whole plane, independent of coefficients. Specializing d=2 supplies H_2. Definitions match AIM without multiplicity.

**Statement locator:** `Theorem 1.1, PDF page 3; Uniform boundedness theorem, label thm:uniform, 01-introduction.tex lines 12-16.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026/uniform-bounds-for-planar-polynomial-limit-cycles-September-24-2026.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/LienardCycles/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Family143 Lean docs link only QuinticLienard: degree<=5 classical Lienard systems, not arbitrary quadratic planar vector fields. Thus complete AIM164 is not covered by the selected formal statement; no Lean verified status.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/143.md).

<a name="aim-169"></a>

### AIM 169 — OpenAI 212

The exponential limit-shape theorem covers undirected nearest-neighbor Z^2 FPP with independent exponential weights of any positive rate, including rate1. It explicitly gives strict convexity and the strict interpolation inequality for every pair of distinct boundary points, with no assumed curvature or geodesic hypothesis.

**Statement locator:** `Theorem 1.1, PDF page 3; The exponential limit shape theorem, label thm:exponential-shape, introduction.tex lines 21-32.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Probability/FirstPassage/BoundaryCurve.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Family212 docs explicitly say strict convexity is outside its selected differentiability comparators. A C1 boundary or unique supporting line does not imply strict convexity. No complete AIM169 formalization/verification supported by these links.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/212.md).

<a name="aim-171"></a>

### AIM 171 — OpenAI 212

The no-bigeodesics theorem rules out all injective doubly infinite nearest-neighbor minimizing paths simultaneously for every nonnegative nonatomic iid weight law satisfying E[min(X1,X2,X3,X4)^2]<infinity. Mean-one exponential weights satisfy this hypothesis (their minimum has rate4 and finite second moment). No direction restriction or shape assumption occurs.

**Statement locator:** `Theorem 1.1, PDF page 1; Introduction theorem label thm:main, 01-introduction.tex lines 24-37.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Probability/FirstPassage/BoundaryCurve.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Family212 selected Lean docs only cover differentiability of limit shapes; no bigeodesic comparator is linked. No full AIM171 formalization/verification supported.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/212.md).

<a name="aim-176"></a>

### AIM 176 — OpenAI 214

The theorem applies to every infinite connected locally finite nonamenable quasi-transitive graph and gives pc<p_(2to2)<=pu. Vertex-transitive AIM graphs are included. Its vertex-boundary nonamenability is equivalent to the AIM edge-boundary form on these uniformly bounded-degree graphs. Definitions of pc/pu agree.

**Statement locator:** `Theorem 1.1, PDF page 3; Introduction theorem label thm:main, introduction.tex lines 58-69; definitions/nonamenability preceding.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf).

**Lean scope:** Family214 docs link BenjaminiSchramm/CayleyPercolation statements for the relevant full graph class. Comparator templates alone are not reproduction evidence; no local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/214.md).

<a name="aim-178"></a>

### AIM 178 — OpenAI 220

Directional transience implies ballisticity is stated for every d>=2, iid nearest-neighbor transition rows with a common positive lower bound, every fixed unit direction, and annealed almost-sure escape. It gives a deterministic vector limit X_n/n and strictly positive projection in the same direction, exactly including AIM d=3.

**Statement locator:** `Theorem 1.1, PDF page 3; Directional transience implies ballisticity theorem, label thm:main, 01-introduction.tex lines 50-61.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Probability/Ballisticity/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** DirectionalBallisticity comparator constructs an environment sampled once and retained along the walk, annealed path law, uniform ellipticity, and the exact vector limit. The declaration uses sorry; no local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/220.md).

<a name="aim-179"></a>

### AIM 179 — OpenAI 220

The zero-one theorem covers every d>=3, iid nearest-neighbor transition rows, every fixed nonzero real direction, and merely strict positivity. Uniform ellipticity of the AIM Z^3 model is stronger and hence sufficient. Its escape event and annealed law from the origin agree exactly.

**Statement locator:** `Theorem 1.1, PDF page 2; Introduction theorem label thm:main, 01-introduction.tex lines 61-69, strict-ellipticity equation and path-law definitions preceding.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Probability/Ballisticity/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** DirectionalWalk comparator gives the iid product environment and annealed origin escape event; main declaration uses sorry. No local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/220.md).

<a name="aim-194"></a>

### AIM 194 — OpenAI 268

Identical pure spin-one antiferromagnetic coupling-one Hamiltonian on even periodic rings and next distinct eigenvalue convention. The positive bound holds for every even N>=60. Taking the minimum with the finitely many positive finite-dimensional gaps N=4,...,58 gives the required all-N uniform positive gap.

**Statement locator:** `build/introduction.tex, thm:main and immediately following small-chain paragraph`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-periodic-spin-one-Haldane-gap-September-24-2026/paper.pdf).

**Lean scope:** No Lean document is linked for this family; numerical/interval verification files are separate from Lean kernel verification.

<a name="aim-196"></a>

### AIM 196 — OpenAI 267

The density-uniform theorem covers every fixed bounded measurable nonzero nonnegative radial finite-range potential, so includes every target Cc-infinity potential. At T=0 its exact canonical ground state has occupation at least c*(V)>0 at every sufficiently dilute fixed density along all thermodynamic sequences, with trace-N density matrix and constant orbital.

**Statement locator:** `build/sections/introduction.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf).

**Lean scope:** docs/267 covers only the hard-sphere ground-state model. The target requires smooth finite-range potentials; that formalization does not cover it.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/267.md).

<a name="aim-199"></a>

### AIM 199 — OpenAI 265

Set interaction range R=1 and strength J=1. Rectangles and all nearest-neighbor/on-site terms are admitted, with only a unique ground state and a full-system gap. The vertical-cut edge boundary has exactly M edges, yielding C(q,1,1,Delta)M uniformly over L,M,ell and the interactions.

**Statement locator:** `build/sections/00-introduction.tex, thm:area and cor:rectangles`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-two-dimensional-area-law-from-a-global-spectral-gap-September-24-2026/paper.pdf).

**Lean scope:** No Lean document is linked for this family.

<a name="aim-205"></a>

### AIM 205 — OpenAI 273

The exact displayed g-inverse entropy photon-number inequality is proved for any finite number of modes, any transmissivity in [0,1], finite photon energy, product inputs, and arbitrary correlations within either port. Entropy uses natural logarithms as in the target.

**Statement locator:** `build/sections/00-introduction.tex, thm:epni`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-entropy-photon-number-inequality-September-24-2026/paper.pdf).

**Lean scope:** docs/273 describes the full EPnI target via EntropyPhotonNumber; only channel-capacity consequences are outside it. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/273.md).

<a name="aim-206"></a>

### AIM 206 — OpenAI 272

The manuscript constructs a trace-preserving PPT channel Theta on M21 whose square is not entanglement breaking. Taking Phi=Psi=Theta directly disproves the all-dimension all-channel target. The separate two non-trace-preserving maps would not by themselves be enough.

**Statement locator:** `build/source/sections/introduction.tex, thm:main-channel`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf).

**Lean scope:** docs/272 covers the dimension-21 trace-preserving PPT channel counterexample via DimensionTenChannel; the zero-secret-key statement is outside the comparators. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/272.md).

<a name="aim-207"></a>

### AIM 207 — OpenAI 276

The theorem establishes unrestricted tensor-power Holevo additivity for all generalized amplitude-damping parameters. At stationary excited population nu=0 the Kraus channel is the target ordinary amplitude-damping channel. Entropy and capacity are in bits, and arbitrary entangled block inputs are included.

**Statement locator:** `build/paper.tex, thm:main and generalized-channel definition`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/InformationTheory/AmplitudeDamping/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/276 covers tensor-power additivity for all parameters via AmplitudeDamping. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/276.md).

<a name="aim-208"></a>

### AIM 208 — OpenAI 077

The theorem states precisely the same S2 extension, phase 2*pi*i*x.omega, surface area measure, complex bounded measurable inputs, and every p>3 with a constant depending only on p. It reaches all remaining exponents. The diagonal positively-curved-surface companion also implies this on S2 by finite-measure embedding.

**Statement locator:** `Theorem thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026/Elliptic-capacity-propagation-and-Fourier-restriction-to-the-sphere-September-24-2026.pdf).

**Lean scope:** No matching Lean scope is declared in the family catalogue/docs inspected.

<a name="aim-209"></a>

### AIM 209 — OpenAI 078

The primary L3 estimate holds for every positive order; the explicitly read analytic-interpolation and duality corollary gives all 1<=p<=infinity under delta>max(3|1/p-1/2|-1/2,0). Restricting to AIM 1<p<infinity gives exactly its multiplier and full strict range. No equality endpoint is needed.

**Statement locator:** `Theorem thm:bochner-riesz; Corollary cor:full-bochner-riesz`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf).

**Lean scope:** No matching Lean scope is declared in the family catalogue/docs inspected.

<a name="aim-210"></a>

### AIM 210 — OpenAI 079

The half-wave and time interval [1,2] agree. The critical p=3 estimate permits every positive Sobolev loss; the read corollary/interpolation proof covers all p>2. For AIM p>=3 choose alpha=1-3/p+epsilon and localize to lambda<=|xi|<=2lambda; the annular multiplier bound gives lambda^alpha times the Lp input norm, uniformly in lambda>=1.

**Statement locator:** `Theorem thm:main; Corollary cor:full-range, eq:phys-full-range and its annular interpolation proof`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf).

**Lean scope:** No matching Lean scope is declared in the family catalogue/docs inspected.

<a name="aim-227"></a>

### AIM 227 — OpenAI 363

Two distinct global solutions have the same datum, exact target hard-sphere |(v-v*) dot omega| normalization, all weighted Q+ and Q- locally integrable, strong L1 initial traces, all five local conservation laws and entropy dissipation. The paper renormalizes F/M for a fixed Maxwellian. Locally integrable unrenormalized transport/collision equation gives the beta(F) chain rule along characteristics; conserved mass and kinetic energy turn relative entropy into the target absolute entropy inequality. The datum is rough, so this does not resolve smooth-data AIM074.

**Statement locator:** `build/paper/01-introduction.tex, thm:main and def:admissible`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf).

**Lean scope:** docs/363 covers the earlier periodic renormalized nonuniqueness theorem, not the later full local-conservation refinement. Comparator BoltzmannNonuniqueness; no local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/363.md).

<a name="aim-234"></a>

### AIM 234 — OpenAI 090

This companion is a separate direct theorem matching the Sandier-Serfaty/Abrikosov target. It uses the same divE=2*pi(sum delta-1), curlE=0, unit background, fixed-width smooth square cutoffs, puncture limit before limsup, self-energy pi*log(eta), normalization 4R^2, and covolume-one triangular field. Its density bound on centered disks is equivalent to AIM square growth bound by disk-square inclusions and local finiteness. The source derives local Lq (q<2) from the equations and permits nonperiodic competitors and infinite energies.

**Statement locator:** `Theorem thm:main; definitions eq:cutoffs, eq:admissible, eq:local-energy, eq:whole-energy`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Triangular-minimality-for-planar-Coulomb-renormalized-energy-September-23-2026/paper.pdf).

**Lean scope:** Family090 Lean docs cover Gaussian minorants/universal nonnegative pair energies and circle packing, not this renormalized Coulomb field theorem; no full AIM234 Lean certificate established.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/090.md).

<a name="aim-273"></a>

### AIM 273 — OpenAI 149

Uniform permanence holds for every finite weakly reversible mass-action network with fixed positive reaction rates and every positive initial state, with a classwise compact absorbing set contained in the strictly positive orthant. The eventual positive lower bound implies each AIM bounded global trajectory has positive liminf for every species; complex balance is not imposed. The theorem is stronger than the target because it also ensures global bounded positive solutions.

**Statement locator:** `Theorem 1.1, PDF page 2; Main theorem label thm:main, introduction.tex lines 43-60; epsilon_P bounds in equation eq:uniform-bounds.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/permanence.pdf).

**Lean scope:** Family149 Lean docs concern the September boundedness/persistence article, giving initial-state-dependent all-time bounds rather than classwise uniform October permanence. This is nevertheless sufficient for AIM273. MassAction comparator main statement uses sorry; no local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/149.md).

<a name="aim-293"></a>

### AIM 293 — OpenAI 102

Take the theorem errors epsilon=delta equal to AIM epsilon. The fixed alphabet F2^s depends only on the errors; translations are permutations. Output graphs are nonempty explicit unweighted simple bipartite instances, and value is ordinary classical fraction of satisfied edges. The deterministic polynomial reduction from 3SAT supplies exactly the NP-hard promise gap.

**Statement locator:** `Theorem thm:ugc`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Unique-Games-Theorem-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/MaxCut/Main.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/UniqueGames/Theorem.lean) · [Module 3](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/VertexCover/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual theorem11 returns BinaryGapReduction with a fixed alphabet/program before inputs, simple bipartite outputs, translations, completeness and soundness. No local replay/axiom log.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/102.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/UniqueGames/Theorem.lean).

<a name="aim-301"></a>

### AIM 301 — OpenAI 124

Arbitrary explicitly listed DAG, nonpreemptive unit-length jobs and exactly three identical machines agree. Its slot values 1..T equal AIM start times plus one. The theorem treats n>=1 and 1<=T<=n: AIM extra cases are immediate in polynomial time (n=0 feasible, T=0 with n>0 infeasible, T>=n feasible by topological sequential schedule). Thus binary arbitrary deadline and empty input add no unresolved case.

**Statement locator:** `Theorem thm:main; deterministic multitape time O((L+2)^150020)`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/Scheduling/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual main_theorem proves one finite machine and binary-input polynomial bound for nonempty n and normalized deadlines; the trivial edge-case adapter is not a separately replayed AIM theorem. No local verification record.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/124.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/Scheduling/Main.lean).

<a name="aim-321"></a>

### AIM 321 — OpenAI 122

Definitions match known length n, fixed known deletion probability q in (0,1), independent complete deletion traces (including length), randomized decoder common to all binary strings, unrestricted computation and exact recovery. Set success s=2/3. For each fixed q, n^(c*log(q^3*log n)) eventually exceeds Cq*n^kq for every constants Cq,kq. Hence the requested polynomial-sample assertion is false at every fixed channel.

**Statement locator:** `Theorem thm:main and thm:tv`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/quantitative-lower-bounds-for-trace-reconstruction-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Probability/TraceReconstruction.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual superpolynomial_sample_complexity and quantitative_sample_lower_bound agree with the unrestricted complete-trace target; inspected estimator definitions include decoder randomization. No successful local replay/axiom log.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/122.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Probability/TraceReconstruction.lean).

<a name="aim-323"></a>

### AIM 323 — OpenAI 174

The theorem quantifies one absolute C>0 over every integer k>=1 and every finite loopless k-edge-connected multigraph with >=2 vertices, counts parallel edges separately, and selects one spanning tree satisfying every nontrivial cut inequality C/k simultaneously. The efficient companion exceeds AIM's existence requirement.

**Statement locator:** `Theorem 1.1, PDF page 1; Main theorem label thm:main, source/sections/introduction.tex lines 17-28.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-strong-thin-tree-conjecture-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Combinatorics/ThinTrees/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** StrongThinTree comparator models edges by separate labels and states exactly the all-cut universal-constant result; declaration uses sorry. AlgorithmicThinTrees is additional. No local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/174.md).

<a name="aim-337"></a>

### AIM 337 — OpenAI 184

For each fixed integer r>=4, correspondence coloring of every K_r-free simple graph is at most ceil(C_r Delta/log Delta) for sufficiently large Delta. Since ordinary chi<=chi_DP, taking Delta sufficiently large that C_r/log Delta<=1/2 implies the exact Reed inequality for this bounded-clique subcase. The constants and threshold depend on the fixed clique cap; this does not handle arbitrary graph-dependent clique number or all degrees. This is a derived subset consequence rather than a manuscript theorem named Reed.

**Statement locator:** `Theorem 1.1, PDF page 2; Correspondence-coloring main theorem label thm:main, introduction.tex lines24-33; chi<=chi_list<=chi_DP preceding.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Correspondence-Coloring-Graphs-with-a-Forbidden-Clique-October-5-2026/correspondence-coloring-forbidden-clique.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Combinatorics/CliqueFree/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Family184 selected Lean docs only formalize the logarithmic independence lower bound (CliqueFreeLog), not the correspondence-coloring theorem used here; no full or direct partial Reed verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/184.md).

**Known cases:** For each fixed clique cap, the correspondence-coloring bound implies the exact Reed inequality at all sufficiently large maximum degrees; the threshold depends on that cap.

**Remaining target:** Prove the stated bound for arbitrary clique numbers and all degrees, or give a counterexample. The fixed-clique asymptotic subcase does not cover that full quantifier.

<a name="aim-341"></a>

### AIM 341 — OpenAI 118

The source explicitly uses unrestricted numerical-size type patterns, whose multiplicities are limited by capacity rather than input demand; this is the exact nonproper-pattern LP in AIM. Set c=1: LP=B integer and OPT>B+1 refutes MIRUP without a ceiling ambiguity. Convert rational sizes to integer item lengths using a common denominator W; positive integer type demands are multiplicities. Removing excess items identifies integer covering optimum with packing optimum. This is an unconditional structural counterexample, independent of NP!=P.

**Statement locator:** `Theorem thm:unbounded-gap; Definition def:configuration-lp`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/BinPacking/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual main_results proves unbounded gaps with both typeLP and individualLP equal integer B. The relevant typeLP preserves unrestricted patterns. Integer-length scaling is a mathematical adapter. No local replay/axiom log.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/118.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/BinPacking/Main.lean).

<a name="aim-346"></a>

### AIM 346 — OpenAI 183

The halving-power theorem counts exactly unordered pairs determining balanced straight lines of arbitrary even planar n-point sets with no three collinear. It gives an absolute fixed positive saving epsilon from4/3 for all sufficiently large even n; enlarging C covers finite smaller n. It neither supplies exponents1+eta for every eta>0 nor gives a disproof of that near-linear target.

**Statement locator:** `Theorem 1.1, PDF page 2; Power-saving halving theorem label thm:halving-power, introduction.tex lines9-16.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf).

**Lean scope:** HalvingLines comparator states the same fixed power saving for general-position sets, and a separate all-level bound for a stronger generic condition. Main declaration uses sorry; no local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/183.md).

**Known cases:** The manuscript improves the upper exponent for planar halving lines from $`4/3`$ to $`4/3-\varepsilon_0`$ for one absolute $`\varepsilon_0>0`$.

**Remaining target:** Reach an upper bound of order $`n^{1+\eta}`$ for every $`\eta>0`$, or disprove that near-linear target.

<a name="aim-350"></a>

### AIM 350 — OpenAI 370

The unweighted corollary covers n>=3 and all p,q>0 under exactly 1/(p+1)+1/(q+1)>(n-2)/n, excluding strictly positive entire C2 solutions without symmetry, decay, integrability, stability or energy assumptions. This includes every n>=5 target case.

**Statement locator:** `build/sections/01-introduction.tex, cor:lane-emden`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/HenonEmden/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/370 covers the complete unweighted target as a specialization of HenonEmden. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/370.md).

<a name="aim-391"></a>

### AIM 391 — OpenAI 353

For n=3,...,9 the theorem classifies smooth positive-Hessian affine maximal graphs complete in induced Euclidean metric. An entire graph is Euclidean-complete because its metric dominates Euclidean distance and the graph is closed. The C4 target bootstraps locally to smoothness: the positive cofactor matrix makes the w equation elliptic on compact subsets, and det(D2u)=w^(-(n+2)/(n+1)) plus local Monge-Ampere regularity iterates Schauder regularity. No growth or affine completeness is needed.

**Statement locator:** `build/main.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf).

**Lean scope:** docs/353 covers the smooth Euclidean-complete graph theorem via AffineBernstein. The C4 bootstrap and target comparison are mathematical implications, not a locally checked Lean theorem. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/353.md).

<a name="aim-401"></a>

### AIM 401 — OpenAI 360

Same squared-distance cost and weak MTW formula. The theorem gives an almost-everywhere unique optimal map with a global bi-Holder homeomorphic representative for measurable probability densities between fixed positive finite bounds on compact connected smooth manifolds. It does not require convex injectivity domains in advance, so covers the target assumptions.

**Statement locator:** `build/sections/introduction.tex, thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/BiholderTransport/Main.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Geometry/WeakMTW/Convexity.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** docs/360 covers full bi-Holder transport via BiholderTransport. Supporting finite-family geometric statements have narrower scope. No local kernel log inspected.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/360.md).

<a name="aim-419"></a>

### AIM 419 — OpenAI 377

The theorem gives interior C1,alpha in every dimension d>=3 for continuous viscosity infinity-harmonic functions, including zero-gradient tests. The corollary explicitly localizes by bounded compact balls, so the target arbitrary continuous 3D solution has continuous gradient locally. Connectedness is handled componentwise.

**Statement locator:** `build/manuscript/sections/01-introduction.tex, thm:main and cor:interior-c1`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Interior-C1alpha-Estimates-for-Infinity-Harmonic-Functions-October-4-2026/interior-c1-infinity-harmonic.pdf).

**Lean scope:** No Lean document is linked for this family.

<a name="aim-447"></a>

### AIM 447 — OpenAI 082

The operator is literally AIM integral F(x+t,y)G(x,y+t)dt/t with both finite hard truncation endpoints. An absolute bound for the pointwise supremum over epsilon,R in L^(3/2), for arbitrary complex L3 inputs, dominates every individual truncation. This is a full resolution, stronger than AIM; it is not merely the dyadic companion.

**Statement locator:** `Theorem thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/TriangularHilbert/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual main_estimate formalizes the maximal estimate and full-measure/measurability conditions with genuine hard integrals. No local replay/axiom log.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/082.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/TriangularHilbert/Main.lean).

<a name="aim-448"></a>

### AIM 448 — OpenAI 075

Source torus R/(2*pi*Z) with normalized measure and e^(ikx) is AIM unit torus after x=2*pi*y. Integrability with log(2+|f|) is equivalent to log(e+|f|), with bounded ratio and finite measure. Both state complex measurable data and a single null set outside which the entire sequence of ordinary symmetric partial sums converges to f.

**Statement locator:** `Theorem thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/FourierLLogL/PaperMain.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual paperMain establishes full symmetric sums for measurable complex LlogL data on the normalized 2*pi torus; coordinate rescaling identifies AIM. No local reproduction/axiom log.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/075.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/FourierLLogL/PaperMain.lean).

<a name="aim-450"></a>

### AIM 450 — OpenAI 083

The theorem assumes all 1-Lipschitz unit fields on R2, allows both coordinates, holds at absolute outer scale a*>0, and proves a strong L2 principal-value bound and the exact weak-(2,2) inequality for Schwartz data. Choose AIM K=1/a* (>=1) and C=C*^2. Symmetric principal values exist pointwise on Schwartz inputs.

**Statement locator:** `Theorem thm:main`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-uniform-Hilbert-transform-estimate-for-Lipschitz-directions-September-25-2026/main.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/LipschitzHilbert/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual main provides principal-value and weak-(2,2) at an existential short scale; uniform_truncation additionally gives the reciprocal-Lipschitz bound. It discharges laceyLiInput through a proved import, not an external assumption in the endpoint. No local replay/axiom audit.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/083.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Analysis/LipschitzHilbert/Main.lean).

<a name="aim-487"></a>

### AIM 487 — OpenAI 089

The results establish constant distortion for all planar graphs and every fixed treewidth bound, with arbitrary positive real lengths and arbitrary demands. They do not cover every fixed excluded minor: minor-free classes can include nonplanar graphs of unbounded treewidth. Finite L1 metrics are finite nonnegative sums of cut metrics, giving AIM finite-dimensional real ell1. Nonnegative edge lengths are obtained by adding epsilon to each edge then taking a limit in the finite-dimensional cut cone (or contracting zero components); distortion constant is preserved.

**Statement locator:** `Theorem thm:main in each manuscript`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Combinatorics/PlanarL1/Embedding.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Combinatorics/TreewidthL1/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Actual endpoints cover positive-length planar and fixed-treewidth metrics only. They do not formalize the full arbitrary-excluded-minor target or the zero-length transfer. No local verification record.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/089.md).

**Proof source:** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Combinatorics/PlanarL1/Embedding.lean) · [Module 2](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Combinatorics/TreewidthL1/Main.lean).

**Known cases:** Universal distortion holds for planar graph metrics, and distortion depending only on the treewidth bound holds for every fixed bounded-treewidth class. The comparison explains the finite-dimensional cut-metric and zero-length-edge reductions.

**Remaining target:** Cover every fixed excluded-minor class; nonplanar minor-free classes may have unbounded treewidth.

<a name="aim-491"></a>

### AIM 491 — OpenAI 104

The deterministic algorithm has bit time 2^O((log(L+2))^2), which is quasipolynomial, not a fixed polynomial. The source explicitly reduces reachability >=1/2 to nonnegative expectation-of-liminf mean payoff with absorbing rewards +/-1, including nonabsorbing plays. AIM strict >1/2 is also obtainable: pure positional SSG values are rational with denominator at most 3^n by integer linear systems and Hadamard; positive 2v-1 is >=3^-n. Multiply all +/-1 rewards by 2*3^n and subtract 1 from every edge, so nonnegative mean payoff holds iff v>1/2. This has polynomial encoding length and preserves the quasipolynomial bound.

**Statement locator:** `Theorem thm:main and explicit simple-stochastic-game reduction in section 1`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Turn-Based-Stochastic-Mean-Payoff-Games-in-Deterministic-Quasipolynomial-Time-October-5-2026/stochastic-mean-payoff-games.pdf).

**Available upstream proof modules (family scope):** [Module 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/OAI/Computability/RandomMean/Main.lean). Their relation to this AIM target is governed by the scope note below; availability is not a kernel verification record.

**Lean scope:** Docs104 formalize only randomized ordinary mean-payoff and a finite Truffet counterexample. They do not declare a formalization of this deterministic stochastic algorithm or AIM491.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/104.md).

**Known cases:** A deterministic quasipolynomial-time algorithm decides the reachability threshold, including the strict comparison requested here after the rational-value gap reduction described in the review. Polynomial algorithms were already known when the number of random vertices is fixed and for the stopping ladder class; see references 1–2.

**Remaining target:** Obtain a fixed polynomial-time algorithm for all encoded inputs. Quasipolynomial running time does not meet that requirement.

<a name="aim-543"></a>

### AIM 543 — OpenAI 101

The source definition of L_K is exactly (det covariance/volume^2)^(1/(2n)), and its all-dimensional arbitrary-convex-body inequality has precisely AIM simplex constant. No symmetry/polytope restriction appears. Equality uniqueness is extra. This resolves the sharp target, not merely the weaker uniform slicing constant.

**Statement locator:** `Theorem intro:simplex; equation intro:simplex-bound`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-sharp-entropy-bound-and-the-simplex-inequality-for-isotropic-constants-October-5-2026/isotropic-simplex.pdf).

**Lean scope:** No matching Lean scope is declared in the family catalogue/docs inspected.

<a name="aim-585"></a>

### AIM 585 — OpenAI 161

Main theorem explicitly produces a finite simple unweighted host G with at least one edge and a fixed finite simple bipartite incidence graph H with35 vertices and66 edges for which t(H,G)<p(G)^66. Definitions t=hom/n^v and p=2|E|/n^2 match AIM, including noninjective maps. Thus this is a complete negative resolution, not only a weighted or graphon counterexample.

**Statement locator:** `Theorem 1.1, PDF page 1; Main theorem label thm:main, introduction.tex lines18-26; definitions lines1-15.`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf).

**Lean scope:** SidorenkoCounterexample comparator explicitly defines the22 triples, incidence graph, all homomorphisms and finite simple host deficit. Main declaration uses sorry; forcing consequence is outside selected Lean statement and irrelevant to AIM585. No local verification claimed.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/161.md).

<a name="aim-590"></a>

### AIM 590 — OpenAI 272

An explicit PPT entangled state on C10 tensor C10 has zero distillable secret key for arbitrary admitted completed protocols; PPT ensures bound entanglement. A positive device-independent key protocol would give a positive trusted-device key protocol, so this supplies a substantive affirmative case of the target, not its universal conclusion.

**Statement locator:** `build/source/sections/introduction.tex, thm:main-state and operational-extension paragraph`.

**External proof:** [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf).

**Lean scope:** docs/272 explicitly excludes the zero-distillable-secret-key statement; only PPT-composition consequences are formalized.

**Upstream documentation:** [Scope 1](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/272.md).

**Known cases:** The explicit dimension-ten PPT bound-entangled state has zero distillable secret key even with trusted devices, and therefore cannot yield a device-independent secret key. Reference [1, Section III.B] also rules out a specified one-way protocol using the Vertesi–Brunner state and measurements; that earlier result leaves arbitrary protocols open.

**Remaining target:** Decide the prohibition for every finite-dimensional bound-entangled state and arbitrary device-independent protocols.

## Related results that do not settle these targets

- AIM 091 / OpenAI 237: The main fixed-length theorem and gyration corollary concern uniformly sampled honeycomb walks, diameter and radius-of-gyration moments. AIM fixes Z^2 square-lattice walks and endpoint mean-square displacement. A lattice-universality transfer and endpoint-versus-diameter lower-moment comparison are absent. This is a substantive analogue, not a solved subcase of the exact target. The actual PDF explicitly states that its assertions do not include a lattice-universality theorem or a fixed-length endpoint-displacement lower bound. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Mass-and-covering-exponents-for-fixed-length-honeycomb-walks-September-26-2026/main.pdf).
- AIM 303 / OpenAI 261: A purely absolutely continuous spectral interval does not imply the fixed-disorder all-large-time two-sided diffusive mean-square displacement rate requested by AIM303. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf).
- AIM 018 / OpenAI 262: The theorem is one-dimensional, finite matrix-valued and has the scalar one-bound-state coefficient. AIM018 fixes the three-dimensional scalar gamma=1 semiclassical coefficient 1/(15*pi^2). Neither the dimension nor sharp coefficient matches; no target subclass resolution follows. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/sharp-matrix-lieb-thirring.pdf).
- AIM 195 / OpenAI 269: The theorem is the fermionic spherical V1 projector at filling 1/3 with cubic Laughlin polynomial. AIM195 is bosonic planar Bargmann contact interaction at filling 1/2 with a total-degree cutoff and squared Laughlin polynomial. These are different Hamiltonians, statistics and geometries, not a subset of the target. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026/A-Fock-space-inequality-and-the-Laughlin-spectral-gap-September-24-2026.pdf).
- AIM 197 / OpenAI 267: Quantum depletion and condensation bounds do not establish the thermodynamic Wu logarithmic energy coefficient with an error little-o of rho*a^3*abs(log(rho*a^3)). [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/fixed-repulsion-quantum-depletion.pdf).
- AIM 100 / OpenAI 263: Ionization asymptotics in the limit m->infinity and Z/m->infinity do not prove convexity of E(N,Z) at every N and integer Z, or give a counterexample. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/paper.pdf).
- AIM 032 / OpenAI 272: The constructed states come from PPT maps and have positive partial transpose. They do not give the negative-partial-transpose all-copy nondistillability required by AIM032. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf).
- AIM 051 / OpenAI 365: The theorem recovers a metric and a unitary rank-two connection. It does not recover an arbitrary real scalar Schrodinger potential on a fixed general manifold from one zero-frequency DN map. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/paper.pdf).
- AIM 055 / OpenAI 365: Metric recovery from an elliptic DN map does not by itself give recovery from the boundary-distance function of smooth simple manifolds; no conversion between these data is proved here. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf).
- AIM 452 / OpenAI 353: Affine maximal surfaces solve a specific fourth-order cofactor equation. AIM452 concerns arbitrary smooth uniformly elliptic second-order F(D2u)=0 with bounded Hessian in dimensions three and four. The objects and equations differ. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf).
- AIM 154 / OpenAI 368: Strong forward W1p diffeomorphic approximation alone does not guarantee convergence of an elastic energy with singular determinant/compression penalties. The high-p manuscript explicitly distinguishes this question. [PDF](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Strong-diffeomorphic-approximation-in-three-dimensions-for-p-gt-2-September-24-2026/main.pdf).

A related theorem on a different model is not labelled a solved subcase. In particular, honeycomb-walk diameter/gyration results do not prove the square-lattice endpoint-displacement assertion in AIM 091; the missing lattice and observable transfers are recorded in the comparison.

Five pre-existing untracked draft solution directories are preserved untouched. Catalogue checks run on a snapshot of the tracked repository plus the intended changes, excluding those unfinished drafts.

## Final integration checks

The [independent integration audit](integration-audit.md) checked all 66 preserved targets, metadata and dates, all 719 manuscript paths, inspected source hashes and reader-facing links. It caught and then confirmed correction of the Sidorenko outcome label. The small math-formatting refinements noted by that review were applied, and earlier special cases for AIM 491 and 590 were retained alongside the new progress.

All **58 catalogue regression tests passed** in 558.738 seconds; the [complete log](catalogue-regression.log) is retained. After the final outcome, presentation and evidence refinements, [catalogue generation and validation](final-catalogue-checks.json) passed for all 651 problem pages, metadata, math formatting, local links and the generated lists. The [final integrity record](final-validation.json) confirms 56 complete matches, ten partial matches, seven counterexamples, and no removed problems or added OpenAI PDFs/sources. The final lists contain 582 open targets and 83 solved entries. No whole-target Lean verification is claimed by this integration.
