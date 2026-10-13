import numpy as np
import mpmath as mp
import pytest
from kdvlogloss import Fourier, covariance, averaging_remainder


@pytest.mark.parametrize("x,y",[(1e-15,.2),(1e-12,3.),(.3,-.3),(1e-4,200.),(.1,.17),(.9,1.3),(1e-14,1e6)])
def test_covariance_against_80_digit_averages(x,y):
    with mp.workdps(80):
        xx,yy=mp.mpf(x),mp.mpf(y)
        def m(z): return mp.expm1(-1j*z)/(-1j*z) if z else mp.mpf(1)
        ref=complex(m(xx+yy)-m(xx)*m(yy))
    value=covariance(x,y)
    assert abs(value-ref)<3e-13*abs(ref)+1e-29,(value,ref)


def test_zero_phase_symmetry_and_resonance():
    assert covariance(0,4)==0
    assert covariance(2,0)==0
    x=np.array([.1,1.,10.])
    assert np.allclose(covariance(x,-x),1-np.sinc(x/(2*np.pi))**2,atol=2e-15)
    assert np.allclose(covariance(x,.4),covariance(.4,x),atol=1e-15)


def literal_remainder(f1,f2,f3,tau,t0):
    out=np.zeros(2*(f1.cutoff+f2.cutoff+f3.cutoff)+1,complex)
    K=len(out)//2
    with mp.workdps(40):
        def m(z): return mp.expm1(-1j*z)/(-1j*z) if z else mp.mpf(1)
        for a,za in zip(f1.modes,f1.coefficients):
            for b,zb in zip(f2.modes,f2.coefficients):
                for c,zc in zip(f3.modes,f3.coefficients):
                    k=int(a+b+c); p=int(a+b)
                    if not (a*b*c*k*p): continue
                    alpha=int(3*a*b*p); beta=int(3*k*c*p)
                    x,y=mp.mpf(tau)*alpha,mp.mpf(tau)*beta
                    eta=complex(m(x+y)-m(x)*m(y))
                    out[k+K]+=-tau/(18j*k)*np.exp(-1j*t0*(alpha+beta))*eta*za*zb*zc
    return out


def test_mixed_remainder_matches_literal_sum_and_sector_partition():
    rng=np.random.default_rng(82)
    inputs=[Fourier(np.r_[rng.normal(size=2)+1j*rng.normal(size=2),0,
                         rng.normal(size=2)+1j*rng.normal(size=2)]) for _ in range(3)]
    tau=.04; t0=.31
    all_=averaging_remainder(*inputs,tau,start_time=t0)
    assert np.allclose(all_.coefficients,literal_remainder(*inputs,tau,t0),atol=2e-15,rtol=2e-12)
    res=averaging_remainder(*inputs,tau,start_time=t0,sector="resonant")
    non=averaging_remainder(*inputs,tau,start_time=t0,sector="nonresonant")
    assert np.allclose(all_.coefficients,res.add(non).coefficients,atol=2e-16)
    envelope=averaging_remainder(*inputs,tau,start_time=t0,absolute=True)
    assert np.all(abs(all_.coefficients)<=envelope.coefficients.real+2e-16)


def test_half_airy_phase_removes_input_oscillation():
    N=4; tau=N**-3
    k=np.arange(1,N+1)
    pos=-1j*k.astype(float)**-.7*np.exp(-.5j*tau*k**3)
    f=Fourier(np.r_[pos[::-1].conj(),0,pos])
    out=averaging_remainder(f,f,f,tau)
    corrected=out.coefficients*np.exp(.5j*tau*out.modes**3)
    assert np.max(abs(corrected.imag))<1e-15
