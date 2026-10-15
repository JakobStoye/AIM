# AIM 644: independent review of PR #113

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#113](https://github.com/MColbrook/AIM/pull/113). Reviewed head: `fbad49f5635de525a998198814613a1bbf8b91f5`.

Outcome: **Solved** — The reduced topological complexity is2 with probability tending to one along all sample sizes in the homogeneous lower model.

Proof: [main.pdf](../../../research/solutions/644-medial-regime-topological-complexity/paper/main.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The model retains each simplex only when all its nonempty raw face variables succeed, including singleton variables. The proof correctly identifies this as the homogeneous lower model. The known connectivity and upper bound apply for every large sample size. For a connected finite complex, Euler characteristic different from zero and one forces one of the rational Betti-number configurations giving reduced TC at least two; the submission checks the contrapositive, including the possibility of a single odd-dimensional generator.

Choose face cardinality near $`\log_2\log n`$ so the probability of an additional complete immediate coface is at most $`n^{-2}`$. Coloring those faces by the sum of labels modulo $`n`$ gives a deterministic large family with no two sharing a codimension-one face. Consequently every immediate coface contains at most one selected face, which is crucial for the later exposure. The exact overlap count contains the extra denominator from the uniquely determined final label. Together with the hypergeometric overlap bound and the estimate for $`2^i`$ over the whole changing overlap range, this makes the relative variance of the number $`W`$ of successful boundaries tend to zero; its mean tends to infinity. This controls growing overlaps, not only each fixed overlap separately.

Expose all raw variables outside the chosen family. Successful boundaries and all coface-blocking tests are measurable at that stage because each immediate coface contains at most one selected face. Conditional on a boundary, its potential coface requires exactly $`2^r`$ further raw variables. The expected number of unsafe faces is at most $`\mathbb EW/n`$. With high probability, at least a quarter of the diverging mean remains both successful and safe. After exposing the remaining nonsafe selected variables, each safe variable can toggle only its own face: every larger coface is blocked by an already exposed failed immediate coface. The unexposed variables are still independent Bernoulli variables because the safe set was chosen without using them. Thus the conditional Euler characteristic is a fixed integer plus a signed binomial variable of diverging length.

Fourier inversion and the elementary sine bound give a uniform binomial point-mass bound of order inverse square root. Combining it with the variance and unsafe-face errors proves that every atom of the Euler characteristic tends to zero, uniformly in its integer location. In particular zero and one become negligible. Intersecting that event with the all-sample-size connectivity and TC upper bound proves the claimed limit through all integers.

## References and scope

[Barmak–Farber's primary manuscript](https://arxiv.org/html/2608.07969v1), Corollary10, Theorem16 and Lemma17, was checked for the exact lower-model hypotheses and reduced TC convention. It supplies connectivity and the upper bound, not the new anti-concentration result. The older Farber article is background. The [DLMF Gaussian formulas](https://dlmf.nist.gov/7.2) cited for the elementary integral have the indicated section; the Fourier and variance estimates themselves are given explicitly.

## Delivery checks

All five PDF pages, including the exposure formulas, changing-overlap estimate and references, were visually inspected. Complete target comparison and ancillary prose were read. No experiment or Lean proof is represented as mathematical certification.
