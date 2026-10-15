# PR 170: independent source-to-target applicability review (12 entries)

Reviewed 2026-10-15 by OpenAI Codex (AI). Submission: [PR 170](https://github.com/MColbrook/AIM/pull/170), pinned head `ea9829b04eabe0017d8a968261335a44a7cc30ed`. Targets were compared with the unchanged statements in the submitted package and the report's frozen repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. This covers AIM030, 044, 092, 108, 111, 123, 125, 126, 348, 392, 393 and 394; other report entries are outside this record.

For every entry, I read the complete submitted report entry, exact catalogue target, and actual primary theorem statements and named interfaces described below. This is a source-to-target applicability review, comparable to the repository's literature crosschecks. It is **not a new independent audit of every argument in the external papers**, journal peer review, or Lean verification. Each source in this assigned subset states a complete result, and the checked statements/interfaces match the full corresponding target. However, no peer-reviewed publication or complete independent proof audit has been established here for any of these twelve sources. Under the repository's conservative distinction between a complete public claim and an accepted resolution, the recommendation is therefore **Solution claimed for all twelve**, awaiting stronger correctness evidence. A full statement match by itself does not justify Solved. This supersedes this review's initial external-source-route status recommendation; the mathematical applicability findings below are unchanged.

All twelve target correspondences are complete. I found no substantive scope mismatch requiring a Partial classification in this assigned subset. This conclusion concerns applicability; it does not independently certify the correctness of these substantial external proofs. The report's public-source links should remain external, with no downloaded papers added to AIM. The versioned PDF bytes used for the comparison are identified below. This record checks extracted primary passages and the mathematical interfaces; it does not claim all-page visual QA or independent compilation of the external papers.

The submitted filename and review dates say 2026-10-16, while this review occurred on 2026-10-15. Update actual catalogue review dates to the date of the review rather than asserting a future check. The one source-locator correction in this subset is listed under AIM394. No other substantive correction was identified in these twelve entries.

<a id="aim-030"></a>

## AIM030

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative existence in every dimension.

**Passages checked:** Radchenko–Wheeler, Hexagon 2610.00186v1, Proposition 7 and following deduction, Section 9.2, p.17; Radchenko–Wheeler, arXiv:2609.21892v2, Theorem 7, Section 4.4 pp.20–21; Remark 7 p.22; Appleby–Flammia–Kopp, arXiv:2501.03970v2, Theorem 1.46; Section 5.6 pp.87–88.

The catalogue asks only for existence of $`d^2`$ unit vectors in $`\mathbb C^d`$ with squared pairwise overlap $`1/(d+1)`$ for each integer $`d\ge2`$. It does not require a prescribed covariance group. The primary source explicitly deduces precisely $`M^2`$ complex equiangular lines for every $`M\ge4`$ and refers to the known dimensions two and three.

I checked the two interfaces, rather than treating the primary source's last sentence as sufficient on its own. Theorem 7 of the finite quantum dilogarithm paper proves the quadratic operator identity yielding a ghost rank-one SIC construction; Remark 7 explicitly identifies simultaneous unit-modulus conjugation as the missing ingredient. Proposition 7 of the newer paper supplies this simultaneously for every nonzero lattice argument and every algebraic automorphism inducing the other quadratic-field embedding. Its proof uses one second-real-sign Artin action and hence is simultaneous, rather than an argument choosing different embeddings for different overlaps.

Section 5.6 of Appleby–Flammia–Kopp explains the conversion: conjugation preserves idempotence; the paired-overlap identity and the simultaneous absolute values give Hermitian overlaps of the required modulus. The trace-one projector then generates the equiangular lines. This checks the roles of both the convolution identity and the unitary embedding. I have not independently audited the number-theoretic proof establishing Proposition 7 or the full preceding constructions. The source's substantial LLM involvement is explicitly disclosed; this record does not substitute a human review claim for that disclosure.

Source: [versioned PDF](https://hexagonmath.org/pdf/2610.00186v1), 22 pages; SHA-256 `e31ed15bfbe9c2efd47b2f44b585c35be68ed28a15c361c6bf5f1db9f60982c9`.

Source: [versioned PDF](https://arxiv.org/pdf/2609.21892v2), 36 pages; SHA-256 `aae135b3cb875ab24d64e0042cb10ced98b64171dd8a760a4c2a96fe88ba7e71`.

Source: [versioned PDF](https://arxiv.org/pdf/2501.03970v2), 177 pages; SHA-256 `d469d975f14501d7593fcd9160c1175026a9159eff2d0b2dbb57d58831a42443`.

<a id="aim-044"></a>

## AIM044

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative bit-complexity bound.

**Passages checked:** Kelner, arXiv:2609.38101v1, Theorem 1.1 p.3; Theorem 3.3 p.10; Lemma 3.4 and Section 3.3 pp.11–12; Section 4 pp.12–14.

The catalogue uses exact rational sparse input, a polynomial condition-number bound and relative forward error. The headline floating-input residual theorem alone would leave an interface gap. The report correctly also invokes the zero-preserving integer core in Theorem 3.3 and the normalization/rounding certificate of Lemma 3.4.

For fixed $`c`$, numerator and denominator lengths are $`O_c(\log n)`$, so nonzero rational entries have polynomially bounded magnitudes and inverses. Exact integer division computes the required dyadic rounded normalized entries in $`\widetilde O_c(m)`$ bit operations; zeros stay zero. Normalize the matrix and right-hand side separately by dyadic scalars and recover their ratio afterward. Lemma 3.4 controls the rounded integer system, with its displayed certificate holding once the precision scale is polynomial in $`n\kappa/\varepsilon`$. Thus its integer parameters have $`O_c(\log n)`$ bits at the catalogue tolerance.

Choose relative residual tolerance at most $`n^{-2c}`$ (with a harmless fixed safety factor). Since $`\|A^{-1}(A\widehat x-b)\|/\|x\|\le\kappa(A)\|A\widehat x-b\|/\|b\|`$, this gives forward error at most $`n^{-c}`$. The integer solve and rational output cost $`\widetilde O_c(mn+n^2)=\widetilde O_c(mn)`$, since a nonsingular matrix has $`m\ge n`$. The source's deterministic guarantee is stronger than success probability $`0.99`$. The relevant rounding lemma and integer-solve statements were read, including the output representation; no full audit of the preprint's fast algebraic core is claimed.

Source: [versioned PDF](https://arxiv.org/pdf/2609.38101v1), 16 pages; SHA-256 `5903800d274b9ce68046cf2972f4cf26142f99c2476ade4671ef8a74ea6b4795`.

<a id="aim-092"></a>

## AIM092

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative dimension-free Poincare inequality.

**Passages checked:** Bizeul–Klartag–Lehec, arXiv:2610.05474v1, definition (5) and Theorem 1.1 p.2; Balasubramanian–Kasiviswanathan, arXiv:2610.07728v1, Theorem 1.1 p.3; conclusion of Section 8 pp.23–24; Appendix F.

The first source defines log-concave densities using a convex potential with values in $`\mathbb R\cup\{+\infty\}`$, so uniform measures on convex bodies and nonsmooth potentials are included. Its Theorem 1.1 is dimension independent for every isotropic log-concave probability measure. Definition (5) uses variance and the Euclidean gradient for all locally Lipschitz tests in $`L^2`$, which contains the catalogue's smooth compactly supported tests. There is no residual subgaussian hypothesis in this theorem.

I also checked the separately cited source. Its Theorem 1.1 assumes covariance bounded by the identity, which includes isotropic measures. The final general-measure passage approximates arbitrary full-dimensional log-concave laws by regular laws, uses bounded continuous $`f,f^2,|\nabla f|^2`$ for compactly supported smooth tests to pass the Poincare inequality through weak convergence, and then extends to locally Lipschitz finite-energy tests. The subsequent affine-support argument covers degenerate laws, although the catalogue's density hypothesis already makes that unnecessary.

The earlier catalogue Partial result was subgaussian only. That limitation belongs to the earlier source and must remain correctly attributed if retained in the review history. The new theorems themselves state the full target. This is a comparison with two public preprint proofs, not an independently reconstructed proof of KLS or an assertion of journal acceptance.

Source: [versioned PDF](https://arxiv.org/pdf/2610.05474v1), 32 pages; SHA-256 `86824722318f2213daf5ae624391b41f76bb4d41118b1657db9ab00d2d1bb0db`.

Source: [versioned PDF](https://arxiv.org/pdf/2610.07728v1), 53 pages; SHA-256 `6f19dd815c69127c4a3ed75abb69aa54a1e6d7c42bcb5c06b2e4769661667ada`.

<a id="aim-108"></a>

## AIM108

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative uniqueness of the critical catenoid.

**Passages checked:** Chodosh–Gianocca, arXiv:2609.13054v1, Theorem 1.1 and Corollary 1.2; concluding proof p.10; Parise–Zhu, arXiv:2609.17512v1, Theorems 1.1, 1.3 and 1.4.

Every annulus in the catalogue has genus zero and the required proper embedded free-boundary hypotheses. Chodosh–Gianocca prove the first-Steklov-eigenvalue assertion for all properly embedded genus-zero surfaces and state the critical-catenoid classification as Corollary 1.2. The concluding application uses the stated Fraser–Schoen characterization, rather than assuming rotational symmetry or an index bound. The second cited paper independently states the annulus classification and separates its coordinate-eigenspace theorem from that characterization.

The explicit catenoid normalizations agree: $`T\tanh T=1`$ implies $`T^2\cosh^2T=\cosh^2T+T^2`$, hence the catalogue's scale $`(\cosh^2T+T^2)^{-1/2}`$ equals $`1/(T\cosh T)`$. An orthogonal classification in one source also gives classification by rotations: if the chosen orthogonal map reverses orientation, compose it with an orientation-reversing symmetry of the model catenoid. This leaves the model unchanged and gives determinant one.

No missing stability, boundary-count or symmetry assumption was found in this theorem-to-target application. Both sources are public preprints. The comparison does not claim a new independent audit of their complete genus-zero or annulus arguments.

Source: [versioned PDF](https://arxiv.org/pdf/2609.13054v1), 13 pages; SHA-256 `a31bc9c6e5652279c2f1c9c234800c6393eb223fe86dd02a80802660f6391549`.

Source: [versioned PDF](https://arxiv.org/pdf/2609.17512v1), 28 pages; SHA-256 `ec8af2384bd3fff71a00787ddb6d55c3a3bd7fbe797c59f3feaf45d563e1eb7f`.

<a id="aim-111"></a>

## AIM111

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative unbounded first Steklov multiplicity.

**Passages checked:** Nifa, Zenodo record 22949635, Theorem A and Corollary 1.1 pp.2–3; ordinary Steklov formulation in the introduction.

Theorem A prescribes the first $`N`$ positive eigenvalues of the ordinary unweighted smooth Steklov problem on a compact connected orientable surface with any chosen boundary-component count $`b`$, provided its genus is sufficiently large. It also places the next eigenvalue beyond a specified gap. This is exact prescription, rather than an approximate convergence result or a boundary-density-weighted operator.

Take $`b=1`$, $`N=j`$, $`a_1=\cdots=a_j=1`$ and $`H=2`$. The threshold in this case is $`\Gamma(j,1)=\lceil j(j-1)/4\rceil`$. The resulting metric has $`\sigma_1=\cdots=\sigma_j=1`$ and $`\sigma_{j+1}>2`$, so the first positive eigenvalue has exactly multiplicity $`j`$. Varying genus and metric while keeping one boundary component gives the required unbounded sequence. Corollary 1.1 explicitly records the multiplicity consequence.

Uniform metric rescaling can normalize total boundary length to one if desired, while preserving multiplicity; it also rescales eigenvalues, so simultaneous preservation of the value one is not asserted. The primary PDF is directly hosted by the cited Zenodo record. Its theorem scope and specialization match the target. Journal acceptance and a separate full audit of the spectral-prescription construction have not been established here.

Source: [versioned PDF](https://zenodo.org/api/records/22949635/files/Prescribed_Steklov_Spectra_nifa.pdf/content), 33 pages; SHA-256 `b4214e8895f8c9e9cd9c300dd89d5d1d1b98a77ada4b7095b9ffe885ec325fe7`.

<a id="aim-123"></a>

## AIM123

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Negative: smooth bracket-generating counterexample.

**Passages checked:** Lerario–Rizzi–Tiberio, arXiv:2609.05991v1, Theorem 1.1(i) p.2; Lemma 2.1 pp.5–6; Lemma 3.1 pp.7–8; Proposition 3.2 pp.8–9; Proposition 4.1 pp.9–10; Lemma 4.3 and Proposition 4.4 pp.11–12.

The target is the unrestricted smooth, constant-rank, bracket-generating endpoint-map nullity conjecture. It does not require an analytic or equiregular bracket flag, nor length minimization. The source constructs smooth global rank-two fields $`X=\partial_x-V(x,y)\cdot\partial_z`$ and $`Y=\partial_y`$ on $`\mathbb R^4`$. The two base-coordinate components make the rank constantly two. Proposition 3.2 computes brackets through length five and their determinant, giving bracket generation at every point, while explicitly showing the flag is not equiregular.

I checked the endpoint-map interface. With $`L^2`$ controls, $`x,y`$ are bounded absolutely continuous paths on the finite interval, so the triangular $`z`$ equation integrates a bounded smooth coefficient against an $`L^2`$ control. Thus trajectories exist globally for the full control domain. Lemma 2.1 computes an actual nonzero annihilator of the endpoint differential when $`\lambda\cdot\partial_yV=0`$ along the path and proves invariance under affine reparametrization to $`[0,1]`$.

The binary smooth-loop construction realizes arbitrary two-dimensional vertical displacement with zero bracket coefficient; Lemma 4.3 then supplies a broken base-plane path with one nonzero multiplier. The concatenation retains that multiplier and reaches any prescribed point, as formalized in Proposition 4.4. Hence singular endpoints fill $`\mathbb R^4`$ from one origin, contradicting nullity for every positive smooth volume density. This does not assert every control is singular or settle analytic, equiregular or minimizing variants. Source-internal prose sometimes calls its lemmas/propositions 'Theorem'; the submitted report correctly gives the actual displayed labels. The author's AI disclosure is retained, without adding a claim of human review by this repository.

Source: [versioned PDF](https://arxiv.org/pdf/2609.05991v1), 15 pages; SHA-256 `4877b5bc4ae5c9ffba4c4924cbb3100b96e3b2f6fe7721edf2a52a2bb9f94588`.

<a id="aim-125"></a>

## AIM125

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Negative: branching analytic equiregular minimizers.

**Passages checked:** Rossi–Schiavoni Piazza–Socionovo, arXiv:2603.23068v3, Theorems 1.1–1.3 pp.3–4; Section 10 pp.35–36, especially projection (10.1) and equality of controls on the initial interval.

The earlier three-dimensional Martinet example alone would not meet the catalogue's equiregularity requirement. Version v3 explicitly adds a Carnot-group lift in Theorem 1.3 and Section 10. A Carnot group's left-invariant analytic horizontal metric has a constant-rank bracket flag, giving both analyticity and equiregularity.

The base minimizing curves agree for $`t\le0`$ and have opposite nonzero first coordinate for $`t>0`$. Their horizontal speeds are both one before zero and both $`\sqrt{1+q^2t^{2q-2}}`$ afterward. The same arclength change therefore puts them on one common interval as unit-speed curves, with a positive interval of agreement. It does not separately reparametrize the branches in incompatible ways.

Section 10 constructs an explicit projection with $`d\pi(Y_i)=Z_i`$ and a submetry, so a lift from the same initial point has the same horizontal control and length as the base minimizer. Its projected endpoint distance bounds any competitor length from below, proving global minimizing status on the selected interval. The two initial controls are both $`(0,1)`$; ODE uniqueness gives equality of lifts until zero. Their different projections later force separation. Thus the source's equiregular lift, not merely the base construction, matches every hypothesis of the counterexample target. The full delicate proof of base minimality is imported from the public preprint and has not been re-audited here.

Source: [versioned PDF](https://arxiv.org/pdf/2603.23068v3), 37 pages; SHA-256 `1dfd32699fb2f7d6ef9f37ddb947cab6f54507ce8ee37976bc9a994a02c18697`.

<a id="aim-126"></a>

## AIM126

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative sharp Heisenberg isoperimetry.

**Passages checked:** Chen–Kao–Lien, arXiv:2610.07632v1, frame p.1; bubble (1.1), Theorem 1.1 and constants (1.3) p.2; Proposition 3.1 pp.13–17; Proposition 4.7 and final proof pp.27–28.

The source's Theorem 1.1 applies to every measurable finite-horizontal-perimeter set of finite positive volume; it does not impose smoothness on the competitor. Its equality case is a left translate and dilation of the Pansu ball. The smooth objects used later in the proof are approximations and do not narrow the theorem statement to a smooth subclass.

The source uses $`\partial_x+y\partial_t`$ and $`\partial_y-x\partial_t`$. The catalogue uses the half-coefficient convention with the other vertical sign. The linear group isomorphism $`\Phi(x,y,t)=(x,y,-2t)`$ sends the catalogue frame to the source orthonormal frame. Its absolute Jacobian is two. Changing variables in the divergence definition of horizontal perimeter gives $`P_{\rm src}(\Phi E)=2P_{\rm AIM}(E)`$ and $`|\Phi E|=2|E|`$, also for finite-perimeter sets. Thus the source constant $`512\pi^2/27`$ becomes $`256\pi^2/27`$ in the catalogue convention.

The source bubble's height is $`\frac12(r\sqrt{R^2-r^2}+R^2\arccos(r/R))`$. Its inverse image under $`\Phi`$ has the catalogue's factor $`1/4`$. Translations, dilations and null-set equality are preserved. The theorem and its finite-perimeter approximation/rigidity interfaces therefore cover the full written target. This comparison is not a new proof audit of those approximation and rigidity arguments or their imported regularity results.

Source: [versioned PDF](https://arxiv.org/pdf/2610.07632v1), 29 pages; SHA-256 `89bb39f2ce771609e55627e27dc1a49c7e95dfcb691fdf3be84dd11f6bb0276c`.

<a id="aim-348"></a>

## AIM348

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Negative: finite-time Brownian branching explosion.

**Passages checked:** Lin–Lu, arXiv:2610.18802v1, Theorem 1.1 p.3; Section 7 pp.49–55: common-clock construction, Lemma 7.2, Proposition 7.3, geometry and final proof.

For every fixed $`N\ge3`$, the source constructs a bounded connected open domain in $`\mathbb R^3`$ for which the classical driftless Brownian Fleming–Viot system with uniform survivor copying explodes with positive probability before each positive time, from every interior configuration. Taking $`N=3`$ suffices to refute the catalogue's universal assertion. The perforated domain is allowed: the target places no boundary-smoothness or cone assumption on arbitrary bounded connected open sets.

The stochastic-model interface matters here. I read the entire Section 7 common-clock construction. Inversion of the operational process uses one clock, $`t(u)=\int_0^u|Y_N|^{-4}\,ds`$, for all labels. The stated operational drift cancels the Ito correction of inversion in dimension three, and the joint quadratic covariations become those of independent standard Brownian coordinates in physical time. The independent donor sequence remains in the enlarged initial filtration; the martingale construction checks the required Brownian/donor joint law, rather than merely the marginal law of each particle. The copying rule commutes with inversion and clock change.

The escape event makes the clock finite. Point polarity in dimension three excludes explaining the simultaneous terminal approach to the puncture by only finitely many branchings, so infinitely many actual resampling times accumulate. Proposition 7.3 transfers the seed event to arbitrary starting configurations within any positive horizon, and the final geometry verifies openness, boundedness and connectedness. These checked interfaces match the actual Brownian model; no conclusion is drawn merely from an auxiliary drifted or separately time-changed process. The preceding long escape construction is an imported public argument, not a new complete audit. Selected formal supplementary code does not establish Lean verification of this target.

Source: [versioned PDF](https://arxiv.org/pdf/2610.18802v1), 86 pages; SHA-256 `05e9604467dcf946512f0314b9bba274601d9209309050c1406d3d7b342340c1`.

<a id="aim-392"></a>

## AIM392

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative codimension-two transport-interface regularity.

**Passages checked:** Chen–Li–Li–Liu–Wu, arXiv:2610.18756v1, polyhedral convention and Theorem 1.1 p.2; Proposition 5.3 pp.23–24; Lemma 5.4 and proof of Theorem 1.1 pp.24–25.

Theorem 1.1 applies to any bounded open source, with no convexity or smooth-boundary condition, and bounded polyhedral target of equal volume. Its $`\Sigma`$ is the closure of the nondifferentiability set inside the source, matching the catalogue. Its conclusion is a relatively closed exceptional subset of Hausdorff dimension at most $`n-2`$, with a locally smooth hypersurface outside it. The theorem holds for dimensions at least two and thus includes the catalogue's $`n\ge3`$.

The source defines polyhedral targets as interiors of finite unions of full-dimensional closed polytopes. The catalogue's finite-facet boundary convention also permits null slits. Cutting a bounding box by the finitely many facet hyperplanes partitions it into finitely many full-dimensional cells; domain membership is constant off those hyperplanes. Taking the interior of the union of the closed selected cells fills only a null set, preserves the closure, and gives the source convention. The same supplied convex Brenier potential still transports the same indicator measures; it need not be replaced by an arbitrary almost-everywhere representative. Consequently its nondifferentiability locus and its closure remain unchanged.

For the geometric wording, Proposition 5.3 gives locally $`u=\max(u_1,u_2)`$ and the interface $`u_1=u_2`$, with distinct gradients, followed by the smooth bootstrap. This is a local embedded graph, not merely an immersed image. The theorem's exceptional set is the complement of these relatively open regular charts and is relatively closed as required. The report's extra convention discussion is sufficient and does not silently assume literal equality of a slit domain and its fill. The external higher-regularity proof remains imported.

Source: [versioned PDF](https://arxiv.org/pdf/2610.18756v1), 31 pages; SHA-256 `d52c8ae09efd57f1668005971d84a083862f28958aa49951edf885a62bfb557f`.

<a id="aim-393"></a>

## AIM393

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative codimension-two partial-transport regularity.

**Passages checked:** Chen–Li–Li–Liu–Wu, arXiv:2610.18756v1, Theorem 1.2 p.3; Section 6 p.25, obstacle relation (6.2); Proposition 6.4 and final proof pp.27–28.

Theorem 1.2 has precisely hyperplane-separated bounded open supports, polyhedral target and every transported mass strictly between zero and the smaller support volume. It imposes no additional boundary regularity or convexity on the source. The exceptional set is relatively closed in the free boundary and has Hausdorff dimension at most $`n-2`$. The result covers all catalogue dimensions.

As for AIM392, finite facet hyperplanes permit replacement of a possible slit target by its polyhedral fill, with unchanged measure and closure. For partial transport, equality of indicator measures alone would not justify equality of the boundary of an arbitrary open representative. The relevant stronger interface is the canonical normalized obstacle pair: source Section 6 writes $`U=\{x\in\Omega:u(x)>|x|^2/2-c_m\}`$. With the same marginal measures and target closure, the same normalized pair remains admissible and supplies the same canonical active source and free boundary. Multiplying the quadratic cost by a positive constant changes neither the fixed-mass minimizer nor this geometric active set, after corresponding potential normalization.

Proposition 6.4 writes the local potential as the maximum of a smooth active branch and the quadratic obstacle. At a regular boundary point their gradients differ because of separation, so the implicit-function theorem gives an embedded local graph; the subsequent bootstrap gives smoothness. The proof takes the exceptional set as the relatively closed complement of these charts. This verifies the report's canonical-region caveat and its local embeddedness claim, without adding a claim about arbitrary open representatives or reconstructing the full external regularity proof.

Source: [versioned PDF](https://arxiv.org/pdf/2610.18756v1), 31 pages; SHA-256 `d52c8ae09efd57f1668005971d84a083862f28958aa49951edf885a62bfb557f`.

<a id="aim-394"></a>

## AIM394

**Source match:** Full. **Recommendation:** Solution claimed pending stronger correctness evidence. **Outcome:** Affirmative convex injectivity domains under weak MTW.

**Passages checked:** OpenAI, pinned math repository fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb, paper dated 25 September 2026, equations (1.1)–(1.3) and Theorem 1.1 p.2; Theorem 4.8 pp.16–17; Corollary 4.9 p.17; Corollary 4.10 pp.17–18; Proposition 4.11 pp.18–19.

The source uses exactly the minimizing-beyond-time-one definition of $`I(x)`$, the squared-distance cost $`d^2/2`$, the $`-3/2`$ normalization of MTW, and nonnegativity only for orthogonal test vectors. Compactness, connectedness, smoothness and absence of boundary match the catalogue. The theorem explicitly allows conjugate cut endpoints; the old nonfocal theorem alone would not have sufficed.

Theorem 1.1 is the desired ordinary linear convexity conclusion for every base point in dimension at least two. Corollary 4.9 supplies the final interface from the global support theorem: for two minimizing velocities, take the maximum of their two supporting mountains. Their segment lies in the ordinary semiconvex subdifferential, and Theorem 4.8 puts the segment in the closed minimizing domain. The interior of that domain is $`I(x)`$, since outward radial perturbations of a cut vector cease to minimize. Hence it is convex. This is ordinary linear convexity, without an extra assertion of strict convexity or boundary regularity.

The remaining low-dimensional cases need no imported theorem: a compact connected boundaryless one-dimensional Riemannian manifold is a circle of length $`\ell`$, whose injectivity domain is $`(-\ell/2,\ell/2)`$; the zero-dimensional connected case is one point. The source's pinned public PDF is directly linked rather than uploaded. The submitted locator calls results 4.8–4.11 'Theorems', but the displayed labels are Theorem, Corollary, Corollary and Proposition respectively; correct that wording. No full independent audit of the source's continuation argument is claimed.

Source: [versioned PDF](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/paper.pdf), 24 pages; SHA-256 `e16087753fc93a840bd357fe203ffd1d7a511245db91f5e629132e91db440724`.

Required editorial correction: Replace AIM394's locator 'Theorems 4.8–4.11' with 'Theorem 4.8, Corollaries 4.9–4.10 and Proposition 4.11' (or 'results 4.8–4.11').
