# Correspondence with AIM problem 499

Target: [Injectivity of the Rips shadow map on fundamental groups](https://github.com/MColbrook/AIM/blob/1b7c7fd251c1643bb41f0e3cef38704bcef410fd/problems/499-rips-shadow-fundamental-group.md), at repository revision `1b7c7fd251c1643bb41f0e3cef38704bcef410fd`.

The question asks whether the affine shadow projection is injective on fundamental groups for every finite Euclidean sample, every positive strict Rips scale, and every sample base vertex. A single admissible loop killed by this projection refutes the universal assertion. The submitted theorem supplies such a sample at every scale and in every ambient dimension at least three.

| Requirement | Location and supplied argument |
| --- | --- |
| Nonempty finite Euclidean sample | Theorem 1 and its proof give six distinct rational points in dimension three. |
| Euclidean distances and strict diameter threshold | The proof's complete fifteen-pair distance table has no threshold equality. It gives exactly the four maximal triangles in display (1). |
| Abstract Rips realization | The vertex map and the homotopy following display (1) give an explicit strong deformation retraction onto the four-cycle. |
| The actual affine shadow map | The introductory definition and the two quadrilaterals in the proof use the affine image of each of those four maximal triangles. |
| A nontrivial based loop | Display (2) is a generator of the infinite cyclic fundamental group of the abstract complex. |
| The loop becomes null-homotopic after projection | Display (3) proves one quadrilateral convex; an explicit isometry treats the other. Their common origin gives an ambient radial contraction of the whole shadow. |
| Every sample base vertex | The proof uses connectedness of the complex and contractibility of the shadow to obtain the same noninjectivity at every sample vertex. |
| Remaining ambient dimensions and every positive scale | The final proof paragraph appends zero coordinates and scales points and threshold together. The source imposes no full-affine-dimension or generic-position requirement. |
| Known planar cases | The example starts in dimension three and preserves the cited planar isomorphism theorem. |

The result concerns individual finite samples at a fixed scale. It is not a limit theorem, a dense-sampling claim, or a surjectivity counterexample. In particular, the older four-dimensional surjectivity example is not used as evidence for the present injectivity failure.

The exact Python checks are supplementary finite verification; the manuscript contains the deformation retraction and shadow contraction. AI use and the request for independent mathematical review appear in the manuscript and package README.
