# Correspondence with AIM problem 633

Target: [Local potential bases on Freudenthal meshes](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/633-freudenthal-local-potential-basis.md),
repository revision `c9929805cece044705abaaebe1cebddac1ba11a6`.
Manuscript: [Local potential bases on Freudenthal meshes](paper/main.pdf),
Kaiwen Jin, 10 October 2026.

This comparison is between the published problem statement and the complete
submitted manuscript. The submission is a complete solution claim supported
by analytical coverage arguments and essential exact finite witnesses;
independent mathematical review remains outstanding.

| Original requirement | Manuscript location and result | Scope |
|---|---|---|
| Unit cube divided into `N^3` cubes, consistently oriented six-tetrahedron coordinate-chain subdivision | Section 2, mesh definition (1) | Same domain and tetrahedra for every integer `N >= 1` |
| Continuous real vector potentials, piecewise total degree at most `k+1`, with continuous curl | Section 2, space definition (2), with `d=k+1` | Same actual potential space; no quotient by gradients |
| No imposed boundary condition; boundary vertices included | Section 2 definition and support criterion; Section 3 boundary coverage | Same unrestricted space and closed stars, including physical-boundary stars |
| Every `N >= 1` and integer `k >= 5` | Theorem 2.1 and its completion in Section 3.3 | All `d >= 6`; degree six in Section 3.1, higher degrees in Section 3.2, one-cube case in Section 3.3 |
| A basis whose every member is supported in a single vertex star, equivalently the stated sum of local spaces | Theorem 2.1, decomposition (3); Section 2.3 normal form; Sections 3.1–3.3 local generation and selection | Full affirmative support conclusion for the potentials themselves |
| Uniform decomposition norm is a further question | Abstract, Introduction and final paragraph | No norm bound or multigrid convergence claim is added |
| Relationship to Farrell–Mitchell–Scott Conjecture 2(b) | Introduction and reference FMS, Section 3.3, Conjecture 2(b) of that source | Direct target attribution; that conjecture is not assumed proved |
| Related divergence right-inverse result is not the requested potential-basis construction | Introduction and reference DMYZ, Theorem 2.1 | Kept separate; neither cited paper is a theorem dependency of the construction |

The additional dimension formula is stated for `N >= 2, d >= 6`, and also
for `N=1,d=6`; it is not asserted for `N=1,d>6`. This restriction does not
restrict the all-parameter local-basis conclusion. The one-cube star at the
origin contains the entire mesh, supplying the remaining support cases.

## Proof-critical computation and reproduction

Section 3.1 proves why bounded degree-six windows transfer both row-space
identities, unit pivots and local repairs to every grid, including the
small-grid certificates and physical boundary. Section 3.2 proves why the
finite type, shifted-boundary and face-profile traversals cover all higher
degrees through affine conditions on unbounded parameter regions. Section
3.3 counts free types exactly and completes the theorem. Section 4.2 states
the finite predicates, integer bounds and computing trust base.

The accompanying `verify_all.py` replays the proof-critical predicates using
the supplied rule/matrix witnesses. The ten Section 4.3 construction cases
are implementation regressions, not extrapolations to untested parameters.
See [reproduction instructions](README.md#reproduction) and
[actual execution evidence](VERIFICATION.md). No formal or independent human
certification is asserted by this correspondence document.
