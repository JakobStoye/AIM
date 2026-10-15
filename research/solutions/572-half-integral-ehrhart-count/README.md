# Counting Ehrhart functions of half-integral polygons

The manuscript counts distinct entire lattice-point functions for every
integer i ≥ 2, for convex polygons with vertices in (1/2)Z², exactly i
interior Z² points and at least two boundary Z² points:

    E(i) = (9i³ + 72i² + 175i + 106) / 2.

Its area/boundary signatures include integral polygons, period collapse and
all arrangements of interior points. The proof cites the complete published
computational classifications for the fixed small cases and five reported
minimum-width maxima. Their polygon catalogues are not independently rebuilt
by this companion package.

- paper/main.tex: full English manuscript, including source citations and
  AI-use disclosure.
- src/half_integral_ehrhart/: exact integer geometry, signature enumeration,
  body/top/line witnesses, rational certificate checks and source decoding.
- test/: independent point-count/dilation controls and certificate/schema
  rejection tests.
- numerical_case/: retained compact certificate inputs, source checksum
  manifest, reproduction scripts and compact validation results.

Python 3.12 was used. The core geometry/certificate tests use only the standard
library. Reading the published HDF5 files additionally needs the versions in
numerical_case/requirements-data.txt.

## Reproduce

From this directory:

~~~sh
python3 -m unittest discover -s test -v
python3 -O -m unittest discover -s test -v
python3 numerical_case/verify.py --output numerical_case/results/dual.json
~~~

To retrieve and compare the complete fixed-version source function sets:

~~~sh
python3 -m venv .venv
.venv/bin/python -m pip install -r numerical_case/requirements-data.txt
.venv/bin/python numerical_case/fetch_inputs.py
.venv/bin/python numerical_case/verify.py \
  --data-dir numerical_case/raw/source_data \
  --output numerical_case/results/source_comparison.json
~~~

The retrieval script checks the official MD5, pinned SHA-256 and byte size
before installing each file. Existing files must already pass those checks.
The comparator checks every coefficient matrix and exact set difference at
i=2,…,16. This comparison is relative to the published catalogue completeness;
it does not establish that completeness by matching counts.

Example without installation:

~~~python
import sys
sys.path.insert(0, "src")
from half_integral_ehrhart import witness, invariants, ehrhart_value

signature = (16, 2, 4)  # A=8*area(P), b(P), b(2P), at i=2
q_vertices = witness(2, signature)  # integer vertices of Q=2P
assert invariants(q_vertices) == (2, 2, 16, 4)
assert ehrhart_value(2, signature, 2) == 11
~~~

The line signature (16,2,8) has the same value at t=1 and a different value
at t=2, namely 13. It has no period collapse. Tests retain this distinction.

The 21 rational dual cases cover every required bounded width index for all
i ≥ 17. The manuscript proves the larger-index tail analytically. The verifier
rejects missing cases, negative or floating weights, unknown constraints,
failed coordinate domination and incorrect bounds even under python -O.

To build the manuscript with a TeX installation:

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=paper/build paper/main.tex
~~~

## Source data and scope

The external inputs are *Half-integral polygons with few interior lattice
points*, Justus Springer and Martin Bohnert, version 1.0.0,
[Zenodo 13928298](https://doi.org/10.5281/zenodo.13928298), CC BY 4.0.
numerical_case/input_manifest.json pins the full function files rather than the separate
collinear polygon dataset. The bibliography identifies the published
classification, coefficient formula, marginal bounds, minimizing-section
estimate and row-pairing source.

This is an exact verification supplement to a mathematics manuscript. It is
not a standalone numerical-method release or an independent reconstruction
of the published polygon catalogues.
