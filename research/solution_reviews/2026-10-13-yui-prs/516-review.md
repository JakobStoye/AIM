# AIM 516: independent review of PR #75

Reviewed 13 October 2026 at head `49687d565a727aeda3ae7a9134ad628a6fc48d4a`. Verdict: **Solved** following a complete independent AI mathematical audit. This is not human review or Lean verification; the submission discloses Codex assistance.

[Proof](../../solutions/kaiwen-jin-516/paper/main.pdf), [source](../../solutions/kaiwen-jin-516/paper/main.tex), [finite verifier](../../solutions/kaiwen-jin-516/verification/verify_small_graphs.py).

## Target and outcome

The target concerns a **uniformly sampled labeled DAG**, with a uniform-in-size tail estimate for its Markov equivalence class, with logarithmic exponent arbitrarily close to two. The manuscript proves the stronger tail with exponent proportional to `(log t/log log t)^2`, and a Gaussian tail for the number of vertices incident to reversible edges. It also explains why the stronger unmodified exponent `(log t)^2` cannot hold uniformly. The stated target is completely addressed.

## Graph-theoretic reduction

I checked the imported essential-graph characterization against its primary author text. The essential graph is a chain graph, its undirected components are chordal, and it contains no induced configuration of an arrow followed by an undirected edge. From this last condition, adjacency to an outside parent propagates along an undirected path in a component. The chain-graph property forces every such additional adjacency to be an incoming arrow: a reverse arrow would create a semidirected cycle. Thus all vertices of a component have the same outside parents. Its internally oriented graph has no unshielded collider, since its permitted orientations are perfect. The component quotient is acyclic. Reversible edges cannot be collider edges because their orientation changes across equivalent DAGs. Counting all linear orders gives class size at most the product of component factorials, hence at most the factorial of the total number of reversible-edge vertices. This is an upper bound, so duplicate orders do not invalidate it.

## The crucial uniform-DAG prefix comparison

The source layers are not replaced by an independent-edge model. Their exact weight is obtained by counting labels, prohibiting within-layer edges, requiring each vertex of a later layer to have a parent in the previous layer, and freely choosing all remaining edges. Conditional on the ordered layers, nonadjacent-layer edge bits are independent fair bits; no such claim is made for adjacent layers.

Replacing one layer of size `y` by `y` singleton layers is injective at fixed layer index and `y`. Direct cancellation of the weight gives the displayed ratio with exponent `-binom(y-1,2)+s`, where `s` is the following layer size. On the designated small-`s` event this is at most `2^(-y^2/4)`. The recurrence passes to a next-layer threshold greater than twice the current threshold, and iteration terminates beyond `n`. This proves the claimed all-size Gaussian layer tail. Adding a unique source, with mandatory edges to the old sources and arbitrary remaining outgoing edges, gives the normalizer comparison. Its fixed small-source probability follows from the just-proved layer tail.

I reconstructed the exact ordered-rank prefix identity separately. Uniformly ordering each source layer introduces its factorial denominator. A prefix ending at a layer boundary has its own source layers determined by its induced graph; the remaining layer vector has the original weights, with precisely one interface factor. Summing those remaining weights is bounded by the smaller normalizer. Its ratio to the full normalizer is controlled above. This proves comparison to independent fair forward edges on the prefix, with the stated exponential factor. A prefix not respecting a possible layer boundary contributes zero. If the first boundary after rank `L` exceeds `2L`, one of the first `L` layers has size exceeding `L`; the layer tail controls this exception. Summing at most `2L` possible boundary positions yields the advertised transfer inequality. There is no assumption that the independent-edge law and uniform-DAG law coincide.

For a possible deep noncollider edge with larger rank `b`, removing the at most six nearby source layers still leaves at least `b/3` earlier witnesses on the good layer-size event. Each witness's two relevant edge bits are distinct, fair and independent of all others, because its layer is nonadjacent to both endpoint layers. One orientation/absence pair creates an unshielded collider with probability one quarter. The edge's own presence constraint is independent of these witnesses. Union bounds and the layer exception give the stated exponential deep-edge tail.

## Quadratic cost and completion

For a fixed ordered set of `r` ranks, the no-collider estimate uses a matching in the missing-edge graph on its first half. A large matching gives independent forbidden pairs for every later vertex; absence of such a matching leaves a large clique, which itself has a quadratic edge cost. Both alternatives produce the explicit quadratic exponent.

For selected reversible-component blocks, all-or-none common-parent restrictions give cross-block cost at least one quarter of `s^2-sum r_i^2`. Internal no-collider costs supply a positive multiple of `sum r_i^2`. Their sum is a positive quadratic cost in `s`, with only a linear error. The count of selected ranks, partitions, and possible quotient orders grows at most as `exp(O(s log m))` when the inspected prefix has length at most `m^2`. The quadratic cost therefore dominates uniformly.

If at least `m` vertices are incident to reversible edges, either take `m` vertices from one large component or accumulate whole smaller components to obtain between `m` and `2m` vertices. The necessary common-parent and no-collider conditions survive taking a subset of a component; connectedness of that subset is unnecessary for this counting bound. Outside the deep-edge exceptional event the chosen vertices lie in the inspected prefix. Choosing its length to be a sufficiently small fixed multiple of `m^2` leaves enough quadratic cost after the prefix transfer factor. This yields the Gaussian tail. Passing through the factorial upper bound gives the required logarithmic tail and all exponents `2-epsilon`. Finally, the `n!` total-order orientations of a complete skeleton, together with the elementary upper count `n! 2^{binom(n,2)}` for all DAGs, really rules out a uniform quadratic-log exponent. This ancillary sharp-scale claim was checked too.

## References and finite replay

Both bibliography entries are real, with matching metadata. [Andersson–Madigan–Perlman](https://stat.uw.edu/sites/default/files/files/reports/1995/tr287.pdf), University of Washington Technical Report 287 (1995), printed pages 10–11, Propositions 4.1–4.2 and Theorem 4.1, give exactly the essential-graph facts used above. The eventual journal citation, Annals of Statistics 25(2) (1997), 505–541, DOI [10.1214/aos/1031833662](https://doi.org/10.1214/aos/1031833662), is correctly identified. The author PDF was read directly after the web viewer failed on its certificate chain.

[Schmid–Sly, version 2](https://arxiv.org/html/2209.04395v2), revised 28 September 2024, has the stated title/authors, earlier tail and open exponent question in Theorem 1.1/introduction, and tower weights and layer estimates in Section 3. The submission's source-layer convention is the reversal of their sink-layer convention and is derived explicitly. Their previous tail is background, not a substitute for the new quadratic estimate.

All 158 verifier lines were inspected before execution. The script exhausts all ternary edge choices on four vertices, rejects directed cycles, derives equivalence classes from skeletons and colliders, and uses exact integers/fractions. Replay passed: 543 DAGs, 185 classes, 1,152 graph/order pairs, 58 exact prefix identities, eight layer-vector identities and 496 component/member checks; largest class has size 24. These are supplementary finite diagnostics, not premises of the all-size argument.

## Presentation and scope

The complete manuscript and ancillary files were read, and all eight PDF pages were inspected. The theorem, proofs, finite-check claims and bibliography agree with the source and replay; no clipping or unresolved references were found. This acceptance decision rests on reconstructing the all-size proof, not on finite enumeration or PDF rendering. No independent human or formal verification is claimed.
