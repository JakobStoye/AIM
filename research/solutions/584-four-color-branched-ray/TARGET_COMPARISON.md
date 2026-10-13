# Correspondence with AIM Problem 584

Original statement:
[584-four-color-branched-ray.md at c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/584-four-color-branched-ray.md).
Statement SHA-256:
`19d39141b7d467c106c8de12a350c701f4c8b8dca0ec62784fb33665c116029e`.

The claimed alternative is nonexistence of the entire requested pair.
Locations below refer to the supplied six-page [paper](paper/main.pdf).

| Original requirement | Result and manuscript location | Coverage |
| --- | --- | --- |
| Vertices `o,a,b,v_1,v_2,...`; edges `oa,ob,ov_1,v_jv_{j+1}` | Section 1 defines this graph immediately before Theorem 1. | Same infinite graph; neither finite arm is discarded. |
| Random proper four-coloring `X` of this graph and proper four-coloring `Y` of the integer line | Theorem 1, item 1; specified cylinder probabilities in Section 2. | Same colors, adjacency constraints, and domains. |
| Both processes one-dependent for arbitrary vertex sets at distance greater than one | Theorem 1, item 2; Section 2 proves deletion identities and joint independence of separated vertices. | Full arbitrary-set hypothesis; no replacement by pairwise independence. |
| Both laws invariant under all permutations of the colors | Theorem 1, item 2; Section 2 explains relabeling and actual-color multiplicities. | Full color symmetry; the two leaf positions remain ordered. |
| `Y` stationary and reflection-invariant | Theorem 1, item 3; Section 2 defines line probabilities and their reversal symmetry. | Same hypotheses. |
| Every ordered simple path in the graph has the consecutive-block law of `Y` | Theorem 1, item 4; leaf marginal equations (6) and `s(A,B,O)=p(A,O,B)` in Section 2. | Same ordered-path requirement, with no leaf-exchange assumption. |
| The line law is arbitrary, rather than prescribed to be the Holroyd--Liggett law | Section 1 and Theorem 1 assume no formula for `Y`; Sections 2--4 derive universal necessary constraints. | All line laws satisfying the original hypotheses. |
| Prove nonexistence or construct such a pair | Theorem 1 and its closing proof, using Lemmas 2--3 and Proposition 4. | Complete nonexistence claim, with a proof-critical exact certificate supplied. |
| Infinite third arm | Lemma 2 uses all finite avoidance lengths along an infinite continuation. | Analytic treatment of the infinite tail; the finite calculation alone is not the theorem. |
| Background or imported results | Introduction: Holroyd--Liggett, arXiv:1403.2448v4, Theorem 4; Liggett--Tang, arXiv:1804.06877v3, Proposition 1.4, its following paragraph, and Section 6, question 1. | Verified background locators. No external theorem is imported into the contradiction. |

The proof-critical finite calculation is reproduced by
`src/verify_certificate.py` with `certificate/farkas.json`. Proposition 4
specifies its exact margin and all constraint families. The 12 supplied
tests provide additional implementation checks.

No stronger claim for a fixed finite truncation, asymmetric laws, or an
unrelated graph is made. There is no claimed human or formal certification.
The package is a complete solution claim awaiting independent review.
