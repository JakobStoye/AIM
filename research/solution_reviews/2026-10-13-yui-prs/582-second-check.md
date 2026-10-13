# AIM 582 — independent second check of PR 87

- Review date: 2026-10-13; submission: [PR 87](https://github.com/MColbrook/AIM/pull/87), Kaiwen Jin.
- Pinned head: `c84ae22b6a0e37b01160367c79eccb970ebce507`.
- Proof: [PDF](../../solutions/582-accumulating-gaps/paper/main.pdf), [source](../../solutions/582-accumulating-gaps/paper/main.tex).
- Exact original target: `problems/582-fractal-screen-sobolev-invertibility.md` at `c9929805cece044705abaaebe1cebddac1ba11a6`.
- Reviewer: a second independent Codex agent, separate from the submission and the coordinating review. This is a natural-language AI mathematical audit, not human refereeing or Lean verification.
- Recommendation: **Solved**, negative answer to the universally quantified original conjecture. No proof correction is required.

## Scope and target

I read the entire source and original target and reconstructed the proof independently, with particular attention to the compact positive operator theorem, the distributional charge at the accumulation point, the original quotient trace spaces, and identification of the positive-wavenumber operator. The target allows $`n=d=1`$; hence one compact regular one-dimensional counterexample disproves its assertion about every screen. This does not claim the conjecture restricted to $`d<n`$, the sharp range for the example, or irregularity for a specified incident plane wave. Those narrower questions are outside the requested disproof alternative.

## Spectral construction: Lemmas 2.1–2.2

The partial Dirichlet trace defines a closed real Hilbert subspace of the periodic cylinder's $`H^1`$ space. The elementary trace estimate, Fourier/cosine compactness, and contradiction with a constant yield the Poincare inequality. For the form $`b_a`$, periodic integration gives zero diagonal drift and a bounded skew-adjoint representation in the gradient inner product. Both $`I+T_a`$ and its adjoint have lower bound one; closed range and the zero adjoint kernel prove surjectivity. Its inverse maps $`L^2`$ boundedly into $`H^1`$ and therefore is compact on $`L^2`$.

Testing with the negative part has the displayed negative gradient sign; the drift again vanishes. It proves positivity. The local gauge $`w=e^{-as}u`$ satisfies $`(-\Delta+a^2)w=e^{-as}f`$. Local $`H^2`$ regularity gives continuity in this two-dimensional setting. On a thin auxiliary cylinder, $`w\cos(ay)`$ is a nonnegative superharmonic function: its Laplacian is $`-e^{-as}f\cos(ay)`$. The mean-value inequality and propagation through overlapping neighborhoods prove strict interior positivity for every nonzero nonnegative input. This also proves ideal irreducibility: truncations bounded by multiples of the strictly positive output approximate any $`L^2`$ function within an invariant closed ideal.

I downloaded and read Chang–Wang–Wu's actual publisher PDF. **Theorem 1.5, pp. 3174–3175, requires a positive, ideal-irreducible, compact operator on a Banach lattice of dimension greater than one.** All these hypotheses hold on real $`L^2(Q)`$. It does not require a positive cone with nonempty interior; applying a strong-positivity theorem on that cone would have been inappropriate, but that is not the cited result. The theorem gives positive spectral radius, a positive direct eigenvector, and a strictly positive adjoint eigenfunctional. Hilbert dual identification and the weak inverse put both eigenvectors in the form domain. Local regularity and even reflection at open Neumann boundary pieces give their stated pointwise positivity there.

The adjoint boundary calculation with $`\sin(\theta/2)`$ is valid although this comparison function does not satisfy the natural Neumann condition at the bottom. Its outward normal derivative is $`-1/2`$ there and zero at the top. The Dirichlet part has zero adjoint trace, so the remaining bottom integral is strictly negative. Thus $`\lambda(a)<1/4`$. Testing the direct equation by its own eigenvector gives the independent positive lower bound. The compactness proof of continuity uses bounded normalized eigenvectors and a strictly positive adjoint pairing, not an unprovided spectral perturbation theorem. The intermediate value argument consequently yields $`0<\alpha<1/2`$ with $`\lambda(\alpha)=\alpha^2`$.

## Harmonic extension and charge: Lemmas 2.3, 3.1–3.2

The logarithmic coordinate and drift signs agree: $`u=e^{-\alpha s}h`$ satisfies the flat strip Laplace equation precisely because $`L_\alpha h=\alpha^2h`$. The repeated Dirichlet intervals correspond to $`[q^{j+1},2q^{j+1}]`$. Even reflection through gaps and the negative real axis gives harmonicity off the repeated screen. Periodizing the weighted test proves the weak Dirichlet identity at mixed junctions as well; the manuscript's integration by parts converts the extra $`\alpha h_s-\alpha^2h`$ terms to $`-\alpha h v_s`$ with the correct sign.

The annular energy scales as $`q^{2j\alpha}`$, and the cutoff-gradient term has the same scaling. These summable bounds prove the $`H^1`$ extension through zero. In the positivity test $`\zeta U/(U+\delta)`$, a logarithmic radial cutoff removes zero. Its vanishing gradient norm and finite local energy justify removing it for each fixed $`\delta>0`$. The second integral is nonnegative; the first converges by dominated convergence because the zero screen is planar measure zero. Hence $`\Delta U`$ is a positive distribution. The compact cutoff has all its derivatives in a screen-free annulus, so its extra term $`F`$ is smooth compactly supported, while $`\mu=\chi\Delta U`$ is positive and supported on exactly the compact proposed screen.

The order-zero bound controls all tests in a common compact neighborhood, including the thin-strip cutoff used for the line-support argument. It excludes derivatives of normal deltas and proves $`\mu=\nu\otimes\delta_0`$. Nonnenmacher's cited one-dimensional measure result is applied after that reduction, not incorrectly imported as a statement about arbitrary planar distributions. The measure is finite by compact support. Vanishing on any open interval in the interior of $`I_0`$ would make the nonnegative function harmonic across a zero trace and contradict the minimum principle. Scaling the planar distribution cancels its area Jacobian with the two derivatives, giving the exact mass factor $`q^{j\alpha}`$.

The Fourier normalization is correct:

```math
\widehat\mu(\xi,\eta)=(2\pi)^{-1/2}\widehat\nu(\xi),\qquad
\|\mu\|_{H^{-1}(\mathbb R^2)}^2
=\tfrac12\|\nu\|_{H^{-1/2}(\mathbb R)}^2.
```

Since $`\Delta W-F\in H^{-1}`$, this proves energy membership. A smooth cutoff which is one on a disk of radius $`r^2`$ and zero outside radius $`r`$ has vanishing $`H^1`$ norm. Positivity and duality therefore rule out an origin atom; compactification cannot hide an extra delta. The scaled test satisfies $`\|\psi_j\|_{H^\varepsilon}\le q^{j(1/2-\varepsilon)}\|\psi\|_{H^\varepsilon}`$. Its charge pairing is $`q^{j\alpha}M`$ with $`M>0`$. Their ratio diverges exactly when $`\varepsilon<1/2-\alpha`$, proving the claimed failure of negative Sobolev membership.

## Original spaces and positive-wavenumber image

I downloaded and inspected Caetano et al.'s cited v2. Theorem 2.7 explicitly covers $`d=n`$, with the strict range $`0<s<1`$ in that case. It identifies the original adjoint quotient trace with supported $`H^{-s}`$ distributions and gives density of $`L^2(\Gamma)`$. Footnote 7 explicitly proves agreement of adjoint maps on intersecting domains. Thus both the energy lift of $`\nu`$ and the contradiction at $`s=\varepsilon`$ use the original pivot duals. Bounded densities are dense too, by finite measure and their density in $`L^2`$.

For $`G=-(2\pi)^{-1}\log|z|`$, the sign $`\Delta G=-\delta_0`$ implies $`G*\mu=-W-G*F`$. The latter volume potential is smooth. A localized $`G`$ has $`(1-\Delta)K=\delta_0+R`$ with $`R\in L^1`$, so its Fourier multiplier gives $`H^{-1}\to H^1`$. The normal Fourier Cauchy–Schwarz estimate gives the exact $`H^1\to H^{1/2}`$ line trace, establishing continuity at energy regularity rather than a pointwise singular integral assertion. The trace of $`W`$ is zero on the screen.

The Bessel formulas yield $`\Phi_k-G=\kappa_k+A_k(x^2)+x^2\log|x|B_k(x^2)`$ on the line. The even correction is $`C^1`$ at zero for every fixed positive wavenumber. Its compactly supported version convolved with the finite measure is $`C^1_c\subset H^1`$. Independently, integration by parts bounds its multiplier by $`C(1+\xi^2)^{-1/2}`$, giving $`H^{-1/2}\to H^{1/2}`$ continuity. Theorem 4.6 gives the original operator's integral representation on bounded densities. Passing that representation along an energy approximation, using the two continuity bounds, establishes equation (20) for the original operator. It is not a newly defined Laplace or positive-wavenumber operator.

The final input inclusion and output inclusion have the proper directions. For $`\varepsilon=1/2-t`$, the constructed datum has an $`H^1`$ extension and belongs to $`\mathbb H^{1-\varepsilon}`$. A hypothetical preimage in $`\mathbb H^{-\varepsilon}`$ embeds in the energy space; its operator value agrees there. Lemma 4.3 and equations (45)–(46) give coercive injectivity at energy regularity, forcing that preimage to equal the proven irregular density. This is a contradiction for every $`\alpha<t<1/2`$ and every $`k>0`$.

## All-reference and document audit

All six bibliography entries are real, correctly identified, and used within their verified scope. No missing proof-critical reference was found.

- Caetano et al.: [primary v2 PDF](https://arxiv.org/pdf/2212.06594v2), [published DOI](https://doi.org/10.1007/s00211-024-01399-7), Numerische Mathematik 156 (2024), 463–532. Theorem 2.7, footnote 7, Lemma 4.3, (45)–(46), Theorem 4.6 and Proposition 4.7 were checked. Conjecture 4.8 expressly includes the proposed integer-dimensional case.
- Chandler-Wilde, Claret, Hewett, Rozanova-Pierrat and Sadeghi: [arXiv:2605.19540v1](https://arxiv.org/html/2605.19540v1), 2026. Proposition 4.10 supplies a local interval under its additional geometry and spectral hypotheses; this is background only.
- Chang, Wang and Wu: [publisher](https://www.aimsciences.org/article/doi/10.3934/dcds.2020054), [actual PDF](https://www.aimsciences.org/data/article/export-pdf?id=ae0bf0bd-c87e-4233-9186-ba751df59733), DCDS 40(6) (2020), 3171–3200. Theorem 1.5's exact hypotheses and conclusions were inspected as described above.
- Casey Rodriguez (lecturer), Andrew Lin (notes): [MIT Spring 2021 notes](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/8fb8d5c170f1613151aca71de21027bc_MIT18_102s21_full_lec.pdf), Theorems 180 and 184, pp. 90–93. They are respectively the Hilbert orthogonal decomposition and Riesz representation statements used here; author, title and date match.
- Stephane Nonnenmacher: [Paris-Saclay September 2022 notes](https://www.imo.universite-paris-saclay.fr/~stephane.nonnenmacher/enseign/Distributions2022_Chap1-3.pdf), Proposition 1.9.11 and Remark 1.9.12, printed pp. 60–61. The order-zero and positive-measure conclusions match the one-dimensional application.
- NIST DLMF: [10.2.2](https://dlmf.nist.gov/10.2.E2), [10.4.3](https://dlmf.nist.gov/10.4.E3), [10.8.2](https://dlmf.nist.gov/10.8.E2). The $`J_0`$, Hankel and $`Y_0`$ formulas give the stated expansion. The live primary source identifies version 1.2.8 and release 2026-09-15, matching the manuscript.

The package README, target comparison and reproduction instructions were read and agree with the mathematical result and limitations. The eight-page rendered contact sheet was inspected independently: all pages and the schematic are present, readable and unclipped, and match the source's section/theorem structure. No computational certificate or executable calculation is required. Global package hashes and compilation checks are separate coordinator checks.

## Decision

The fresh independent reconstruction found no false step, unsupported bottleneck, or unmatched target hypothesis. The constructed admissible screen disproves the full universally quantified target. I concur with recording **Solved (negative)** and accepting the package, with this AI review and its lack of human or formal certification explicitly disclosed. No Lean status is justified.