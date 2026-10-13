# Exact finite certificate

This directory contains the essential signed-chain certificate for the fixed
closed torus Rips complex `K_13(5)`. The calculation is exact integer linear
algebra. Its purpose is to verify the finite part of the manuscript's proof.

Python 3.10 or later and the standard library suffice.

From the package root:

```sh
python3 src/verify_certificate.py numerical_case/certificates/k5_certificate.json
python3 -m unittest discover -s test -v
python3 numerical_case/generate_certificate.py --output /tmp/k5-regenerated.json
```

The generator refuses to overwrite an existing output. Compare the regenerated
JSON with the fixed certificate; it contains no timestamps or machine-specific
fields. The verifier imports no generator code. It independently enumerates
all nonliftable cliques using explicit core diamonds, reconstructs signed
boundaries, checks their squares, and replays every unit cancellation with its
adjacent chain identities. Its row elimination modulo three is separate from
the generator's column elimination.

Expected relative chain dimensions in degrees 2 through 6:
`1352, 4394, 4394, 1690, 338`. The 6056 unit cancellations leave dimensions
`2, 28, 26` in degrees 2 through 4. The sole residual differential is a
`28 x 26` integer matrix with 24 nonzero columns and rank 24 modulo three.
These two matching bounds establish rational rank 24 and integral fourth
homology free rank 2 for the relative chain complex.

The manuscript proves that the core is homotopy equivalent to the torus and
that relative fourth homology agrees with fourth homology of the original
Rips complex. That topological argument is distinct from running the verifier.

The fixed certificate is proof-critical input and is retained. There are no
large ordinary numerical trajectories or arrays in this package.
