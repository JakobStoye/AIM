# Reproduction record

The supplied standalone Python script was run from a curated package containing
only the manuscript and the listed verification inputs on October 13, 2026.
Its JSON output exactly matched verification/summary.json. It imports only the
standard library and reads no development material.

| Exact finite quantity | Result |
|---|---:|
| Vertices | 4 |
| Labeled DAGs | 543 |
| Markov equivalence classes | 185 |
| Graph / intralayer-order pairs | 1152 |
| Exact prefix identities | 58 |
| Source-layer vector identities | 8 |
| Component / member checks | 496 |
| Largest class | 24 |

All checks use exact integer and rational arithmetic. The result is PASS for
these finite structural and counting identities. It is not a certificate for
the universal asymptotic estimates.

The manuscript was compiled from its standalone source with pdfTeX 1.40.27
(TeX Live 2025), driven by latexmk 4.86a. All eight pages were read and visually
inspected. The reference-type preflight found no mismatch or unresolved
reference. No unresolved citations or material layout warnings remained; a
minor underfull bibliography paragraph was checked visually.

Reproduction commands and the tested environment are in README.md and
ENVIRONMENT.json. The manuscript proof is analytic and independent of the
finite enumeration. No Lean formalization or independent human verification
is claimed.
