"""Independent literal polynomial checks and ODE convergence validation."""
import numpy as np
import pytest
from scipy.integrate import solve_ivp
from kdvlogloss import Fourier, convolve, li_wu_step, quadratic_stage, integrate, twisted_rhs


def literal_step(f, tau):
    """Dictionary implementation, independent of library convolution/alignment."""
    v = {int(k): z for k,z in zip(f.modes, f.coefficients) if k != 0}
    def product(a,b):
        c = {}
        for k,x in a.items():
            for j,y in b.items():
                c[k+j] = c.get(k+j,0)+x*y
        return c
    def airy(a,t): return {k:z*np.exp(1j*t*k**3) for k,z in a.items()}
    def inv(a,q=1): return {k:z/(1j*k)**q for k,z in a.items() if k}
    def p(a): return {k:z for k,z in a.items() if k}
    def plus(*pairs):
        c={}
        for factor,a in pairs:
            for k,z in a.items(): c[k]=c.get(k,0)+factor*z
        return c
    d=inv(v); sd=airy(d,tau)
    ff=plus((1/6,p(product(sd,sd))),(-1/6,airy(p(product(d,d)),tau)))
    h1=p(product(sd,inv(ff)))
    mass=sum(z*v.get(-k,0) for k,z in v.items())
    h3=plus((1,inv(product(product(sd,sd),sd))),(-1,airy(inv(product(product(d,d),d)),tau)))
    a=inv(ff,2)
    h4=plus((1,inv(product(a,sd),2)),(-1,airy(inv(product(airy(a,-tau),d),2),tau)))
    out=plus((1,airy(v,tau)),(1,ff),(1/3,h1),(tau*mass/9,sd),(-1/54,h3),(-1/(27*tau),h4))
    return np.array([out.get(int(k),0) if k else 0 for k in f.modes])


def real_data(k, seed=5):
    rng=np.random.default_rng(seed)
    z=(rng.normal(size=k)+1j*rng.normal(size=k))*0.15
    return Fourier(np.r_[z[::-1].conj(),0,z])


@pytest.mark.parametrize("cutoff,step",[(1,.3),(3,.017),(6,.002)])
def test_complete_step_matches_literal_fourier(cutoff,step):
    f=real_data(cutoff)
    assert np.allclose(li_wu_step(f,step).coefficients,literal_step(f,step),atol=3e-14,rtol=3e-13)


def test_full_intermediate_support_and_padding():
    f=real_data(4)
    a=quadratic_stage(f,.04)
    assert a.cutoff==8
    cubic=convolve(a,f)
    assert cubic.cutoff==12
    full=li_wu_step(f,.04,cutoff=12)
    assert np.allclose(full.project(4).coefficients,li_wu_step(f,.04).coefficients,atol=2e-15)
    # Enlarging storage without changing the polynomial cannot change its step.
    assert np.allclose(li_wu_step(f.project(12),.04).coefficients,full.coefficients,atol=2e-14)


def test_fft_linear_convolution_matches_literal():
    f,g=real_data(18),real_data(13,17)
    assert np.allclose(convolve(f,g,method="fft").coefficients,
                       convolve(f,g,method="direct").coefficients,atol=6e-16,rtol=2e-13)


def test_zero_mean_reality_and_translation():
    f=real_data(7); tau=.027; theta=.381
    out=li_wu_step(f,tau)
    assert out.coefficients[out.cutoff]==0
    assert np.max(abs(out.coefficients[::-1].conj()-out.coefficients))<3e-15
    shifted=Fourier(f.coefficients*np.exp(1j*theta*f.modes))
    assert np.allclose(li_wu_step(shifted,tau).coefficients,
                       out.coefficients*np.exp(1j*theta*f.modes),atol=3e-14)


def test_zero_input_zero_step_and_input_validation():
    f=real_data(3)
    assert np.array_equal(li_wu_step(f,0).coefficients,f.coefficients)
    assert np.all(li_wu_step(Fourier(np.zeros(7)),.1).coefficients==0)
    with pytest.raises(ValueError): li_wu_step(f,-.1)
    with pytest.raises(ValueError): li_wu_step(Fourier(np.ones(3)),.1)
    with pytest.raises(ValueError): Fourier(np.zeros(4))


def test_independent_galerkin_ode_and_smooth_time_refinement():
    f=real_data(2).project(12); end=.12
    ode=solve_ivp(twisted_rhs,(0,end),f.coefficients,method="DOP853",rtol=2e-12,atol=2e-14)
    assert ode.success
    ref=Fourier(ode.y[:,-1]).airy(end).coefficients
    errors=[np.linalg.norm(integrate(f,end,n,snapshots=False).coefficients-ref) for n in (16,32,64)]
    assert all(errors[i]/errors[i+1]>3.4 for i in (0,1)),errors
    assert errors[-1]<3e-7


def test_longdouble_storage_path():
    # longdouble has only 52 mantissa bits on the recorded Apple Silicon runtime.
    # This checks the dtype path; independent mpmath tests check actual precision.
    f=real_data(4)
    high=li_wu_step(Fourier(f.coefficients.astype(np.clongdouble)),1e-5)
    assert high.coefficients.dtype==np.clongdouble
    assert np.max(abs(high.coefficients-li_wu_step(f,1e-5).coefficients))<2e-11
