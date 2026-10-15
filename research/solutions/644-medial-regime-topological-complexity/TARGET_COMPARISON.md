# Correspondence with AIM Problem 644

Original target: [Topological complexity in the homogeneous medial regime
for all sample sizes](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/644-medial-regime-topological-complexity.md),
repository revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.

Submitted result: Theorem 1 of the accompanying manuscript,
*Topological complexity two in the homogeneous lower model*, by Kaiwen Jin.

| Original requirement | Manuscript location | Scope |
| --- | --- | --- |
| Every fixed $`p\in(0,1)`$ | Model (1), Theorems 1 and 3; constant dependence after Theorem 1 | Entire fixed-p range; no size-dependent-p assertion |
| Independent Bernoulli(p) variable for each nonempty subset | Section 1, equation (1) | Exact original product sampling law |
| Vertices sampled along with higher faces | Paragraph after (1); successful-boundary definition in Section 2.2; Section 3 law comparison | Singleton variables are included throughout |
| Retain a face iff every nonempty subface succeeds | Equation (1) and Section 3 containment-law calculation | Same downward-closed lower model |
| Path connectivity with probability tending to one | Section 3, applying Barmak--Farber Corollary 10 | All ambient sample sizes |
| Reduced topological complexity | First paragraph of Section 1 | k+1 section domains, agreeing with the original normalization |
| Exact value two with probability tending to one | Theorem 1; Lemma 2 and Theorem 3; final proof in Section 3 | Lower bound from chi outside {0,1}, upper bound from cited Theorem 16 |
| Full sequence of positive integer sample sizes | Theorem 1; deterministic choice (3), bounds (4), entire overlap sum (7)--(9), coface and point-mass bounds (10)--(13) | Every sufficiently large integer is covered, including adjacent-count transitions |
| Probability limit equals one | Section 3 intersection of connectivity, upper-bound and chi events | Every complementary-event probability tends to zero |

The new supplementary argument is in Section 2: it proves
$`\sup_{z\in\mathbb Z}\mathbb P\{\chi(X_n)=z\}\to0`$ along all sample sizes.
It does not infer the full sequence from a density-one subsequence.

Public dependencies and their use:

- Barmak--Farber,
  [arXiv:2608.07969v1](https://arxiv.org/abs/2608.07969v1),
  Section 3.1, equation (1), p. 5: containment-law description;
  Corollary 10, p. 7: connectivity; Theorem 16, p. 9: reduced upper bound;
  Lemma 17, p. 10: rational Betti-number lower-bound criterion.
  Section 3 explicitly specializes the parameter bounds to the submitted model.
- Farber,
  [doi:10.1007/s41468-023-00134-9](https://doi.org/10.1007/s41468-023-00134-9),
  Remark 8.2: background conjecture and attribution.
- [NIST DLMF Section 7.2(i)](https://dlmf.nist.gov/7.2),
  equations 7.2.1 and 7.2.2: the Gaussian integral used in the elementary
  binomial point-mass estimate (13).

This correspondence records a complete solution claim supported by the
manuscript and its public dependencies. Independent mathematical review and
catalogue classification remain with the receiving repository.
