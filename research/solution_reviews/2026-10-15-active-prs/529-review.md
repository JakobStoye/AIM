# AIM 529: independent review of PR #100

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#100](https://github.com/MColbrook/AIM/pull/100). Reviewed head: `0da42f3f8c186fa9b965b3e6c0745f3b12885086`.

Outcome: **Solved** — The normalized high-dimensional Betti numbers converge to an explicitly described nondegenerate law with all positive moments, excluding the proposed power-law tail.

Proof: [main.pdf](../../../research/solutions/529-preferential-attachment-betti-limit/paper/main.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The model and its normalization were checked before the asymptotics. The independent beta variables have first parameter $`m+\delta`$ and second parameter $`(2m+\delta)(j-1)-m`$. The conditional target probability is the beta variable times the intervening product of one-minus-beta variables. The manuscript's posterior calculation recovers the actual sequential eligible weights, including reinforcement during each birth, rather than a different independent-target variant. Convergence of the centered logarithmic product follows from its summable variance; its deterministic mean gives the positive limits $`R_v`$ and weights $`D_v`$.

The joint required-edge and weight moment estimate was reconstructed from beta moments and a finite assignment of required edges to birth slots. For an ordered graph, exponents for every terminal label segment are strictly negative once each vertex has its prescribed weight factor and the required minimum degree. Dyadic label summation therefore bounds the complete sum, not only a fixed graph embedding. Taking unions of overlapping octahedral bases preserves the necessary minimum degree and at least one weight per vertex. This proves convergence and all positive moments of the random weighted induced-base series $`A`$. The separate estimate conditioned on one beta coordinate retains its explicit power of $`1-\psi_K`$.

For a fixed $`2q`$-vertex base, occupancy probabilities from the independent birth slots give its common-neighbor count divided by $`T^{1-2qx}`$ converging almost surely and in L1 to the stated product of the $`D_v`$ weights. The next occupancy order is negligible, and the conditional variance series is summable. Weighted joint-edge estimates provide uniform second moments and a summable bound for the full base sum. Thus finite-base convergence extends to all bases by an explicit tail cutoff, rather than interchanging an infinite sum and limit without domination.

The link topology is also needed to identify the series with Betti numbers. Repeated removal of vertices below the minimum link degree preserves the two relevant homology groups. A remaining core on at most $`2q`$ vertices is either a cone or the boundary of a cross-polytope, with its unique induced octahedral base. Larger exceptional cores have an extra factor in their probability and contribute $`o(T^{1-2qx})`$ in L1. Each fixed base eventually has an earlier common-neighbor cone, making its inclusion into the preceding complex null on the needed homology; the divergent independent-apex supply proves this almost surely. The link birth-minus-death exact sequence then leaves precisely the common-neighbor base count asymptotically. Choosing a finite base cutoff first and using the uniform second moments controls the random waiting times; no unjustified finite expected waiting time is assumed.

At least one induced octahedral base occurs almost surely, by successive suspensions using two nonadjacent common neighbors, so $`A>0`$ almost surely. To prove nondegeneracy, condition a distant beta coordinate close to one. Bases with older labels are suppressed by its one-minus-beta factor, while bases at or beyond that label have summably small expectations by the strict exponent estimates. Choose the label first and the beta interval second; that interval has positive probability. This gives essential infimum zero, whereas the mean is positive. Consequently the normalized limit $`A/\mathbb EA`$ is nonconstant and has every positive moment. A regularly varying tail with finite exponent would violate its sufficiently high moment, giving the claimed negative answer about the proposed power law. The conclusion is for the full specified strict subcritical parameter range and full sequence, not only a subsequence or a numerical fit.

## References and scope

The exact environment parameters and model equivalence were checked in [Siu](https://arxiv.org/html/2406.17619v2), Definition5.1, Theorem5.2 and Lemma5.3. The submission independently supplies its posterior check. The link rank identity matches [Siu–Samorodnitsky–Yu–He](https://arxiv.org/pdf/2305.11259v3), Proposition14 and its Mayer–Vietoris proof. In the cited [Durrett author draft](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf), Theorems2.5.6, 2.5.9 and2.3.7 give the independent-series convergence, Kronecker and Borel–Cantelli facts with the stated hypotheses. The original services.math.duke.edu URL did not fetch in the web tool; the author's sites.math.duke.edu copy has the exact January11,2019 version. [Dey–Terlov](https://arxiv.org/abs/2605.28776v1) has the cited title/authors and is triangle-count context, not a substitute for a high-dimensional theorem.

## Delivery checks

All eleven PDF pages, the entire proof and bibliography, full target comparison and ancillary prose were read and visually inspected. This audit includes the infinite-label estimates and exceptional-link error terms. No simulation or Lean certificate is used.
