"""80-digit checks of the full small-step formula, without library operators."""
import mpmath as mp
import numpy as np
import pytest

from kdvlogloss import Fourier, li_wu_step


def mp_literal_step(coefficients, cutoff, tau):
    def product(a, b):
        out = {}
        for k, x in a.items():
            for j, y in b.items():
                out[k+j] = out.get(k+j, mp.mpc(0)) + x*y
        return out

    def airy(a, t):
        return {k: z*mp.exp(mp.j*t*k**3) for k, z in a.items()}

    def inv(a, q=1):
        return {k: z/(mp.j*k)**q for k, z in a.items() if k}

    def p(a):
        return {k: z for k, z in a.items() if k}

    def plus(*pairs):
        out = {}
        for factor, a in pairs:
            for k, z in a.items():
                out[k] = out.get(k, mp.mpc(0)) + factor*z
        return out

    # mp.mpf(float) preserves the input's binary value, not a rounded decimal.
    v = {k: mp.mpc(float(z.real), float(z.imag))
         for k, z in zip(range(-cutoff, cutoff+1), coefficients) if k}
    t = mp.mpf(tau)
    d = inv(v)
    sd = airy(d, t)
    ff = plus((mp.mpf(1)/6, p(product(sd, sd))),
              (-mp.mpf(1)/6, airy(p(product(d, d)), t)))
    h1 = p(product(sd, inv(ff)))
    mass = sum(z*v.get(-k, 0) for k, z in v.items())
    h3 = plus((1, inv(product(product(sd, sd), sd))),
              (-1, airy(inv(product(product(d, d), d)), t)))
    a = inv(ff, 2)
    h4 = plus((1, inv(product(a, sd), 2)),
              (-1, airy(inv(product(airy(a, -t), d), 2), t)))
    out = plus((1, airy(v, t)), (1, ff), (mp.mpf(1)/3, h1),
               (t*mass/9, sd), (-mp.mpf(1)/54, h3),
               (-mp.mpf(1)/(27*t), h4))
    return np.array([complex(out.get(k, 0)) if k else 0
                     for k in range(-cutoff, cutoff+1)])


@pytest.mark.parametrize("tau", [0.002, 1e-8])
def test_small_step_against_80_digit_literal_formula(tau):
    z = np.array([0.11+0.03j, -0.06+0.17j, 0.08-0.09j, -0.04-0.02j])
    f = Fourier(np.r_[z[::-1].conj(), 0, z])
    with mp.workdps(80):
        expected = mp_literal_step(f.coefficients, f.cutoff, tau)
    observed = li_wu_step(f, tau).coefficients
    assert np.max(np.abs(observed-expected)) < 3e-14
