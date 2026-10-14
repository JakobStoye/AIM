# Target comparison

The package addresses AIM problem 571, “Counting half-integral polygons with
collinear interior lattice points,” at statement revision
`a153f469ee0ea64e876b2ad97c79d252c19a3e22`.
The mathematical target is also Bohnert-Springer Conjecture 3.7.
The manuscript and its supplement are a computer-assisted complete solution
claim; maintainer classification and independent mathematical review remain
separate.

| Original requirement | Manuscript location | Scope |
| --- | --- | --- |
| Two-dimensional convex polygons with vertices in `(1/2)Z^2` | Introduction and Theorem 1.1; Lemma 2.2 reconstructs the polygons from chains | Identical; integral polygons are included |
| Exactly `i` collinear interior `Z^2` points | Theorem 1.1; Section 2.1 fixes the row, and Lemma 2.2 proves the inverse correspondence | Identical; no additional interior row is admitted |
| Every integer `i >= 3` | Theorem 1.1; Section 4.2 keeps `n=i+1` unbounded; Section 4.3 extracts all coefficients | Full range; finite regression data are not the infinite-parameter bridge |
| `GL2(Z)` and integer translations | Introduction and Section 3.1 recover every normalized equivalence | Identical; half-integral translations are excluded |
| The exact seventh-degree formula | Equation (1.1); Sections 4.2-4.3 and the final proof | Full rational functions, Burnside multiplicities and exact coefficient identity |
| Applicable published normalization | Proposition 2.1 cites Bohnert-Springer Proposition 3.5, pp. 1248-1249 | `k=2` and `i>2` satisfy its hypotheses, including polygons of denominator dividing two |
| Computational evidence | Lemma 4.1 and the following software statement; complete compact inputs/results and drivers in the supplement | Trusted exact-software calculation; declared degree/LLL/version limits; no independent counting certificate |

The author/contact fields in the manuscript are Kaiwen Jin and
yui.ui.siki@gmail.com. The manuscript contains an AI-use statement and genuine
source citations. The package does not claim formal-kernel verification,
independent human certification, novelty certification or upstream acceptance.
