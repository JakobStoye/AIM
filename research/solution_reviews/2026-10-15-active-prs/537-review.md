# AIM 537: independent review of PR #101

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#101](https://github.com/MColbrook/AIM/pull/101). Reviewed head: `ed0c8eff31e6a22c9bc5509c0413e9e513aeff8e`.

Outcome: **Solved** — The prescribed no-finite-bar persistence fibre has the same F2 homology as the underlying simplicial complex.

Proof: [persistence_fiber.pdf](../../../research/solutions/537-persistence-fiber-betti-numbers/paper/persistence_fiber.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The initial deformation continuously clamps all filter values after the second barcode endpoint while strictly preserving their order before the endpoint of the homotopy. At the endpoint those stages are the whole complex. The prescribed barcode is unchanged throughout, including the connected acyclic case where there is only one persistent zero-dimensional interval. This is a strong deformation retraction to the stated bounded filter subspace.

That subspace is exactly the order complex of nonempty $`\mathbb F_2`$-acyclic subcomplexes. A chain with barycentric coefficients gives the filter value $`2-\sum_A\lambda_A1_{\sigma\in A}`$. Conversely, the distinct attained values between one and two recover nested acyclic sublevels and their successive differences as barycentric coefficients. The formulas are mutually inverse; compactness of the order complex and the Hausdorff ambient filter space justify the homeomorphism across changing chains.

The map from the face poset of $`K`$ to the acyclic-subcomplex poset sends a face to its whole simplex. Its lower fibre at $`A`$ is the face poset of $`A`$ and is therefore acyclic over the specified field. It need not be contractible. The submission proves the precise homology comparison through a finite mapping-cylinder poset: the face-poset inclusion is a homotopy equivalence by comparable maps; adjoining the target-poset elements in reverse order attaches cones on joins whose lower factors are the acyclic fibres. The augmented chain tensor product of such a join is acyclic over the field. Each cone attachment thus preserves homology. This proves equality in all degrees, including degree zero, without silently invoking the stronger homotopy fibre lemma. The empty case is separately consistent with the stipulated barcode and ordinary H0.

## References and scope

The exact target was checked in [Leygonie–Henselman-Petrusek's published primary text](https://link.springer.com/article/10.1007/s41468-024-00165-w), Conjecture1 and its barcode definition. [Björner–Wachs–Welker's author text](https://www.mathematik.uni-marburg.de/~welker/preprints/fiber.pdf), Section4, gives the relevant homology rather than contractible-fibre context. [Harrington–Tillmann–Torras-Pérez](https://arxiv.org/html/2608.04640v1) is correctly contextualized as a polyhedral-fibre result. Hatcher and Munkres are used only for standard homology and compact-to-Hausdorff topology; the needed finite-poset comparison is proved explicitly.

## Delivery checks

All four PDF pages and bibliography were visually inspected. Complete target comparison and ancillary prose were read; no clipping or unresolved markers were seen. No Lean or human certification is asserted.
