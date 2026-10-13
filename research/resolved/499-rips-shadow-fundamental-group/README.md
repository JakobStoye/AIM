# A six-point counterexample to Rips shadow injectivity

This package accompanies Kaiwen Jin's manuscript, *Six points with a contractible Rips shadow and nontrivial fundamental group*, submitted for [AIM problem 499](https://github.com/MColbrook/AIM/blob/1b7c7fd251c1643bb41f0e3cef38704bcef410fd/problems/499-rips-shadow-fundamental-group.md).

Six rational points in three-dimensional Euclidean space have a strict Vietoris–Rips complex that strongly deformation retracts onto a four-cycle. Its affine shadow is contractible: it is the union of two convex quadrilaterals containing the origin. The shadow projection therefore kills a nontrivial fundamental-group generator. Scaling and adding zero coordinates give a counterexample at every positive scale and in every ambient dimension at least three.

The manuscript gives the full analytic argument. The Python supplement checks exact rational distances, the complete simplex list, the carried vertex retraction, and an integer cocycle detecting the displayed cycle. It does not compute arbitrary fundamental groups or replace either homotopy proof.

## Materials

- [Complete manuscript](paper/rips_shadow_counterexample.pdf) and [editable LaTeX source](paper/rips_shadow_counterexample.tex).
- [Correspondence with the original target](TARGET_COMPARISON.md).
- [Exact finite checker](src/exact_geometry.py) and [tests](test/test_exact_geometry.py).
- [Payload checksums](manifest.json).

## Reproduction

Run from this package directory using ordinary Python 3 without the `-O` option:

```sh
python3 src/exact_geometry.py
python3 -m unittest discover -s test -v
```

Only the Python standard library is required. The tests cover all fifteen distance types, strict threshold behavior, and a scaled witness padded to dimension nine. The default checker prints normalized exact squared distances and the four maximal triangles. The submitted package was checked with Python 3.13.3; no floating-point tolerance is used.

Compile the manuscript with a LaTeX installation providing the packages listed in its preamble:

```sh
pdflatex -halt-on-error -interaction=nonstopmode paper/rips_shadow_counterexample.tex
pdflatex -halt-on-error -interaction=nonstopmode paper/rips_shadow_counterexample.tex
```

## Attribution and review

The target is Conjecture 7.2 of Adamaszek, Frick and Vakili, [*On homotopy types of Euclidean Rips complexes*](https://arxiv.org/abs/1602.04131v1). The planar isomorphism theorem is due to Chambers, de Silva, Erickson and Ghrist, [*Rips Complexes of Planar Point Sets*](https://arxiv.org/abs/0712.0395v1). The manuscript cites the precise statements and elementary topology used in the proof.

OpenAI Codex helped develop and analyze the construction, check arithmetic, and draft the paper and code. A same-context AI audit and a separate fresh-context, same-vendor AI manuscript review found no unresolved major objection within their recorded scopes. No human review or Lean verification is claimed. No detailed review report is submitted; independent mathematical review is requested. This package reports a proposed counterexample and does not change the catalogue's classification.
