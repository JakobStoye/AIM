#!/usr/bin/env python3
"""Independent rough-data Galerkin references for two archived trajectories."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
import json,time
import numpy as np
from scipy.integrate import solve_ivp
from kdvlogloss import Fourier,twisted_rhs

ROOT=Path(__file__).resolve().parent/'results'
start=time.perf_counter(); rows=[]
for name in ('mixed_g0.1_N8','power_g1_N8'):
    archived=np.load(ROOT/'references'/f'{name}_L16384.npz')
    times=archived['time']; initial=archived['initial']; solutions=[]; evaluations=[]
    for rtol,atol in ((1e-10,1e-12),(2e-12,2e-14)):
        sol=solve_ivp(twisted_rhs,(0,float(times[-1])),initial,method='DOP853',t_eval=times,rtol=rtol,atol=atol)
        if not sol.success: raise RuntimeError(sol.message)
        values=np.array([Fourier(z).airy(t).coefficients for z,t in zip(sol.y.T,times)])
        solutions.append(values); evaluations.append(sol.nfev)
    rows.append({'case':name,'method':'DOP853','rtol':[1e-10,2e-12],'atol':[1e-12,2e-14],
                 'nfev':evaluations,'tolerance_difference':float(np.max(np.linalg.norm(solutions[0]-solutions[1],axis=1))),
                 'difference_from_finest_li_wu':float(np.max(np.linalg.norm(solutions[1]-archived['states'],axis=1)))})
    np.savez_compressed(ROOT/'validation'/f'rough_ode_{name}.npz',time=times,initial=initial,
                        loose=solutions[0],tight=solutions[1])
    print(json.dumps(rows[-1]),flush=True)
(ROOT/'rough_ode_validation.json').write_text(json.dumps({'cases':rows,'wall_seconds':time.perf_counter()-start},indent=2)+'\n')
