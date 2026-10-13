# Numerical library contract

The public package is `kdvlogloss`, installed with `pip install -e .`.
It solves the finite Fourier realization of
`u_t + u_xxx = (u²)_x / 2` on a period `2*pi`. Fourier coefficients use the
measure `dx/(2*pi)`, so the squared `L²` norm is the coefficient square sum.

`Fourier(a)` copies a finite one-dimensional, odd-length array. An array of
length `2*K+1` represents modes `-K,...,K`. There is no Nyquist mode. Real
data have `a[-k] = conjugate(a[k])`; the integrator requires an exactly zero
mean. Array storage remains accessible, so callers should treat coefficients
as immutable while a computation is in progress.

| Public routine | Meaning |
|---|---|
| `convolve(f,g)` | Full linear product, with output cutoff `K_f + K_g`; direct or padded FFT |
| `l2_norm(f)` | Normalized Fourier `L²` norm |
| `sobolev_norm(f,gamma)` | Inhomogeneous weight `(1+k²)^gamma` |
| `quadratic_stage(f,tau)` | Exact quadratic stage, retaining output through `2*K` |
| `li_wu_step(f,tau,cutoff=None)` | Literal fixed update; all cubic intermediates through `3*K`; projection only at the completed output |
| `integrate(f,T,L,snapshots=True)` | `L` steps of size `T/L`; returns every state or the final `Fourier` object |
| `twisted_rhs(t,a)` | Independently discretized Galerkin ODE in Airy coordinates |
| `covariance(x,y)` | Average of two exponential phases minus the product of their averages on `[0,1]` |
| `averaging_remainder(f,g,h,tau)` | Exact ordered mixed cubic multiplier, unprojected output through the sum of input cutoffs |

The Airy multiplier is `exp(i*t*k**3)`. Inverse derivatives set mode zero to
zero. `li_wu_step` accepts finite nonnegative steps; step zero is the identity
extension. `integrate` requires `T>0` and a positive integer number of steps.

The production step uses `O(K log K)` time with FFT convolution and `O(K)`
working storage. Saving all states takes `O(L*K)` storage. The diagnostic
remainder explicitly materializes triple indices and takes `O(N³)` time
and memory at comparable input bandwidths. Its intended use is bounded
verification, not large-scale evolution.

```python
import numpy as np
from kdvlogloss import Fourier, integrate, l2_norm

# u0(x) = 0.2*sin(x), padded to a fixed cutoff 16.
u0 = Fourier(np.array([0.1j, 0.0, -0.1j])).project(16)
uT = integrate(u0, 0.1, 64, snapshots=False)
print(l2_norm(uT))
```

The cutoff is independent of the timestep. No filter or numerical Sobolev
bound is silently imposed. Extremely small steps can suffer cancellation in
the endpoint formula; the archived parameter range is supported by literal,
80-digit and independent ODE checks in `test` and `numerical_case`.
