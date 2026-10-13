"""Stable phase covariance and independent exact three-frequency sums."""
import math
import numpy as np
from .fourier import Fourier


def _average(x):
    return np.exp(-0.5j*x) * np.sinc(x/(2*np.pi))


def covariance(x, y):
    """M(x+y)-M(x)M(y), with x=tau*alpha and y=tau*beta.

    Near zero use the absolutely convergent bivariate covariance series.
    When one phase alone is small use its moment expansion. This avoids the
    subtraction of nearly equal FFT endpoint expressions or averages.
    """
    x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float))
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("Phases must be finite")
    out = np.empty(x.shape, dtype=np.complex128)
    zero = (x == 0) | (y == 0)
    out[zero] = 0
    small = (np.maximum(np.abs(x), np.abs(y)) <= 0.5) & ~zero
    if np.any(small):
        xx, yy = x[small], y[small]
        value = np.zeros(xx.shape, complex)
        px = np.ones(xx.shape, complex)
        for r in range(1, 15):
            px *= -1j*xx/r
            py = np.ones(yy.shape, complex)
            for s in range(1, 15):
                py *= -1j*yy/s
                value += px*py * (r*s/((r+s+1)*(r+1)*(s+1)))
        out[small] = value
    one = (np.minimum(np.abs(x), np.abs(y)) < 1e-3) & ~small & ~zero
    if np.any(one):
        swap = np.abs(x[one]) > np.abs(y[one])
        a = np.where(swap, y[one], x[one])
        b = np.where(swap, x[one], y[one])
        m0 = _average(b)
        moment = m0.copy()
        value = np.zeros(a.shape, complex)
        power = np.ones(a.shape, complex)
        exp_b = np.exp(-1j*b)
        for r in range(1, 8):
            moment = (r*moment-exp_b)/(1j*b)
            power *= -1j*a/r
            value += power*(moment-m0/(r+1))
        out[one] = value
    regular = ~(zero | small | one)
    out[regular] = _average(x[regular]+y[regular]) - _average(x[regular])*_average(y[regular])
    return out.item() if out.ndim == 0 else out


def averaging_remainder(f1, f2, f3, step, *, start_time=0.0, sector="all", absolute=False):
    """Full mixed R2 output to K1+K2+K3, via O(K1 K2 K3) literal sum.

    This reference implementation is for bounded diagnostic bandwidths. The
    absolute variant sums the magnitude of each Fourier contribution. Sector
    restriction is exact integer total-resonance testing, not a floating test.
    """
    if not np.isfinite(step) or step <= 0 or not np.isfinite(start_time):
        raise ValueError("A positive finite step and finite start_time are required")
    if sector not in ("all", "resonant", "nonresonant"):
        raise ValueError("Invalid sector")
    a,b,c = np.meshgrid(f1.modes, f2.modes, f3.modes, indexing="ij")
    k = a+b+c
    p = a+b
    phi = k**3-a**3-b**3-c**3
    valid = (a*b*c*k != 0) & (p != 0)
    if sector == "resonant":
        valid &= phi == 0
    if sector == "nonresonant":
        valid &= phi != 0
    av,bv,cv,kv,pv,pf = [z[valid] for z in (a,b,c,k,p,phi)]
    product = (f1.coefficients[(av+f1.cutoff)] * f2.coefficients[bv+f2.cutoff]
               * f3.coefficients[cv+f3.cutoff])
    values = (-step/(18j*kv) * np.exp(-1j*start_time*pf)
              * covariance(step*3*av*bv*pv, step*3*kv*cv*pv) * product)
    cutoff = f1.cutoff+f2.cutoff+f3.cutoff
    indices = kv+cutoff
    if absolute:
        out = np.bincount(indices, weights=np.abs(values), minlength=2*cutoff+1)
    else:
        out = (np.bincount(indices, weights=values.real, minlength=2*cutoff+1)
               +1j*np.bincount(indices, weights=values.imag, minlength=2*cutoff+1))
    return Fourier(out)
