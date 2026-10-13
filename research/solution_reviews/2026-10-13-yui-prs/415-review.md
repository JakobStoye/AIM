# AIM 415 — independent review of PR 58

- Date: 2026-10-13.
- Submission: [PR 58](https://github.com/MColbrook/AIM/pull/58), Kaiwen Jin.
- Reviewed head: `060bceb02fd167080976f6bb780f4be9dc1b9910`.
- Proof: [PDF](../../solutions/415-nongradient-neumann-uniform-control/paper/main.pdf), [source](../../solutions/415-nongradient-neumann-uniform-control/paper/main.tex).
- Target: `problems/415-nongradient-neumann-uniform-control.md` at the pinned original problem revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
- Reviewer: independent Codex agent, separate from manuscript preparation. AI natural-language argument audit; no human referee or Lean certification claimed.
- Verdict: **Solved**, affirmative answer for the complete autonomous strictly outward target.

## Scope

The theorem includes every stated smooth bounded connected domain, interior observation region, autonomous $`W^{2,\infty}`$ drift, strictly positive outward component, and the original neighborhood flushing condition. It keeps the Neumann state boundary condition and every $`L^2`$ initial datum. The conclusion is stronger than requested: a common threshold time and control bound apply to all subsequent times and all $`0<\varepsilon<1`$. It does not claim the merely nonnegative or time-dependent drift cases, which are not the target.

## Complete proof reconstruction

**Weak equation and gauge, lines 151–224.** The transposed form gives the adjoint boundary condition $`\varepsilon\partial_\nu\phi+(B\cdot\nu)\phi=0`$ with the correct sign. Its energy identity has nonnegative diffusion and boundary terms when time runs toward the terminal datum; hence earlier mass is bounded by later mass. The compatible Neumann problem $`\Delta g=k`$, $`\partial_\nu g=(B\cdot\nu)/2`$ supplies $`g\in C^{2,1/2}`$. Direct differentiation of $`u=e^{g/\varepsilon}\phi`$ gives

```math
u_t+\varepsilon\Delta u+(B-2\nabla g)\cdot\nabla u
 +\{(|\nabla g|^2-B\cdot\nabla g)/\varepsilon+\mathop{\mathrm{div}}\nolimitsB-k\}u=0.
```

The new drift is tangent, the Robin coefficient is strictly positive, and the required coefficients have the stated bounded derivatives. A constant Laplacian avoids a missing third-derivative assumption on $`g`$.

**Every Carleman product, lines 264–339 and 529–609.** Independently expanded the transformed differential operator and checked all twenty products in the appendix. The mass-leading products have coefficients $`-2`$ and $`+3`$, giving the positive coefficient $`1`$. Integrating the Laplacian product of the directional derivative once and then its Hessian term gives the displayed normal-square/tangential-square boundary signs and the positive directional-gradient square. The time/Laplacian product leaves only its boundary term because the weighted endpoint values vanish. The drift/Laplacian product has the displayed deformation-tensor error; the normal drift is zero. The time-weight and drift-weight products have their exact derivative factors. The potential product is

```math
\int[-s\lambda^2Wm\xi+\sigma s\lambda\xi(\nabla W\cdot\nabla\eta+W\Delta\eta)
 -(2\varepsilon)^{-1}\mathop{\mathrm{div}}\nolimits(WD)]w^2
 -\sigma s\lambda\int_{\Sigma}W\xi a w^2.
```

The extra potential is retained inside the mixed product, so it is not squared into an uncontrolled right-hand-side error. At the boundary the two weights and their tangential/time derivatives agree. Substituting

```math
\partial_\nu w_\sigma=(-\beta/\varepsilon+\sigma s\lambda\xi a)w
```

and summing signs gives exactly $`4\varepsilon s\lambda^2\beta a^2\xi+4\varepsilon s^2\lambda^2\beta a^2\xi^2+\mathop{\mathrm{div}}\nolimits_\Gamma(\beta D)`$ times $`w^2`$. The potential and tangential-gradient terms cancel; the time term integrates to zero because $`\beta`$ is autonomous. The bounded surface divergence is dominated by the two strictly positive terms. This is an actual Robin cancellation, not an imported Neumann cancellation.

**Bulk errors and observation, lines 342–445.** Choose $`\lambda`$ first to absorb the lower-$`\lambda`$ leading errors outside the smaller observation set. With that fixed parameter and $`s=K/\varepsilon`$, the remaining mass-error ratios are bounded by inverse powers of $`K`$; the terms $`\varepsilon s^2\xi^3`$ and $`s\xi^3`$ have ratios $`O(K^{-1})`$ and $`O(K^{-2})`$. Gradient errors relative to $`\varepsilon^2s\lambda^2\xi`$ similarly have fixed-$`\lambda`$ inverse-$`K`$ ratios. Only second derivatives of $`\eta`$ enter after the chosen integration order. Recovering the Laplacian from $`L_2`$ and weighting its square by $`(s\xi)^{-1}`$ gives the claimed bound: the potential-square ratio is $`O((\varepsilon s\xi)^{-4})`$, so it is bounded at this scale. The compactly supported observation cutoff and Young inequality absorb its local gradient with an arbitrarily small fraction of this Laplacian bound. Ordering the two weights leaves the positive-weight observation. On the middle third of the unit interval its weight is bounded below by an exponential of order $`e^{-C/\varepsilon}`$; on the full interval the weighted density is bounded above. Undoing the gauge introduces only its bounded oscillation divided by $`\varepsilon`$. The adjoint energy estimate transfers middle-interval mass to the initial time. Thus the fixed-time cost has precisely the required $`e^{K_o/\varepsilon}`$ scale.

**Uniform dissipation and control, lines 449–525.** The primary general-drift dissipation estimate is applicable to these exact adjoints. Autonomy translates the proposed backward ball flow into the source's flushing convention; halving the open-ball radius gives its closed-ball condition. Its positive exponential decay constant depends on the flushing radius/time and the fixed drift norm, and can be fixed before enlarging the ambient interval. Select an integer $`m`$ with $`m\delta_d>K_o`$, then fix the interval and its finite prefactor. Iterating over $`m`$ blocks and applying unit-interval observation at their end cancels the exponential loss with the correct time orientation. The resulting observation inequality applies uniformly to every longer terminal time by restriction. Riesz representation on the closure of adjoint observations supplies an $`L^2`$ control with the desired norm; transposed-form duality gives zero terminal state for every terminal test.

**Rough terminal data, lines 612–690.** The collar trace estimate and the Neumann Hessian identity give an $`H^2`$ estimate; smooth-data Neumann resolvent solutions and variational convergence extend it to weak Neumann functions. The exponential multiplier converts the original Robin condition into Neumann and preserves $`H^2`$ at each fixed viscosity. Averaging semigroup orbits against a smooth compactly supported positive-time kernel gives dense initial data with derivatives expressed by derivatives of the kernel, without presupposing orbit smoothness. Each of these averaged data belongs to $`H^1`$ because weak solutions are square integrable in time with values there. The cited strong-solution and continuity results then give continuous $`H^1`$ orbits; the equation and Robin estimate give continuous $`H^2`$ orbits and time derivatives. All product integrations above are therefore legitimate Sobolev Green identities. Endpoint weights eliminate all temporal boundary terms. Passing to general $`L^2`$ terminal data occurs at fixed viscosity with the already uniform constants, so no density limit and vanishing-viscosity limit are exchanged.

## Reference and ancillary-claim audit

All five entries are real and correctly identified. Their proof-critical hypotheses and version-specific locators were checked; no missing essential citation was found.

- Bárcena-Petisco, ESAIM COCV **27** (2021), 106, [primary PDF](https://www.numdam.org/item/10.1051/cocv/2021103.pdf), [DOI](https://doi.org/10.1051/cocv/2021103): title, author, year and article number match. The cited boundary-condition examples are context and are not used to infer a new theorem.
- Dier, [arXiv:1406.2884v2](https://arxiv.org/html/1406.2884v2): Theorem 1.1 states Lions' variational existence/uniqueness and continuity in $`H`$ for bounded coercive forms. The shifted form and its transpose satisfy those hypotheses. The manuscript does not mistakenly apply the later symmetric-form maximal-regularity theorem to its nonsymmetric drift form.
- Et-Tahri, Bárcena-Petisco, Boutaayamou and Maniar, [arXiv:2308.07497v1](https://arxiv.org/html/2308.07497v1): authors/title/version and Section 6's tangential-drift Carleman calculation confirmed. Its impossible boundary flushing issue is correctly distinguished from the strictly outward case.
- The same authors, Mathematical Methods in the Applied Sciences **48** (2025), 6531–6552, [DOI](https://doi.org/10.1002/mma.10693), [cited primary version](https://arxiv.org/html/2412.16660v1): Proposition 4.7(1), equation (51), gives exactly the general-drift dissipation used. Proposition 4.5 specifies the decay dependence. Propositions 3.6 and 3.9 supply fixed-viscosity $`H^1`$ continuity and strong solutions with the asserted drift regularity. The gradient-only control theorem is not being reused as a general-drift theorem.
- Nardi, L'Enseignement Mathématique **60** (2014), 421–435, [publisher](https://ems.press/journals/lem/articles/13077), [DOI](https://doi.org/10.4171/LEM/60-3/4-9), [cited arXiv v4](https://arxiv.org/html/1302.4103v4): metadata match. Theorem 3.1 gives the compatible Neumann Poisson solution; Theorem 5.2 gives the $`\Delta-1`$ Neumann resolvent used in approximation. The smooth domain and $`C^{1,1}`$ boundary datum meet its $`C^{2,1/2}`$/Hölder requirements.

## Decision

The paired Carleman argument, its uniform scaling, and its rough-data justification establish the full target. No proof gap remains after reconstructing the mixed products and dependency order. Recommend accepting the package and recording **Solved**, with this independent AI review disclosed. No Lean status is justified. Typesetting and package hash checks are separate coordinator checks.


## Document and package checks

The coordinator parsed and rendered the supplied ten-page PDF. This reviewer independently inspected the all-page contact sheet: the document has no blank, clipped or missing page content, and its displayed statements and proof structure agree with the reviewed source. The package README, target comparison and AI-use disclosure were read and agree with the manuscript and exact target scope. No separate executable proof or numerical certificate is a mathematical premise. Hash and repository integration checks belong to the coordinating review.
