# AIM 434 — independent review of PR 70

- Date: 2026-10-13; submission: [PR 70](https://github.com/MColbrook/AIM/pull/70), Kaiwen Jin.
- Reviewed head: `2e3c856584ed33f10b88389dd0ff65b9518e88d6`.
- Proof: [PDF](../../solutions/434-p-harmonic-second-sobolev-derivatives/paper/main.pdf), [source](../../solutions/434-p-harmonic-second-sobolev-derivatives/paper/main.tex).
- Target: `problems/434-p-harmonic-second-sobolev-derivatives.md` at the immutable original revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
- Reviewer: independent Codex agent, separate from drafting/self-review; AI natural-language mathematical argument audit. No human or Lean certification.
- Verdict: **Solved**, unweighted local $`W^{2,2}`$ regularity for every finite $`p\ge5`$ in three dimensions.

## Target comparison

Every weak solution on every open subset of $`\mathbb R^3`$ is covered, including neighborhoods of critical points, arbitrary sign and every finite exponent in the target range. No assertion uniform as $`p\to\infty`$ or in higher dimensions is needed. The limit identifies all nine unweighted distributional Hessian entries; it does not substitute a weighted nonlinear gradient composition.

## Complete proof audit

**Block identities and critical set, lines 131–280.** For a fixed smooth regularized solution, the equation gives $`\mathop{\mathrm{tr}}\nolimitsB=-sa`$ with $`1\le s\le p-1`$. The displayed Hessian decomposition implies $`|H|^2\le3(|H|^2-|He|^2)`$. Direct differentiation of $`q_\delta=(|Dv|^2+\delta^2)^{1/2}`$ produces the nonnegative norm-Hessian term. Its integrated right side has a finite limit because the fixed solution is smooth. Fatou therefore proves local integrability of $`|H|^2/q`$ **for this fixed solution**, with the favorable distributional inequality. It does not assume a uniform estimate at this step. The field $`G=(\Delta v)e`$ extends $`C^1`$ through zeros: its numerator is homogeneous of degree two in the gradient, with derivative tending to zero, and its denominator is bounded below by the positive regularization. Integrating this field by parts preserves the sign of the Fatou inequality. The Hessian vanishes almost everywhere on the gradient zero set by the level-set derivative argument, so the identity $`|H|=\sqrt E\sqrt q`$ holds almost everywhere, including on that set.

**Curvature coercivity, lines 286–320.** Recomputed $`\mathcal K=\det B/q=(s^2a^2/4-|B_0|^2/2)/q`$. Its absolute value is bounded by $`E/2`$. With $`\ell=p-1`$, $`c_p=\ell+\ell^{-1}`$ and $`d_p=2c_p-2`$, subtracting $`E`$ from $`c_pf+d_p\mathcal K`$ cancels the trace-free block and leaves

```math
\{(c_p-2)|w|^2+(sc_p-s^2-1)a^2\}/q,
\qquad sc_p-s^2-1=(\ell-s)(s\ell-1)/\ell\ge0.
```

Thus the pointwise inequality is correct despite neither signed term being individually positive.

**Integrated curvature, lines 325–420.** At simultaneous regular volume/boundary values, the level set in the closed ball is a compact orientable smooth surface with smooth boundary and finitely many components. A closed embedded level component would bound a region inside the ball. Freezing the regularized uniformly elliptic nondivergence operator and testing the maximum principle with $`v\pm\rho e^{x_1}`$ forces the solution constant in that region; continuity of its gradient contradicts the regular level at its boundary. Every level component therefore has a boundary circle. Its Euler characteristic is at most its number of boundary circles. Gauss–Bonnet, the bound of geodesic by Euclidean curvature, and Fenchel separately on each closed curve give the displayed upper bound by twice total boundary curvature. This direction is needed because $`\mathcal K`$ is signed. Twice differentiating the boundary level curve on the sphere gives $`\kappa |D_{\partial B_r}v|\le|H|+2q/r`$. Volume and surface coarea consequently give the exact ball upper bound. Absolute integrability was established before signed coarea is used.

The appendix's regular-value assertion follows by the written induction on dimension: Taylor covering makes the deepest critical stratum's image null, and an implicit hypersurface reduces every preceding stratum to one lower dimension. Its local graph substitutions yield both coarea identities for nonnegative Borel integrands, and then for absolutely integrable signed integrands. Only fixed smooth regularizations and their sphere restrictions are used, not an unproved Sard theorem for the weak limit.

**Uniform cutoff and iteration, lines 425–506.** A decreasing radial cutoff has a nonnegative radial layer weight. Applying the signed ball upper bound under this weight gives a shell Hessian term and a shell gradient-norm term. The distributional field bound controls the other cutoff term. Using $`|H|=\sqrt E\sqrt q`$ and Young gives $`F(a)\le\vartheta F(b)+C(b-a)^{-2}Q`$. The radii tending to $`2R`$ with $`\vartheta=1/8`$ make the geometric series ratio $`4\vartheta=1/2`$. The terminal term tends to zero using only finiteness of the fixed solution's $`F(2R)`$; no uniform preliminary bound is assumed. This yields the claimed viscosity-independent estimate.

**Weak-limit Hessian, lines 508–575.** The primary approximation supplies smooth regularized Dirichlet solutions with uniform interior gradient bounds and local uniform gradient convergence for every finite $`p>1`$. Multiplying the weighted Hessian estimate by the common gradient supremum gives a full unweighted $`L^2`$ bound, including the almost-everywhere critical set. Integration by parts and uniform gradient convergence identify each second distributional derivative as a bounded functional on $`L^2`$. Density and Riesz produce its $`L^2`$ representative. Local covers and distributional uniqueness give the stated $`W^{2,2}_{\rm loc}`$ conclusion without an assumption on the limiting critical set.

## All nine references checked

- Lindqvist, Report 161 (2017), [primary monograph](https://jyx.jyu.fi/bitstreams/2a8cbc94-58e9-4e75-94d6-0f1f5bc22ac1/download): author/title/edition match. The quoted gradient regularity and three-dimensional unweighted range are correctly distinguished from the new target.
- Sarsa, [arXiv:2009.10102v1](https://arxiv.org/html/2009.10102v1): metadata and nonlinear weighted regularity formula match. Equations (3.2)–(3.4) explicitly supply smooth regularizations, uniform local $`C^{1,\alpha}`$ bounds and subsequential uniform gradient convergence for all finite $`p>1`$, exactly as required.
- Haarala–Sarsa, JDE **339** (2022), 232–260, [primary v2](https://arxiv.org/html/2204.13550v2), [DOI](https://doi.org/10.1016/j.jde.2022.08.022): authors/title/pages/year match; its Cordes-based background is not treated as an unrestricted theorem.
- Sullivan, TU Berlin 2013, [surface notes](https://www3.math.tu-berlin.de/geometrie/Lehre/SS13/DGI/dg1.pdf): actual B16–B19 notes inspected. They give Gauss–Bonnet, Euler-characteristic formulas and the closed embedded surface's bounded/unbounded separation used here.
- Sullivan, [Curves of Finite Total Curvature, arXiv v2](https://arxiv.org/html/math/0606007v2): title/version match; the total-curvature and Fenchel results apply to the smooth closed regular boundary curves. No simplicity of each curve beyond embedded regularity is silently needed for Fenchel.
- Tao, [measure-theory author version](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf), AMS 2011: actual source confirmed; Fatou, dominated convergence, Fubini and monotone-class uses have the displayed integrability hypotheses.
- Tao, [An epsilon of room, author version](https://terrytao.wordpress.com/wp-content/uploads/2010/02/epsilon.pdf), 2010: actual source confirmed; density and Hilbert Riesz representation are standard facts also reconstructed in the proof.
- Lebl, [Basic Analysis I](https://www.jirka.org/ra/realanal.pdf) and [Basic Analysis II](https://www.jirka.org/ra/realanal2.pdf): both title pages confirm version 6.3, May 15, 2026. Taylor, substitution and implicit-function statements apply to the smooth finite-dimensional charts used. The new critical-value/coarea lemmas are proved explicitly rather than delegated to these elementary references.

No missing proof-critical source or unsupported mathematical step remained after the reconstruction.

## PDF and disposition

Coordinator parsed/rendered all nine pages; independently inspected the complete contact sheet. The critical-set proof, geometric estimate, approximation, appendices and all bibliography entries are complete, legible at normal page size and not clipped. Recommend accepting the package and marking **Solved**, with this independent AI review recorded. No Lean/human certification is implied.


The package README and target comparison, including their AI-use disclosures, were also read. Their mathematical scope agrees with the manuscript and the original target; they introduce no separate executable proof or numerical certificate as a premise. Package hashes and repository integration are separate coordinating checks.
