# Comparison with AIM 514

Target: [Maximal motion-planning complexity of aspherical connected sums](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/514-aspherical-connected-sum-complexity.md), revision a153f469ee0ea64e876b2ad97c79d252c19a3e22. This is a complete affirmative solution claim. Independent mathematical review is requested.

| Original requirement | Manuscript location and argument | Scope |
| --- | --- | --- |
| Every pair M,N | Theorem 1.1 and Section 5; the argument uses only the stated manifold hypotheses | All pairs, including abstractly isomorphic fundamental groups |
| Closed and connected | Theorem 1.1; Section 5 uses their classifying spaces and top homology | Preserved |
| Oriented | Theorem 1.1; Section 5 uses the two rational fundamental classes and the degree +1 pinch maps | Preserved |
| Each summand aspherical | Section 5: the factors are nontrivial torsion-free groups and M wedge N is a classifying space for their free product | Required of M and N |
| Same dimension n >= 3 | Theorem 1.1; free-product van Kampen and degree 2n homology in Sections 4-5 | Every such n; no restriction to dimension 3 or 4 |
| Oriented connected sum M#N | Section 5: the pinch map induces the free-product isomorphism and sends [M#N] to the sum of the two fundamental classes | The connected sum need not be aspherical |
| Ordinary unreduced TC | Introduction and Lemma 2.1 use the number of open local motion-planner domains | No reduced/unreduced shift |
| Equality TC(M#N)=2n+1 | Proposition 4.3 and Section 5 give the lower bound; Farber's dimension bound gives the upper bound | Full equality |
| A result about connected sums, rather than only wedges | Lemma 2.1 applies to arbitrary closed connected manifolds; Section 5 applies its classifying-map obstruction directly to M#N | Wedge used only as BG |

The two mixed classes a cross b and b cross a occupy separate ordered Kunneth coordinates. They do not cancel when n is odd or when the two manifolds are isomorphic.

The cited results provide the dimensional upper bound, the diagonal-cover/join framework, foundational CW/homology facts, and the existing wedge/partial frontier. The manuscript proves its coset-block homology bridge in Sections 3-4. It does not claim that a wedge computation alone resolves the connected-sum target.

| Public source | Use in this manuscript |
| --- | --- |
| Farber, arXiv:math/0111197v1, Theorem 4 | Ordinary unreduced TC dimension upper bound |
| Farber--Grant--Lupton--Oprea, arXiv:1711.10132v2, Sections 2.5-2.9 and proof of Theorem 2.1 | Diagonal covering and join framework; the nonaspherical planner obstruction is proved explicitly in Lemma 2.1 |
| Lueck, arXiv:0902.2480v3, Lemma 3.1, Theorem 5.3 and proof of Lemma 3.2 | Torsion freeness, finite CW type and the connected-sum pinch/free-product facts |
| May, A Concise Course in Algebraic Topology, Chapters 5, 10 and 17 Section 2 | CW and compactly generated conventions and rational Kunneth theorem |
| Dranishnikov--Sadykov, arXiv:1710.04711v2 | Free-product/wedge background, with normalization adjusted as stated |
| Neofytidis, arXiv:2212.08962v2, Question 5.5(b) and Corollary 1.3 | The source question and verified partial frontier |
| Daundkar--Santhanam--Thandar, arXiv:2304.01274v3, Proposition 5.3 | Wedge computation and connected-sum bounds, not a full prior connected-sum solution |

All source links appear in the paper's bibliography. The submission contains a natural-language argument; no Lean or computer-verification certificate is claimed.
