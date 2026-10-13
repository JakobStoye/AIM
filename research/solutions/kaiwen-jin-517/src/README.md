# Numerical library

The elliptic_widths package depends only on NumPy and the Python standard
library. Public functions are exported from elliptic_widths/__init__.py.

~~~python
from elliptic_widths import (
    RadialCoefficient, log_radial_spectrum, expanded_spectrum,
    log_determinant_bound,
)
coefficient = RadialCoefficient(
    radii=[0.1, 0.5, 1.0],
    radial=[1.0, 4.0, 0.25],
    tangential=[1.0, 0.25, 4.0],
)
by_degree = log_radial_spectrum(3, coefficient, 0.5, 80)
included = expanded_spectrum(3, by_degree)
bound = log_determinant_bound(
    3, len(included), 0.5, 1.0, coefficient.alpha, coefficient.beta,
)
~~~

Each radii[i] is the outer endpoint of interval i; the first interval
starts at zero and uses a finite-energy regular power solution. Coefficients
and radii must be positive and finite, radii strictly increasing, and the
inner radius strictly between zero and the final endpoint. The constructor
copies inputs and marks those copies read-only.

log_radial_spectrum returns natural logarithms by positive degree. It
uses exact two-state propagation, removes the growing exponential and
records logarithmic rescaling. The inner radius can be in the core, inside
a layer or on an interface. Its convention is unit sphere area measure;
the energy is r^(d-2)*f(r)*q(r), with q=a_r*r*f'.

expanded_spectrum repeats and sorts only the supplied finite set with
sphere multiplicity. It does not certify an infinite ordering.
log_determinant_bound and log_singular_bound return one value per prefix;
spherical_degrees and multiplicity provide the corresponding counting.

generalized_eigenvalues(Q,G) requires real finite symmetric forms and a
positive-definite denominator. Cholesky whitening avoids explicitly forming
G^(-1)Q. A singular denominator is rejected. Symmetry tolerance is relative
to each form's infinity norm.

No spatial grid, quadrature or time-step parameter appears. Roundoff remains;
extreme contrasts can be unrepresentable in binary64. These routines do not
provide interval enclosures. Unrepresentable coefficient ratios, rates or
states raise FloatingPointError; malformed inputs raise ValueError.
