# Target comparison for AIM problem 518

**Target revision:** [MColbrook/AIM, c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/518-kdv-integrator-logarithmic-loss.md).  
**Submitted result:** Kaiwen Jin, *Removing the logarithmic loss in the Li-Wu KdV integrator*, Theorem 1; see [PDF](paper/main.pdf) and [source](paper/main.tex).  
**Claim:** the affirmative alternative of the full stated problem. Independent mathematical review is requested.

This comparison uses the pinned public problem and the submitted manuscript.
It is a statement and proof-location map, not an independent proof review.

## Statement and quantifiers

For every T > 0, 0 < gamma <= 1 and R > 0, Theorem 1 asserts the existence
of C and tau_0 depending only on T, gamma and R, such that every real,
mean-zero u_0 in H^gamma(\mathbb T) with norm at most R satisfies

```math
\max_{0\le n\le L}\|u(n\tau)-u^n\|_{L^2(\mathbb T)}\le C\tau^\gamma,
\qquad \tau=T/L\le\tau_0.
```

Here `\mathbb T` is the torus of period 2*pi. The manuscript uses normalized measure
dx/(2*pi); changing to the unnormalized L2 norm changes only a fixed factor
in C. In particular, choosing R at least the norm of the specified datum
gives the dependence requested by the problem.

| Public target requirement | Manuscript location and content |
| --- | --- |
| Real periodic KdV, u_t + u_xxx = (u^2)_x/2, period 2*pi | Section 2, equation (1); the sign and torus agree. |
| Mean-zero data in H^gamma, 0 < gamma <= 1 | Section 2 definitions and Theorem 1. No higher regularity is assumed in the theorem. |
| The particular F_tau and H_tau update | Section 2, equation (2) and the two displayed definitions immediately following it reproduce all four H_tau terms, the coefficients, inverse derivatives and endpoint differences. |
| No spatial cutoff or additional filter in that update | Section 2 defines the time-semidiscrete map on the full torus; Section 4 uses a frequency threshold only in the proof of stability. |
| Error at every grid time, including 0 and T | Theorem 1 takes the maximum over 0 <= n <= L. Section 4.4 identifies the interpolant with the actual iterates at every grid point. |
| Rate C tau^gamma without a logarithm | Theorem 1 and Section 4.4. |
| C and tau_0 depend only on T, gamma and the data norm | Theorem 1 states bounded-ball uniformity. Section 2.1 bounds the exact flow uniformly; Section 4.4 chooses the stability block size and timestep uniformly. |
| No hidden smooth-data restriction | Section 4.4 approximates the datum by mean-zero real Fourier polynomials, uses uniform constants and continuity of each fixed-timestep iterate, then passes to the limit. |

## Where the improvement and global proof appear

Section 3.1 proves the two phase-ratio covariance bounds and the short-time
bound. Section 3.2 proves the two four-frequency majorants and a summable
four-linear estimate using the third largest of four frequencies.
Theorem 5 in Section 3.3 gives the mixed cubic-remainder estimate with
tau^(1+gamma), including its local exponent-zero endpoint. Corollary 6
compares the remainder at an L2 numerical state to that at an exact
H^gamma state.

Section 4 supplies the global argument: the continuous estimates and
normal-form identities, stage and correction bounds, the actual stepwise
residual, high/low frequency stability with both endpoint terms, the
restarted bootstrap and the fixed-timestep approximation passage. The
old logarithmic convergence theorem is not invoked to deduce the new rate.

## Public analytic dependencies

- B. Li and Y. Wu, *An Unfiltered Low-Regularity Integrator for the KdV Equation
  with Solutions Below H1*, Foundations of Computational Mathematics 26
  (2026), 1321-1380, [DOI](https://doi.org/10.1007/s10208-025-09702-0).
  The manuscript uses equation and theorem locators from the
  [50-page author manuscript](https://www.polyu.edu.hk/ama/profile/byli/FoCM-3.pdf),
  particularly Proposition 3.4, Lemma 7.2 and the interpolation identities
  identified in Sections 3-4. The applicability and normalization changes
  are stated in the submitted paper.
- A. V. Babin, A. A. Ilyin and E. S. Titi, *On the regularization mechanism for
  the periodic Korteweg-de Vries equation*,
  [arXiv:0910.1389v2](https://arxiv.org/abs/0910.1389v2), 23 October 2010.
  Section 2.1 identifies Theorems 4.2-4.3, 5.1 and 6.3-6.5 and explicitly
  gives the reflection/sign transformation to the target equation.

The bibliography identifies these source versions so that a reviewer can
check the actual cited statements rather than infer them from a title.

## Numerical and review limits

Section 5 and the code use a fixed finite Fourier cutoff and projection
after the completed step. These computations are supplemental numerical
evidence. They do not substitute for the full-space theorem, give a rigorous
reference enclosure or prove an optimal rate. The global theorem requires
gamma > 0; the local exponent-zero estimate is not a global L2-ball rate.

The paper claims neither a uniform fully discrete convergence theorem nor
a rate lower bound. No formal verification, human peer review or receiving
catalogue acceptance is claimed. No separate detailed AI review is included.
