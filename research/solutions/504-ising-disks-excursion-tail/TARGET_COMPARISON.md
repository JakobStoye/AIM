# Target comparison for AIM 504

Original problem: [Exponential excursion tails for topology-preserving Ising disks](https://github.com/MColbrook/AIM/blob/1b7c7fd251c1643bb41f0e3cef38704bcef410fd/problems/504-ising-disks-excursion-tail.md), frozen revision `1b7c7fd251c1643bb41f0e3cef38704bcef410fd`.

Submitted manuscript: *The exponential excursion-height rate of planar Ising disks*, by Kaiwen Jin, October 13, 2026. [PDF](paper/ising_disks_excursion.pdf), [source](paper/ising_disks_excursion.tex).

| Original requirement | Manuscript location | Coverage |
| --- | --- | --- |
| Closed squares Q_z, regular contractible planar clumps | Section 1, model definitions | Same geometric and local regularity definitions |
| Deletion through a strong deformation retraction remaining inside the deleted square; addition is its inverse | Section 1 definitions; Lemma 2 and its proof | Exact legality, including the connector moves and extension of block homotopies |
| Pin Q_0 and start at the singleton; legal rates beta and 1 | Section 1; Section 2 conductance equation (2); Lemma 2 | Same chain; every constructed path retains Q_0 |
| Every real 0 < beta < 1/kappa | Theorem 1 and its concluding proof | Entire open interval, with no additional restriction or uniformity assumption |
| a_n counts area-n square-lattice self-avoiding polygons up to translation, with the same area growth constant | Section 1; Section 3 choice N=a_m and final m limit | No selected shape subclass or orientation quotient |
| Maximum over the first excursion until return after departure | Section 1 definition of xi; Section 2 equation (3) | Exact stopped hitting event, unchanged by holding times |
| Exact exponential limit over all integer thresholds | Theorem 1; equations (5)-(7) and final ceiling comparison | Full limit; the ceiling argument passes from block heights to every integer T |
| Equivalent eta_T limit with positive finite mu | Theorem 1, cited recurrence statement in Section 1, final proof paragraph | Exact equivalent conclusion |

The imported source is [Baryshnikov and Onaran, Journal of Applied and Computational Topology 10, article 16 (2026)](https://doi.org/10.1007/s41468-026-00248-w). Its Definition 4.2 and Theorem 5.1 supply planar indentability, Remark 6.3 and equation (4) supply the polygon/clump correspondence and rooted counting bound, and Theorem 6.5 with Definition 7.2 supplies the subcritical recurrence facts. The manuscript explicitly proves the rooted growth consequence and the normalization of its finite network.

The additional argument is the lower-conductance construction in Section 3: one-square concatenation, unique recovery of completed prefixes, and a unit-flow energy bound. The source's Lemma 7.10 supplies only the opposite bound and Conjecture 7.11 states the missing equality. The manuscript re-proves the used upper bound directly. No numerical extrapolation, mixing estimate or unproved conjecture is an input.

This is a complete analytic solution claim awaiting independent mathematical assessment. No partial or conditional target remains in the submitted argument.
