# AIM 527 — independent review of PR 86

- Review date: 2026-10-13.
- Submission: [PR 86](https://github.com/MColbrook/AIM/pull/86), Kaiwen Jin.
- Reviewed head: `adbe6891d9441d819df9d6acc614fc747f5821a3`.
- Proof: [PDF](../../solutions/kaiwen-jin-527-negative-jump-flow/paper/main.pdf), [source](../../solutions/kaiwen-jin-527-negative-jump-flow/paper/main.tex).
- Target: `problems/527-negative-jump-adaptive-flow.md` at `c9929805cece044705abaaebe1cebddac1ba11a6`.
- Reviewer: an independent Codex agent, separate from the submission's drafting and prior self-review. This is an AI natural-language mathematical audit, not human peer review or a Lean proof.
- Recommendation: **Solved**, affirmative existence for the complete stated free-transition target.

## Target comparison

The theorem retains every bounded connected Lipschitz domain in dimension $`d\ge2`$, every finite $`r\ge2`$, the original continuous nondecreasing laws and negative jump, the prescribed rough volume force/source and boundary-flux spaces, both mixed-boundary and pure-flux pressure conventions, and the original weak mass equation. Crucially, the target allows an arbitrary vector $`L^s`$ drag on $`\{|u|=1\}`$. Choosing solutions with $`|u|\ge1`$ is an output, so avoiding the low branch is legitimate. The proof does not establish a selected transition law or energy minimization, and neither is requested.

## Independent reconstruction

1. **Affine spaces and pressure recovery (lines 185–219).** Poincaré's inequality on the pressure test space gives a bounded inverse for the gradient onto its closed image. The source functional is bounded by Hölder and the Lipschitz-domain trace bound. Hahn–Banach on that gradient image, followed by $`(L^s)^*=L^r`$, gives a velocity with the required affine mass data. The annihilator of its homogeneous kernel is exactly the closed gradient image. Thus every subsequent compactly supported divergence-free correction preserves all weak flux data, and every scalar gradient drag correction corresponds to a pressure in the original affine space. This remains valid on domains with holes.

2. **Monotone auxiliary law (lines 221–330).** Extend the high coefficient constantly below speed one. The nonnegative nondecreasing remainder after subtracting $`\beta=\phi_2(1)`$ is monotone, giving the quadratic estimate. Splitting the two radii into comparable and noncomparable cases gives the displayed $`r`$-power estimate with a positive constant. Both estimates have the correct signs. The growth bound implies continuity from $`L^r`$ to $`L^s`$; the varying-field version follows from convergence in measure and uniform integrability, not an unassumed Lipschitz coefficient. Coercivity of the convex radial potential and weak lower semicontinuity give the auxiliary minimizer; differentiating along the homogeneous mass kernel recovers its pressure. Strict monotonicity proves uniqueness.

3. **Exact cutoff equations (lines 332–382).** Adding $`b\chi_R`$ loses at most $`(\|b\|_\infty/R)|a-c|^2`$. Averaging the two monotonicity estimates and taking $`\|b\|_\infty/R\le\beta/4`$ leaves both a positive quadratic and a positive $`r`$-power bound. The auxiliary-solution map is a contraction on $`L^2`$ with factor at most $`1/4`$. Its limit is a value of that map and hence belongs to $`L^r`$. Testing the exact-minus-approximate equation by the common-affine velocity difference cancels pressure and gives the stated $`L^r`$ correction estimate. No boundary regularity of the velocity is silently imposed.

4. **Full finite div/curl hull (lines 410–498).** The wave relation $`\Delta a\cdot\Delta z=0`$ permits one normal with velocity difference perpendicular and drag difference parallel. In dimension at least two the zero-drag case also has a normal. Inside the unit ball, the two equal-drag unit states have the required mean. Outside it, the preliminary split has identical velocities. For each resulting drag the unit point and high-ray point satisfy the wave relation at the root of $`F_\sigma`$. At the initial ray point,

   ```math
   F_\sigma(1)=a\cdot(A(a)-z)-|A(a)-z-\sigma Tb|<-1.
   ```

   Strong monotonicity makes this function strictly increasing and unbounded; the root therefore exists uniquely. The displayed weights recover both mean coordinates. Its transverse component bounds the ray direction away from zero on bounded input sets; the strict negative initial margin and continuity keep the root away from one, so the unit-state drag denominators do not blow up. Atom bounds and tree depth are finite uniformly on each bounded input range.

5. **Small moments near the graph (lines 505–574).** The subunit split costs $`(1-|a|^2)^{r/2}`$, bounded by a constant times $`1-|a|`$ because $`r\ge2`$. The near-sphere split uses a high pair with weight $`2\varepsilon`$ and a subunit mean with the complementary weight; its velocities differ radially and drags tangentially, so the split is legal. Bounded high atoms and the unit-state deviations give $`O(\varepsilon)`$ cost in both conjugate powers. Near a high graph point, a same-velocity split leaves a weight equal to its drag defect on bounded atoms and costs $`O(|z-A(a)|)`$. Taking the cheaper split gives the minimum defect. The continuous weight $`k`$ supplies a local majorant. No global polynomial-growth bound for this weighted defect is used.

6. **Measurable masks (lines 581–684).** On a bounded measurable defect set, finite value bins allow graph-atom constructions with uniformly small defect by continuity. A binary phase profile has zero mean and a bounded Lipschitz primitive. The compactly supported skew potential and scalar potential give exact divergence-free/gradient corrections, with the leading oscillation and a remainder of order $`N^{-1}\|\nabla\eta\|_\infty`$. Smooth approximation of each measurable mask is chosen first, frequency second. Periodic averaging on an arbitrary measurable parent follows by density of smooth weights in $`L^1`$ and the bounded primitive identity. At each fixed finite tree, outer phases are fixed before inner frequencies are chosen. Thus conditional leaf fractions and mixed moments converge as claimed; errors and compact-support bounds are controlled for that tree. The ideal phase field is equal to the old field off the measurable set, while exact affine fields approximate it in both norms. Neither arbitrary measurable masks nor infinitely many splits are treated as smooth without approximation.

7. **Exact improvement (lines 696–789).** Defects of an exact cutoff solution have bounded pair values. Interior exhaustion loses arbitrarily little defect mass, making the preceding lemma applicable even to rough initial data. The ideal targets differ from a fixed rough pair by uniformly bounded increments and have a bounded compactly supported residual. Choose one common cutoff radius and residual bound before taking frequency limits. Their affine approximation error in the cutoff equation tends to zero: Nemytskii continuity is justified by uniform integrability; the cutoff is Lipschitz and $`L^r\subset L^s`$ on the bounded domain. Exact monotone correction therefore tends to zero in velocity and drag. The weighted-defect integrals also converge: exact and ideal defects have uniform bounds, convergence in measure is proved by discarding rough tails and using compact-range uniform continuity, and boundedness gives $`L^1`$ convergence. No defect integrability of the intermediate affine approximants is needed.

8. **Strong limit (lines 791–829).** The improvement tolerance $`2^{-r(j+1)}`$ makes velocity increments $`O(2^{-j})`$ and drag increments $`O(2^{-(r-1)j})`$, so both norms converge. The bounded inverse gradient recovers pressure convergence in $`W^{1,s}`$. Hölder passes every fixed weak mass test to the limit. An almost-everywhere subsequence, continuity and Fatou force zero graph defect. The resulting global threshold drag is in $`L^s`$ and satisfies the exact original law.

## Reference audit

All five bibliography entries identify real sources. No missing proof-critical reference was found; the nonstandard construction and convergence steps are proved in the manuscript rather than delegated to a citation.

- Fumagalli–Patacchini, ESAIM M2AN **56** (2022), 565–592, [DOI](https://doi.org/10.1051/m2an/2022016), [primary PDF](https://www.numdam.org/item/10.1051/m2an/2022016.pdf): downloaded and inspected. Lemmas 4.1–4.2 on pp. 573–574 give exactly the linear facts and rough data spaces. Remark 3.6 explicitly permits any $`L^s`$ threshold drag and distinguishes weak solutions from minimizers. Theorems 4.10–4.11 have the stated jump/dimension distinction.
- Fumagalli–Patacchini, [arXiv:2206.07970v1](https://arxiv.org/html/2206.07970v1): title/authors/version confirmed. Theorem 3.3, Remark 3.4 and Corollary 4.5 have the stated monotone/nonmonotone scope; this is cited for context, not as the new higher-dimensional theorem.
- Sorella–Tione, [arXiv:2107.10785v1](https://arxiv.org/html/2107.10785v1): title/authors/version and Proposition 4.5 confirmed. That proposition concerns finite-order laminates and localized differential potentials; the submission supplies its own measurable-mask adaptation.
- Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations*, Springer (2011), [book DOI](https://doi.org/10.1007/978-0-387-70914-7): metadata confirmed. The invoked reflexivity, density, subsequence and Sobolev approximation facts are standard and were independently used in the reconstruction above; these citations are not replacements for a new bottleneck lemma.
- The AIM entry links the actual immutable problem and revision. Its formulation matches the theorem reviewed here.

## Decision and limits

The complete existence target is established by the audited argument. The strongest conclusion is existence with speed at least one almost everywhere, enabled by the expressly free threshold law. No mathematical gap remained after the finite-phase, exact-correction and strong-limit reconstruction. Recommend merging the solution package and classifying AIM 527 as **Solved**, with this report disclosed as an independent AI argument audit. There is no Lean verification. Package byte identity, PDF typesetting and repository integration are separate checks performed by the coordinating review, not evidence substituted for this proof.


## Document and package checks

The coordinator parsed and rendered the supplied twelve-page PDF. This reviewer independently inspected the all-page contact sheet: the document has no blank, clipped or missing page content, and its displayed statements and proof structure agree with the reviewed source. The package README, target comparison and AI-use disclosure were read and agree with the manuscript and exact target scope. No separate executable proof or numerical certificate is a mathematical premise. Hash and repository integration checks belong to the coordinating review.
