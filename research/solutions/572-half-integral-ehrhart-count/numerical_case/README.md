# Exact verification cases

certificates/dual_weights.json contains the retained rational combinations
for the EE/EO/OO section models at n=2,…,8. The model's feasible vectors are
necessary real section constraints, not polygon realizations. The verifier
checks nonnegative weights, every objective coordinate and the exact upper
bound. Floating discovery and primal solver output are unnecessary for replay.

input_manifest.json pins version 1.0.0 of Zenodo 13928298 and all fifteen
full-function HDF5 files. fetch_inputs.py retrieves them with checksum/size
checks; verify.py validates and compares their exact signatures to C_i.
Large downloaded inputs stay in raw/, which is excluded from the projection.
The public DOI and pinned hashes are the reproducibility source.

results/verification.json records the executed 21 exact certificate checks
and the fifteen fixed-source comparisons. results/dual-optimized.json
checks the retained inequalities with assertions disabled. The test logs
record normal and optimized runs. These files concern code validation and
finite exact inputs, not independent catalogue completeness or proof review.

The tests exhaust all 408 and 761 signatures at i=2,3 against exact geometric
counts and independent bounding-box enumeration; compare dilated point counts
at t=0,…,5 for every i=2 signature; exercise large parameter endpoints and
collinear edge merging; and reject corrupted rational/schema inputs.

Run from the archive root:

~~~sh
python3 numerical_case/verify.py --output dual.json
~~~

The root README.md gives the pinned optional HDF5 installation, retrieval
and full-comparison commands. The input manifest identifies every fixed file.
