# Package guide

The `freudenthal` package uses potential degree `degree = d = k + 1`.
The manuscript's locality range is `N ≥ 1, d ≥ 6`.

```python
from freudenthal import BernsteinSpace, Mesh, PotentialBasis, construct_basis, dimension

mesh = Mesh.build(2)
space = BernsteinSpace.build(mesh, 7)
A, face_rows = space.curl_constraints(all_components=True)
basis = construct_basis(N=2, degree=7)
assert len(basis) == dimension(2, 7)
report = basis.verify()
```

`Mesh.vertices` are integer cube coordinates on `[0,N]^3`; tetrahedra index
those vertices. `BernsteinSpace.nodes` are integer coefficient labels on
`[0,Nd]^3`, not nodal point values. A row of `basis.coefficients` uses columns
`3*q_id + component`, with components indexed by `0,1,2`.
`basis.owners[i]` is the vertex whose closed star contains basis row `i`.
The full constraint matrix contains all three Cartesian curl jumps, divided
by the common physical scale `d*N`.

## Construction branches

* At `d = 6`, small grids use fixed integer bases. Grids `N ≥ 5` translate
  normal-form rules and local repair parts, then select independent local
  generators by exact modular elimination.
* At `N ≥ 2, d ≥ 7`, clipped canonical coefficient types give the normal form,
  its unit pivot block and a local owner for every canonical kernel row.
* At `N = 1, d > 6`, modular elimination and rational reconstruction produce
  an integer kernel, which is accepted only after exact membership and rank
  checks. All tetrahedra share a vertex, so every accepted row is local.
  Reconstruction can fail and raises an error rather than returning an
  unverified basis. No closed dimension formula for this branch is claimed.

By default `construct_basis` verifies its result. The uniform theorem also
requires the analytical coverage proof and the full `verify_all.py` replay;
an isolated instance test does not certify all parameters.

## Evaluation and storage

```python
potential, curl = basis.evaluate(basis_id=0, point=[0.2, 0.3, 0.4])
potential, curl = basis.evaluate_on_tetrahedron(0, 0, [0.25, 0.25, 0.25, 0.25])
basis.save("numerical_case/results/example")
restored = PotentialBasis.load("numerical_case/results/example")
```

Physical evaluation includes the factor `N` in the curl. Floating-point
evaluation uses a direct Bernstein formula; arbitrarily high-degree numerical
stability is not promised. Construction coefficients and certification are
integer, separately from floating-point evaluation.

Saving requires an empty directory. It writes `basis.npz`, optional
`normalform.npz`, `metadata.npz` and `summary.json`. Loading disables NumPy
pickle support and rechecks the actual saved coefficients by default. Sparse
integer multiplication checks conservative accumulation bounds before using
signed 64-bit arithmetic and raises on unsafe bounds.

The tests independently derive affine gradients, compare modular ranks on
two primes, evaluate a known global quadratic vector polynomial, compare
both traces on internal faces, and reject corrupted storage and wrong owners.
