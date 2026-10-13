# An integral counterexample for AIM Problem 531

For the closed radius-five Rips complex of the thirteen-by-thirteen torus
grid with periodic Manhattan metric, the fourth integral homology has free
rank **2**. The [frozen problem](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/531-torus-grid-transition-homology.md)
predicts **26** at `k=5`. This one admissible counterexample disproves its
universal integral assertion.

- [Complete manuscript](paper/torus_grid_counterexample.pdf)
- [Editable source](paper/torus_grid_counterexample.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [Exact certificate and reproduction](numerical_case/README.md)

The proof identifies a torus subcomplex, then computes its signed relative
chain complex by homology-preserving integer operations. A modular determinant
check proves a rational rank lower bound; finite-field homology is not used
as a substitute for integral homology. The result makes no assertion about
the whole integral homology for other values of `k` or torsion-freeness in
degrees three and four.

Python 3.10 or later and the standard library suffice. From this directory:

```sh
python3 src/verify_certificate.py numerical_case/certificates/k5_certificate.json
python3 -m unittest discover -s test -v
python3 numerical_case/generate_certificate.py --output /tmp/k5-regenerated.json
```

The fixed certificate contains all 6056 unit pivots and the complete residual
integer matrix. The verifier imports no generator code and reconstructs its
relative bases by a different enumeration. Analytic controls include a
four-sphere boundary and a real-projective-plane triangulation.
The reported finite checks were performed exactly; they are part of the
computer-assisted proof described in the manuscript.

Author: Kaiwen Jin, yui.ui.siki@gmail.com.
OpenAI Codex assisted with the proof, software, source checking and writing.
No separate detailed AI review report is included. Independent mathematical
review of the manuscript and certificate is requested; filing these materials
does not establish maintainer acceptance or a formal proof-verification status.
