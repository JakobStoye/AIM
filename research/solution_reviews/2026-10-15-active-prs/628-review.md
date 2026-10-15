# AIM 628: independent review of PR #110

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#110](https://github.com/MColbrook/AIM/pull/110). Reviewed head: `d80c3a8d997fdead30bedef850ee5d7360974f39`.

Outcome: **Solved** — There exists a closed connected PL four-manifold with odd Euler characteristic and a finite flag-no-square triangulation.

Proof: [odd_euler_flag_no_square.pdf](../../../research/solutions/628-odd-euler-flag-no-square/paper/odd_euler_flag_no_square.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The quotient lemma requires graph displacement at least five at every vertex, not merely freeness on vertices. Under that condition each vertex star projects isomorphically, cliques lift, and a projected four-cycle lifts to a closed four-cycle: otherwise it would be a path of length at most four from a vertex to its involutive image. Thus an originally flag-no-square complex remains so, and a free realization gives an actual covering and preserves PL manifold links.

For a vertex deletion $`A=N-v`$ with antipodal600-cell link, take two copies of $`A`$ glued by the boundary antipodal map. The antipodal map has degree positive one on this three-sphere; opposite orientations on the two copies make the double an oriented PL four-manifold. The no-square property implies that all boundary neighbors of an exterior vertex form a clique. This excludes new nonflag cliques and squares across the seam. Swapping the copies is free, and a putative path of length at most four to the swapped vertex rotates to a short path from a boundary vertex to its antipode. One excursion reads as such a path in $`A`$; two excursions have length two apiece and can be replaced by boundary edges. Both contradict the assumed antipodal separation. The quotient lemma therefore applies. Counting the two-element face orbits gives Euler characteristic $`\chi(N)-1`$.

The required separation is proved rather than inferred from the intrinsic link alone. In the regular hyperbolic tessellation, the chamber fundamental-domain geometry gives distance at least the edge length $`e`$ between distinct vertices. Dual chamber regions centered at different tessellation vertices have disjoint interiors and contain balls of radius $`e/2`$, which proves that metric lower bound. The simplex Gram matrix gives $`\cosh e=2\varphi+1`$ and face angle $`\pi/5`$. The Lorentz cosine law then bounds the change of radial direction along any edge outside the center by $`\pi/5`$. Antipodal directions are distance $`\pi`$ apart, so any path outside the center joining antipodal link vertices has at least five edges.

A torsion-free orientation-preserving finite-index subgroup with arbitrarily large graph displacement gives a finite seed quotient $`Y`$. Choose two centers at graph distance ten; the displacement bound at least31 prevents a shorter quotient path and makes the relevant stars injective. The star-connected sum of two copies has $`\chi(N)=2\chi(Y)-2`$. A hypothetical four-edge antipodal shortcut in the untouched first vertex complement cannot reach the gluing boundary. Lifting it to the tessellation would close a loop of length at most six in the quotient; the displacement bound forces its endpoint to be the actual antipodal lift, contradicting the radial-direction estimate. Folding that untouched boundary yields $`\chi(Q)=2\chi(Y)-3`$, which is odd. This supplies the full closed-manifold existence statement; orientability of the final quotient is not needed by the problem.

## References and scope

The regular flag-no-square tessellation, residual-finiteness construction and arbitrary graph-displacement quotients are stated explicitly in [Kalmanovich–Nevo–Sorcar's primary version](https://arxiv.org/html/2310.13495v1), whose Lemma1.3 also gives the star-connected sum and Euler formula. It identifies the cited Przytycki–Świątkowski Remark4.4(2) as the construction source. The PS author-PDF fetch failed in this web tool; its published metadata and the matching construction as quoted in KNS were verified, and no additional unsupported PS hypothesis is used. [Heckman's author notes](https://www.math.ru.nl/~heckman/CoxeterGroups.pdf), Example1.27, Theorem4.17, Corollary4.19 and Proposition5.8, supply the600-cell antipodal symmetry, stabilizer/fundamental-chamber and hyperbolic coverage facts. The new radial bound and folding argument were reconstructed directly.

## Delivery checks

All five PDF pages, full target comparison and ancillary prose were read and visually inspected. The manifold, graph-displacement and parity requirements were checked separately. No computational search, human certification or Lean verification is asserted.
