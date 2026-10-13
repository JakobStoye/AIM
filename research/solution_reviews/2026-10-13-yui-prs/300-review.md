# AIM 300 — independent review of PR 67

- Date: 2026-10-13; submission: [PR 67](https://github.com/MColbrook/AIM/pull/67), Kaiwen Jin.
- Reviewed head: `efb5c003723b01af6090482c58330db2da99e86b`.
- Proof: [PDF](../../solutions/300-carrying-simplex-interior/paper/interior_smoothness.pdf), [source](../../solutions/300-carrying-simplex-interior/paper/interior_smoothness.tex).
- Reviewer: independent Codex agent, separate from manuscript drafting/self-review; AI natural-language mathematical audit. No human or Lean certification.
- Verdict: **Solved**, interior $`C^1`$ regularity for the full stated class.

## Exact scope

The theorem retains the original $`C^1`$ per-capita law, strict positivity/competition, axial fixed points and spectral-radius assumption on the full box. It does not assume convexity, permanence, a uniform positive lower bound on every population, or boundary smoothness. It establishes exactly the positive-interior embedded hypersurface and radial-function regularity requested.

## Complete independent reconstruction

The axial fixed points lie on the compact attracting simplex; unorderedness then puts every simplex coordinate below its corresponding axial value. Compactness away from zero gives a positive lower bound on the **sum** of populations. The cited inverse theorem makes the invariant simplex map a homeomorphism, preserving support. In logarithmic coordinates every positive ray has one intersection, so projection along the all-ones vector gives an everywhere-defined graph on the zero-sum plane. Unorderedness gives its stated Lipschitz bound without differentiability assumptions.

Recomputed the logarithmic derivative: $`DH=I-K\mathop{\mathrm{diag}}\nolimits(x)`$. The physical and logarithmic matrix products have identical characteristic polynomials even at extinction faces. Thus the inverse matrix is continuous and nonnegative on the whole compact box, and

```math
A=(I-K\mathop{\mathrm{diag}}\nolimits(x))^{-1}=I+B\mathop{\mathrm{diag}}\nolimits(x),\qquad B=AK.
```

All entries of $`B`$ have positive compact lower and upper bounds. This proves cone invariance using $`a-\kappa b\ge0`$. The derivative of the log-ratio map is row stochastic, and every row dominates the same measure of total mass at least $`a\kappa s/(1+bL)>0`$. Integrating along the log-linear segment within the cone proves uniform Hilbert-distance contraction. This remains valid as a backward orbit approaches an extinction face, because only the sum of its physical coordinates is bounded below.

The normalized forward matrix products yield nested compact cone sections with uniformly decreasing diameter. Their limiting positive direction is continuous and obeys the inverse-step covariance identity. Normalizing the inverse derivatives by this direction gives row-stochastic products contracting oscillation uniformly. Their nested row convex hulls shrink to a continuous probability row. Dividing by the positive direction gives a continuous nonnegative covector with a strictly positive value on the all-ones vector. Checked every diagonal and scalar cancellation in the product identity (lines 329–346); every component of a transported vector has the eventual sign of its covector pairing.

Any contingent tangent vector transported by a **fixed finite** local inverse composition remains contingent on the logarithmic unordered graph. If its covector pairing were nonzero, sufficiently many finite inverse steps would make it strictly signed, contradicting unorderedness. This proves containment in the covector kernel without differentiating an infinite orbit or assigning a logarithm/tangent plane to an extinction point. The Lipschitz graph's normalized secants have convergent subsequences; their kernel constraint forces every derivative remainder subsequence to vanish. Hence it is Fréchet differentiable at every point, with the displayed linear derivative. Covector continuity makes that derivative continuous. The graph projection gives an injective derivative and continuous inverse, proving embeddedness, and the explicit radial formula transfers $`C^1`$ regularity to the probability-simplex interior.

## All-reference and background audit

- Baigent, ICDEA 2017 proceedings (2019), pp. 3–29, [DOI](https://doi.org/10.1007/978-3-030-20016-9_1), [institutional manuscript](https://www.ucl.ac.uk/~ucess29/resources/ICDEA_RPS.pdf): primary indexed manuscript confirms Theorem 1's AS1–AS4 are exactly the submission hypotheses and Lemma 16(1)'s homeomorphism applies on the rectangular box. Its nonnegative inverse expansion matches the matrix use. Direct PDF retrieval through the browser returned an access/404 error, so the theorem text was checked through the indexed primary manuscript; the elementary inverse expansion was also reconstructed directly from the spectral-radius assumption.
- Mierczyński–Niu–Ruiz-Herrera, JDE **267** (2019), 7385–7410, [arXiv v2](https://arxiv.org/html/1902.08914v2), [DOI](https://doi.org/10.1016/j.jde.2019.08.001): authors/title/metadata match; the local fixed-point results are correctly distinguished from global interior regularity.
- Mierczyński, ETDS **40** (2020), 1335–1350, [arXiv v2](https://arxiv.org/abs/1801.01032v2), [DOI](https://doi.org/10.1017/etds.2018.85): metadata and extra convexity/neat-embedding scope match. Convexity is not quietly imported.
- Naderi Yeganeh–Baigent, JDEA **30** (2024), 1671–1691, [publisher](https://www.tandfonline.com/doi/full/10.1080/10236198.2024.2369215): title/authors/year/pages match. Logarithmic-convexity work is background; none of its extra hypotheses are used in the new contraction argument.

No essential missing reference or proof gap remained. The new cone/covector/contingent argument is explicit and independently reconstructed above.

## PDF and decision

Coordinator parsed/rendered all seven pages. Independently inspected the all-page contact sheet: complete theorem, matrix formulas, proof and references, with no missing or clipped content. Recommend accepting the package and marking **Solved**, with this independent AI audit identified; do not imply boundary smoothness or Lean verification.


The package README and target comparison, including their AI-use disclosures, were also read. Their mathematical scope agrees with the manuscript and the original target; they introduce no separate executable proof or numerical certificate as a premise. Package hashes and repository integration are separate coordinating checks.
