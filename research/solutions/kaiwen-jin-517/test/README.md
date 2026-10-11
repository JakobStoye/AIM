# Validation suite

Run from the repository root:

~~~bash
PYTHONPATH=src python3 -m unittest discover -s test -v
~~~

The independent radial reference uses mpmath.expm at 70 decimal digits
to propagate the unscaled ODE matrix. It does not call the production
projector formula. Exact isotropic and polar-anisotropic solutions check
the energy normalization and exponents.

Other tests cover:

- core, interface and arbitrary annular inner radii in both dimensions;
- subdivision of constant layers and geometric/coefficient scaling;
- large exponential growth represented in logarithms;
- multiplicities, prefix counting and determinant comparisons;
- independent generalized-eigenvalue formulas and basis invariance;
- positive-definiteness, symmetry, finite-value and parameter validation;
- copying of coefficient input arrays.
- clear failure for unsupported core and shell dynamic ranges.

Tolerances belong to the individual tests. Reference agreement and
invariance measure implementation reliability for these inputs; they
do not certify the continuum theorem or every floating-point input.
