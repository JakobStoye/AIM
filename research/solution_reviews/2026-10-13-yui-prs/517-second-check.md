# AIM 517: second independent argument and source audit of PR #39

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, separate maintainer-review context from the primary audit; independent AI argument audit, not human or Lean verification.

**PR:** [#39](https://github.com/MColbrook/AIM/pull/39). **Audited head:** `c5902207726a88e2f2922c7ffb1189272e755cdb`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Submitted manuscript source](https://github.com/MColbrook/AIM/blob/c5902207726a88e2f2922c7ffb1189272e755cdb/research/solutions/kaiwen-jin-517/paper/main.tex).

The entire 674-line manuscript, target comparison, reference guide, all eight bibliography entries, and all eleven rendered manuscript pages were inspected. The Gram determinant argument, singular-value passage, and finite-cover transfer were reconstructed directly, without consulting the primary review report. The numerical evidence is supplemental; the decision below is based on the analytic proof.

**Conclusion:** This second check supports **Solved, affirmative** for the exact AIM 517 scalar symmetric measurable-coefficient problem. No proof-critical false step, missing hypothesis, or required mathematical correction was found. No unique-continuation property, coefficient derivative, coefficient boundary trace, scale separation, or contrast-independent constant is assumed.

## Energy spaces and compact restriction

On each ball, choosing the ordinary mean-zero representative turns the quotient by constants into a Hilbert space: Poincare and ellipticity make the energy norm equivalent to the H1 norm on the closed harmonic mean-zero subspace. The weak harmonicity constraints are continuous. Contractivity of restriction follows from inclusion of volume integrals (source lines 120-157).

The weak cutoff test gives the Caccioppoli estimate in line 168. Its factors are correct: the cross term is bounded by twice the product of the two square roots of A-weighted energies, and dividing gives the constant $`2\sqrt\beta/(s-r)`$. The test belongs to H1-zero by the Lipschitz product rule. A bounded outer mean-zero sequence has an L2-convergent subsequence; applying this estimate to pairwise harmonic differences gives convergence in the inner quotient energy norm. Thus restriction is compact without using regularity of A or unique continuation (158-174).

## Boundary forms, scaling, and counting

For a spherical mode of degree $`\ell`$, ordinary harmonic extension of trace coefficient $`c`$ has volume energy $`t^{d-2}\ell c^2`$ and tangential boundary energy $`t^{d-3}\ell(\ell+d-2)c^2`$. These were recomputed from polar coordinates. The generalized eigenvalue is therefore $`(\ell+d-2)/t`$. The area-measure convention changes only the normalization of the spherical basis, not these eigenvalues (176-227).

The submitted regularity argument establishes both identities for H1 traces by smooth density, Parseval, and convergence of the harmonic series in H1. The extension has the given trace and is weakly harmonic. It does not apply a classical integration-by-parts identity to arbitrary nonsmooth A-harmonic data.

The multiplicities are 2 in dimension 2 and $`2\ell+1`$ in dimension 3. In dimension 2, $`\ell_j=\lceil j/2\rceil`$ gives $`\Sigma_2(m)\ge m^2/4`$. In dimension 3, the number of positive modes through degree $`\ell`$ is $`\ell(\ell+2)`$, giving $`\nu_j\ge\sqrt j`$ and $`\Sigma_3(m)\ge(2/3)m^{3/2}`$. Both inequalities have the stated constants.

For any independent m-dimensional trace family, whitening its extension-energy Gram matrix gives orthonormal vectors with squared coordinate weights $`0\le w_j\le1`$ and total mass m. Moving any tail mass to missing positions among the first m modes cannot increase the eigenvalue-weighted sum. This proves the trace lower bound for an arbitrary family, not only for spherical modes, including the infinite-sum limit (237-258).

## Measurable coefficients and the determinant derivative

Each volume energy density is integrable. Polar Fubini therefore makes every Gram entry absolutely continuous and identifies its almost-everywhere derivative with the spherical integral of that measurable density. This requires neither a prescribed value of A on an exceptional sphere nor a Sobolev trace of A. A common full-measure set can be chosen for the finite family and the ellipticity bounds.

On annuli bounded away from zero, smooth polar charts have bounded derivatives and inverse derivatives. H1 approximation and Fubini give H1 angular slices for almost every radius, with tangential weak gradients equal to the tangential projections of the ambient gradient. The same approximations converge in H1 of any fixed inner ball, so trace continuity identifies those slices with the ordinary ball trace. The countable-annulus and finite-family intersections in lines 280-291 are sufficient. No assertion about every radius is needed.

At these good radii, the two matrix inequalities have the correct directions:

```math
G'(t)\ge\alpha Q(t),\qquad G(t)\le\beta B(t).
```

The first discards the normal component from the lower ellipticity bound. For the second, the ordinary harmonic extension h is a permitted competitor with the same trace as the A-harmonic combination u. Their difference is in H1-zero of the ball, whose test can be extended by zero to the outer ball. Symmetry and weak harmonicity imply

```math
a(h,h)=a(u,u)+a(h-u,h-u)\ge a(u,u),
```

and upper ellipticity gives $`a(h,h)\le\beta\int|\nabla h|^2`$. Thus ordinary harmonic extension is used for an upper comparison, not incorrectly claimed to minimize the A-energy (293-309).

If G(r) is singular, the desired determinant bound is immediate. Otherwise monotonicity keeps G uniformly positive definite on the whole closed radial interval. A constant trace combination at a good radius would, by testing u minus that constant, have zero energy on that same ball, contradicting positive definiteness. Hence B is also positive definite there. This is Dirichlet uniqueness on one ball; it is not unique continuation from an inner region.

Inverse monotonicity gives $`G^{-1}\ge\beta^{-1}B^{-1}`$. For a positive semidefinite Q the trace of its product with a positive semidefinite matrix is nonnegative even when the two matrices do not commute. Combining this fact with the boundary estimate gives

```math
\mathop{\mathrm{tr}}\nolimits(G^{-1}G')
 \ge (\alpha/\beta)\Sigma_d(m)/t.
```

Because G has absolutely continuous entries and stays uniformly positive definite, composition with log determinant is absolutely continuous. The cofactor differential formula holds almost everywhere. Integrating gives exactly the exponent and inequality direction in Lemma 2.3. The outer endpoint R needs only continuity of the volume integral and need not be a good boundary slice (311-335). All these steps remain valid when some restriction directions disappear on smaller balls.

## Restriction singular values and widths

The compact nonnegative operator $`S^*S`$ has the required spectral decomposition. For its first m positive singular directions the outer Gram matrix is the identity and the inner matrix is diagonal with entries $`s_j^2`$. The determinant bound therefore applies directly. If $`s_m=0`$, the product is zero and that case is already covered.

For nonincreasing singular values, $`s_m^{2m}\le\prod_{j\le m}s_j^2`$. Taking roots gives the submitted individual estimate. The counting bounds yield $`b=(\alpha/(8\beta))\log(R/r)`$ in dimension 2 and $`b=(\alpha/(3\beta))\log(R/r)`$ in dimension 3, with no off-by-one loss in the asserted exponent.

The best k-dimensional image space is spanned by the first k left directions. Conversely, in the span of k+1 right directions any competitor space of dimension at most k has a nonzero image-orthogonal direction; its norm is at least $`s_{k+1}`$. This proves the width identity, including k=0, finite rank, and nontrivial kernel cases. The real-space reduction is valid because all operators and forms commute with conjugation (338-372).

## Normalization, cutoff, and closure to the precise target

The cutoff identity in line 381 follows by testing the two harmonic equations with the zero extensions of $`\chi^2v`$ and $`\chi^2u`$, expanding, and using symmetry. These are legitimate H1-zero tests. It gives $`a(\chi u,\chi v)=\int q uv`$ with $`q=A\nabla\chi\cdot\nabla\chi`$. The nonzero H1-zero cutoff has positive integral of q by ellipticity and Poincare. Taking v=1 identifies the target normalization with a weighted mean. This selects a unique constant representative.

For a normalized u, the displayed mean estimate and ordinary mean Poincare bound its H1 norm by its outer energy. Hence the normalized space is a Hilbert space in the exact source norm, and the original T is bounded. Rellich plus the cutoff identity on differences also gives compactness. The test does not silently replace the target normalization by an unrelated mean-zero condition (375-401).

The positive gap between the closed inner cube and the outer boundary gives a fixed finite family of doubled balls entirely inside the outer cube. The partition construction in lines 407-412 has a denominator bounded away from zero on its compact support. Its sum is one on a neighborhood of the closed inner cube.

A W1-infinity cutoff on a convex cube has a Lipschitz representative on its closure. Zero Sobolev trace makes its boundary values zero; a segment to an exterior point shows its zero extension is globally Lipschitz. Each product $`\phi_j=\chi\psi_j`$ thus has the required weak derivative. For a local mean-zero error, scaled Poincare gives exactly

```math
\|\phi_j e\|_{a,\omega}
\le \sqrt{\beta/\alpha}
 (\|\phi_j\|_\infty+C_Pr\|\nabla\phi_j\|_\infty)
 \|e\|_{a,B_r(x_j)}.
```

Compact support within the ball removes ball-boundary jumps, and the cutoff's zero cube trace places the product in the **prescribed** H1-zero target space.

The local singular projection is taken on the quotient, with the ordinary local mean added back. Consequently each error has zero mean, and the multiplier bound applies. Including each independent local constant costs one dimension per patch: the total space has dimension at most $`M(k+1)`$, as stated. Its basis is independent of u. The local input energy is bounded by the original outer-cube energy. Summing the finitely many patch errors yields the exact target energy approximation. Choosing $`k+1=\lfloor n/M\rfloor\ge n/(2M)`$ proves the rate for $`n\ge M`$; boundedness of T covers the finitely many smaller n by increasing C. Every covering choice is fixed before n. The resulting constants have precisely the dependence allowed by the problem (403-457).

## Ancillary radial formulas and numerical evidence

The ordinary harmonic energy spectrum was recomputed as $`(r/R)^{\ell+(d-2)/2}`$. The excluded singular radial branches have infinite energy at zero, including the logarithmic degree-zero branch in dimension 2. This establishes the stated energy-space comparison with the distinct L2 Bergman exponent.

For radial polar anisotropy the weak separated equation, interface continuity, logarithmic state matrix, and energy identity in lines 483-517 are consistent. In particular, continuity of the physical flux $`\rho^{d-1}a_rf'`$ also gives continuity of the state entry $`q=a_r\rho f'`$ at a fixed interface. The positive core exponent and its rationalized form are correct. The exact exponential formula follows from the two eigenvalues of the 2-by-2 matrix; its positive-state normalization and logarithmic energy accounting are algebraically consistent. The stated complexity counts and limitations concerning roundoff and omitted-degree ordering are appropriate.

The parent audit reports that all 23 unit tests and the 40 radial/80 finite-form trials replayed successfully. This second analytic review did not treat those tests as premises or as certification for every measurable coefficient. It independently checked the differential/form arguments that the finite trials illustrate. The paper itself makes the same distinction.

## Eight-reference audit

| Entry | Primary evidence and applicability check |
|---|---|
| AIM517 | The downloaded target is the pinned [catalogue problem](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/517-sharp-local-elliptic-widths.md); all hypotheses, normalization, norms, dimensions and quantifiers match. |
| Ma2024 | The exact [arXiv v3 record/text](https://arxiv.org/abs/2311.08761v3) confirms author, title and 17 December 2024 version. Theorem 3.8 and Remark 3.9 give the preceding rate, Section 6.1 includes scalar elliptic diffusion as zero-convection specialization, and Section 7 states the sharper conjecture. It is background, not a source already proving this result. |
| MSD2021 | The [v3 record/text](https://arxiv.org/abs/2103.09545v3) confirms authors, title and 21 December 2021 version. Section 3.1, equation 3.3 and Lemma 3.1 contain the normalization and cutoff identity at the asserted regularity. The identity is also proved independently in the submission. |
| LiWang2000 | The [Annals record](https://annals.math.princeton.edu/articles/11855) and [actual preprint](https://arxiv.org/pdf/math/0009254) confirm title, authors, volume 152(2), 2000, pages 645-658 and DOI. Lemma 1 and Section 2 do use boundary spectral/determinant ideas. They are contextual credit rather than a borrowed theorem establishing measurable-coefficient cutoff widths. |
| BandtlowChu2009 | The [publisher record](https://academic.oup.com/blms/article-abstract/41/5/903/299566) confirms authors, title, 41(5), 2009, 903-915 and DOI. The downloaded [author final text](https://webspace.maths.qmul.ac.uk/o.bandtlow/publ/harmonic_final.pdf) has the cited Proposition 3.3 and Theorem 4.5, for L2 harmonic Bergman restriction and finite covers. The manuscript correctly distinguishes that norm and proves its own energy transfer. |
| Axler2001 | The [actual author PDF](https://www.axler.net/HFT.pdf) confirms second edition 2001 and electronic date 17 July 2020. Proposition 5.8 and Theorem 5.12 are the stated dimension and L2 spherical-completeness results. The manuscript explicitly converts probability measure to area measure. |
| GuermondNotes | The exact [official archive](https://people.tamu.edu/~guermond/M661_FALL_2025/index.html) and linked chapters/appendix were downloaded. All cited locators were checked: 1.47, 2.2, 2.9, 2.21, 2.25, 2.30, 2.35, 3.10, 3.24, 3.27 and A.16. Their domain/regularity assumptions apply to balls, cubes and the fixed smooth annular coordinate charts. The archive label is not presented as the notes' publication date. |
| Melrose2017 | The [official Lecture 14 PDF](https://math.mit.edu/~rbm/18-155-F17/L14.pdf) confirms author, course and 31 October 2017 date; page 1 states the compact self-adjoint spectral theorem used for S-star-S. Its hypotheses were proved before application. |

No missing proof dependency, incorrect bibliography entry, or inappropriate theorem substitution was found. Some external sources are contextual acknowledgments; the rough-coefficient determinant estimate and cutoff transfer are supplied in the submitted argument itself.

All eleven rendered PDF pages agree with the source, including both numerical figures, the table, all eight references and the AI-use statement. No blank page, clipping or unresolved reference was observed. The target comparison and reference guide accurately describe what is proved and what the numerical checks do. No solution-package or GitHub changes were made in this second review.
