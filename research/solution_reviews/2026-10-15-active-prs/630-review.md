# AIM 630: independent review of PR #109

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#109](https://github.com/MColbrook/AIM/pull/109). Reviewed head: `5301ae4e418e9268de0680487b4741ee9bbcca08`.

Outcome: **Solved** — Every fixed extrapolation parameter outside[0,1] produces a relatively dense set in its full real or complex ambient space.

Proof: [relative_density.pdf](../../../research/solutions/aim-630-extrapolation-relative-density/paper/relative_density.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

For every parameter outside the real interval, reciprocal roots in the Chebyshev formula supply an integer polynomial $`h(x)=x(1-x)T_n(2x-1)`$ that is at most one quarter in absolute value on the interval and has $`|h(\lambda)|>1`$. The excluded endpoints ensure its prefactor is nonzero. This argument needs no algebraicity hypothesis.

Let $`\beta=h(\lambda)`$ and use the lattice $`\mathbb Z`$ for a real parameter, or $`\mathbb Z+\lambda\mathbb Z`$ for a nonreal one. Its elementary rounding bound is finite in either case. With radius $`\rho=|\beta|\delta`$, each point in the radius-$`\rho`$ ball is within $`\delta`$ of one of finitely many lattice digits, so that $`K\subset D+\beta^{-1}K`$. Scaling an arbitrary target into $`K`$ and iterating this inclusion a finite number of times gives a finite polynomial in $`\beta`$ with digit coefficients and uniformly bounded approximation error. The digit set is fixed before choosing the target.

Each digit is represented by an affine integer polynomial in $`\lambda`$. Since $`\|h\|_{[0,1]}\le1/4`$, all resulting digit polynomials have one common interval bound $`B`$, independent of their degree and chosen target. Fixing an integer $`\ell>B`$ and then a large enough $`k`$ makes $`[x(1-x)]^k(\ell+f(x))`$ strictly between zero and one on $`(0,1)`$ for every such digit polynomial. The cited characterization therefore puts the same nonzero affine image of the entire relatively dense digit set inside $`Q_\lambda`$. Multiplication by its fixed nonzero complex factor preserves relative density, proving the assertion about finite generation itself.

## References and scope

The single main reference, [Fenner–Green–Homer's published primary article](https://link.springer.com/article/10.1007/s00454-025-00816-4), was checked for Fact3.3, Theorem3.6, Corollary3.8 and Open Question11.3. These statements concern values of finite extrapolation polynomials, so applying them does not silently take a closure. The remaining expanding-polynomial and digit arguments are supplied and reconstructed directly.

## Delivery checks

All three PDF pages were visually inspected, with no clipping or unresolved references. The complete target comparison and ancillary prose were read. No computational or Lean verification is needed or asserted.
