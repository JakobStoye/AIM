# Exact six-variable case

`counterexample.json` supplies the covariance, invertible noise transform, the true graph and three component graphs, all 240 almost-principal determinant numerators and graph-separation sets, and the reconstruction tables. It contains small proof-critical integer data, not disposable trajectories or a large search output.

Vertex labels in the data are 1 through 6; the graph implementation internally uses 0 through 5. For each increasing pair, two bits encode absence (0), an edge from the smaller to the larger vertex (1), the opposite directed edge (2), or a bidirected edge (3). Pair order is lexicographic. Conditioning-set codes in `minor_tables` use the four remaining vertices in increasing order, with bit weights 1, 2, 4, 8. The `ancestors` masks include each vertex itself. Conditional covariances are exact rational strings.

The distribution is the Gaussian structural equation model in [Bernstein, Saeed, Squires and Uhler (2020), Figure 1](https://proceedings.mlr.press/v108/bernstein20a.html). The submitted paper analyzes its search component and credits that source.

From the package root, run `python3 scripts/verify_certificate.py` to recompute these data and the transition list. See [VERIFICATION.md](../VERIFICATION.md) for the complete command and scope. No all-poset discovery search is required.
