# AIM 639: second independent argument audit of PR #89

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, a separate maintainer-review context from the primary audit; independent AI argument audit, not human or Lean verification.

**PR:** [#89](https://github.com/MColbrook/AIM/pull/89). **Audited head:** `7c5a97db1d7f13732cdfe8900e14a9e52ab6d64b`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Submitted standalone source](https://github.com/MColbrook/AIM/blob/7c5a97db1d7f13732cdfe8900e14a9e52ab6d64b/research/solutions/639-wis-fractional-euler-rate/paper/main.tex).

The complete 971-line manuscript, exact target, ancillary scope statements, bibliography and all twelve rendered PDF pages were read. This second check independently reconstructed the signed quadrature, delayed fractional conditioning, Brownian time reversal, and localization around zero. The submission's own AI checks and the separate primary maintainer audit were not used as mathematical premises.

**Conclusion:** This reconstruction supports **Solved, affirmative** for the exact fixed terminal WIS Euler target. No substantive gap, false proof-critical step, incorrect stochastic independence assumption, or required mathematical correction was found. The proof covers autonomous globally Lipschitz drifts without higher derivatives, all fixed H in (0,1), arbitrary real initial values, nonzero drift at zero and zero crossings. It does not claim a supremum-in-time solution error, an approximated-noise rate, or uniform constants as H approaches the Brownian endpoint.

## Exact WIS representation and common estimates

The actual ELS arXiv v2 formulas (3.6)-(3.9) and (3.12)-(3.13) were checked. For fixed terminal T they give precisely the submitted deterministic correction, transformed ordinary differential equation, common terminal divisor J, and prescribed recurrence. The auxiliary Z process depends on this chosen horizon; the paper uses it to represent X(T), not to claim an incorrect identity for all intermediate X(t) with the same horizon. Hence using an equivalent continuous fractional Gaussian realization preserves the required joint terminal law. [Primary ELS text](https://arxiv.org/pdf/2404.07013v2).

For each fixed noise value the transformed F has exactly the original deterministic state-Lipschitz constant L. Its growth is bounded by $`L|z|+|a(0)|J`$. Moment bounds and time increments for both the exact and Euler states follow from ordinary/discrete Gronwall and Minkowski, with Gaussian exponential moments controlling J. The terminal singularity in c-prime when H is below one-half is handled through total variation, not an unjustified bounded derivative (source lines 183-293).

Writing $`a_1=a-a(0)`$ and dividing by the nonzero state in logarithmic coordinates is legitimate: $`b_\sigma(q)=a_1(\sigma e^q)/(\sigma e^q)`$ is bounded by L and has global Lipschitz constant at most 2L, as the displayed difference calculation proves. Thus $`F_1=z b_\sigma(\log|z|-c+\beta b)`$ has noise/c increments proportional to $`|z|`$, and is zero at z=0. The separately retained constant-drift term has exponential noise weights. No derivative of a is used.

The heat-convolution derivative bounds are correct. Subtracting a constant inside the zero-integral Gaussian derivative kernels exploits the noise-variable increment bound. Gaussian scaling gives the first derivative of order one and the variance derivative of order $`v^{-1/2}`$, including the exponential weights for bounded v. For the difference of two states, the global state-Lipschitz property gives an unweighted bounded function, yielding the sharper mixed estimates $`|z-z'|v^{-1/2}`$ and $`|z-z'|v^{-1}`$. Derivatives are taken in the smoothed noise variable, not in the original nondifferentiable drift (237-268).

## Fractional realization and prediction

The two-sided moving-average kernel is square integrable for every H in (0,1) excluding the separately treated one-half value. Its point singularities have squared exponent greater than minus one and its negative-time tail has integrable squared decay. Translation, dilation, and normalization give stationary increments with variance $`|t-s|^{2H}`$, hence exactly the prescribed covariance. Large Gaussian moment orders provide a continuous version.

Conditioning is with respect to the underlying Brownian past including negative times, rather than falsely treating fractional Brownian increments as independent. The innovation at r>s is independent of this filtration and has variance $`q_H(r-s)^{2H}`$. The conditional mean derivative estimate follows by integrating the squared deterministic kernel derivative on the past half-line. In particular, changing a mean over a step costs $`h\ell^{H-1}`$ once the conditioning time is separated by a distance comparable with ell (298-340).

The prediction lemma also survives nongrid conditioning times. The Euler state at the first grid endpoint after s is already measurable at s because that completed Euler step uses the preceding grid noise. Freezing this state and the noise at s, while retaining the deterministic c schedule, gives a measurable predictor. State increments contribute an integrated order two term and noise increments an integrated order $`1+H`$ term. Conditional contraction yields the displayed $`(t-s)^{1+H}`$ prediction error and its tower-property difference bound (344-377).

## Signed quadrature and exact fractional exponents

The local conditional increment uses the past time $`v=(s-\ell)\vee0`$. Its two size bounds are

```math
b_h(\ell)=\min\{\ell h^H,h\ell^H\}.
```

The first is the direct integrated increment estimate. For ell at least 2h away from the initial interval, all grid evaluations remain at least ell/2 after v. The conditional mean change and variance change are respectively of orders $`h\ell^{H-1}`$ and $`h\ell^{2H-1}`$. Applying the first heat derivative and the $`\ell^{-H}`$ variance derivative gives the same order $`h\ell^{H-1}`$ for both terms; integrating gives the second bound. The initial interval is handled by its first 2h segment and then the integrable kernel $`r^{H-1}`$. Small lengths use the direct bound. Higher moments control all random state and exponential factors by Holder without requiring their independence (398-431).

The three-point conditional defect is genuinely smaller. The tower property cancels the terms with the same predicted state. For small scales the deterministic 2L Lipschitz constant and the prediction difference give $`\ell^{2+H}`$, bounded by a constant times $`h\ell^{1+H}`$. For larger scales, both parent and child predictions are measurable at the child's past conditioning time, and the grid evaluations are separated from it by at least ell/4. Applying the mixed heat estimates to their bounded state difference gives integrand order $`h\ell^H`$; its integral has order $`h\ell^{1+H}`$. On the initial dyadic interval all three conditioning times are zero and the defect is exactly zero (433-463).

At each fixed dyadic scale the defect associated with interval i is measurable at the **start** of that interval, since that is the latest child's conditioning time. Subtracting its conditional expectation at the preceding interval's start creates an actual martingale-difference sequence. Thus the square-root summation estimate is not an unsupported deletion of correlated cross terms. The displayed elementary fourth-moment proof uses L2 orthogonality of the martingale increments and conditional Jensen for partial sums, and gives the stated bound. Together with the defect mean this proves

```math
\|S_{j+1}-S_j\|_4
 \le C\sqrt{t/\ell_j}\,b_h(\ell_j)+Cth\ell_j^H.
```

The conditional sums converge in L4 to the original signed integral: state prediction costs order $`\ell^{1+H}`$ after summing, and noise innovations have variance at most a constant times $`\ell^{2H}`$. At grid noise times before the conditioning time the projection cost is zero. The given estimates therefore justify the limiting integral, not just a formal telescoping series (465-501).

For coarse scales, the martingale term is $`h\sqrt t\sum\ell_j^{H-1/2}`$; for fine scales it is bounded by $`C\sqrt t h^{H+1/2}`$. For H below one-half the coarse geometric sum is controlled by the scale nearest h; above one-half it is controlled by its largest scale. The conditional-mean terms sum to order h. This gives exactly the claimed exponents without an epsilon loss. The constants may diverge near one-half, which is permitted because H is fixed. The critical Brownian logarithm is explicitly not used to claim order one (504-521).

## Brownian quadrature for a merely Lipschitz function

For a smooth Lipschitz test function, integrating its increments over cells gives the deterministic sawtooth-weighted differential, with the correctly stated partial-cell correction. The sawtooth is bounded by h. Its differential against f(W) is the average of the forward Ito integral and the right-endpoint backward integral: the second-derivative corrections cancel with opposite signs. Deterministic bounded variation of the weight adds no quadratic covariation.

The reverse process $`Y_u=W_{d-u}`$ in its natural reverse filtration is a Brownian bridge toward zero. Its stated conditional transition gives the martingale obtained by adding $`\int Y_u/(d-u)\,du`$ to $`Y_u-Y_0`$. Quadratic variation is u; Levy's characterization supplies Brownian driving noise. The finite-variation term remains integrable at the terminal reverse time, because its Lp norm is bounded by the integral of $`(d-u)^{-1/2}`$.

Reversal converts the backward integral into a martingale increment and this bridge drift. Both have maximal Lp size at most $`C_p [f]_{\rm Lip}h\sqrt d`$. The partial-cell correction obeys the same bound by the Brownian maximum. Gaussian mollification has no increase of the Lipschitz constant and converges uniformly, so the estimate extends to every globally Lipschitz f. This does not require f to have a classical second derivative (534-607).

For a bounded progressive drift in logarithmic coordinates, Girsanov applies. Powers of the forward and inverse densities have uniformly controlled moments when $`M^2d`$ is bounded, and Holder transfers the Brownian estimate at a higher exponent. A grid stopping time with its block length and drift parameters known at its start has the same conditional estimate. The proof conditions on its finitely many possible grid values and uses independent **Brownian** future increments, which is appropriate in this section (610-643).

## Brownian zero-crossing and localization stress test

When a(0)=0, the transformed exact state remains of fixed sign unless it is identically zero. Its absolute value and variation have deterministic bounds. The logarithmic SDE has bounded drift, and integration by parts with the primitive of the Lipschitz b quadrature yields order h. State/c freezing adds only order h. When both initial state and a(0) vanish, both exact and numerical states are identically zero (645-681).

For nonzero a(0), reflection allows a(0)>0. On $`E_K=\{\max(1,\sup J,\sup J^{-1})\le K\}`$, Gronwall bounds $`\sup|Z|`$ and $`\sup|Z'|`$ by constants times K. Inside the specified band around zero, the positive constant-drift contribution dominates $`L|Z|`$, so $`Z'\ge a(0)/(2K)`$. This is a genuine monotone traversal: a continuously differentiable path cannot reenter the band downward through an edge at which its derivative is positive. Each positive/negative small annulus is traversed at most once, and its occupation time has the asserted $`CK\varepsilon`$ bound. Thus no sign-preservation assumption is imposed on the full solution (701-722).

For small h relative to K, outer blocks have known-at-start lengths proportional to $`\varepsilon^2/K^2`$. Their floor is uniformly positive, with the stated lower length except for the one final truncation. The local variation bound keeps Z within its expanded annulus and away from zero, including at the intermediate nongrid times. Clipping the singular logarithmic drift agrees with the original drift there on E_K and produces a globally Lipschitz bounded drift. Its bound is $`CK/\varepsilon`$, whose square times the block length is uniformly controlled. Strong uniqueness gives agreement of the clipped and original local processes on E_K. The conditional quadrature bound is therefore $`C_p h\varepsilon/K`$ for the primitive, and summation by parts gives block error $`C_p h\varepsilon^2/K`$ (724-791).

The local freezing comparison is also valid: either use the deterministic state-Lipschitz bound directly, or compare the two logarithmic arguments using that both Z values are comparable with epsilon. In either form, the factor Z in F1 removes any logarithmic derivative singularity, giving the asserted $`CKh`$ cost.

For small annuli, occupation time divided by the lower block length gives at most $`CK^3/\varepsilon`$ blocks, with one harmless final truncation. Their norms sum to $`C_phK^2\varepsilon`$ plus the final-block term. These bounds are summable over the dyadic annuli. Large blocks have length at least a constant times $`K^{-4}`$, so there are at most $`CK^4`$ of them, each costing at most $`C_phK`$.

The event E_K is not measurable at the block start, but no independence from it is needed. For a fixed annulus, enumerate its adapted starts as grid stopping times. On E_K only the first deterministic count bound can occur; each event-masked contribution is pointwise dominated by a fixed multiple of the clipped primitive, whose conditional norm estimate is uniform. For large annuli retain only the known-at-start condition $`\varepsilon\le C_ZK`$. Applying these conditional estimates and Minkowski is sufficient. This handles the random number of blocks correctly (794-819).

Cells starting near zero are treated without logarithms. All their times stay in the monotone band, with total length at most $`CK\delta`$. The F1 noise coefficient is proportional to $`|Z_{\eta(s)}|\le\delta`$, so the contribution is bounded by $`CK^3h D_h`$, retaining the Brownian increment maximum $`D_h`$. Its Lp bound $`C_p\sqrt{h\log(2n)}`$ is uniformly bounded for fixed T. Consequently its logarithm causes no rate loss here: it multiplies an already order-h factor (821-833).

The polynomial localization estimate follows for every n; larger h are covered by the direct square-root-h increment bound and $`h>cK^{-4}`$. Gaussian tails for the Brownian supremum imply a Gaussian tail in log K for the localization variable. Holder at exponent 8 on dyadic K shells makes the polynomial factor summable and produces the desired unconditional L4 order-h bound. No exponential-of-K cost is hidden in Girsanov (834-857).

## Terminal stability and target closure

The constant-drift component is separately a multiple of J. Its ordinary Brownian Ito differential has drift coefficient $`-\alpha+\beta^2`$, as stated, and deterministic sawtooth weighting plus maximal martingale bounds yields order h. Freezing c at grid times changes this integral by only order h.

For non-Brownian H, the proof uses the Euler-state signed quadrature already established. For the Brownian case it uses the exact-state residual. In both cases state stability has the original deterministic constant L. Moment increment and total-variation bounds give the remaining order-h terms and lead to the stated discrete Gronwall inequality at every grid prefix. Holder with the common terminal $`J_T^{-1}`$ converts the L4 transformed-state estimate to the exact target's L2 terminal estimate. Deterministic noise coefficient zero, homogeneous drift zero, constant drift, zero initial values and the finitely many large steps are all covered. The approximation uses the original recurrence and exact samples from the same path throughout (860-925).

## Reference and ancillary-content check

All six bibliography entries were checked against primary text/records. The proof-critical dependencies are the exact ELS terminal construction and standard Gaussian/Wiener, Ito, Levy, Girsanov and maximal-martingale tools; the additional quadrature and localization argument is supplied in the manuscript.

- **ELS:** The actual [arXiv v2](https://arxiv.org/abs/2404.07013v2) has the cited hypotheses and formulas. [Oxford's advance-article record](https://academic.oup.com/imajna/advance-articles?login=false&page=1) confirms the title, 2026 journal record and DOI drag055. The weak existing rate and sharper conjecture are correctly distinguished.
- **Butkovsky-Dareiotis-Gerencser:** The [publisher record/text](https://link.springer.com/article/10.1007/s00440-021-01080-2) confirms title, authors, volume 181 (2021), pages 975-1034 and DOI. The neighboring additive result has the stated nearly optimal rate under its own Holder assumptions; it is not substituted for the present result.
- **Moritoki:** The actual [v1 record and Theorem 1.1](https://arxiv.org/abs/2607.24166v1) confirm the author/title, 2026 version, order one above one-half, and epsilon loss at/below one-half for the additive Lipschitz problem.
- **Altmeyer:** The actual [v4](https://arxiv.org/abs/1706.03418v4), revised 31 January 2021, has the cited Theorems 4-5 on unperturbed fractional occupation quadrature under Sobolev assumptions. The manuscript accurately keeps these distinct hypotheses.
- **Kloeden-Rosa:** The actual [v8](https://arxiv.org/abs/2306.15418v8), revised 17 October 2025, confirms the title/authors and semimartingale RODE result, and its Appendix A includes the linear fractional example. It is contextual rather than a proof of random-state WIS quadrature.
- **Chafai:** The [actual official notes](https://djalil.chafai.net/docs/M2/m2-stochastic-calculus-course-2020-2021.pdf) show the stated 2020-2021 course and corrected compilation date 7 December 2025. Exact locators 3.6.3, 3.7.1, 7.1.1, 7.2.1, 7.5.1 and 7.7.1 were checked. Their hypotheses apply to the constructed Wiener integrals, smooth mollified test functions, reverse martingale and bounded progressive clipped drifts. Conditional versions at grid stopping times are justified in the submitted proof.

No missing proof dependency or bibliography correction was identified. Every PDF page agrees with the audited source, including the fractional conditioning, Brownian crossing argument, final theorem proof, references and AI disclosure; no clipping, blank page or unresolved reference was observed. The package README, target comparison and reproduction record match the theorem's terminal fixed-data scope and do not claim human or formal verification. This second check made no solution-package or GitHub changes.
