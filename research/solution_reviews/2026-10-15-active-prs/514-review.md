# AIM 514: independent review of PR #97

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#97](https://github.com/MColbrook/AIM/pull/97). Reviewed head: `5d53c3a78588eb1cb31362a337ab5b0e146eee91`.

Outcome: **Solved** — Every connected sum of two closed oriented aspherical n-manifolds has maximal unreduced TC=2n+1 for n>=3.

Proof: [aspherical-connected-sums.pdf](../../../research/solutions/514-kaiwen-jin-aspherical-connected-sums/paper/aspherical-connected-sums.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The proof first constructs an obstruction for a possibly nonaspherical space $`Y`$, which matters because a nontrivial connected sum is not aspherical. Let $`E`$ be the infinite join of copies of $`G`$ under the left-right $`G^2`$ action. Its Borel construction has the homology of $`BG^2`$. If unreduced TC is at most $`m`$, actual lifted motion-planner sections and a partition of unity give an equivariant map from the universal cover of $`Y^2`$ to the $`m`$-fold join. Its orbit space has dimension at most $`m-1`$. The resulting Borel-to-orbit map must kill the relevant class in higher degree, without assuming that $`Y`$ is aspherical.

For $`G=A*B`$, the Bass–Serre tree gives a precise family of vertex stabilizers and maximal hyperbolic-axis cyclic groups. Distinct members have trivial intersection and each is self-normalizing. Torsion freeness excludes an axis reflection and trivial edge stabilizers exclude a nontrivial translation kernel. Centralizers are contained in one family member. Consequently every nonfree simplex of $`E`$ lies in the join on a coset block $`uHv^{-1}`$; distinct blocks intersect in at most one label. The complement of the union $`Z`$ of these blocks has only free cells. A cellular filtration therefore makes the relative Borel-to-orbit map an integral homology isomorphism.

The block union's Borel construction is a homotopy pushout of the $`BH^2`$ pieces and their diagonal incidence spaces. In degree $`2n`$, the diagonal group homology vanishes for dimensional reasons, and the cyclic pieces vanish in that degree. Thus the image of $`H_{2n}(Z_{hG^2})`$ in $`H_{2n}(BG^2)`$ contains only the two same-factor summands. Künneth leaves the two ordered mixed fundamental classes independent and nonzero in the relative group.

The connected-sum pinch/classifying map sends its fundamental class to $`a+b`$. Its square has both mixed terms $`a\times b`$ and $`b\times a`$; they occupy distinct summands and cannot cancel, even when the manifolds are equal or the dimension is odd. The relative comparison then shows that the orbit image survives, contradicting the factorization that would follow from TC at most $`2n`$. The standard dimension upper bound gives equality. No assumption on centre rank, lower positive-degree rational cohomology or parity is used.

## References and scope

[Farber](https://arxiv.org/pdf/math/0111197v1) gives the unreduced convention and dimension bound. [Farber–Grant–Lupton–Oprea](https://arxiv.org/pdf/1711.10132v2), Sections2.5–2.9/Theorem2.1, supplies the labelled diagonal-join framework; its asphericity hypothesis is not misapplied to the sum, since the needed direction for that space is proved directly. [Lück](https://arxiv.org/pdf/0902.2480v3), Lemma3.1 and Theorem5.3, supplies torsion freeness and finite n-dimensional CW type for the summands. [Neofytidis](https://arxiv.org/pdf/2212.08962v2), Question5.5(b), is the requested target. The DS free-product paper and DST Proposition5.3 were checked as contextual wedge results rather than substituted for the connected-sum assertion. May's revised author text is the cited source for standard homotopy-pushout facts.

## Delivery checks

All seven PDF pages, complete target comparison and ancillary prose were read and visually inspected. The full obstruction, rather than only a group-TC estimate, was checked. No computation or Lean certificate is used.
