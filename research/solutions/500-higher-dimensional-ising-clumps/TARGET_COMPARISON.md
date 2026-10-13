# Correspondence with AIM Problem 500

Original source: [the complete statement at revision
1b7c7fd251c1643bb41f0e3cef38704bcef410fd](https://github.com/MColbrook/AIM/blob/1b7c7fd251c1643bb41f0e3cef38704bcef410fd/problems/500-higher-dimensional-ising-clumps.md).
Manuscript: [Reducible cube dynamics on regular contractible sets in four
dimensions](paper/cube_dynamics.pdf), Kaiwen Jin, 13 October 2026.

The original question asks whether the irreducibility and small-parameter
ergodicity theorem holds for every dimension at least two, on all regular
contractible pinned clumps. The manuscript answers this universal question
negatively by a dimension-four counterexample. It does not claim to settle
each dimension separately.

| Original clause | Manuscript correspondence |
| --- | --- |
| Unit cubes centered at integer lattice points | Section 1 uses the exact definition. Lemma 4.1 rescales a canonical fine grid, shifts half a unit and applies an integer translation. |
| Finite, contractible union | The witness is the compact ambient image of Lickorish's contractible four-manifold; Lemma 4.1 proves that finitely many whole grid cells exactly recover it. |
| Every sufficiently small punctured Euclidean-ball intersection is contractible at a noninterior point | Section 1 states the original regularity. Lemma 4.1 proves that exact condition for the witness using nested conical ball intersections and a manifold half-ball neighborhood. |
| All clumps containing the pinned cube | The witness is translated to contain the pinned cube. Proposition 2.2 and Proposition 3.3 apply to every intermediate four-dimensional clump, not a selected smooth or reachable subclass. |
| Removal leaves a clump and admits a strong deformation retraction keeping the moved cube in itself; addition is its inverse | Section 1 retains this rule. Lemma 3.1 restricts that very homotopy to the moved cube and uses regularity on both sides. Proposition 3.3 proves boundary preservation for both directions. |
| All allowed rates lie in the given positive range | Theorem 1.1 holds for every such pair of rates. They do not alter the move-graph components. |
| Irreducibility in every dimension at least two | The singleton and the witness have different boundary fundamental groups and cannot be joined by any finite path in dimension four. One such dimension refutes the universal assertion. |
| Nonexplosion and ergodicity with the normalizable all-state size-weighted law for sufficiently small positive ratio | Reducibility already makes the requested conjunction false for every positive ratio. Remark 4.2 additionally gives a positive total-variation obstruction to convergence from the singleton whenever the proposed law is normalizable. No separate failure of normalization, nonexplosion or stationarity is asserted. |
| Remaining dimensions at least three, without restricting to the reachable component | The result uses the complete dimension-four state space with no bounding-box constraint; dimension three remains a separate open question. |

The external four-manifold and cubulation results are credited explicitly.
Their application requires the manuscript's additional local-topology and
lattice-realization arguments. The package makes no claim of priority beyond
the presented argument and its stated citations.

Review status: a complete AI-assisted natural-language proof claim.
Codex checked the complete argument and cited-source applicability; a separate fresh Codex context reviewed the full manuscript and original-target correspondence, finding one minor citation-placement issue and no major objection. The final citation repair and two wording clarifications were checked by the authoring context.. No human or kernel certification, or upstream
acceptance, is asserted. This is a mathematical target comparison, not a
detailed AI review report.
