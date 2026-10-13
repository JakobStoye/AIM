# AIM 051 — independent review of PR 71

- Date: 2026-10-13.
- Submission: [PR 71](https://github.com/MColbrook/AIM/pull/71), Kaiwen Jin.
- Reviewed head: `8ac038c0eb03ee265826ad268aa458f7513ab27a`.
- Proof: [PDF](../../solutions/051-potential-on-general-manifold/paper/main.pdf), [source](../../solutions/051-potential-on-general-manifold/paper/main.tex).
- Target: the immutable AIM 051 statement at `c9929805cece044705abaaebe1cebddac1ba11a6`, compared directly with the theorem.
- Reviewer: an independent Codex agent, separate from the submission's drafting/self-review. This is an AI natural-language mathematical argument audit, not human peer review or Lean verification.
- Verdict: **Solved**: uniqueness of the complete smooth real potential on any known manifold under the stated nonresonance assumption.

## Exact target and qualifications

The theorem fixes the same known metric on the same labeled compact connected smooth manifold with smooth nonempty boundary, assumes only dimension at least three and zero outside both Dirichlet spectra, and uses the full ordinary Dirichlet-to-Neumann map at zero energy. No simplicity, global positive solution, positivity of the Dirichlet form, analyticity, ray-transform hypothesis or extra frequencies are inserted. Negative eigenvalues and sign-changing smooth potentials are allowed. The local positive conjugations are constructed only after selecting a nonzero source at a frontier. Thus they do not impose an additional hypothesis on the input.

## Independent argument audit

### Signed inverse, exterior sources and finite jets

Lines 168–284 establish the initial data without a positive-form assumption. Adding a constant produces a coercive weak inverse. Its difference from the desired operator is compact through the compact $`H^1_0\to L^2`$ inclusion. The kernel is precisely the excluded zero eigenspace, by boundary regularity, so the self-adjoint compact alternative gives a bounded inverse. A small outward boundary perturbation has a small pulled-back weak-form norm, hence preserves invertibility by a Neumann series. Equal full DN symbols give equal normal potential jets for the fixed metric; the scalar factor recursion has the displayed nonzero coefficient of each successive normal derivative. Their flat difference admits a smooth zero exterior extension, permitting a common thin cap.

The weak gluing identity cancels the original-interface boundary pairing because the two DN maps agree. It therefore gives equality of all cap-source solutions on the cap and equality of Green kernels there, without energy minimization. For the jet-surjectivity lemma, transpose the inverse against an order-at-most-two point distribution annihilating the source jets. Scalar unique continuation on the connected punctured interior makes the inverse distribution point-supported. Its top delta-derivative polynomial is multiplied by the nonzero elliptic quadratic symbol, so its order increases by exactly two. Consequently the only annihilator is the equation itself. This proves the full value/first-jet surjectivity and the equation-constrained second-jet statement; it does not assume positivity of Green functions.

### Local grounding and cross continuation

The exact identity $`s_j^{-1}L_j(s_jv)=-\Delta_gv-2\langle d\log s_j,dv\rangle_g`$ removes zero order locally. Its symmetric density is $`s_j^2dV_g`$, with kernel $`G_j(x,y)/(s_j(x)s_j(y))`$. Its two cross prescriptions are separately homogeneous for the two grounded operators because on the known set the groundings and original kernels agree. Dilation makes the common principal metric Euclidean to arbitrary finite order on a fixed compact buffer, while the lower-order drift tends to zero.

The scalar Carleman inequality at lines 350–404 follows from the symmetric/skew split of the conjugated Laplacian. Adding the displayed quadratic form shifts the tangential and normal coefficients into positivity under the stated strict Hessian condition; the normal derivative is controlled by the skew part. Lower-order and fixed-coefficient errors have smaller powers of the large parameter and are absorbed. Balancing its two cutoff losses gives the stated interpolation exponent.

Reconstructed the cross lemma at lines 407–490: restriction of the closed homogeneous $`L^2`$ space to a compact interior observation set is compact and injective. Its singular values decay faster than every power by interior derivative estimates and finite-rank Fourier truncation. Compatibility identifies the two sets of coefficients; the second cross piece's coefficient norm costs precisely one inverse singular value. Two interpolation exponents with sum greater than one make the product coefficients absolutely summable. The sum solves both equations; their sum is elliptic on the product. Orthogonal-complement pairings and unique continuation show that its actual intersections agree with both prescribed pieces, so extension is not just a formal series without identification. Only upper singular-value bounds are needed.

For the product hypersurface crossing, checked the dual-cone reduction and the cylinder geometry (lines 493–568). An annihilating positive dual covariance has opposite normal components, no normal/tangential covariance, and the two tangential trace constraints. Reducing rank by trace-preserving symmetric variations decomposes it into the stated rank-one tests. Strict positivity on their compact normalized slice gives the quadratic gap after adding a multiple of $`d\rho\otimes d\rho`$. The top and lateral observed crosses lie on the known side: top heights have positive sum; lateral collars have a quadratic gap larger than their possible negative height sum. Slight concavity of the scalar weights preserves strictness and gives both interpolation exponents above one half. Their overlap with the output contains an open top band; second-variable continuation along the permitted height path identifies the extended positive-side germ. Thus the crossing lemma has both existence and agreement, not merely unique continuation.

The fixed-separation tubes at lines 570–665 have a compact positive minimum radius. Their criterion has a positive square away from the explicitly prescribed exceptional directions. For small $`b`$, its real part controls the perpendicular component and its imaginary length difference controls the parallel component; the only additional zero is $`b=-2\omega`$. The excluded neighborhoods already lie in the known seed. The radius Hessian is a small fraction of this square after the stated sequential parameter choices. At a last reached level, a finite cover uses data strictly above that level; vertical overlap segments to a common already-prescribed height identify all germs. This avoids assuming a bound on a kernel approaching an unprescribed level.

### Shrinking geometry, actual density and complete radial maps

The conformal reference metric and depth in lines 669–754 satisfy

```math
\mathop{\mathrm{Hess}}\nolimits_\gamma t
 =e^{-2Lt_0}\{\mathop{\mathrm{Hess}}\nolimits_{g_\lambda}t_0-L|dt_0|^2g_\lambda\}< -c\gamma.
```

The soft positive-part radii give $`\beta\ge\beta_0`$, negative depth Hessian of size $`\beta`$, finite derivative bounds of size $`\beta^j`$, and $`r\beta^2\le\varepsilon`$. The short-geodesic Jacobi expansion has error $`O(r^2)`$. The equal lengths of the real/imaginary criterion vectors bound its negative $`|b\cdot U_2|^2`$ term; concavity supplies the positive $`cr^2\beta`$ remainder. The errors $`Cr^2+Cr^3\beta^3`$ are absorbed in that order using large $`\beta_0`$ and small $`r\beta^2`$. For each fixed positive shrinking parameter the spheres form a compact separated family, so the previous crossing and overlap argument applies without a uniform bound at radius zero.

The conformal grounded density is $`\sigma_j^2dV_\gamma=e^{-2Lt_0}s_j^2dV_g`$. Multiplying the operator by $`e^{2Lt_0}`$ exactly compensates its delta normalization; the weighted physical flux is unchanged. The transfer functional can be put on a locally fixed surrounding surface. Applying the second operator under its integral proves its second-side equation. Its known lower-side Green formula and unique continuation give transfer of every matching pair and mass one. No arbitrary smooth elliptic Cauchy problem is solved here.

The fixed-unit-ball Schrödinger operator differs from the Euclidean one by $`O(r^2)`$ in smooth coefficients, including potential and conormal. Poincaré and boundary elliptic estimates give a smooth inverse family in integer norms. The boundary symbol recursion, decaying normal parametrices and exact inverse correction control the complete smoothing kernel as well as the principal symbol. Hence the radial map has zero first radius variation and a smooth complete $`\Psi^1`$ remainder. Ground conjugation gives exactly

```math
D_{\rm gr}=B+r([B,m]-m)+r^2\widetilde D_2.
```

Center variation combines the tangential derivative and this radial map. Its Jacobi error is $`r\Psi^1`$, and grounding contributes bounded angular order zero. Differentiating the actual transfer pairing yields $`P\psi=0`$ for all smooth traces: smooth Dirichlet problems on slightly larger balls approximate any such trace, rather than invoking an ill-posed Cauchy extension. The apparent inverse-square terms cancel because $`[B,A_i^*]=A_i^*`$ and $`\sum_i(A_i^*)^2=0`$. The remaining base orders fit the stated small class using $`r\beta^2\le\varepsilon`$.

### Angular coercivity reconstructed

Checked the Fischer projection identity and norm conversion at lines 954–974. For degree $`k`$, multiplication/differentiation are Fischer adjoints, and projecting $`\sum z_iq_i`$ subtracts $`|z|^2\sum\partial_iq_i/(2d)`$, with $`d=k+n/2-1`$. Its norm is the displayed three-term expression. The probability-sphere adjoint is $`(2d+2)\Pi_{k+1}z_i`$.

The three integrated identities in lines 987–991 follow by commuting $`D_i^-`$ with $`D_j^+`$; their leading commutator is $`-2k\mathop{\mathrm{Hess}}\nolimitsf`$. Curvature acts on a degree-$`k`$ tensor with size $`O(k)`$ and the contractions add a factor $`k`$, giving the stated lower-order errors. Substitution gives the exact raising/lowering norm difference. The integrated contraction bound uses $`\sum_i\|\partial_iv\|_F^2=k\|v\|_F^2`$; the separate pointwise contraction bound is at most $`k+n-1`$. Combining fractions of these bounds leaves a coefficient $`c+c'k/\beta`$ on $`|D^+v|^2`$, a nonnegative lowering-divergence coefficient, and a negative-Hessian contribution controlling $`k^3\beta\|v\|^2`$. The coefficient $`d-1+\theta`$ is positive even at $`k=1,n=3`$. Small $`c_1`$ and then large $`\beta_0`$ absorb the loss and curvature. The two weighted integrations of $`|D^+v|^2`$ have favorable signs: $`\Delta f<0`$, and $`\mathop{\mathrm{div}}\nolimits(\nabla f/\beta)`$ is the tangential Hessian trace divided by $`\beta`$. These control all four terms of the stated joint norm. Summing harmonic degrees is justified at every positive parameter before taking the shrinking limit.

Reconstructed the error-type bookkeeping in lines 1048–1083. Full adjunction differs from the chosen lowering operator by $`Z=\sum f_iA_i`$. Scalar angular commutators lower angular order. Potential third-base terms cancel because the second-base coefficient is real and fiber-independent; for the self-commutator, $`U^\dagger-U`$ has base order at most one and the leading scalar coefficients commute. The only remaining form types are the stated small second-base/first-base/zero-base operators. One base integration by parts and the proven off-diagonal harmonic form estimate bound them by $`C\varepsilon\mathcal N^2`$. The bounded order-one term is absorbed by large $`\beta_0`$. Thus the coercive estimate applies to the actual compactly supported mean-zero density, rather than a hypothetical model density.

The cutoff derivative supports lie either on the ordinary lower-side Poisson density, smooth down to zero radius, or at fixed positive separation. Their bounds control the actual commutator. Coercivity gives a joint $`L^2`$ density bound. Subtracting the value at the center in the transfer identity and using the first-side solution's smooth derivative yields a bound by the maximum radius times this joint norm. It tends to zero on one fixed neighborhood; its choice precedes the additional source, which is essential to the final universal quantifier.

### Global closure

All cap-source solutions agree on an open component containing the cap. Their arbitrary values identify the potentials there, and unique continuation of the smooth difference kernel identifies the Green kernels on its product. A proper component has an interior frontier touched by a ball contained in that component; no regularity of the full frontier is assumed. A single source with value one supplies local positive groundings. A finite set of source first jets supplies spanning ratio gradients. The just-proved local theorem equates every ratio pair on one common neighborhood. Subtracting their normalized equations forces equality of the two logarithmic grounding gradients; matching on the known side fixes their scalar constant. Hence the original potentials and all source solutions agree past the frontier, contradiction. Connected interior and smooth boundary continuation finish the exact global target.

## All-reference audit

All nine bibliography entries are identifiable primary sources. No absent or fabricated proof-critical citation was found.

- [Aronszajn's institutional paper](https://sites.math.washington.edu/~blwilson/Nodal/Aronszajn.pdf): author/title, 1957, volume 36, pp. 235–249 match. Smooth scalar elliptic principal coefficients and bounded lower terms in this proof meet its unique-continuation hypotheses.
- [Cekić arXiv:1704.01362v2](https://arxiv.org/html/1704.01362v2): author/title/revision date match. Lemma 3.2 and Proposition 3.3 give the factorization/DN symbol. The **last clause** of Theorem 3.4 applies when the two metric jets agree without requiring simultaneous metric normalization; here the metric is identical and both connection gauges are identity. Thus its electric-potential boundary jets apply to the target, not merely to a Yang–Mills uniqueness theorem.
- [Hunter PDE notes](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf): actual notes and stated revision identify the source; Lax–Milgram and smooth-boundary elliptic regularity are the uses. Smooth bounded potentials enter as lower-order forcing and are bootstrapped.
- [Hunter measure notes](https://www.math.ucdavis.edu/~hunter/m201b/measure.pdf): actual brief notes identify the source. Fubini and dominated convergence are used only for the explicitly integrable series/products; they are not invoked to exchange an uncontrolled shrinking limit.
- Ma–Sahoo–Salo, [arXiv:2207.02623](https://arxiv.org/abs/2207.02623), [DOI](https://doi.org/10.1112/jlms.13006): authors/title and JLMS **110** (2024), e13006 match the primary metadata. Its large-frequency/invertible-ray-transform conclusion is accurately distinguished and is not used as the new theorem.
- OpenAI metric preprint: immutable [September 24 source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026). GitHub API confirmed the commit path, README title/date/author and PDF. The method is credited, while the necessary scalar continuation/coercivity statements are proved in this submission and were reconstructed above.
- OpenAI connection preprint: immutable [October 5 source](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026). GitHub API confirmed the commit path and PDF; it is contextual attribution, not a claimed theorem for an independent electric potential.
- [Tao Fourier notes](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/): author/title/date and the periodic Fourier/Parseval material match. The manuscript proves its own singular-value consequence.
- [Taylor's author-hosted pseudodifferential short course](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2022/05/psidolect.pdf): actual course document confirmed. The relevant scalar elliptic parametrix, symbol recursion, smoothing correction and Sobolev estimates are used with smooth compact buffers. The submission also spells out the uniform complete radial-map construction required for its new shrinking argument.

The mathematical uses are covered by these nine sources or explicit manuscript proofs. The two Hunter works and two OpenAI works are distinct bibliography entries and were checked separately.

## PDF and disposition

The supplied 17-page PDF was text-extracted and all-page rendered by the coordinator. Independently inspected both contact sheets (pages 1–17): complete title, numbered argument sections, formulas and references are visible without missing pages, blank content or clipped display blocks. Source theorem and PDF theorem agree. The coordinator's citation-key and byte checks are separate from the mathematical audit.

The proof-critical continuation, uniform density and global quantifier steps have now been reconstructed; the earlier triage recommendation for a further bottleneck audit is superseded by this report. Recommend accepting the package and recording **Solved**, with the independent AI review identified. No human peer-review or Lean certification is asserted.


The package README and target comparison, including their AI-use disclosures, were also read. Their mathematical scope agrees with the manuscript and the original target; they introduce no separate executable proof or numerical certificate as a premise. Package hashes and repository integration are separate coordinating checks.
