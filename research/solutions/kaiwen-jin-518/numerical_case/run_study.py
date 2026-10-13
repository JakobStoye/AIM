#!/usr/bin/env python3
"""Reproduce the finite numerical evidence; run from any working directory."""
import os
for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[name] = "1"
import argparse
import csv
import hashlib
import json
import platform
import resource
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from kdvlogloss import Fourier, sobolev_norm, l2_norm, integrate, li_wu_step, twisted_rhs, averaging_remainder

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent


def initial_data(N, gamma, family, norm, seed):
    k=np.arange(1,N+1)
    if family=="mixed":
        z=np.zeros(N,complex); z[0]=1
        z[k>N//2]=-1j*(k[k>N//2]/N)**(-.5-gamma)/np.sqrt(N)
    elif family=="power":
        z=k**(-.5-gamma)*np.exp(1j*np.random.default_rng(seed).uniform(-np.pi,np.pi,N))
    else:
        raise ValueError(f"Unknown family {family}")
    f=Fourier(np.r_[z[::-1].conj(),0,z])
    return f.scale(norm/sobolev_norm(f,gamma))


def save_csv(path, rows):
    with path.open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)


def case_id(case):
    return f"{case['family']}_g{case['gamma']:g}_N{case['N']}"


def trajectory_diagnostics(f,T,steps,ref,ref_check,output):
    tau=T/steps
    numerical=integrate(f,T,steps)
    error=ref-numerical
    errors=np.sqrt(np.sum(abs(error)**2,axis=1))
    ref_diff=np.sqrt(np.sum(abs(ref-ref_check)**2,axis=1))
    defect=np.zeros_like(numerical[:-1]); feedback=defect.copy()
    defect_sum=np.zeros_like(numerical); feedback_sum=defect_sum.copy()
    rows=[]; sum_norms=0.0
    for n in range(steps+1):
        if n:
            j=n-1
            ref_step=li_wu_step(Fourier(ref[j]),tau).coefficients
            num_step=li_wu_step(Fourier(numerical[j]),tau).coefficients
            defect[j]=ref[n]-ref_step
            feedback[j]=ref_step-num_step-Fourier(error[j]).airy(tau).coefficients
            defect_sum[n]=defect_sum[j]+Fourier(defect[j]).airy(-n*tau).coefficients
            feedback_sum[n]=feedback_sum[j]+Fourier(feedback[j]).airy(-n*tau).coefficients
            sum_norms+=float(np.linalg.norm(defect[j]))
        norm=errors[n]
        amp2=float(np.sum((abs(ref[n])-abs(numerical[n]))**2))
        rows.append({"n":n,"time":n*tau,"error_l2":norm,"normalized_error":norm/tau**0.0,
                     "reference_difference_l2":ref_diff[n],
                     "phase_energy_fraction":1-amp2/norm**2 if norm>1e-14 else 0,
                     "lowest_mode_error_fraction":float((abs(error[n,f.cutoff-1])**2+abs(error[n,f.cutoff+1])**2)/norm**2) if norm>1e-14 else 0,
                     "numerical_mean_abs":float(abs(numerical[n,f.cutoff])),
                     "numerical_reality_error":float(np.max(abs(numerical[n]-numerical[n,::-1].conj()))),
                     "mass_change":float(np.sum(abs(numerical[n])**2)-l2_norm(f)**2),
                     "defect_coherence":float(np.linalg.norm(defect_sum[n])/sum_norms) if sum_norms else 0,
                     "feedback_sum_l2":float(np.linalg.norm(feedback_sum[n]))})
    reconstruction=np.array([Fourier(error[n]).airy(-n*tau).coefficients for n in range(steps+1)])
    identity_error=float(np.max(np.linalg.norm(reconstruction-defect_sum-feedback_sum,axis=1)))
    np.savez_compressed(output,initial=f.coefficients,modes=f.modes,time=np.arange(steps+1)*tau,
                        numerical=numerical,reference=ref,reference_check=ref_check,error=error,
                        defect=defect,feedback=feedback,transported_defect_sum=defect_sum,
                        transported_feedback_sum=feedback_sum)
    return rows,errors,ref_diff,identity_error


