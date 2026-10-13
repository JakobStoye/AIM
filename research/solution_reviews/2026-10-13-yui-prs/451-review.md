# AIM 451 — independent review of PR 69

- Date: 2026-10-13; submission: [PR 69](https://github.com/MColbrook/AIM/pull/69), Kaiwen Jin.
- Reviewed head: `c27cd2a4b9a1f4a11d0f4cda8b33b233695260da`.
- Proof: [PDF](../../solutions/451-mixed-sobolev-counterexample/paper/main.pdf), [source](../../solutions/451-mixed-sobolev-counterexample/paper/main.tex).
- Reviewer: independent Codex agent, separate from drafting/self-review; AI natural-language mathematical audit. No human or Lean certification.
- Verdict: **Solved**, negative answer: a smooth two-dimensional counterexample sequence disproves the universal estimate.

## Exact target

The counterexample uses the stipulated unit-volume torus, inhomogeneous half-order Sobolev norms, Euclidean vector energies and infimum sum norms. Each scalar function is real, smooth and mean zero. A failure in dimension two disproves the statement quantified over every dimension at least two. The proof bounds the right **sum norm** and tests every decomposition of the left sum norm, rather than showing only the failure of a stronger separate-norm inequality.

## Complete independent construction audit

The finite nested equal-interval partitions make the signs independent with the required stationary initial law. The reflected walk's transition matrix is symmetric, so uniformity persists. Its boundary drift has squared $`L^2`$ energy $`J\beta^2/[2(2M+1)]\le1/4`$. Its centered sign sum has norm one. Pairing that sum with each martingale increment removes every earlier/later independent sign and keeps its own positive average. Telescoping the bounded walk gives the divergent total pairing $`-\sum\langle a_M,e_j\rangle\ge\sqrt M/2-1`$.

The radial annuli are disjoint. The first field component telescopes to a convex combination of adjacent bounded walk values; the primitive bounds control the second component on each annulus. The full field is uniformly bounded despite the number of scales. Differentiation for divergence cancels the initial and martingale terms, leaving precisely $`f_M=\sum\alpha_je_j`$. The primitive functions are periodic because their increments have zero integral.

Recomputed the normal Fourier transform $`\widehat\alpha_t(n)=i2\pi nt\widehat\eta(2\pi nt)`$. Its small/large-frequency bounds imply the cross-scale Gram sum is $`O(t/s)`$ when $`t\le s`$. Splitting at $`1/s`$ and $`1/t`$ gives the displayed powers; the final range is even smaller. Dropping the tangential frequency from the negative Sobolev denominator is a valid upper bound. Parseval in that variable and the summable geometric row sums therefore bound $`\|f_M\|_{H^{-1/2}}`$ uniformly using only the already bounded total drift energy. No tangential orthogonality or false independence of boundary drifts is required.

The distributional sheet potential has the displayed nonzero Fourier coefficients of $`\Delta^{-1}\mathop{\mathrm{div}}\nolimits`$, is mean zero, and has a uniformly bounded $`L^2`$ norm by summing the normal frequencies. Differentiating the periodic Green function gives its positive-half Poisson representation with the correct sign. The remainder operator is $`O(x)`$ in $`L^2`$. The Poisson approximation of each piecewise constant drift is $`O(\beta\sqrt{x/h_{j-1}})`$; the adjacent scale ratio makes the summed error $`O(M^{-1})`$. Oddness of both normal factors and their signed annular integrals gives the divergent scalar pairing with $`f_M`$.

For each finite $`M`$, positive Poisson smoothing produces a real smooth flux with $`L^1`$ norm at most one. The complementary Fourier projection has uniformly bounded $`H^{-1/2}`$ norm: its normal sum is at most $`3/(2\pi)`$ times the tangential $`L^2`$ energy. Thus the gradient is explicitly decomposed into the required $`L^1`$ and $`H^{-1/2}`$ terms. Smoothing converges to the sheet potential in $`L^2`$ with $`M`$ fixed. Choosing its scale only after fixing $`f_M`$ preserves the divergent pairing; no uniform smoothing rate is asserted.

Finally $`f_M=\mathop{\mathrm{div}}\nolimitsZ_M`$, with both its negative-Sobolev norm and the bounded field norm uniformly controlled. Fourier duality bounds its pairing with any $`H^{1/2}`$ component; integration by parts bounds its pairing with any $`W^{1,1}`$ component. Periodic mollification justifies this for nonsmooth decompositions. Taking the infimum yields the divergent left sum norm. This closes the precise counterexample, not just a finite-frequency numerical observation.

## All references and ancillary statements

- Bourgain–Brezis, JAMS **16** (2003), 393–426, [author PDF](https://sites.math.rutgers.edu/~brezis/PUBlications/171-J.pdf): authors/title/pages match; equation (1.16), p. 397, is the stated mixed potential estimate.
- Brezis, Rendiconti Lincei **34** (2023), 307–335, [publisher](https://ems.press/journals/rlm/articles/13272471), [author PDF](https://sites.math.rutgers.edu/~brezis/PUBlications/234.pdf): metadata confirmed. Open Problem 7.1 asks this exact sum-norm estimate; it is correctly distinguished from its weaker Lebesgue analogue.
- Guillemin, MIT 18.117 notes, spring 2005, [primary PDF](https://math.mit.edu/~vwg/classnotes-spring05.pdf): actual notes and torus Fourier material match; changing period gives the stipulated convention.
- Tao, *An Introduction to Measure Theory*, AMS (2011), [author version](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-126-tao5-measure-book.pdf): actual book/version confirmed. Fubini is applied only to integrable fixed-scale expressions or nonnegative Fourier estimates.
- Hunter, PDE notes chapter 3, [primary PDF](https://www.math.ucdavis.edu/~hunter/pdes/ch3.pdf): the weak-derivative mollification result justifies periodic $`W^{1,1}`$ approximation in the final integration by parts. No new nonstandard claim is delegated to this citation.

All five entries are real and correctly identified; no missing proof-critical source was found. The novel construction and every quantitative estimate were reconstructed above.

## PDF and decision

Coordinator parsed/rendered all six pages. Independently inspected the full contact sheet: theorem, reflected-walk construction, Fourier estimates, smoothing, dual conclusion and bibliography are complete and unclipped. Recommend accepting the package and marking **Solved**, with **counterexample/negative** outcome and independent AI review recorded. Do not describe the estimate as proved affirmative or imply Lean verification.


The package README and target comparison, including their AI-use disclosures, were also read. Their mathematical scope agrees with the manuscript and the original target; they introduce no separate executable proof or numerical certificate as a premise. Package hashes and repository integration are separate coordinating checks.
