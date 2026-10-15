# AIM 532: independent review of PR #102

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#102](https://github.com/MColbrook/AIM/pull/102). Reviewed head: `cdebeeb97d00ca40e2250d85b557598789db7b1b`.

Outcome: **Solved** — The closed Rips complex of the2k-by-2k torus grid at half its diameter has the full conjectured wedge homotopy type for every k>=3.

Proof: [torus-grid-half-diameter.pdf](../../../research/solutions/532-torus-grid-half-diameter-homotopy/paper/torus-grid-half-diameter.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

Each adjacent-row or adjacent-column band is a cross-polytope boundary: its only missing edges are the opposite matched pairs. The chosen alternating facet in each band is maximal in the whole Rips complex and belongs to no other band, since any vertex outside it is too far from a selected vertex. Deleting those $`4k`$ facets leaves a subcomplex $`K^-`$. The remainder of each band is a ball that contracts the corresponding attaching sphere, so restoring the facets wedges on exactly $`4k`$ spheres of dimension $`2k-1`$. This uses null attaching maps, not a count of top-dimensional simplices alone.

The union $`L^-`$ of the punctured bands has a good subcomplex cover with nerve the join of two cycle graphs, hence is homotopy equivalent to $`S^3`$. To compare it with $`K^-`$, the proof shows that every Rips clique projects into a closed coordinate semicircle in at least one coordinate. The circle-vector inner products are nonnegative for pairs in a clique. If the origin is in their convex hull, the squared first-coordinate sum for an appropriate weighted vector is strictly positive; otherwise a separating vector already supplies an open hemisphere. Both cases give the required coordinate semicircle.

The finite-cylinder induction is explicit. Adding the last column gives a union of its stars, and the intersection with the previous cylinder has a nerve equal to a simplex boundary: every proper collection admits a cone point one column earlier, while the whole collection has empty intersection. Its attaching map is null because the previous cylinder is connected through the required dimension. Thus the cylinder is a wedge of its adjacent-band spheres. Removing the selected facets kills precisely those spheres; homology vanishes and simple connectivity is unchanged since the removed facets have dimension at least five. The punctured cylinder is contractible. Finite rectangles are handled by the taxicab-ball nerve and the coordinate-clamping retraction of its union to the rectangle.

The coordinate-semicircle cover now compares $`L^-`$ and $`K^-`$ on every intersection: rectangles and cylinders are contractible on both sides, antipodal-pair and singleton restrictions coincide, and empty restrictions coincide. An induction using the natural integral Mayer–Vietoris sequences gives the homology isomorphism. Shortest grid paths replace Rips edges through retained simplices; unit-square homotopies commute their steps, and full rows and columns contract the resulting loops. Therefore $`K^-`$ is simply connected. Hurewicz and homology Whitehead upgrade its integral homology to $`K^-\simeq S^3`$. Restoring the facets proves the full wedge formula. The separately known $`k=2`$ case is not improperly used in the higher-dimensional deletions.

## References and scope

The target, closed-scale convention and taxicab-grid nerve lemma were checked in [Adams and coauthors](https://arxiv.org/html/2502.07134v2), especially Corollary4.3 and the null-union lemma. Björner's Topological Methods, Theorems10.6(i) and10.7, has the needed finite subcomplex/open good-cover forms. The Hatcher cellular-approximation, Hurewicz and homology-Whitehead applications have their connectivity/CW hypotheses proved in the submission. All cited bibliography entries and manuscript/PDF titles agree.

## Delivery checks

All six PDF pages, including the cylinder and semicircle comparisons, were visually inspected. The TeX and PDF have different basenames; the reviewed proof link is the actual submitted PDF. Complete ancillary prose and target comparison were read. No finite calculation is substituted for the all-k proof and no Lean certificate is claimed.
