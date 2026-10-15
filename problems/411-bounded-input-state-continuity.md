# 411. Continuity of states driven by bounded admissible inputs

**Area:** Infinite-dimensional control / evolution equations

**Status:** ✅ SOLVED

**Last checked:** 2026-10-15

## Problem statement

Let $`X,U`$ be Banach spaces, let $`A`$ generate a strongly continuous semigroup $`S(t)`$ on $`X`$, and let $`X_{-1}`$ be the completion of $`X`$ for the norm $`\|x\|_{-1}=\|(\lambda-A)^{-1}x\|_X`$, where $`\lambda`$ belongs to the resolvent set of $`A`$. Denote the extended semigroup by $`S_{-1}`$ and fix $`B\in\mathcal L(U,X_{-1})`$. Assume $`L^\infty`$-admissibility: for every $`T>0`$, there is $`K_T<\infty`$ such that for every strongly measurable $`u\in L^\infty(0,T;U)`$,

```math
\Phi_Tu:=\int_0^T S_{-1}(T-s)Bu(s)\,ds\in X,\qquad \|\Phi_Tu\|_X\le K_T\|u\|_{L^\infty}.
```

Must $`t\mapsto\int_0^t S_{-1}(t-s)Bu(s)\,ds`$ be continuous from $`[0,T]`$ to $`X`$ for every such input and every $`T>0`$?

## Application

Boundary actuators for evolution PDEs are often unbounded operators on the state space. This asks whether having a well-defined state at each time automatically prevents state discontinuities under bounded measurable actuation.

## References

1. G. Weiss, *Admissibility of Unbounded Control Operators*, SIAM Journal on Control and Optimization 27 (1989), 527–545, Problem 2.4. [DOI](https://doi.org/10.1137/0327028).
2. F. Marbach, *Time-iteration methods for controllability*, lecture notes (2026), Remark 2.32. [Full text](https://arxiv.org/html/2602.19272v1).
3. P. Preußler and F. L. Schwenninger, *Implications of structured continuous maximal regularity*, preprint (2026), §4.4, Corollary 4.10 and following discussion. [Full text](https://arxiv.org/html/2605.12121v1).

## Status review

Reviewed 15 October 2026 against the original target in [PR #162](https://github.com/MColbrook/AIM/pull/162). Admissibility for all strongly measurable bounded inputs implies zero-class admissibility and norm-continuous convolution states on every closed finite interval.

[Proof or source](../research/solutions/411-bounded-input-state-continuity/paper/continuity.pdf) · [Independent AI review](../research/solution_reviews/2026-10-15-active-prs/411-review.md). The linked review records the exact scope and verification limits; this is not human peer review or Lean verification.

**Scope:** Full affirmative answer for arbitrary real or complex Banach state and input spaces in the stated extrapolation representation.

### Earlier review notes

The following historical notes are retained; the current decision and review date are given above.

**Known cases:** The cited partial theorem establishes continuity in reflexive-space cases and several further Banach-space classes.

**Remaining target:** Continuity for arbitrary Banach state and input spaces under the stated bounded-input admissibility assumption.

**Literature check:** Open in cited literature; no later resolution located.

The May 2026 source explicitly describes its answer to Weiss’s question as partial: it covers reflexive spaces and several further Banach-space classes. The statement here retains arbitrary Banach state and input spaces. Searches through 22 September 2026 located no unrestricted proof or counterexample. This concerns continuity in time, not the disproved L2 resolvent-characterization version of the Weiss conjecture.
