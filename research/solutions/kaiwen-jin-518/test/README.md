# Test suite and scope

Run `python -m pytest -q` from the installed package root. There are 21 tests:

- `test_integrator.py` compares the full step against an independent literal
  dictionary expansion, checks full intermediate support, padding,
  FFT/direct agreement, mean zero, reality, translations, input validation,
  the longdouble storage path and smooth Galerkin-ODE refinement.
- `test_remainder.py` checks covariance against 80-digit mpmath averages,
  small and imbalanced phases, an independent mixed-input remainder at
  40 digits, the resonant-sector partition and half-Airy phases.
- `test_high_precision.py` checks an independent 80-digit expansion of the
  entire step at tau = 0.002 and tau = 1e-8.

The literal expansions do not use the library convolution or alignment
helpers. Tolerances reflect binary64 roundoff and cancellation in the tested
regime. The ODE test checks refinement against a different time discretization;
it does not treat that reference as exact. The tests validate sampled
implementations, not the infinite-dimensional theorem.
