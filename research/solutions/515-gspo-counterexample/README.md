# Counterexample to Greedy Sparsest Poset consistency

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This package submits a complete counterexample claim for [AIM 515](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/515-greedy-sparsest-poset-consistency.md), at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
For the stated Markov and restricted-faithfulness assumptions, a six-variable Gaussian model has a starting poset whose entire reachable search component consists of three graphs with eight edges each. The global minimum is six edges. All three component graphs are fixed by both adjacency constructions and maximal ancestral closure.

The Gaussian input is the structural equation model in Figure 1 of [Bernstein, Saeed, Squires and Uhler (2020)](https://proceedings.mlr.press/v108/bernstein20a.html). The contribution submitted here is the analysis of its closed search component. This does not refute their theorem about global sparsest graphs, and it gives no conclusion under full faithfulness.

- [Complete manuscript](paper/counterexample.pdf) and [standalone LaTeX source](paper/counterexample.tex).
- [Comparison with the original target](TARGET_COMPARISON.md).
- [Verification commands, coverage and limitations](VERIFICATION.md).
- [Exact mathematical certificate](numerical_case/counterexample.json), [definition-based graph and rational-arithmetic code](src/dmag_reference.py), [checker](scripts/verify_certificate.py), and [controls](test/test_certificate.py).
- [Public file manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS).

The proof includes all 240 Gaussian conditional-independence numerators, reconstruction tables, and a complete argument excluding every other single mark change. The checker reproduces these finite calculations from the supplied covariance and exhaustive path definitions; a full-poset discovery search is not needed.

## Reproduce

From this package directory, using Python 3.10 or later with no third-party packages:

```sh
python3 scripts/verify_certificate.py
python3 -m unittest discover -s test -p 'test_*.py' -v
```

Run Python without `-O` or `-OO`; the checker rejects those modes. The expected result is `PASS`, 240 Gaussian queries, three reachable vertices with eight edges, and a global minimum of six. The six tests include controls for collider descendants, a nonmaximal ancestral graph, pivoted rational determinants, and rejection of a changed covariance.

To build the standalone manuscript with a standard TeX installation:

```sh
mkdir -p paper/build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper/build paper/counterexample.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper/build paper/counterexample.tex
```

## AI use and review

OpenAI Codex assisted with discovery, exact-arithmetic code, proof development, source checks and writing. A separate fresh-context OpenAI Codex agent, with no manuscript preparation involvement, reviewed the complete seven-page manuscript, its three references and the finite calculations reconstructed from the paper; it found no major or substantive minor objection within that scope. The final source differs only by a checked reference URL. The submitted claim has not been certified by a human reviewer or a proof assistant. No detailed AI review report is submitted; independent mathematical review is requested. Catalogue classification remains subject to maintainer review.
