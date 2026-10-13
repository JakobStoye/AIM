# Exact certificate replay

This case is the proof-critical finite computation in Proposition 4 of the
paper. It is an exact arithmetic calculation, with no simulation or
floating-point feasibility test.

Run from the package directory:

```sh
python3 numerical_case/replay_certificate.py
python3 numerical_case/replay_certificate.py --output replay.json
```

The wrapper calls `src/verify_certificate.py` using the supplied
`certificate/farkas.json`. It reconstructs the identities, solves the short
table, and accumulates rational coefficients. The recorded
`critical_certificate_replay.json` is an actual successful exported-package
run, with the following proof-relevant output:

| Quantity | Exact result |
| --- | --- |
| Short cylinders | 78 |
| Weighted equations | 8,245 |
| Weighted nonnegative expressions | 7,244 |
| Probability and moment symbols | 8,298 |
| Nonzero coefficients | 0 |
| Positive contradiction margin | `4663173554073621650668701/229601458397122150289899520` |
| Required margin bound | Strictly greater than `1/50` |

The certificate has SHA-256
`c64ca628b2ea2b324a840827ef7571b9d68f2a8fd4039c7c0baab43581bf4f67`.
The report's decimal approximation and elapsed seconds are informational.
The constraints' mathematical validity and the infinite-tail argument are
proved in the manuscript; a passing finite replay checks the stated exact
calculation and does not by itself replace those analytic arguments.
