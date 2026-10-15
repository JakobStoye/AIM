# Prior-resolution reports for 37 Open or Partial catalogue targets

**Evidence review date:** 2026-10-16

**Prepared by:** OpenAI Codex at the request of Kaiwen Jin (yui.ui.siki@gmail.com). The source comparisons, summaries and editorial assembly were performed by AI. The original mathematical results are credited to the linked sources.

**Catalogue snapshot:** [`a153f469ee0ea64e876b2ad97c79d252c19a3e22`](https://github.com/MColbrook/AIM/tree/a153f469ee0ea64e876b2ad97c79d252c19a3e22). The IDs and target comparisons below refer to this revision.

## Scope and review status

A review of 85 previously identified prior-resolution records found 48 already marked Solved at this snapshot. The other 37 were still Open (28) or Partial (9). This report collects those 37 source reports in one place, with a link from each affected problem page.

Each entry identifies a public proof or counterexample, its relevant theorem or proof location, and the correspondence with the full catalogue target. Applicability comparisons reuse readings of theorem statements and the named proof interfaces made on 12–15 October 2026; the target snapshot and public source availability were checked again for this report. These readings do not constitute a new independent audit of every argument or imported dependency.

The source evidence varies: recent preprints, an explicitly labeled candidate proof, a public formal-proof claim, and applications of published results. Under the [contribution policy](../../CONTRIBUTING.md#status-and-evidence), a complete claim awaiting independent review belongs in Solution claimed; Solved requires the specified publication or independent audit evidence. This evidence report leaves final catalogue status decisions to that review. Current badges are recorded below, and the earlier dated search notes are preserved on the problem pages.

## Index

| ID | Target | Current badge | Reported direction |
| --- | --- | --- | --- |
| [030](#aim-030) | [SIC measurements in every finite dimension](../../problems/030-sic-povms.md) | 🔵 OPEN | Reported affirmative full-target resolution |
| [044](#aim-044) | [Quadratic-scale bit complexity for well-conditioned sparse systems](../../problems/044-sparse-linear-solve-bit-complexity.md) | 🔵 OPEN | Affirmative prior-result attribution |
| [092](#aim-092) | [The dimension-free Kannan–Lovász–Simonovits inequality](../../problems/092-kls-poincare.md) | 🟡 PARTIAL | Claimed affirmative dimension-free Poincaré bound |
| [098](#aim-098) | [A universal bound on excess molecular charge](../../problems/098-maximal-molecular-ionization.md) | 🟡 PARTIAL | Reported full eigenstate application, including threshold states |
| [108](#aim-108) | [Uniqueness of the critical catenoid](../../problems/108-critical-catenoid-uniqueness.md) | 🔵 OPEN | Claimed affirmative uniqueness of the critical catenoid |
| [110](#aim-110) | [Linear growth of interior Steklov nodal volume](../../problems/110-steklov-bulk-nodal-volume.md) | 🟡 PARTIAL | Negative: no universal linear interior nodal-volume upper bound |
| [111](#aim-111) | [Unbounded first Steklov multiplicity with fixed boundary count](../../problems/111-steklov-fixed-boundary-multiplicity.md) | 🔵 OPEN | Affirmative prior theorem plus elementary specialization |
| [123](#aim-123) | [Sard conjecture for smooth bracket-generating distributions](../../problems/123-sard-conjecture-endpoint-map.md) | 🟡 PARTIAL | Counterexample to the universal nullity claim |
| [125](#aim-125) | [Nonbranching of analytic equiregular sub-Riemannian geodesics](../../problems/125-equiregular-analytic-nonbranching.md) | 🔵 OPEN | Negative: branching counterexample |
| [126](#aim-126) | [Pansu's isoperimetric conjecture in the Heisenberg group](../../problems/126-pansu-heisenberg-isoperimetry.md) | 🔵 OPEN | Affirmative isoperimetric inequality |
| [142](#aim-142) | [An irrational polygon with nonergodic billiard flow](../../problems/142-irrational-nonergodic-polygon.md) | 🟡 PARTIAL | Reported negative answer via the zero-frequency argument |
| [175](#aim-175) | [Does supercritical percolation preserve transience?](../../problems/175-percolation-preserves-transience.md) | 🟡 PARTIAL | Affirmative transience of every infinite cluster |
| [195](#aim-195) | [The bosonic Laughlin contact-interaction gap](../../problems/195-laughlin-gap.md) | 🔵 OPEN | Claimed affirmative spectral gap |
| [214](#aim-214) | [Optimal spectral signings of regular graphs](../../problems/214-bilu-linial-signing.md) | 🟡 PARTIAL | Negative: cubic signing counterexample |
| [216](#aim-216) | [Boundary-flux commutators for rough conductors](../../problems/216-rough-coefficient-boundary-commutator.md) | 🔵 OPEN | Reported negative answer from a published elliptic example |
| [241](#aim-241) | [Uniqueness of a hemispheric saddle profile on a magnetic sphere](../../problems/241-spherical-ferromagnet-profile-uniqueness.md) | 🔵 OPEN | Reported negative uniqueness result |
| [250](#aim-250) | [A periodic nonsingular billiard trajectory in every triangle](../../problems/250-periodic-triangular-billiard.md) | 🟡 PARTIAL | Affirmative periodic billiard orbit |
| [251](#aim-251) | [Asymptotic density of reflected wavefronts in a disk](../../problems/251-disk-wavefront-density.md) | 🔵 OPEN | Reported affirmative late-time wavefront density |
| [298](#aim-298) | [The Li–Li multiple-unicast conjecture](../../problems/298-li-li-multiple-unicast.md) | 🔵 OPEN | Negative: network coding beats multicommodity routing |
| [325](#aim-325) | [A constant bound for fixed-order prefix discrepancy](../../problems/325-strong-komlos-prefix-discrepancy.md) | 🔵 OPEN | Negative: fixed-order prefix discrepancy is unbounded |
| [330](#aim-330) | [The sharp matroid secretary conjecture](../../problems/330-sharp-matroid-secretary.md) | 🔵 OPEN | Claimed affirmative sharp matroid-secretary guarantee |
| [338](#aim-338) | [Decidability of local asymptotic stability for polynomial ODEs](../../problems/338-polynomial-local-stability-decidability.md) | 🔵 OPEN | Negative: local asymptotic stability is undecidable |
| [340](#aim-340) | [The modern integer 3SUM conjecture](../../problems/340-integer-three-sum-hardness.md) | 🔵 OPEN | Negative answer to the proposed quadratic-time barrier |
| [342](#aim-342) | [Additivity of entanglement of purification](../../problems/342-entanglement-of-purification-additivity.md) | 🔵 OPEN | Claimed negative additivity result |
| [348](#aim-348) | [Non-explosion of Brownian Fleming–Viot systems in arbitrary domains](../../problems/348-brownian-fleming-viot-nonexplosion.md) | 🔵 OPEN | Negative: finite-time branching explosion |
| [361](#aim-361) | [Can one-dimensional entropy-dissipating systems have two bounded solutions?](../../problems/361-one-dimensional-convex-entropy-nonuniqueness.md) | 🔵 OPEN | Affirmative existence of two entropy-dissipating solutions |
| [392](#aim-392) | [Regularity of transport interfaces for nonconvex polyhedral targets](../../problems/392-polyhedral-transport-singular-interface.md) | 🔵 OPEN | Affirmative interface regularity |
| [393](#aim-393) | [Singular-set dimension of polyhedral partial-transport free boundaries](../../problems/393-polyhedral-partial-transport-free-boundary.md) | 🔵 OPEN | Affirmative partial-transport free-boundary regularity |
| [394](#aim-394) | [Villani’s convex-injectivity-domain conjecture](../../problems/394-villani-mtw-convex-injectivity-domains.md) | 🔵 OPEN | Affirmative convex injectivity domains |
| [412](#aim-412) | [Sharp vanishing-viscosity control time for downstream transport](../../problems/412-positive-transport-sharp-uniform-control-time.md) | 🔵 OPEN | Negative: transport time alone does not suffice |
| [425](#aim-425) | [Excess Floquet multiplicity for complex periodic Schrödinger equations](../../problems/425-complex-hill-excess-multiplicity.md) | 🔵 OPEN | Affirmative existential example via published primary source and elementary translation |
| [433](#aim-433) | [A nonlinear Weyl lemma at the minimal p-harmonic integrability threshold](../../problems/433-very-weak-p-harmonic-energy-regularity.md) | 🔵 OPEN | Negative: very weak p-harmonic solutions need not have p-energy |
| [446](#aim-446) | [The sharp Beurling–Ahlfors bound for planar elliptic systems](../../problems/446-beurling-ahlfors-sharp-norm.md) | 🔵 OPEN | Claimed affirmative sharp Beurling–Ahlfors norm |
| [462](#aim-462) | [A finite-integrability ABP estimate for general nonlocal Pucci operators](../../problems/462-nonlocal-pucci-finite-integrability-abp.md) | 🔵 OPEN | Negative: no general finite-integrability ABP estimate |
| [521](#aim-521) | [Six-point persistence on the Euclidean two-sphere](../../problems/521-six-point-sphere-persistence.md) | 🔵 OPEN | Negative for the literal proposed persistence region |
| [578](#aim-578) | [A real nearest matrix with spectrum in the closed left half-plane](../../problems/578-nearest-hurwitz-real-minimizer.md) | 🔵 OPEN | Negative: the complex minimum can be strictly smaller |
| [619](#aim-619) | [Spanning triangulated spheres with holes in surface triangulations](../../problems/619-spanning-holed-sphere-triangulation.md) | 🟡 PARTIAL | Negative: a ten-vertex genus-two obstruction |

<a id="aim-030"></a>

## 030 — SIC measurements in every finite dimension

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/030-sic-povms.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Danylo Radchenko and Campbell Wheeler, Stark units for real quadratic fields and reciprocity laws (Hexagon 2610.00186v1, 2026-10-10)](https://hexagonmath.org/pdf/2610.00186v1).

**Location:** Proposition 7 and its proof, Section 9.2, printed p.17, and the immediately following SIC deduction

**Reported answer:** Reported affirmative full-target resolution.

**Full-target correspondence:** The source claims simultaneous unit-modulus conjugation and deduces M² equiangular lines in C^M for every M≥4. Together with the explicit low-dimensional cases, this was classified as covering the existence of d² unit vectors with squared overlaps 1/(d+1) for every d≥2; covariance is not required by the target.

**Scope and evidence limits:** Recent public preprint explicitly involving substantial LLM assistance. The inherited classification is source-target attribution, not independent correctness certification. The deduction uses the cited earlier construction interfaces.

**Evidence status:** Public preprint/source claim; not a journal-accepted theorem on the evidence extracted. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

**Supporting source:** [Danylo Radchenko and Campbell Wheeler, Real quadratic fields and finite quantum dilogarithms I, arXiv:2609.21892v2 (2026-09-29); Theorem 7, Section 4.4 pp.20–21; Remark 7 p.22](https://arxiv.org/html/2609.21892v2).

**Supporting source:** [Marcus Appleby, Steven T. Flammia and Gene S. Kopp, A constructive approach to Zauner’s conjecture via the Stark conjectures, arXiv:2501.03970v2 (2025-03-17); Theorem 1.46 and Section 5.6 pp.87–88](https://arxiv.org/pdf/2501.03970v2).

<a id="aim-044"></a>

## 044 — Quadratic-scale bit complexity for well-conditioned sparse systems

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/044-sparse-linear-solve-bit-complexity.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Jonathan A. Kelner, Solving Linear Systems in Otilde(mn log(kappa/epsilon)) Bit Operations (arXiv:2609.38101v1, 2026-09-29)](https://arxiv.org/pdf/2609.38101v1).

**Location:** Theorem 1.1 p.3; Theorem 3.3 p.10; Lemma 3.4 and Section 3.3 pp.11–12; Section 4 pp.12–14

**Reported answer:** Affirmative prior-result attribution.

**Full-target correspondence:** The cited zero-preserving integer solve and residual representation, with elementary rational-input and residual-to-forward-error translation, were classified as covering the frozen sparse rational linear-system bit-complexity target. For fixed c, polynomial condition number and input bit length yield the requested soft O_c(nm) bit bound and relative error n^(-c); the cited core is deterministic.

**Scope and evidence limits:** The headline floating-input residual theorem alone is insufficient. The inherited match relies on the cited integer/normalization interfaces and elementary translation; this report does not independently certify the recent preprint.

**Evidence status:** Public preprint, v1; publication or independent acceptance not established. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-092"></a>

## 092 — The dimension-free Kannan–Lovász–Simonovits inequality

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/092-kls-poincare.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [Pierre Bizeul, Boaz Klartag and Joseph Lehec, Presenting a proof of the Kannan–Lovász–Simonovits conjecture, arXiv:2610.05474v1](https://arxiv.org/abs/2610.05474v1).

**Location:** Theorem 1.1, p. 2; concluding proof, p. 30.

**Reported answer:** Claimed affirmative dimension-free Poincaré bound.

**Full-target correspondence:** The source theorem covers every dimension and all isotropic log-concave densities, including convex extended-real potentials. Its variance and gradient definition agrees with the catalogue, and smooth compactly supported tests are a subclass of its locally Lipschitz tests. The separately listed second source covers covariance bounded by the identity and includes a weak-limit treatment of general nonsmooth laws.

**Scope and evidence limits:** The original target is unchanged in the current snapshot. Its newer Partial note concerns a different, subgaussian-only source; that restriction is not being silently removed from that theorem.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

**Supporting source:** [Krishnakumar Balasubramanian and Shiva Kasiviswanathan, A Dimension-Free Bound on the Poincaré Constant of Isotropic Log-Concave Measures, arXiv:2610.07728v1, Theorem 1.1 and the general-measure argument](https://arxiv.org/abs/2610.07728v1).

<a id="aim-098"></a>

## 098 — A universal bound on excess molecular charge

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/098-maximal-molecular-ionization.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [OpenAI, Uniform excess charge for Coulomb molecules and the outer radius of neutral atoms, 24 September 2026](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-excess-charge-for-Coulomb-molecules-and-the-outer-radius-of-neutral-atoms-September-24-2026/paper.pdf).

**Location:** Introduction theorem and threshold caveat; Sections 2, 6, 8 and the final molecular bound in Section 9.

**Reported answer:** Reported full eigenstate application, including threshold states.

**Full-target correspondence:** The reported application uses the supplied ground-state eigenfunction rather than the strict-binding argument used to produce one. For a sufficiently large violating eigenstate, the source plateau and sector monotonicity place its energy at the global sector minimum. The existing weighted estimate permits E_(N-1)>=E_N, including equality, and yields N<=3*Z. The molecular screening and terminal contradiction are then applied to that given normalized eigenstate without a new quantitative estimate.

**Scope and evidence limits:** The source headline theorem explicitly excludes threshold eigenstates, and the current catalogue correctly records that limitation. The extension above concerns the existing proof interfaces and requires review; it is not a quotation of an all-threshold theorem stated in the source. No strict-binding hypothesis is silently substituted for the original target.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-108"></a>

## 108 — Uniqueness of the critical catenoid

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/108-critical-catenoid-uniqueness.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Otis Chodosh and Matilde Gianocca, Free boundary minimal surfaces of genus zero, arXiv:2609.13054v1](https://arxiv.org/abs/2609.13054v1).

**Location:** Theorem 1.1 and Corollary 1.2; concluding proof, p. 10.

**Reported answer:** Claimed affirmative uniqueness of the critical catenoid.

**Full-target correspondence:** An annulus has genus zero, so the corollary gives the full rotation classification without additional index or symmetry assumptions. The explicit normalizations agree: T*tanh(T)=1 implies T^2*cosh(T)^2=cosh(T)^2+T^2, equating the catalogue scale with 1/(T*cosh(T)).

**Scope and evidence limits:** The independent source listed below also states the annulus classification. These are public preprints; their mere existence does not establish independent proof acceptance.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

**Supporting source:** [Davide Parise and Jonathan J. Zhu, Uniqueness of free boundary minimal annuli, arXiv:2609.17512v1, Theorem 1.1](https://arxiv.org/abs/2609.17512v1).

<a id="aim-110"></a>

## 110 — Linear growth of interior Steklov nodal volume

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/110-steklov-bulk-nodal-volume.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [OpenAI, Power-law violations of Yaus nodal upper bound, 23 September 2026](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Power-law-violations-of-Yaus-nodal-upper-bound-September-23-2026/paper.pdf).

**Location:** Theorem 1.1; exact eigenfunction construction and concluding proof in Section 5.7, pp. 31–33.

**Reported answer:** Negative: no universal linear interior nodal-volume upper bound.

**Full-target correspondence:** The source gives one fixed smooth closed five-manifold N and exact real eigenfunctions phi_j with H4(Z_phi_j)/sqrt(lambda_j) unbounded. On the fixed smooth product M=N times [-L,L], U_j=phi_j*cosh(sqrt(lambda_j)*t) is a Steklov eigenfunction with sigma_j=sqrt(lambda_j)*tanh(L*sqrt(lambda_j)) at both boundary components. Its interior nodal set is Z_phi_j times (-L,L), so the nodal volume divided by sigma_j is unbounded.

**Scope and evidence limits:** This refutes the universal two-sided assertion through its upper bound in dimension six. It does not disprove the lower bound or every lower-dimensional version. The product estimate includes singular nodal sets.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-111"></a>

## 111 — Unbounded first Steklov multiplicity with fixed boundary count

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/111-steklov-fixed-boundary-multiplicity.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Anass Nifa, Prescribed Steklov spectra and multiplicities on surfaces, Zenodo v1, DOI 10.5281/zenodo.22949635](https://zenodo.org/api/records/22949635/files/Prescribed_Steklov_Spectra_nifa.pdf/content).

**Location:** Theorem A; genus threshold Gamma(N,1)=ceil(N(N−1)/4)

**Reported answer:** Affirmative prior theorem plus elementary specialization.

**Full-target correspondence:** The inherited mapping fixes one boundary component and prescribes the first j positive Steklov eigenvalues to equal 1, with the next eigenvalue above 2, on an orientable surface of sufficiently large genus. Hence first-positive multiplicity j is unbounded when genus and metric may vary, while boundary count remains fixed.

**Scope and evidence limits:** The theorem concerns the ordinary unweighted smooth Steklov operator, with exact spectra rather than an approximate or weighted model. The official record API and its PDF were accessible; both bytes and PDF hash match the earlier reviewed version.

**Evidence status:** Public Zenodo manuscript; journal publication status UNVERIFIED. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-123"></a>

## 123 — Sard conjecture for smooth bracket-generating distributions

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/123-sard-conjecture-endpoint-map.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [Antonio Lerario, Luca Rizzi and Daniele Tiberio, A sub-Riemannian endpoint map with no regular values, arXiv:2609.05991v1](https://arxiv.org/pdf/2609.05991v1).

**Location:** Theorem 1.1(i) p.2; Lemma 2.1 pp.5–6; Lemma 3.1 and Proposition 3.2 pp.7–9; Proposition 4.1 pp.9–10; Lemma 4.3 and Proposition 4.4 pp.11–12

**Reported answer:** Counterexample to the universal nullity claim.

**Full-target correspondence:** The inherited mapping uses a smooth global rank-two bracket-generating distribution on R⁴ for which every endpoint from a fixed origin is reached by a singular L² control. The triangular system gives a global endpoint map on the full L² control domain, so its singular endpoints fill R⁴ and have nonzero volume for every smooth positive volume density.

**Scope and evidence limits:** This refutes the unrestricted smooth target. It does not say every control is singular or settle variants with additional analytic, equiregular or minimizing assumptions.

**Evidence status:** Public preprint v1, submitted 2026-09-05; PDF manuscript date differs (September 9). OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-125"></a>

## 125 — Nonbranching of analytic equiregular sub-Riemannian geodesics

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/125-equiregular-analytic-nonbranching.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Tommaso Rossi, Alec Jacopo Almo Schiavoni Piazza and Alessandro Socionovo, Interior singularity and branching of geodesics in real-analytic sub-Riemannian manifolds, arXiv:2603.23068v3](https://arxiv.org/abs/2603.23068v3).

**Location:** Theorem 1.3 and Section 10, pp. 35–36; Section 9 supplies the base construction.

**Reported answer:** Negative: branching counterexample.

**Full-target correspondence:** The Carnot-group lift gives an analytic left-invariant frame with a constant-rank bracket flag and globally minimizing branches. The two controls agree before the branching time. Their speeds agree, so a common arclength parametrization puts both unit-speed curves on the same interval with positive initial agreement and later separation.

**Scope and evidence limits:** Version v3 contains the equiregular Carnot lift; the earlier Martinet-only construction would not suffice.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-126"></a>

## 126 — Pansu's isoperimetric conjecture in the Heisenberg group

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/126-pansu-heisenberg-isoperimetry.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Chen, Kao and Lien, The Sharp Isoperimetric Inequality in the First Heisenberg Group, arXiv:2610.07632v1](https://arxiv.org/abs/2610.07632v1).

**Location:** Theorem 1.1; Proposition 3.1, pp. 13–17; Proposition 4.7 and final proof, pp. 27–28.

**Reported answer:** Affirmative isoperimetric inequality.

**Full-target correspondence:** The theorem covers all measurable sets with finite positive volume and finite horizontal perimeter. The coordinate change Phi(x,y,t)=(x,y,-2t) sends the catalogue frame to the source frame and multiplies both volume and perimeter by 2. Its sharp inequality therefore becomes P(E)^4 >= (256*pi^2/27)|E|^3 in the catalogue normalization, with the stated bubbles giving equality.

**Scope and evidence limits:** The smooth sets used in approximation are not additional regularity assumptions on competitors. Imported regularity results have not been independently recertified here.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-142"></a>

## 142 — An irrational polygon with nonergodic billiard flow

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/142-irrational-nonergodic-polygon.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [OpenAI, Weak mixing of triangular billiards with an irrational angle, 5 October 2026](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/weak-mixing-triangular-billiards.pdf).

**Location:** Theorem 1.1; Sections 2–4 at zero frequency; Section 5 reflection argument.

**Reported answer:** Reported negative answer via the zero-frequency argument.

**Full-target correspondence:** The proposed applicability reduction uses the source's zero-frequency argument on the double of a fixed bounded simple polygon. There are finitely many cone tips; replacing three local cone neighborhoods by finitely many changes fixed constants. Spatial constancy and reflection across adjacent sides then give invariance under an irrational angular rotation, eliminating nonconstant angular Fourier modes for the full Liouville flow.

**Scope and evidence limits:** The published source statement concerns triangles. The all-simple-polygon extension is the applicability argument being reported, not a theorem literally stated in the source. This distinction needs explicit mathematical review before changing the catalogue status.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-175"></a>

## 175 — Does supercritical percolation preserve transience?

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/175-percolation-preserves-transience.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [Diskin, Easo, Radhakrishnan, Sudakov and Tassion, Supercritical sharpness of percolation, arXiv:2603.03257v1](https://arxiv.org/abs/2603.03257v1).

**Location:** Corollary 1.1, equation (1) and footnote 1, p. 3; model and main results, p. 1.

**Reported answer:** Affirmative transience of every infinite cluster.

**Full-target correspondence:** The corollary states that on an infinite locally finite transitive transient graph, every infinite iid bond-percolation cluster is almost surely transient for every p>p_c. A Cayley graph for a finite generating set is in this class. Countability and transitivity identify the catalogue's existence threshold with the fixed-origin threshold. The endpoint p=1 follows from the assumed transience.

**Scope and evidence limits:** The simultaneous 'every infinite cluster' quantifier is essential. The cited proof dependencies are imported; no assertion about critical percolation is made.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-195"></a>

## 195 — The bosonic Laughlin contact-interaction gap

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/195-laughlin-gap.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Xin Shen (prepared and curated), The Bosonic Laughlin Spectral Gap: A Candidate Proof, version 0.1, 7 October 2026](https://github.com/Shencongli/bosonic-laughlin-spectral-gap/blob/fda5da170a1a87c2a7a8e970254c7073c228a99a/paper.pdf).

**Location:** Main proof in paper.tex, lines 55–823, including the final all-particle, all-degree plane inequality.

**Reported answer:** Claimed affirmative spectral gap.

**Full-target correspondence:** The Gaussian Bargmann orbital normalization and unordered-pair coefficients agree with the catalogue. The claimed full-plane inequality H^2>=H/3 holds for all particle numbers and degree sectors; restricting to the invariant degree range at most N(N-1) and applying finite-dimensional spectral calculus gives the catalogue's uniform lower bound 1/3 for positive eigenvalues.

**Scope and evidence limits:** The source explicitly says candidate proof and discloses AI involvement. Human review and a full Lean theorem are not established. No independent replay of every finite certificate or optimized-threshold appendix is claimed.

**Evidence status:** AI-assisted candidate proof, explicitly labeled by the source. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-214"></a>

## 214 — Optimal spectral signings of regular graphs

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/214-bilu-linial-signing.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [Zhiqiang Xu, A 3-regular counterexample to the Bilu–Linial signing conjecture, arXiv:2609.15591v4](https://arxiv.org/abs/2609.15591v4).

**Location:** Theorem 1.1; Section 2 construction, Section 4 main proof and Sections 3, 5–6 supporting interfaces.

**Reported answer:** Negative: cubic signing counterexample.

**Full-target correspondence:** The source gives a finite connected simple 3-regular graph for which every signing has signed-adjacency operator norm greater than 2*sqrt(2). Because the signed adjacency matrix is real symmetric, this means an eigenvalue lies outside the catalogue's required two-sided interval. One cubic graph refutes the assertion for every degree and every graph.

**Scope and evidence limits:** A bound only on the largest eigenvalue would not answer the two-sided question. No Ramanujan-base hypothesis occurs in the catalogue.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-216"></a>

## 216 — Boundary-flux commutators for rough conductors

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/216-rough-coefficient-boundary-commutator.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Norman G. Meyers, An Lp-estimate for the gradient of solutions of second order elliptic divergence equations, 1963](https://www.numdam.org/article/ASNSP_1963_3_17_3_189_0.pdf).

**Location:** Section 5, printed p. 204, displayed equations (65)–(66) and the homogeneous solution.

**Reported answer:** Reported negative answer from a published elliptic example.

**Full-target correspondence:** In the upper unit half-disk take the rotated Meyers example C=P_radial+(1/16)P_tangential and u=y*r^(-3/4). It has finite energy and boundary trace g=y. With multiplier phi=1, its weak conormal derivative on the positive flat diameter must be -x^(-3/4)/16, whose square is not integrable. Thus g*phi is not in the L2 Dirichlet-to-Neumann domain, contradicting the asserted universal domain inclusion.

**Scope and evidence limits:** This is a concrete applicability counterexample to the catalogue formulation, not a claim that Meyers stated the modern commutator theorem. A later literature description still calling the problem open is a scope conflict requiring review.

**Evidence status:** Published primary source; the displayed applicability reduction needs review. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-241"></a>

## 241 — Uniqueness of a hemispheric saddle profile on a magnetic sphere

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/241-spherical-ferromagnet-profile-uniqueness.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [shivm, public proof dated 5 October 2026](https://prove2.me/theorems/2f49ead8-433f-4b5e-9fc9-c44349429863).

**Location:** Full-profile construction and slope-3/slope-5 shooting certificates for kappa=4.

**Reported answer:** Reported negative uniqueness result.

**Full-target correspondence:** At the allowed parameter kappa=4, the source constructs both h(theta)=2*theta and a different smooth profile from an initial slope in [3,5]. The source includes the endpoint, reflection, pole-regularity and induced Cartesian-field bridges required by the catalogue. Restriction of that field to the unit sphere is elementary, so one legal parameter disproves universal uniqueness.

**Scope and evidence limits:** The site reports a Lean proof, but the exact source was not locally elaborated with a pinned dependency and axiom audit in this review. Do not label this report Lean verified or infer closure from a statement template containing sorry.

**Evidence status:** Public formal-proof claim; local kernel reproduction not performed. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-250"></a>

## 250 — A periodic nonsingular billiard trajectory in every triangle

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/250-periodic-triangular-billiard.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [Giovanni Forni, Existence of a Periodic Orbit for Billiards in Polygons, arXiv:2606.10102v1](https://arxiv.org/abs/2606.10102v1).

**Location:** Theorem 1.1; regular unit-tangent phase space in Section 2; final proof via Lemma 5.11 and Corollary 5.13.

**Reported answer:** Affirmative periodic billiard orbit.

**Full-target correspondence:** The polygon theorem specializes directly to every nondegenerate triangle, without rational-angle or genericity restrictions. A regular compact periodic orbit has finitely many transverse side-interior collisions, obeys the specular law and returns with both position and direction. This is exactly the catalogue's nonsingular periodic trajectory.

**Scope and evidence limits:** The fixed-version PDF controls the correspondence; the experimental HTML displayed a date discrepancy. Independent whole-paper proof review is not asserted.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-251"></a>

## 251 — Asymptotic density of reflected wavefronts in a disk

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/251-disk-wavefront-density.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Damien Thomine, Keplerian shear in ergodic theory, Annales Henri Lebesgue 3 (2020), 649–676](https://ahl.centre-mersenne.org/item/10.5802/ahl.42.pdf).

**Location:** Theorem 3.3 and the forward proof of Theorem 3.9.

**Reported answer:** Reported affirmative late-time wavefront density.

**Full-target correspondence:** For a noncentral source of radius r>0 in the disk, use a compact impact-parameter interval inside [0,r/2]. In unit-speed chord coordinates the two frequencies are 1/(2*sqrt(1-b^2)) and acos(b)/(2*pi*sqrt(1-b^2)). Analytic nonresonance lets the Keplerian-shear result apply to the fixed base marginal with Dirac fibers. Continuous positive bump functions and a finite cover give the catalogue's spatial density for every sufficiently late real time.

**Scope and evidence limits:** The invariant base sigma-algebra is part of the argument; Theorem 3.9 alone is not cited as an explicit disk-wavefront theorem. The center r=0 and a uniform rate are excluded. The physical frequency normalization must be checked rather than copied from Proposition 3.7.

**Evidence status:** Published primary source; the displayed applicability reduction needs review. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-298"></a>

## 298 — The Li–Li multiple-unicast conjecture

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/298-li-li-multiple-unicast.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Mark Braverman and Zhongtian He, The Multiple Unicast Conjecture is False, arXiv:2610.10108v1](https://arxiv.org/abs/2610.10108v1).

**Location:** Theorem 1.1; deterministic causal construction in Section 4 and Appendix B.

**Reported answer:** Negative: network coding beats multicommodity routing.

**Full-target correspondence:** The source's finite undirected unit-capacity graph has 182 vertices, 735 physical edges and 157 independent F9 messages. Its finite causal schedule uses each physical edge for one symbol in one direction and decodes every input tuple. Repeating independent executions meets the hard block-symbol capacities, whereas routing requires paths of length at least 5 and hence common rate at most 147/157<1.

**Scope and evidence limits:** The noncausal Section 3 certificate is not used. Zero-capacity connecting edges, if needed for connectedness, carry no routing flow and are allowed by the catalogue.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-325"></a>

## 325 — A constant bound for fixed-order prefix discrepancy

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/325-strong-komlos-prefix-discrepancy.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Shiva Kintali, On the Fixed-Order Strong Komlós Conjecture, ECCC TR26-242](https://eccc.weizmann.ac.il/report/2026/242/).

**Location:** Definition 1.1; Lemma 2.2; Theorem 3.1 and proof, p. 5.

**Reported answer:** Negative: fixed-order prefix discrepancy is unbounded.

**Full-target correspondence:** The theorem constructs fixed finite sequences of Euclidean-unit columns in dimension 2^(2^k-1), such that every offline sign assignment has a prefix and coordinate with discrepancy at least 2^(k/2-1). This tends to infinity with k, refuting an absolute constant independent of dimension and sequence length.

**Scope and evidence limits:** The signs may be selected offline and separately for every column occurrence. The positive witness is a nonempty prefix, not the empty prefix.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-330"></a>

## 330 — The sharp matroid secretary conjecture

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/330-sharp-matroid-secretary.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Zhiyi Huang, Settling the Matroid Secretary Problem, arXiv:2609.30421v1](https://arxiv.org/abs/2609.30421v1).

**Location:** Theorem 1; model on pp. 2–3; Sections 4–5 and proof on p. 12.

**Reported answer:** Claimed affirmative sharp matroid-secretary guarantee.

**Full-target correspondence:** The source covers finite abstract matroids in a less-informed ordinal model. Assigning sorted internal iid uniform arrival times to the observed random permutation gives the source model without future information. Each optimal-basis element is selected with probability at least 1/e; linearity of expectation gives expected selected weight at least OPT/e. Feasibility and online irrevocability are preserved.

**Scope and evidence limits:** The catalogue imposes no polynomial-running-time requirement. Empty optimum and loops are trivial cases; no missing efficiency claim is added.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-338"></a>

## 338 — Decidability of local asymptotic stability for polynomial ODEs

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/338-polynomial-local-stability-decidability.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Ivan O. Shevchenko, Jun Liu and Xinzhi Liu, Global asymptotic stability of homogeneous polynomial vector fields is undecidable, arXiv:2610.12434v1](https://arxiv.org/abs/2610.12434v1).

**Location:** Theorem 1.5; Section 1.1 definitions; rational polynomial reduction in Sections 13–15.

**Reported answer:** Negative: local asymptotic stability is undecidable.

**Full-target correspondence:** The undecidable rational homogeneous subclass has an effective finite coefficient encoding. For a homogeneous field of degree d, rescaling a nearby solution y from lambda*x gives lambda^(-1)*y(lambda^(1-d)*t) from x. Thus local attraction and nearby forward completeness imply global attraction and completeness; stability is the same clause. A total local-stability decider would decide the source subclass.

**Scope and evidence limits:** The correspondence concerns autonomous continuous-time rational polynomial fields and maximal classical solutions, including stability and forward completeness, rather than a weaker convergence-only property.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-340"></a>

## 340 — The modern integer 3SUM conjecture

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/340-integer-three-sum-hardness.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Josh Alman and Virginia Vassilevska Williams, Truly Subquadratic 3SUM and Truly Subcubic APSP via Triangles in Sparse Lopsided Graphs, arXiv:2610.06783v1](https://arxiv.org/abs/2610.06783v1).

**Location:** Theorems 2 and 22; Section 3.4, p. 36; distinct 3-LDT application, p. 10.

**Reported answer:** Negative answer to the proposed quadratic-time barrier.

**Full-target correspondence:** The source gives a deterministic O(n^1.9992) integer 3SUM algorithm for every fixed polynomial universe. Its cited distinct-3-LDT reduction applies to the coefficients (1,1,-1), preserving distinct elements for a+b=c. Deterministic color coding adds only O(log^2 n) calls and O(n log^2 n) preprocessing, retaining a fixed exponent saving in the specified logarithmic-word RAM model.

**Scope and evidence limits:** The distinctness condition and all preprocessing are included. This is not an inference from a real-RAM result with an incompatible integer representation.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

**Supporting source:** [Dudek, Gawrychowski and Starikovskaya, Equivalences between Non-trivial Variants of 3LDT and Conv3LDT, arXiv:2001.01289v2, Theorem 2.3 and Lemmas 3.3–3.4](https://arxiv.org/abs/2001.01289v2).

<a id="aim-342"></a>

## 342 — Additivity of entanglement of purification

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/342-entanglement-of-purification-additivity.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Artus Krohn-Grimberghe, The entanglement of purification is not additive, arXiv:2609.29539v1](https://arxiv.org/abs/2609.29539v1).

**Location:** Theorem 1; Section 2 and Appendix A.1; proof/certificate interfaces in the appendices.

**Reported answer:** Claimed negative additivity result.

**Full-target correspondence:** The source claims a finite n for which E_P(W^n)<n*E_P(W) for ordinary von Neumann entanglement of purification. Taking the first failing power k gives E_P(W^(k-1) tensor W)<E_P(W^(k-1))+E_P(W), an allowed pair of finite-dimensional states in the requested party grouping. This reduction does not require k=2.

**Scope and evidence limits:** The proof is computer-assisted. Its public artifact was retrieved and its documented hashes checked in the source screen; a complete independent verifier replay was not performed. The finite-ancilla interface also uses Ibinson–Linden–Winter, Corollary 3.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

**Supporting source:** [Essential verification artifact, Zenodo record 22097511](https://zenodo.org/records/22097511).

**Supporting source:** [Ibinson, Linden and Winter, quant-ph/0611057, Corollary 3](https://arxiv.org/abs/quant-ph/0611057).

<a id="aim-348"></a>

## 348 — Non-explosion of Brownian Fleming–Viot systems in arbitrary domains

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/348-brownian-fleming-viot-nonexplosion.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Yaohui Lin and Tiankui Lu, Branching explosion of Brownian Fleming–Viot systems, arXiv:2610.18802v1](https://arxiv.org/abs/2610.18802v1).

**Location:** Theorem 1.1; Section 7, especially Lemma 7.2, Proposition 7.3 and the concluding proof, pp. 49–55.

**Reported answer:** Negative: finite-time branching explosion.

**Full-target correspondence:** For each fixed N>=3 the source constructs a bounded connected open domain in R^3 where the classical driftless Brownian system with uniform copying explodes with positive probability before every positive time, from every interior configuration. Taking N=3 and d=3 refutes the catalogue's universal non-explosion assertion. The final common-clock construction establishes the actual Brownian/copying model and infinitely many branchings.

**Scope and evidence limits:** The domain has no smooth-boundary guarantee, and none is required by the catalogue. An auxiliary singular-drift process alone would not settle this target.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-361"></a>

## 361 — Can one-dimensional entropy-dissipating systems have two bounded solutions?

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/361-one-dimensional-convex-entropy-nonuniqueness.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Sam G. Krupa, The computational ansatz for convex integration of hyperbolic systems and a resolution of the Strong Trace Conjecture, arXiv:2609.09353v1](https://arxiv.org/abs/2609.09353v1).

**Location:** Theorem 1.3, p. 8; Section 9, pp. 56–58; Appendix D and the p-system interfaces.

**Reported answer:** Affirmative existence of two entropy-dissipating solutions.

**Full-target correspondence:** Choose the two-component p-system on (0,infinity) times R with p'<0. Its mechanical entropy has Hessian diag(-p',1)>0 and an exact entropy flux. The theorem supplies distinct bounded solutions with the same Riemann data. Its fixed finite positive-state neighborhoods give a common compact range inside the state domain; the fan construction gives the global entropy inequality and strong local L1 initial trace.

**Scope and evidence limits:** The nonunique solutions are not assumed to have strong spatial traces. That stronger hypothesis belongs to a different uniqueness statement. Supporting source proofs and computational work are imported.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-392"></a>

## 392 — Regularity of transport interfaces for nonconvex polyhedral targets

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/392-polyhedral-transport-singular-interface.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [S. Chen, Q.-R. Li, Y. Li, J. Liu and X. Wu, Optimal transport to non-convex polyhedral domains, arXiv:2610.18756v1](https://arxiv.org/abs/2610.18756v1).

**Location:** Theorem 1.1 and Section 5.

**Reported answer:** Affirmative interface regularity.

**Full-target correspondence:** The theorem covers dimensions n>=2 and gives the requested locally smooth hypersurface outside a relatively closed exceptional set of Hausdorff dimension at most n-2. For the catalogue's finite-facet convention, the arrangement of facet hyperplanes fills possible null slits without changing the target indicator measure, its closure, the supplied Brenier potential, or its nondifferentiability locus.

**Scope and evidence limits:** Literal equality of the original and filled domains is not asserted. Local embeddedness follows from the source's graph constructions; no global embedding claim is added.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-393"></a>

## 393 — Singular-set dimension of polyhedral partial-transport free boundaries

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/393-polyhedral-partial-transport-free-boundary.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [S. Chen, Q.-R. Li, Y. Li, J. Liu and X. Wu, Optimal transport to non-convex polyhedral domains, arXiv:2610.18756v1](https://arxiv.org/abs/2610.18756v1).

**Location:** Theorem 1.2 and Section 6.

**Reported answer:** Affirmative partial-transport free-boundary regularity.

**Full-target correspondence:** The theorem treats hyperplane-separated domains, every admissible transported mass and dimensions n>=2, yielding the stated codimension-two exceptional set. Finite hyperplane-arrangement filling preserves target measure and closure. Keeping the same normalized obstacle pair then preserves the canonical active source region and its free boundary; multiplying the quadratic cost by a positive constant does not change minimizers.

**Scope and evidence limits:** Equality of marginals alone would not preserve an arbitrary open representative's boundary. The comparison uses the canonical active region in the cited partial-transport formulation.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-394"></a>

## 394 — Villani’s convex-injectivity-domain conjecture

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/394-villani-mtw-convex-injectivity-domains.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [OpenAI, Global Support and Convex Injectivity Domains under Weak MTW, 25 September 2026](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/paper.pdf).

**Location:** Theorem 1.1 and equations (1.2)–(1.3); Section 4, Theorems 4.8–4.11.

**Reported answer:** Affirmative convex injectivity domains.

**Full-target correspondence:** The theorem uses the same minimizing-beyond-one injectivity domain and orthogonal weak MTW condition, including the catalogue's -3/2 normalization, and permits focal cut endpoints. It applies in dimensions at least 2. For a closed connected one-dimensional manifold the domain is the interval (-ell/2,ell/2); dimension zero is the singleton case.

**Scope and evidence limits:** The source's public proof and its required interfaces are imported. This report does not provide a new independent audit of the full argument.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-412"></a>

## 412 — Sharp vanishing-viscosity control time for downstream transport

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/412-positive-transport-sharp-uniform-control-time.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Kai Koike and Vincent Laheurte, Uniform null-controllability times for the Coron–Guerrero problems are 2 and 2+2sqrt(2), arXiv:2609.35355v1](https://arxiv.org/abs/2609.35355v1).

**Location:** Theorem 1.3; cost definition, p. 2; transposition/scaling in Section 2.1; Theorem 4.1 and proof, pp. 16–18.

**Reported answer:** Negative: transport time alone does not suffice.

**Full-target correspondence:** The exact worst-case minimal inflow L2 control cost diverges when T*M/L<2. Choosing T=3*L/(2*M) gives a time strictly larger than the catalogue transport time L/M but divergent cost as viscosity tends to zero. The source already treats the same transposition solutions, boundary placement, initial-state norm and parameter scaling.

**Scope and evidence limits:** The endpoint T=2*L/M is unnecessary for this refutation. A formal adjoint estimate in a different control norm would not suffice.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-425"></a>

## 425 — Excess Floquet multiplicity for complex periodic Schrödinger equations

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/425-complex-hill-excess-multiplicity.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Erjuan Fu, Deformation of the spectrum for Darboux–Treibich–Verdier potential along Re tau=1/2, Journal of Spectral Theory 13 (2023), 347–381, DOI 10.4171/JST/453](https://ems.press/content/serial-article-files/33923).

**Location:** Theorem 2.1, equation (2.2), p.356; Lemma 2.4 p.358; Section 3.1 pp.364–366, with definitions p.355 and elliptic sign facts pp.362–363

**Reported answer:** Affirmative existential example via published primary source and elementary translation.

**Full-target correspondence:** The cited elliptic-potential construction supplies a smooth nonconstant complex periodic potential with scalar monodromy at a spectral point. The source’s multiplicity identity, together with the cited equality of periodic Dirichlet indices, yields positive excess d−p−r=1. The inherited map explicitly handles the operator sign, trace normalization, real period and pole-avoiding shift.

**Scope and evidence limits:** The operator sign, full-trace normalization, real period and pole-avoiding shift are part of the comparison. Selected proof interfaces were reviewed; the complete two-paper argument was not independently recertified.

**Evidence status:** Published journal article. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

**Supporting source:** [Fritz Gesztesy and Rudi Weikard, Picard potentials and Hill’s equation on a torus, Acta Mathematica 176 (1996), 73–107, Theorem 3.2 and equation (3.44)](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6528-11511_2006_Article_BF02547336.pdf).

<a id="aim-433"></a>

## 433 — A nonlinear Weyl lemma at the minimal p-harmonic integrability threshold

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/433-very-weak-p-harmonic-energy-regularity.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Maria Colombo and Riccardo Tione, Non-classical solutions of the p-Laplace equation, JEMS 27 (2025), 4845–4890, DOI 10.4171/JEMS/1462](https://ems.press/journals/jems/articles/14297760).

**Location:** Theorem 1.2, p. 4847; construction in Theorem 9.4, pp. 4886–4888.

**Reported answer:** Negative: very weak p-harmonic solutions need not have p-energy.

**Full-target correspondence:** For each p>2, extend the published planar example u to U(x,z)=u(x) on a product with an open cube in R^(d-2), for every d>=3. Local finite-measure inclusions give the required W1,p-1 regularity and integrable nonlinear flux. Integrating a compactly supported test over the extra variables reduces the weak equation to the planar one by Fubini. Tonelli preserves the infinite local p-energy.

**Scope and evidence limits:** The extension is a product-domain counterexample to the universal higher-dimensional assertion. Changing the representative cannot repair the failure of local Sobolev p-energy.

**Evidence status:** Published journal article; its higher-dimensional product application is stated explicitly here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-446"></a>

## 446 — The sharp Beurling–Ahlfors bound for planar elliptic systems

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/446-beurling-ahlfors-sharp-norm.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Andrea Agazzi and coauthors, Sharp Higher Integrability Theory, Part I: The Lp-norm of the Beurling–Ahlfors transform, arXiv:2609.28311v2](https://arxiv.org/abs/2609.28311v2).

**Location:** Corollary 2 and equation (4), p. 2; transform characterization in equation (3).

**Reported answer:** Claimed affirmative sharp Beurling–Ahlfors norm.

**Full-target correspondence:** The source states norm equality p-star-1 for every real 1<p<infinity on unrestricted complex Lp inputs. Its classical Beurling transform normalization agrees with the catalogue disk-principal-value kernel -1/(pi*z^2). Restricting the bounded operator to smooth compactly supported complex inputs gives the requested inequality.

**Scope and evidence limits:** The source result concerns the full complex-valued operator, rather than a real, radial or other restricted input class. This recent proof is imported without a new independent full audit.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-462"></a>

## 462 — A finite-integrability ABP estimate for general nonlocal Pucci operators

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/462-nonlocal-pucci-finite-integrability-abp.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Yongsheng Jiang and Lei Xu, A counterexample to integral Aleksandrov–Bakelman–Pucci estimates for a nonlocal operator, arXiv:2610.16162v1](https://arxiv.org/abs/2610.16162v1).

**Location:** Theorem 1.1; fixed-coefficient limiting and localization argument, pp. 13–14.

**Reported answer:** Negative: no general finite-integrability ABP estimate.

**Full-target correspondence:** For strict ellipticity pairs lambda<Lambda, the source supplies a fixed even coefficient and smooth compactly supported functions u_j,g_j with 0<=g_j<=1, shrinking support of g_j, L_a u_j>=-g_j and positive heights bounded below. Pointwise extremality gives Mplus u_j>=L_a u_j/2. Taking f_j=-g_j/2 makes every finite Lp norm tend to zero while the heights stay positive, refuting every proposed finite-p power bound.

**Scope and evidence limits:** The upper-touch viscosity convention and zero exterior values match the catalogue. This refutes the general question; it does not assert failure at lambda=Lambda.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-521"></a>

## 521 — Six-point persistence on the Euclidean two-sphere

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/521-six-point-sphere-persistence.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Mario Gómez and Facundo Mémoli, Curvature Sets Over Persistence Diagrams, arXiv:2103.04470v5](https://arxiv.org/abs/2103.04470v5).

**Location:** Definition 5.13 and Propositions 5.14 and 5.17, pp. 52–54.

**Reported answer:** Negative for the literal proposed persistence region.

**Full-target correspondence:** When b<d, the farthest-neighbor edges of the six-point sample form three mutual pairs. Choosing two pairs gives a four-point set whose two matching diagonals have length at least d and all other edges at most b. The source four-point Ptolemy bound gives d<=sqrt(2)*b. The claimed right-hand region nevertheless contains (b,d)=(1,2), which violates this necessary inequality.

**Scope and evidence limits:** This refutes the displayed region equality, including its unrestricted second branch. It does not supply or endorse a corrected region with an additional lower bound on b.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-578"></a>

## 578 — A real nearest matrix with spectrum in the closed left half-plane

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/578-nearest-hurwitz-real-minimizer.md). Current catalogue badge: 🔵 OPEN.

**Primary source:** [Vanni Noferini and Matvei Zhukov, Matrix nearness problems: Do real inputs admit real solutions?, arXiv:2609.14828v1](https://arxiv.org/abs/2609.14828v1).

**Location:** Theorem 4.1 and its proof; Sections 1 and 4 define closed-half-plane stability.

**Reported answer:** Negative: the complex minimum can be strictly smaller.

**Full-target correspondence:** For the Frobenius norm, the source constructs real matrices with d_R=m^2 and 0<d_C<=1+sqrt(8*m^2+9)<m^2 for m>=4; a 3-by-3 instance suffices. The admissible matrices use the closed left half-plane and permit the zero or imaginary-axis eigenvalues appearing in the construction.

**Scope and evidence limits:** No semisimplicity requirement on imaginary-axis Jordan blocks is added. An exact formula for the complex minimizer is unnecessary once the strict distance inequality is established.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

<a id="aim-619"></a>

## 619 — Spanning triangulated spheres with holes in surface triangulations

**Target:** [Exact statement at the reviewed revision](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/619-spanning-holed-sphere-triangulation.md). Current catalogue badge: 🟡 PARTIAL.

**Primary source:** [Stefan Hougardy, Frank H. Lutz and Mariano Zelke, Polyhedra of genus 2 with 10 vertices and minimal coordinates](https://arxiv.org/abs/math/0507592v1).

**Location:** The ten-vertex genus-two realization and author dataset, first 24-triangle record.

**Reported answer:** Negative: a ten-vertex genus-two obstruction.

**Full-target correspondence:** The explicit author triangulation has 10 vertices, 36 edges and 24 faces, and is a closed connected orientable genus-two surface, hence Euler genus 4. Any triangulation of a sphere with four holes with disjoint closures has four vertex-disjoint boundary cycles. In a simple graph each cycle needs at least three vertices, so at least 12 are required. A spanning subgraph of this ten-vertex graph cannot qualify.

**Scope and evidence limits:** The vertex-count obstruction applies to any proposed embedding of the spanning subgraph; the input genus and connected-manifold properties come from the explicit author example.

**Evidence status:** Public preprint/proof; journal acceptance and independent full-proof review are not established here. OpenAI Codex compared the source theorem and named proof interfaces with the target; a new independent whole-proof audit is not claimed.

**Supporting source:** [Frank H. Lutz, primary genus-two, ten-vertex triangulation data](https://www3.math.tu-berlin.de/IfM/Nachrufe/Frank_Lutz/stellar/manifolds_lex/manifolds_lex_d2_n10_o1_g2.txt).

## Maintainer review

For each entry, the remaining editorial decision is whether the linked proof and the stated target reduction satisfy the catalogue’s evidence rule for Solved or should be recorded as a complete solution claim pending further review. Particular care is needed where the reported application is broader than the source theorem’s literal wording, where a computer-assisted proof has not been independently replayed, or where a public formal proof has not been locally reproduced with its exact dependencies.