def run_global(config,out,log):
    summary=[]; references={}
    T=config["final_time"]; maximum=max(config["steps"])
    for case in config["global_cases"]:
        name=case_id(case); N=case["N"]; K=4*N; gamma=case["gamma"]
        f=initial_data(N,gamma,case["family"],config["data_norm"],config["seed"]).project(K)
        refs=[]
        for count in config["reference_steps"]:
            t=time.perf_counter(); full=integrate(f,T,count)
            sparse=full[::count//maximum].copy(); refs.append(sparse)
            np.savez_compressed(out/"references"/f"{name}_L{count}.npz",initial=f.coefficients,
                                modes=f.modes,time=np.linspace(0,T,maximum+1),states=sparse,
                                internal_steps=count,stored_stride=count//maximum)
            log(f"reference {name} L={count} seconds={time.perf_counter()-t:.2f}")
        ref_low,ref_high=refs
        references[name]=(f,ref_low,ref_high)
        for count in config["steps"]:
            stride=maximum//count
            rows,err,rd,identity=trajectory_diagnostics(f,T,count,ref_high[::stride],ref_low[::stride],out/"checkpoints"/f"{name}_L{count}.npz")
            tau=T/count
            for r in rows: r["normalized_error"]=r["error_l2"]/tau**gamma
            save_csv(out/"checkpoints"/f"{name}_L{count}.csv",rows)
            peak=int(np.argmax(err)); quality=float(np.max(rd)/max(float(np.max(err)),1e-300))
            summary.append({"case":name,"family":case["family"],"gamma":gamma,"N":N,"K":K,
                            "steps":count,"tau":tau,"max_error_l2":float(np.max(err)),
                            "normalized_max_error":float(np.max(err)/tau**gamma),
                            "reference_difference_max":float(np.max(rd)),"reference_quality_fraction":quality,
                            "reference_quality_pass":quality<=config["reference_quality_fraction"],
                            "peak_time":peak*tau,"peak_phase_fraction":rows[peak]["phase_energy_fraction"],
                            "peak_lowest_mode_fraction":rows[peak]["lowest_mode_error_fraction"],
                            "final_defect_coherence":rows[-1]["defect_coherence"],
                            "reconstruction_error":identity})
        log(f"finished global case {name}")
    save_csv(out/"global_summary.csv",summary)
    return summary,references


def run_local(config,out,log):
    rows=[]
    for gamma in config["local_gammas"]:
        for N in config["local_bandwidths"]:
            tau=N**-3; k=np.arange(1,N+1); amplitude=k**(-.5-gamma)
            for phase in config["local_phases"]:
                if phase=="even": positive=amplitude.astype(complex)
                elif phase=="odd": positive=-1j*amplitude
                elif phase=="half_airy": positive=-1j*amplitude*np.exp(-.5j*tau*k**3)
                else: positive=amplitude*np.exp(1j*np.random.default_rng(config["seed"]+N).uniform(-np.pi,np.pi,N))
                f=Fourier(np.r_[positive[::-1].conj(),0,positive]); f=f.scale(1/sobolev_norm(f,gamma))
                value=averaging_remainder(f,f,f,tau)
                res=averaging_remainder(f,f,f,tau,sector="resonant")
                envelope=averaging_remainder(f,f,f,tau,absolute=True)
                rows.append({"gamma":gamma,"N":N,"tau":tau,"phase":phase,
                             "normalized_remainder":l2_norm(value)/tau**(1+gamma),
                             "normalized_resonant_remainder":l2_norm(res)/tau**(1+gamma),
                             "absolute_envelope_ratio":l2_norm(value)/max(l2_norm(envelope),1e-300)})
                np.savez_compressed(out/"local"/f"g{gamma:g}_N{N}_{phase}.npz",input=f.coefficients,
                                    input_modes=f.modes,output=value.coefficients,output_modes=value.modes,
                                    resonant=res.coefficients,absolute_envelope=envelope.coefficients)
            log(f"finished local gamma={gamma} N={N}")
    save_csv(out/"local_summary.csv",rows)
    return rows


def validation(config,out,refs,log):
    T=config["final_time"]; L=max(config["steps"]); checks={"spatial":[]}
    for case in config["spatial_checks"]:
        base={**case,"family":"mixed"}; name=case_id(base)
        f,low,high=refs[name]; fine=f.project(2*f.cutoff)
        ref_fine=integrate(fine,T,config["reference_steps"][-1])[::config["reference_steps"][-1]//L]
        num_fine=integrate(fine,T,L); num_base=integrate(f,T,L)
        lo=f.cutoff; hi=fine.cutoff; projected=ref_fine[:,hi-lo:hi+lo+1]
        projected_num=num_fine[:,hi-lo:hi+lo+1]
        # Compare on the common larger space, retaining high-frequency tails.
        padded_ref=np.pad(high,((0,0),(lo,lo)))
        padded_num=np.pad(num_base,((0,0),(lo,lo)))
        checks["spatial"].append({"case":name,"K":lo,"K_fine":hi,"steps":L,
            "reference_full_space_difference":float(np.max(np.linalg.norm(ref_fine-padded_ref,axis=1))),
            "numerical_full_space_difference":float(np.max(np.linalg.norm(num_fine-padded_num,axis=1)))})
        np.savez_compressed(out/"validation"/f"spatial_{name}.npz",modes=fine.modes,
                            reference_fine=ref_fine,numerical_fine=num_fine)
        log(f"spatial validation {name}")
    case=config["precision_check"]; name=case_id(case); f,low,high=refs[name]; count=case["steps"]
    num64=integrate(f,T,count)
    numx=integrate(Fourier(f.coefficients.astype(np.clongdouble)),T,count)
    refx=integrate(Fourier(f.coefficients.astype(np.clongdouble)),T,config["reference_steps"][-1])[::config["reference_steps"][-1]//L]
    checks["precision"]={"case":name,"steps":count,"longdouble_mantissa_bits":int(np.finfo(np.longdouble).nmant),
         "numerical_difference":float(np.max(np.linalg.norm(numx-num64,axis=1))),
         "reference_difference":float(np.max(np.linalg.norm(refx-high,axis=1)))}
    np.savez_compressed(out/"validation"/"precision.npz",numerical_extended=numx,reference_extended=refx)
    small=initial_data(2,1.,"mixed",1.,config["seed"]).project(12)
    times=np.linspace(0,.12,129); independent=[]
    for rtol,atol in ((1e-10,1e-12),(2e-12,2e-14)):
        sol=solve_ivp(twisted_rhs,(0,.12),small.coefficients,method="DOP853",t_eval=times,rtol=rtol,atol=atol)
        if not sol.success: raise RuntimeError(sol.message)
        independent.append(np.array([Fourier(z).airy(t).coefficients for z,t in zip(sol.y.T,times)]))
    errors=[]
    for n in (32,64,128):
        num=integrate(small,.12,n); err=np.max(np.linalg.norm(num-independent[-1][::128//n],axis=1)); errors.append(float(err))
    checks["independent_ode"]={"method":"DOP853","K":12,"T":.12,"rtol":[1e-10,2e-12],"atol":[1e-12,2e-14],
      "reference_tolerance_difference":float(np.max(np.linalg.norm(independent[0]-independent[1],axis=1))),
      "steps":[32,64,128],"max_errors":errors,"refinement_ratios":[errors[0]/errors[1],errors[1]/errors[2]]}
    np.savez_compressed(out/"validation"/"independent_ode.npz",time=times,reference_loose=independent[0],reference_tight=independent[1],initial=small.coefficients)
    (out/"validation.json").write_text(json.dumps(checks,indent=2)+'\n')
    log("precision and independent ODE validation complete")


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",type=Path,default=HERE/"results")
    parser.add_argument("--config",type=Path,default=HERE/"config.json")
    args=parser.parse_args(); config=json.loads(args.config.read_text()); out=args.output.resolve()
    out.mkdir(parents=True,exist_ok=True)
    for name in ("references","checkpoints","local","validation"): (out/name).mkdir(exist_ok=True)
    start=time.perf_counter()
    with (out/"run.log").open("w") as stream:
        def log(message):
            line=f"{time.perf_counter()-start:.2f}s {message}"; print(line,flush=True); stream.write(line+'\n'); stream.flush()
        global_,refs=run_global(config,out,log)
        local=run_local(config,out,log)
        validation(config,out,refs,log)
    source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT/'src').rglob('*.py'))}
    source_hashes[str(Path(__file__).relative_to(ROOT))]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    manifest={"generated_at":datetime.now(timezone.utc).isoformat(),"config":config,"seed":config["seed"],
        "python":sys.version,"platform":platform.platform(),"numpy":np.__version__,"scipy":scipy.__version__,
        "threads":{k:os.environ[k] for k in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS")},
        "wall_seconds":time.perf_counter()-start,"peak_rss_bytes":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "source_hashes":source_hashes,"global_rows":len(global_),"local_rows":len(local),
        "quality_pass_rows":sum(r["reference_quality_pass"] for r in global_),
        "classification":"NUMERICAL EVIDENCE; finite bandwidths and nonrigorous references"}
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({k:manifest[k] for k in ("wall_seconds","peak_rss_bytes","global_rows","local_rows","quality_pass_rows")}),flush=True)


if __name__=="__main__": main()
