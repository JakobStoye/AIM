# AIM 554: second independent argument audit of PR #84

**Date:** 2026-10-13. **Reviewer:** OpenAI Codex, a separate maintainer-review context from the primary audit. This is an independent AI argument audit, not human or Lean verification.

**PR:** [#84](https://github.com/MColbrook/AIM/pull/84). **Audited head:** `5461765e0fc13968ceb5767db690615ffbe1d2e2`. **Target revision:** `c9929805cece044705abaaebe1cebddac1ba11a6`.

**Direct proof:** [Submitted source](https://github.com/MColbrook/AIM/blob/5461765e0fc13968ceb5767db690615ffbe1d2e2/research/solutions/554-stieltjes-rational-asymptotic-constant/paper/main.tex).

The complete 541-line manuscript, target, package scope statements, and all eight PDF pages were read. The proof was reconstructed before consulting the primary review report. The particular points stressed were the weighted Blaschke constant, applicability of the multipoint interpolation theorem to the constructed scheme, and whether the final alternation comparison really covers the full unrestricted real rational class.

**Conclusion:** The second reconstruction supports **Solved, affirmative** for the exact fixed-interval, fixed-exponent target. No substantive gap, false proof-critical step, or required mathematical correction was found. The argument does not assume the desired absolute minimax constant from a relative-error or L1 theorem.

## 1. Weighted construction and its sharp constant

The disk interval is $`I=[u,v]\subset(0,1)`$. The annulus map has inner radius $`\rho`$. Its real symmetry makes the two slit sides the two halves of the inner circle. Analytic reflection away from the endpoints, followed by the endpoint square-root chart, gives the holomorphic doubled inverse with involution $`\zeta\mapsto\rho^2/\zeta`$. At an endpoint the inverse is quadratic; the sheet interchange changes the sign of the square-root chart. Thus an invariant analytic expression in the doubled parameter descends across the slit and has a removable endpoint singularity. This is sufficient for the later argument principle and factorization; merely continuing a function on the slit complement would not have sufficed.

The potential $`-\log|\Phi|`$ has boundary values zero on the unit circle and $`-\log\rho`$ on the slit. Its slit flux, transported to the annulus, is angular measure with total flux $`2\pi`$. Consequently the pushforward of $`d\theta/(2\pi)`$ is the unit disk-Green equilibrium measure. There is no extra factor of two from the two sides: the full inner circle already covers both sides once. This also checks the measure used in the geometric mean (source lines 96-129).

For $`W=e^P`$, let $`g=\log C-P\circ Z`$ on the inner circle. Its mean is zero and it is even and analytic. The Laurent coefficients in source lines 155-160 give a normally convergent single-valued $`F`$ on a neighborhood of the closed annulus. Direct substitution yields zero real part on the outer circle and $`\mathop{\mathrm{Re}}\nolimitsF=g`$ on the inner circle. The denominators $`\rho^j-\rho^{-j}`$ are nonzero. Exponential decay of the Fourier coefficients gives the required normal convergence, including a fixed neighborhood at both boundaries. The zero mean is exactly what removes a non-single-valued logarithmic term.

On the inner circle the reflection identity for $`F`$ agrees with complex conjugation because its Laurent coefficients are real and $`P\circ Z`$ is real there. It therefore gives the same analytic continuation, not an unrelated second boundary function. The continued $`A=e^F`$ stays zero-free and bounded on the closed doubled annulus. The polynomial weight keeps $`P\circ Z`$ bounded at the reflected outer boundary.

For

```math
H_m(\zeta)=\zeta^m A(\zeta)+\rho^{2m}\zeta^{-m}A(\rho^2/\zeta),
```

invariance gives a holomorphic disk function. On the outer circle the first term has modulus one and the second is uniformly $`O(\rho^{2m})`$. Its winding number is $`m`$: the annulus map has boundary degree one, the exponential factor has winding zero, and the smaller second term cannot change it. The argument principle therefore gives precisely $`m`$ disk zeros, counted with multiplicity.

On the slit, independently combining the conjugate terms gives

```math
e^{P(Z(\rho e^{i\theta}))}h_m(Z(\rho e^{i\theta}))
 =2C\rho^m\cos(m\theta+\psi(\theta)).
```

The phase is real, has bounded derivative independent of $`m`$, and is zero at both endpoint angles. For large $`m`$ the total phase increases strictly from zero to $`m\pi`$. This yields exactly $`m`$ simple interior zeros and $`m+1`$ alternating values of magnitude $`2C\rho^m`$. They account for all disk zeros. Thus the factorization $`h_m=B_mO_m`$ has no omitted complex zeros. Applying the maximum principle to $`O_m`$ and its reciprocal gives $`|O_m|=1+O(\rho^{2m})`$ uniformly. It is positive on the interval, since both factors are real there, the quotient is continuous and nonzero, and both are positive at the right endpoint. Hence the factorization preserves the alternation signs and the claimed sharp amplitude (lines 171-227).

The lower bound for competing degree-$`m`$ products is valid. At the alternating points any strictly smaller weighted norm forces $`m`$ distinct zeros of the difference. Its numerator $`N=pq^*-qp^*`$ has degree at most $`2m`$ and is anti-reciprocal. Each interval zero gives a distinct reciprocal zero outside the disk, and $`N(1)=0`$ gives another distinct root. A nonzero polynomial of that degree cannot have $`2m+1`$ distinct roots. This argument permits repeated or endpoint zeros in the competitor. If the numerator vanishes identically, the two products are identical and cannot have strictly different norms.

For general positive continuous weights, approximating $`\log W`$ by a real polynomial changes weighted norms and geometric means by multiplicative $`e^{\pm\varepsilon}`$. The two changes together explain the $`e^{\pm2\varepsilon}`$ tolerance. The submitted Bernstein estimate follows from the binomial second moment and splitting at distance $`\delta`$. Fixing this polynomial before taking the degree limit is essential and is done explicitly. The zero angles differ from midpoint angles by $`O(1/m)`$, so their empirical measures converge. All claims of Lemma 2, including the sharp leading factor 2, follow (lines 229-260).

## 2. Radius and geometric-mean normalization

The half-plane identity in line 267 was recomputed algebraically. The kernel is unchanged under $`s\mapsto\alpha\beta/s`$, which also preserves $`[\alpha,\beta]`$. Uniqueness of its unit equilibrium measure implies inversion symmetry. Applying it to $`\log s`$ gives

```math
\int\log s\,d\lambda_J=\tfrac12\log(\alpha\beta).
```

The weight $`s^{-2\gamma}`$ therefore has geometric mean $`(\alpha\beta)^{-\gamma}`$, equal to $`(ab)^{-\gamma/2}`$ when the interval is $`[\sqrt a,\sqrt b]`$. This is the absolute-error weight and is retained throughout.

For the unweighted degree-$`2n`$ product, $`B(s)=P(s)/P(-s)`$. The comparison

```math
v_n(s^2)=s\frac{P(-s)+P(s)}{P(-s)-P(s)}
```

has an even numerator of degree at most $`2n`$ and an odd denominator of degree at most $`2n-1`$. Canceling its factor $`s`$ gives type $`(n,n-1)`$ in $`x=s^2`$. The denominator is nonzero on the target interval because $`\|B\|<1`$ for large degrees. Its signed relative error is $`-2B/(1-B)`$, whose factor is positive in magnitude and $`2+o(1)`$ uniformly. The $`2n+1`$ alternating values therefore give the relative minimax asymptotic $`4\rho^{2n}(1+o(1))`$ by a difference-numerator count of degree at most $`2n-1`$.

The actual Braess-Hackbusch Theorem 4.2 uses this same relative type, interval, modulus, and asymptotic factor 4. It identifies $`\rho=e^{-\mu(k)}`$ by taking roots. This use fixes the radius only; it does not assert the absolute fractional-power result under review (lines 279-308). [Primary revised preprint, Section 4.1](https://files-www.mis.mpg.de/mpi-typo3/preprints/2024/preprint2024_10.pdf).

## 3. Interpolation existence, degree and theorem applicability

The Möbius change has $`c=a/2`$ and sends the fixed positive interval to a compact interval strictly to the right of 1. The Jacobi representation was recomputed using $`v=(1-t)/(1+t)`$: its transformed integral is precisely $`\int_0^\infty v^{\gamma-1}/((z-1)+(z+1)v)\,dv`$, with no missing factor 2. The beta integral gives the stated Markov function, and both endpoint exponents are integrable.

With all $`2n`$ transformed nodes real and greater than 1, $`V`$ is positive on the cut. Its orthogonality measure is positive and integrable. The Gram construction gives a real degree-$`n`$ denominator whose roots are all simple and interior. The sign-changing-root argument proves this location directly. The polynomial difference quotient and the orthogonality identities remove all numerator coefficients of degree at least $`n`$. The resulting rational function has the exact interpolation and infinity conditions needed for the cited multipoint theorem.

Transferring back does not increase the numerator degree to $`n`$: the leftover factor $`x-c`$ in the composition cancels the $`1/(x-c)`$ in $`z-1`$. Thus the original type is $`(n-1,n)`$. Every constructed pole is strictly negative, so the constructed approximant is admissible. These pole restrictions are only a property of the constructed upper-bound approximant, not a restriction later imposed on competitors (lines 354-384).

The actual arXiv v1 Definition 1 and Theorem 2 were checked. For this scheme the cut boundary products have modulus one; off the cut each disk factor is uniformly smaller than one on any fixed compact set, giving geometric decay; the zeros stay uniformly separated from the cut; and the empirical node measures converge. The fixed residual density is constant and smooth, and the endpoint powers lie in the permitted range with $`s=3`$. The theorem's error is multiplicative relative to its product, locally uniformly off the cut, so it applies at the entire fixed evaluation interval, including the varying alternation points. [Baratchart-Yattselev, arXiv:0911.3850v1, pp. 5-7](https://arxiv.org/pdf/0911.3850v1).

The normalized Szego factor and geometric mean were recalculated using the odd cosine coefficients of the endpoint logarithms. On the positive transformed interval,

```math
G=\sin(\pi\gamma),\qquad
\frac{c^{-\gamma}(z-1)}{\sqrt{z^2-1}}S(z)^2=x^{-\gamma}.
```

Rewriting each source factor through $`\eta=1/(z+\sqrt{z^2-1})`$ gives $`(\eta-\eta_j)/(1-\eta\eta_j)`$ with the stated sign. The half-plane identity then supplies the product in line 349. There is no exponent shift, branch mismatch or extra factor of $`c`$ (lines 386-452).

## 4. Final minimax comparison and quantifiers

For each fixed tolerance, the weighted construction supplies distinct nodes and $`2n+1`$ alternating weighted values. The interpolation formula has a positive multiplier for large $`n`$, because $`\sin(\pi\gamma)>0`$ and its uniform remainder tends to zero. It therefore supplies alternating **absolute** errors of size at least $`4(ab)^{-\gamma/2}\sin(\pi\gamma)e^{-2\varepsilon}\rho^{2n}(1+o(1))`$, as well as the corresponding upper norm bound.

If any admissible real rational function had error below all those magnitudes, its difference from the constructed interpolant would change sign between successive points. Both rational functions are continuous on the whole interval, so there are $`2n`$ distinct interior zeros. The difference numerator has degree at most $`2n-1`$ and the denominators are nowhere zero there. This excludes the competitor, regardless of its lower actual degrees or any poles outside the interval. Identical rational functions cannot improve on the displayed error. Thus this is a universal lower bound, not just a lower bound for Stieltjes approximants.

The degree limit is taken with interval, exponent, and polynomial weight approximation fixed. Only afterwards is the tolerance sent to zero. The lower and upper constants therefore converge to exactly the target constant. No uniform claim at $`\gamma=0,1`$, at a branch point, or on an unbounded interval is required or used (lines 456-499).

## 5. References, presentation, and scope

All four submitted bibliography entries were checked against primary publisher/author evidence. [Oxford's article record](https://academic.oup.com/imrn/article-abstract/2010/22/4211/735676) confirms the BY authors, title, 2010 issue 22, pages 4211-4275 and DOI. [Springer's BH record](https://link.springer.com/article/10.1007/s00211-025-01523-1) confirms volume 158, 2026, pages 455-490. [The BPS author PDF, Section 3](https://math.vanderbilt.edu/saffeb/texts/193.pdf) and [publisher record](https://link.springer.com/article/10.1007/BF03321004) confirm the geometry and the stated volume/year/pages; its L1 conclusions are not used as uniform minimax conclusions. [Springer's Bak-Newman record and contents](https://link.springer.com/book/10.1007/978-1-4419-7288-0) confirm third edition, 2010, and Section 7.2 on reflection across analytic arcs. The local endpoint/descent argument was checked directly above. No missing proof dependency or necessary bibliography correction was identified.

All eight rendered PDF pages agree with the audited source and show the full construction, interpolation checks, final proof, bibliography and AI-use statement. No clipping, blank page or unresolved reference was observed. The README and target comparison consistently claim the fixed-parameter absolute target and disclose AI assistance; they do not claim human or formal verification. This second review made no changes to the submitted solution, GitHub PR, or catalogue.
