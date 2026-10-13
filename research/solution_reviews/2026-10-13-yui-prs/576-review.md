# Independent review of AIM 576: uniform constrained-Ising covariance

**Date:** 2026-10-13  
**Submission:** [PR #78](https://github.com/MColbrook/AIM/pull/78), Kaiwen Jin  
**Reviewed head:** `9f7637ced9f656199f8ce36eba7feb7d857c764a`  
**AIM statement:** problem 576 at `c9929805cece044705abaaebe1cebddac1ba11a6`  
**Reviewer:** independent Codex AI mathematical audit, separate from submission development. No human or Lean verification is claimed.  
**Decision:** **Solved**, with the reference-locator correction below.

[Manuscript](../../solutions/576-ising-replica-covariance/paper/ising_replica_covariance.pdf) · [Source](../../solutions/576-ising-replica-covariance/paper/ising_replica_covariance.tex)

## Target and complete proof audit

The theorem gives a finite constant depending on the fixed real symmetric interaction and partition, uniformly over all replica counts, feasible block magnetizations, and arbitrary replica-dependent fields. The Euclidean covariance of all spins is bounded; no high-temperature, identical-field, or interior-magnetization assumption is introduced. This is the full AIM target.

The two-copy reduction was reconstructed directly. For two independent constrained configurations define their coordinatewise half-sum c and half-difference x. At a supported fixed c, only the disagreement mask D in each replica remains variable. Both configurations meet their original totals exactly if and only if x has zero totals in each partition part. The joint energy is the sum of the constant c-energy and external-field terms plus x-transpose J x. Thus its conditional distribution is exactly a product of the finitely many symmetric, full-support mask laws, conditioned on zero totals. The external fields disappear without a bound or limit in their size. Active counts are even; zero counts and empty masks are included.

For those conditioned independent blocks, the proof obtains a denominator lower bound and second-moment numerator upper bound with identical active-count factors. Write K_A for the active count in part A. The diagonal interaction is constant, and the non-diagonal energy oscillation is at most four times the sum of absolute off-diagonal entries. Each mask law therefore dominates delta times the uniform spin cube, with a strictly positive delta depending only on J.

Pair identical masks and leave at most one of each of the at most 2-to-the-n mask types unpaired. The remaining counts are even, so a zero-total assignment exists among the unpaired coordinates and has probability bounded below by a fixed positive constant. The paired-block characteristic functions are real and occur to even powers; their Fourier product is nonnegative on the full torus. Restricting to a box of widths proportional to one over the square root of 1+K_A gives the denominator bound. On that box the quadratic moment bound and elementary cosine/log inequalities bound the integrand below by a fixed positive constant. This argument is uniform even when some K_A vanish or only finitely many blocks are active.

For the numerator, the characteristic function of each mask is bounded in modulus by an exponential damping in the sum of its active counts times sine squared. The decomposition into delta times the uniform cube and a positive remainder justifies the modulus estimate even if the original characteristic function is negative. A linear statistic within a block has mean zero by global sign symmetry. Its first characteristic moment is bounded by its coefficient energy times the quadratic Fourier parameter; summing across blocks uses Cauchy--Schwarz. Expanding the second moment times the full characteristic function omits at most two factors. Their loss is bounded by a fixed exponential constant, since each block contains at most n active coordinates. On the small torus sine squared bounds the square of the Fourier coordinate. Integrating the resulting Gaussian damping yields precisely the same product of (1+K_A) to the power -1/2 as the denominator. S_A is deterministically even, so inversion on this small torus is valid. The formulas are finite sums/integrals, with no local-limit approximation or asymptotic uniformity issue.

Dividing the numerator by the denominator gives a finite uniform conditional second-moment constant U/L. The independent-copy variance identity supplies twice this constant for the original linear statistic. Since this holds for every real coefficient array, it gives the stated covariance operator bound. I recomputed the constants L, U, and the explicit final expression; they are finite for every fixed J and have no N, magnetization, or field dependence. The large size of the constant is permitted by the question. No entropy-decay theorem beyond this covariance result is claimed.

## Reference audit and required correction

The sole cited source, [Caputo and Morellini, arXiv:2511.05223v1 (2025)](https://arxiv.org/html/2511.05223v1), has the correct authors/title/year and states the arbitrary-tilt, replica-uniform covariance conjecture in Section 4.5. Its Proposition 3.6 and Section 3.4 support the background high-temperature comparison. The new finite Fourier argument is proved directly and imports no additional nonstandard theorem.

**Editorial correction:** source line 55 attributes the canonical measure to Definition 1.9, equations (1.15)--(1.16). In the explicitly cited version 1 the correct equation numbers are **(1.23)--(1.24)**. Definition 1.9 itself is correct, and the submission's explicit measure and target comparison are correct. This locator correction should be propagated to source, PDF, and artifact hashes by the maintainer; it does not change the proof or justify a partial-progress classification.

## Conclusion

All proof-critical steps, degeneracies, uniformity parameters, covariance normalization and target quantifiers were independently audited. The finite conditioned-mask estimate completes the stated conjecture and supports `Solved` under the repository's independent-audit policy. This record is an AI audit, not external human certification or Lean verification.

## Rendered PDF check

All 6 pages of the supplied main PDF were visually inspected against the source presentation. Titles, theorem statements, mathematical tables/equations, proof structure and bibliography agree; no clipped content or unresolved references were found. Root package checks separately parsed all pages and checked payload and archive hashes. Rendering is supplementary artifact evidence, not mathematical or formal verification.
