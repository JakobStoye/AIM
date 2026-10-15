# AIM 531: independent review of PR #99

Date: 2026-10-15. Reviewer: OpenAI Codex, independent AI review in the receiving repository; no human review or Lean verification is asserted.

PR: [#99](https://github.com/MColbrook/AIM/pull/99). Reviewed head: `e2dea2b4ec0c80368c680466fe1d7dded861212c`.

Outcome: **Solved** — An exact integral chain certificate disproves the proposed all-k homology formula at k=5.

Proof: [torus_grid_counterexample.pdf](../../../research/solutions/yuiyuiui-531-integral-counterexample/paper/torus_grid_counterexample.pdf). The original problem page, complete manuscript, target comparison, package README and other supplied explanatory material were compared.

## Mathematical audit

The geometric reduction identifies the liftable-clique subcomplex $`M`$ with the nerve of open taxicab balls on the torus. The coordinate change to sum/difference coordinates turns those balls into squares. The strict intersection condition becomes the integer distance bound used by the closed scale-five Rips complex. Since the period is thirteen, the relevant ball intersections lift uniquely and convexly; the cover fills the torus. Hence $`M\simeq T^2`$, and the long exact sequence gives $`H_4(K;\mathbb Z)\cong H_4(K,M;\mathbb Z)`$.

The relative complex is not obtained by truncating a large simplex enumeration at an arbitrary dimension. The manuscript proves that every nonliftable clique contains an anchored wrapping triangle; extension by all common-neighbor cliques and all translations therefore exhausts it. The independent verifier does a separate all-origin-clique enumeration and prunes only when the current clique together with all candidates lies in a known liftable diamond. Its liftable test uses the full list of338 diamonds. These two enumeration semantics and their integer signed-boundary conventions were read in full, along with the generator and all eight tests.

Each recorded pivot is an actual unit $`\pm1`$ in the current integral chain complex. The verifier checks the changed upper-boundary row and the corresponding lower-boundary linear combination at each cancellation, so every step is an integral elementary contraction. It never substitutes a rank over a finite field for integral homology. Starting relative chain ranks in degrees two through six are1352,4394,4394,1690,338. After6056 unit cancellations the residual ranks are2,28,26 in degrees two, three and four, with no degree-five group. Its sole nonzero boundary has24 nonzero columns, and a nonzero24-rank minor modulo three proves rational rank24. Consequently its degree-four integer kernel is free of rank26−24=2; no incoming degree-five boundary remains.

A single admissible $`k=5`$ counterexample suffices to refute the all-$`k\ge5`$ assertion. The certificate establishes exactly the degree-four discrepancy required for that refutation; it is not being promoted into a theorem describing every other homology group or every scale.

## References and scope

The target was checked against [Adams and coauthors](https://arxiv.org/html/2502.07134v2), including the integral interpretation of Question8.4 and the distinction between the displayed finite-field data and integer homology. The geometric nerve and relative-chain arguments are supplied explicitly in the submitted manuscript. Generator and verifier use only Python's standard library.

## Delivery checks

The full five-page rendered manuscript was inspected. The receiving repository independently ran the complete verifier, all eight unit tests and certificate generator, with exact regenerated JSON equality. It also deliberately changed a unit-pivot sign, a residual-matrix entry and the advertised rank; each was rejected with a specific ValueError. Receipts are 531-replay.json and 531-corruption-controls.json in this review directory. These executions support the finite certificate; the mathematical reduction was reviewed separately.
