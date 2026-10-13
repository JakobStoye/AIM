#!/usr/bin/env python3
"""Finite signed-integer sanity checks, never an infinite-dimensional proof."""
import json
from pathlib import Path
import numpy as np
from kdvlogloss import covariance


def main():
    grid=np.r_[np.arange(-64,0),np.arange(1,65)]
    b,c=np.meshgrid(grid,grid,indexing="ij")
    count=0; maximum0=0.; maximum1=0.
    for a in grid:
        d=-a-b-c; valid=d!=0
        A=abs(a*b[valid]); B=abs(c[valid]*d[valid]); D=abs(d[valid])
        n3=np.sort(np.array([np.full(D.shape,abs(a)),abs(b[valid]),abs(c[valid]),D]),axis=0)[1]
        assert np.all(np.where(A<=B,A*n3<=3*B*D,B*n3<=3*A*D))
        assert np.all(abs(a+b[valid])*n3<=6*np.maximum(A,B))
        maximum0=max(maximum0,float(np.max(np.minimum(A/B,B/A)*n3/D)))
        maximum1=max(maximum1,float(np.max(abs(a+b[valid])*n3/np.maximum(A,B))))
        count+=D.size
    rng=np.random.default_rng(518); samples=0
    for _ in range(1000):
        a,b,c=rng.choice(grid,size=3); k=a+b+c; p=a+b
        if not (k*p): continue
        tau=10**rng.uniform(-8,0); alpha=3*a*b*p; beta=3*k*c*p
        eta=abs(covariance(tau*alpha,tau*beta))
        n3=sorted(map(abs,(a,b,c,k)),reverse=True)[2]
        assert eta<=2*min(abs(alpha/beta),abs(beta/alpha))*(1+1e-10)+1e-14
        assert eta<=tau*min(abs(alpha),abs(beta))*(1+1e-10)+1e-14
        for gamma in (0.,.1,.5,1.):
            left=eta/(abs(k)*abs(a*b*c)**gamma)
            right=6**(1-gamma)*18**gamma*tau**gamma/n3
            assert left<=right*(1+1e-10)+1e-14
        samples+=1
    result={"quadruples":int(count),"covariance_samples":samples,"normalized_geometry_maxima":[maximum0,maximum1],
            "exact_integer_comparisons":True,"status":"FINITE_CHECK_PASSED",
            "limitation":"Numerical and finite combinatorial evidence only; not a proof premise."}
    path=Path(__file__).resolve().parent/'results/frequency_checks.json'
    path.parent.mkdir(exist_ok=True); path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__': main()
