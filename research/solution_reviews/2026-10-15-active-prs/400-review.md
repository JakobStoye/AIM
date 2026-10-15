# AIM 400: radiative insulation and concentric balls

**PR:** [128](https://github.com/MColbrook/AIM/pull/128). **Date:** 2026-10-15. **Decision:** Solved. Reviewed head: `e9d45c98722999ecb5b4aeb19c2c4ba872631448`.

Independent OpenAI Codex AI audit; no human or Lean verification is claimed. All manuscript sections, references, README, target comparison and manifests were read, and all ten PDF pages were visually inspected.

[Proof](../../../research/solutions/400-radiative-insulation-concentric-balls/paper/main.pdf).

The argument retains every original parameter, including ambient parameter zero and dimension two, bounded Lipschitz outer sets without connectedness, measurable heated cores, and the option to leave insulation unused. Weak trace lower semicontinuity gives the actual minimum. Spherical averaging, weighted Cauchy–Schwarz and boundary convexity give the exact radial formula and continuity down to the bare ball.

I recomputed the scalar concavity calculation. For the radiation polynomial, G is Lipschitz and H(y)=y²/G(y) has nonpositive second derivative: the displayed numerator is the positive-coefficient polynomial obtained from q²q'q'''−(q'²−2qq'')². The zero-ambient case has its separate2/5 power law. Its continuous zero extension is concave as required for tail multiplication.

The zero extension of the boundary potential records its whole boundary cost as variation. Completing a square and weighted coarea allow rearrangement before optimizing the scalar dual parameter. The completed monotone graph includes both endpoint atoms and Cantor variation. Its one-dimensional area identities justify a single Borel function of level realizing the pointwise dual optimum, including plateaus and the top core. No singular drop is discarded.

Polygonal potentials approximate the relaxed cost from above with an explicit mesh error. Cutting off small positive levels permits a bound on the inverse potential derivative before microjumps are inserted. These inserted jumps exactly realize the frozen convex relaxed density; the subsequent errors tend to zero in the specified order. Multiplying the entire potential tail after a jump has a concave total cost. An endpoint either removes that jump or deletes the tail. Finite repetition gives a genuine H1 concentric-ball temperature, rather than leaving an inadmissible jump profile. This proves the full constrained comparison at every original volume budget.

All five references were checked. The published Bucur–Nahon–Nitsch–Trombetti paper really leaves the radiative constrained case open after Remark4. Amato–Gentile–Nitsch–Trombetti's Theorem2.1 has the required Euclidean perimeter normalization. Górny's coarea theorem and Corollary1.29 supply the bounded-Lipschitz trace characterization; its proof being omitted in those notes is accurately disclosed. Hunter's weak chain rule is supplemented by the written Borel representative argument. Leonardi–Vianello's published Theorems2.6,2.8,2.9 have the coarea/area/Gauss–Green content used here; the submission correctly distinguishes the printed interior-point typo in(2.5) from the boundary assertion in(2.6). The authors' preprint has the same theorem content with shifted equation numbering. No proof-critical citation is missing.

The complete source rebuilt successfully and matched the submitted PDF text. No unresolved mathematical gap was identified. The conclusion is restricted to the specified radiation polynomial; no arbitrary-potential or uniqueness result is claimed.
