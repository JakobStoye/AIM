# Reproduction environment

The exact replay and all 12 tests were run with CPython 3.13.3 on macOS.
All executable inputs are included in this package. Only the Python standard
library is required; there are no third-party Python dependencies, solver
dependencies, random seeds, network accesses, or downloaded data in the replay.
Other Python versions have not been validated for this release.

From the package directory:

```sh
python3 src/verify_certificate.py certificate/farkas.json
python3 -m unittest discover -s test -v
python3 numerical_case/replay_certificate.py --output replay.json
```

The required output has status `EXACT_CERTIFICATE_REPLAY_PASSED`, zero
nonzero coefficients, and the exact rational margin printed in the paper.
The supplied `numerical_case/critical_certificate_replay.json` records an
actual run. Its elapsed time and decimal approximation are not proof inputs.
All coefficients and validity decisions use `fractions.Fraction`.

The PDF was built with pdfLaTeX and latexmk from TeX Live 2025. The source is
a standalone article, using the standard packages `geometry`, `amsmath`,
`amssymb`, `amsthm`, `booktabs`, `fontenc`, `lmodern`, `microtype`, and `hyperref`.
It requires no bibliography database, images, shell escape, or additional
project files.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=paper paper/main.tex
```

PDF byte identity is not expected across TeX installations because metadata
and font versions may differ. `SHA256SUMS` identifies the delivered artifacts;
the proof-critical certificate hash is also printed in Proposition 4.
