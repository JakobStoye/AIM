# Comparison with the pinned AIM 138 target

The source is [Problem 138 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/138-unique-minimum-time-positive-heat-control.md), “Uniqueness of nonnegative heat controls at the minimum time.” This package claims the entire target, with no restriction to a finite set of modes, a parameter subrange, or an a priori symmetric or impulsive control class.

| Source clause | Manuscript location | Correspondence |
|---|---|---|
| Every a,b>0 with a different from b | Theorem 1.1, p.2; ratio r=a/b in (4) | Both heating (r<1) and cooling (r>1) are included; the positive scaling is invertible. |
| Heat equation on (0,1), constant initial a and target b, two nonnegative Dirichlet controls | (1), p.1 | The equation, geometry, two controls and constant-state assumptions are identical. |
| T_* is the infimum for bounded nonnegative controls | (2), p.1; Lemma 2.1, pp.3-4 | The definition is retained. Positive smoothing proves equality with the L1 and closed-measure moment infima, and compactness proves attainment at this same time. No common amplitude cap is added. |
| Nonnegative finite Radon measure pair on [0,T_*] | (3) and Theorem 1.1, p.2; (5), p.3 | The admissible class is exactly the original positive pair. The average/difference map is invertible under total-variation domination. |
| The displayed sine identity for every integer k>=1 | (3), p.2; (6)-(7), p.3 | The parity sign, decay factor, denominator and time orientation match the pinned statement. All odd equations prescribe the average and all even equations constrain the signed difference. |
| Exactly one admissible pair at the attained minimum time | Proposition 4.5, pp.10-11; final proof, p.11 | Critical tests determine the average and force every dominated even-moment difference to vanish. Inverting the parity map yields the unique original pair. |
| Closed integration interval, including endpoint atoms | Definition preceding (3), p.2; Lemmas 2.1-2.2; final proof, p.11 | One-sided smoothing retains both endpoints, and every final test inequality is on the closed interval. No endpoint exclusion is imposed. |

The additional conclusion is equality of the two boundary measures. Symmetry is obtained from the signed-difference rigidity argument; it is not imposed on the original admissible class.

The finite cones in the proof are auxiliary analytic objects. Their exact limit and a common fixed coefficient subsequence are established before comparing arbitrary critical measures. No finite discretization or numerical test substitutes for the all-mode conclusion. Standard finite-measure integration and compactness, the stated heat null-control interface, and the cited sparse-power estimates are used with their hypotheses explained in the paper.

This is a complete solution claim pending independent mathematical review. It does not claim a quantitative formula for T_*, nonconstant-state uniqueness, whole-problem formal verification, or repository acceptance. The manuscript and package README disclose actual AI involvement and review limits.
