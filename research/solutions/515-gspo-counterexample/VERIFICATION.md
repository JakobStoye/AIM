# Exact verification

The certificate is a small exact mathematical input, not a floating-point experiment. `src/dmag_reference.py` uses Python integer and `fractions.Fraction` arithmetic. No numerical zero tolerance or third-party dependency is used.

Run from this package directory:

```sh
python3 scripts/verify_certificate.py
python3 -m unittest discover -s test -p 'test_*.py' -v
```

The checker verifies positive definiteness through the displayed invertible noise transform, every Gaussian almost-principal minor, every pairwise graph separation, and all adjacency/orientation and restricted-faithfulness queries. The only additional independence is `(1,6 | empty)`. These endpoints cannot be discriminating-path endpoints because such endpoints share a neighbor. For Gaussian vectors, zero conditional cross-covariances also establish the group Markov statements, as explained in Section 3.

For each of `H0`, `H1`, `H2` and `G*`, it checks ancestry, maximality and the exact original two-pass-and-closure map. It tries every allowed single mark change, retains precisely those preserving DMAG status and the complete separation signature, and reconstructs their search successors. Finally it checks closure of the three-vertex component, its eight-edge count, the six-edge competing image, and the all-conditioning dependence of every true adjacency. These last dependences prove the global lower bound for every poset.

Expected successors, using the two-bit graph encoding documented in the source:

| Graph | Key | Successors |
| --- | --- | --- |
| `H0` | 1036190769 | `H1` |
| `H1` | 1036190737 | `H0`, `H2` |
| `H2` | 1036190739 | `H1` |
| `G*` | 289408017 | Used as a six-edge image; not part of the trapped component. |

The six unit tests exercise empty, pivoted, singular and rational determinants; collider activation through a conditioned descendant; chain blocking; a nonmaximal ancestral graph and its closure; a Gaussian fork; the complete certificate; and rejection of a changed covariance.

The manuscript is self-contained, including all finite tables. Its proof uses the stated local transformation theorem of Zhang and Spirtes (2005), Lemma 1; the checker independently compares separation signatures rather than assuming that theorem. Its general graph operations use exhaustive simple paths and conditioning subsets, so they are intended for these small exact checks, not as a scalable causal-learning implementation.

Successful finite checks support these explicit calculations. They are not a Lean formalization, a human mathematical audit, a proof for full faithfulness, or community acceptance. The final package was compiled and checked in isolation using only its included files; the dated local validation record is retained by the submitter.

## Recorded replay

On 2026-10-12 (UTC), the selected public files passed the commands above with Python 3.13.3, including an isolated-mode replay (`python3 -I scripts/verify_certificate.py` and `python3 -I test/test_certificate.py -v`). The actual result was `status=PASS`, `gaussian_queries=240`, `component_vertices=3`, `component_edges=8`, and `global_minimum_edges=6`; all six controls passed. A two-pass pdfTeX 1.40.27 build using only the exported standalone source produced seven pages with no undefined citations, references, or overfull boxes. Its rendered pages matched the supplied final PDF.
