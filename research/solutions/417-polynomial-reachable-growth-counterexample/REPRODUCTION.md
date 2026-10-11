# Reproduction

The mathematical proof is in the six-page paper. No numerical experiment or machine certificate is needed for the theorem.

## Build the paper

Use a LaTeX installation containing `article`, `fontenc`, `lmodern`, `geometry`, `amsmath`, `amssymb`, `amsthm` and `hyperref`. From this package root:

```sh
SOURCE_DATE_EPOCH=1791750560 FORCE_SOURCE_DATE=1 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
```

The supplied PDF was built with pdfTeX 1.40.27 (TeX Live 2025), through latexmk 4.86a. The fixed epoch makes timestamps reproducible; other TeX versions can change PDF bytes or typography. Compare the mathematical content and references as well as the build log.

## Optional exact polynomial check

With Python 3.10 or newer, without `-O` or `-OO`:

```sh
PYTHONOPTIMIZE=0 python3 code/check_profiles.py
```

The script uses `fractions.Fraction`. It reconstructs the degree-five polynomial patches from their endpoint jets, verifies the jets, integrates their quartic expressions exactly, checks the integration-by-parts identity including both boundary terms, and checks the central profile's ratio `1/9`.

Expected totals are

```text
A0 = 39711684231/4460904448
E0 = 27933688011/1312030720
central_A_log_coefficient = 81/256
assertions_passed = true
```

These are finite algebraic checks for Lemma 3. They do not establish the clipped-log estimate for arbitrary measurable controls, the complete reachable-ball construction, or a general theorem certificate. Those arguments must be checked in the paper.

## File integrity

From this package root, run

```sh
shasum -a 256 -c SHA256SUMS
```

`PUBLIC_MANIFEST.json` records the payload file purposes and hashes. The checksum file also covers that manifest; neither container hashes itself recursively. Build products are outside the delivered payload.
