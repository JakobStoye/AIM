#!/usr/bin/env python3
"""Reproduce the paper's fixed cases; retain full outputs locally."""

from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import numpy as np
from elliptic_widths import (
    RadialCoefficient, expanded_spectrum, generalized_eigenvalues,
    log_determinant_bound, log_radial_spectrum, log_singular_bound,
    spherical_degrees,
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("config.json"))
    parser.add_argument("--output", type=Path, default=ROOT / "numerical_case/results/paper-v1")
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    # Refuse accidental campaign expansion without a new recorded configuration.
    require(config["dimensions"] == [2,3] and config["cases_per_dimension"] == 20, "expected the fixed paper case set")
    require(config["maximum_degree"] == 80 and config["annuli"] == 64, "expected the fixed paper degree/layer budget")
    require(
        config["core_radius"] == 2**-8
        and config["inner_radius"] == 0.5
        and config["outer_radius"] == 1.0,
        "expected the fixed paper geometry: core=2^-8, inner=0.5, outer=1",
    )
    require(not args.output.exists(), "result directory exists; choose a fresh --output")
    args.output.mkdir(parents=True)
    start_time = time.perf_counter()
    rng = np.random.default_rng(config["seed"])
    form_records = []
    count_records = []
    for d in config["dimensions"]:
        n = np.arange(1,config["maximum_count_check"]+1)
        sums = np.cumsum(spherical_degrees(d,len(n)) + d - 2)
        lower = n*n/4 if d == 2 else (2/3)*n**1.5
        require(np.all(sums >= lower), "spherical count bound")
        count_records.append({"dimension":d,"count":len(n),"minimum_margin":float(np.min(sums-lower))})
    # Keep the recovered seed's draw order for a comparable original campaign.
    for d in config["dimensions"]:
        for trial in range(config["form_trials_per_dimension"]):
            ambient = 40
            m = int(rng.integers(1,18))
            radius = float(rng.uniform(0.3,1.2))
            alpha,beta = 0.15,4.0
            degrees = spherical_degrees(d,ambient)
            subspace,_ = np.linalg.qr(rng.normal(size=(ambient,m)))
            bform = subspace.T @ (degrees[:,None] * subspace)
            qform = subspace.T @ ((degrees*(degrees+d-2)/radius)[:,None] * subspace)
            vals,vecs = np.linalg.eigh(bform)
            half = (vecs*np.sqrt(vals))@vecs.T
            rotation,_ = np.linalg.qr(rng.normal(size=(m,m)))
            comparison = (rotation*rng.uniform(alpha,beta,size=m))@rotation.T
            gram = half@comparison@half
            random_matrix = rng.normal(size=(m,m))
            growth = alpha*qform + random_matrix.T@random_matrix
            eigenvalues = generalized_eigenvalues(qform,gram)
            lower = (spherical_degrees(d,m)+d-2)/(beta*radius)
            trace = float(np.trace(np.linalg.solve(gram,growth)))
            expected = float(alpha*np.sum(lower))
            require(np.all(eigenvalues >= lower-1e-9), "finite-form eigenvalue comparison")
            require(trace >= expected-1e-9, "finite-form trace comparison")
            form_records.append({"dimension":d,"trial":trial,"subspace_dimension":m,"trace_margin":trace-expected,"minimum_eigenvalue_margin":float(np.min(eigenvalues-lower))})
    nodes = np.geomspace(config["core_radius"],config["outer_radius"],config["annuli"]+1)
    nodes[np.argmin(abs(nodes-config["inner_radius"]))] = config["inner_radius"]
    records = []
    for d in config["dimensions"]:
        for case in range(config["cases_per_dimension"]):
            if case == 0:
                label = "isotropic"
                radial = tangential = np.ones(len(nodes))
            elif case == 1:
                label = "polar_anisotropy"
                radial,tangential = np.full(len(nodes),4.0),np.full(len(nodes),0.25)
            elif case == 2:
                label = "alternating"
                radial = np.where(np.arange(len(nodes))%2,0.2,5.0)
                tangential = 1/radial
            else:
                label = "random_layers"
                radial = np.exp(rng.uniform(-3,3,size=len(nodes)))
                tangential = np.exp(rng.uniform(-3,3,size=len(nodes)))
            coefficient = RadialCoefficient(nodes,radial,tangential)
            logs = log_radial_spectrum(d,coefficient,config["inner_radius"],config["maximum_degree"])
            expanded = expanded_spectrum(d,logs)
            product_bound = log_determinant_bound(d,len(expanded),0.5,1,coefficient.alpha,coefficient.beta)
            individual_bound = log_singular_bound(d,len(expanded),0.5,1,coefficient.alpha,coefficient.beta)
            product_excess = float(np.max(2*np.cumsum(expanded)-product_bound))
            individual_excess = float(np.max(expanded-individual_bound))
            require(product_excess <= 1e-8 and individual_excess <= 1e-8, "radial determinant/singular comparison")
            # Split each shell into two equal logarithmic subintervals.
            refined_nodes = [nodes[0]]
            refined_radial = [radial[0]]
            refined_tangential = [tangential[0]]
            for j in range(1,len(nodes)):
                refined_nodes.extend([math.sqrt(nodes[j-1]*nodes[j]),nodes[j]])
                refined_radial.extend([radial[j],radial[j]])
                refined_tangential.extend([tangential[j],tangential[j]])
            refined = RadialCoefficient(refined_nodes,refined_radial,refined_tangential)
            refined_logs = log_radial_spectrum(d,refined,0.5,config["maximum_degree"])
            splitting_error = float(np.max(abs(logs-refined_logs)))
            require(splitting_error <= 2e-11, "analytic shell splitting invariance")
            exact_error = None
            if case == 0:
                reference = (np.arange(1,len(logs)+1)+(d-2)/2)*math.log(0.5)
                exact_error = float(np.max(abs(logs-reference)))
                require(exact_error <= 1e-9, "isotropic exact reference")
            elif case == 1:
                degree = np.arange(1,len(logs)+1)
                gamma = (np.sqrt((d-2)**2+degree*(degree+d-2)/4)-(d-2))/2
                reference = (gamma+(d-2)/2)*math.log(0.5)
                exact_error = float(np.max(abs(logs-reference)))
                require(exact_error <= 1e-9, "polar anisotropy exact reference")
            file_name = f"d{d}_case{case:02d}.npz"
            path = args.output/file_name
            np.savez_compressed(path,radii=nodes,radial=radial,tangential=tangential,log_by_degree=logs,expanded_logs=expanded,product_bound=product_bound,individual_bound=individual_bound)
            records.append({"dimension":d,"case":case,"label":label,"alpha":coefficient.alpha,"beta":coefficient.beta,"degrees":len(logs),"modes":len(expanded),"maximum_product_excess":product_excess,"maximum_individual_excess":individual_excess,"splitting_error":splitting_error,"exact_reference_error":exact_error,"file":file_name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    manifest = {"status":"PASS","evidence":"ordinary floating point checks on radial models and finite forms","config":config,"python":platform.python_version(),"numpy":np.__version__,"thread_caps":{k:os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","VECLIB_MAXIMUM_THREADS")},"elapsed_seconds":time.perf_counter()-start_time,"count_checks":count_records,"form_checks":form_records,"radial_cases":records,"limitations":["The radial family is separable and does not numerically test general nonradial coefficients.","The expanded arrays are spectra of the computed finite-degree subspaces.","No floating point output certifies the analytic theorem or an infinite tail."]}
    (args.output/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    summary = {"status":manifest["status"],"seed":config["seed"],"dimensions":[2,3],"form_trials":len(form_records),"radial_cases":len(records),"minimum_form_trace_margin":min(x["trace_margin"] for x in form_records),"maximum_splitting_error":max(x["splitting_error"] for x in records),"maximum_product_excess":max(x["maximum_product_excess"] for x in records),"maximum_individual_excess":max(x["maximum_individual_excess"] for x in records),"reference_errors":[{k:x[k] for k in ("dimension","label","exact_reference_error")} for x in records if x["exact_reference_error"] is not None],"environment":{"python":manifest["python"],"numpy":manifest["numpy"]}}
    summary_dir=ROOT/"numerical_case/summaries"
    summary_dir.mkdir(exist_ok=True)
    (summary_dir/"paper_results.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps(summary,indent=2))


if __name__ == "__main__":
    main()
