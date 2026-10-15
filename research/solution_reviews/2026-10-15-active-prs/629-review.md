# AIM 629: independent review of PR #111

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#111](https://github.com/MColbrook/AIM/pull/111). Reviewed head: `c1f79e312f2b7bae2636469c506376a873100691`.

Outcome: **Solved** — Discreteness of the finite extrapolation set is equivalent to the full strong-PV conjugate condition.

Proof: [extrapolation_discreteness.pdf](../../../research/solutions/629-extrapolation-discreteness/paper/extrapolation_discreteness.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The integer Bernstein lemma rounds the coefficients of the usual Bernstein approximant, fixes integer endpoint values exactly, and bounds the rounding error separately near the endpoints and on the middle interval. The resulting error tends to zero uniformly. This proves the exact approximation property needed for the residue construction, rather than appealing to ordinary real-coefficient approximation.

For an irreducible monic minimal polynomial $`m`$ and a prescribed residue polynomial $`f`$, positivity is already feasible at every root of $`m`$ inside $`(0,1)`$. A continuous auxiliary function can be chosen locally at those roots, at the endpoints with integer values, and elsewhere, then glued by a partition of unity because both strict inequalities are affine in that function. Compactness gives positive margins. The integer Bernstein approximation preserves those margins, yielding an integer polynomial strictly between zero and one on the interval with the desired exact value at $`\lambda`$ modulo $`m`$.

For the arithmetic density step, the closure of an additive subgroup of Euclidean space splits into its maximal vector subspace and a discrete lattice part. A proper closure consequently admits a nonzero real functional integral on the subgroup. Applied to a proper selection of whole real or complex embedding coordinates of $`\mathbb Z[\lambda]`$, the trace pairing represents that functional by an element of the number field. The full embedding vectors of a power basis are a real basis, by the distinct-root Vandermonde argument. Vanishing on an omitted coordinate forces an embedding of the trace element to vanish, hence the element itself is zero, a contradiction. Thus every proper coordinate projection is dense.

The known integrality theorem first makes a discrete parameter an algebraic integer. If a nonphysical conjugate is outside $`(0,1)`$, retain the physical coordinate and all conjugates in that interval, omitting the offending real or complex factor. Density supplies polynomials with arbitrarily small but nonzero physical value and simultaneous interior positivity at the retained interval roots. The residue lemma then produces actual nonzero members of $`Q_\lambda`$ converging to zero. This is stronger than finding small differences of unrelated members, which alone would not refute local discreteness. Conversely, for a strong PV parameter every nonphysical conjugate of a difference of two generated values has absolute value at most one. Its nonzero integer algebraic norm bounds the physical difference below by one, including the conjugate-pair square in the complex case. The exceptional seed parameters0 and1 and the real interior parameters are handled explicitly.

## References and scope

The polynomial characterization was checked in [Fenner–Green–Homer's published text](https://link.springer.com/article/10.1007/s00454-025-00816-4), Theorem3.6/Corollary3.8. Its extended version [arXiv:1212.2889v6](https://arxiv.org/pdf/1212.2889v6), Theorem8.2, does apply to arbitrary complex parameters and supplies the necessary algebraic integrality. [Campbell](https://arxiv.org/html/2609.30771v1), Theorem2, is correctly credited for the prior totally real restriction. [Draganov](https://arxiv.org/abs/1804.08248v2) has the quoted integer-Bernstein title and version; the precise weaker approximation lemma used here is proved within the submission.

## Delivery checks

All five PDF pages, including the embedding-coordinate conventions and references, were visually inspected. Complete ancillary prose and target comparison were read. This is a conventional mathematical proof with independent AI review, not a Lean certificate.
