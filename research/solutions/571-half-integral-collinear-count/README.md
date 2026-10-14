# Half-integral polygons with collinear interior lattice points

Local package version **1.0.0** accompanies the manuscript by Kaiwen Jin
(contact: yui.ui.siki@gmail.com). It contains the complete manuscript
and the compact computational material used in its rational-series step.
Hosting and external submission are pending.

This is computational supplement **1.0.0** for the manuscript source
SHA256 `27d1759f59b1c7d2fce1c026e631541f0658c76d75d1486eeaa4c7ac937f7c67`
and PDF SHA256
`9f751a6486068f9afe74320d82fa8639f711d02a04a4f18d5015f4af9c43bc5b`.
The matching delivery archive is `aim-571-half-integral-collinear-count-v1.0.0.zip`.
The [payload manifest](PUBLIC_MANIFEST.json) records every selected file and
its hash; [SHA256SUMS](SHA256SUMS) also fixes the manifest bytes. These identify
the exact supplement independently of a mutable repository branch.

For every integer `i >= 3`, the manuscript counts two-dimensional convex
polygons with vertices in `(1/2)Z^2`, including integral polygons, with exactly
`i` collinear interior points of `Z^2`, modulo `GL2(Z)` and integer
translations. The count is

```text
(i+1) * (512i^6 + 12928i^5 + 137740i^4 + 685145i^3
         + 1582743i^2 + 1665222i + 710640) / 1260.
```

Read [the manuscript](paper/manuscript.pdf), its [editable source](paper/manuscript.tex),
and the [target comparison](TARGET_COMPARISON.md).
The proof reduces the family to 618 integer-system members, with 608 distinct
complete inputs. The degree variable `n = i + 1` remains unbounded in each
system. The software computes whole rational functions, not finite samples
from which the count is extrapolated.

## Files

- `src/chain_models.py`: exact chain and fixed-class system generator.
- `src/exact_algebra.py`: integer-only polynomial and rational-function arithmetic.
- `numerical_case/exact_series.json`: all 608 selected exact inputs, original
  gradings, complete rational results and the assignment of all 618 members.
- `numerical_case/verify.py`: regenerate the cells, check every input/grade/member
  and verify the four full generating functions, Burnside sum and polynomial identity.
- `numerical_case/replay.py`: recompute one selected cell or the whole calculation.
- `test/`: finite integer-geometry controls and exported-data rejection checks.
- `ENVIRONMENT.json`: the actual Python/PyNormaliz versions, wheel and native
  hashes, arithmetic options and implementation limits.

## Verification without Normaliz

Use ordinary Python, without `-O`. The stored-data verifier and tests use only
the Python standard library:

```bash
python3 numerical_case/verify.py
python3 -m unittest discover -s test -v
```

The verifier checks all 618 members against regenerated exact matrices and
unit `n` gradings. It compares full rational functions using integer
polynomial arithmetic and proves the displayed degree-seven coefficient
identity algebraically. This verifies the exported inputs and stored
algebra; it does not independently certify that Normaliz produced the correct
series for each polyhedron.

The geometry controls independently construct convex hulls and enumerate
interior even-lattice points for finite examples. They check shear/reflection
orbits, point extrema, the integral `i=3` count of 79, a thin-row family and a
pair that must not be identified by a half-integral translation.
These finite controls support the implementation and do not prove the
all-parameter theorem.

## Recomputing the software-dependent series

The recorded calculation used Python 3.13.3 and PyNormaliz 2.24 on macOS arm64,
one Normaliz thread, and ordinary `BigInt` with `NoGradingDenom`.
An isolated installation can use:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python numerical_case/replay.py --action identity --cell 0 \
  --output numerical_case/raw/cell0.json
```

To recompute every distinct system, use a fresh output filename:

```bash
.venv/bin/python numerical_case/replay.py --all \
  --output numerical_case/raw/full_replay.json
```

The full calculation is substantially longer than the stored-algebra check.
The driver computes each complete Hilbert series with
`Compute("HilbertSeries", "BigInt", "NoGradingDenom")`, verifies its original
grading, and compares it to the supplied full rational function. It checkpoints
completed systems into the selected output and refuses to overwrite an
existing output. Equality is rational equality; a different but equivalent
numerator/denominator representation is accepted.

`ENVIRONMENT.json` identifies the exact cp313 macOS arm64 wheel and its native
bytes. A different platform or Python version may select different native
libraries; the supplied hashes describe the recorded run. The exact compiled
Normaliz minor version was not exposed and is not inferred from the cited
3.11.1 manual.

The computation relies on trusted exact software and ordinary hardware/runtime
correctness. `BigInt` avoids the initial 64-bit main attempt but does not widen
bounded degree types; ordinary LLL remains enabled. No independent counting
implementation or separately checked simplicial-decomposition certificate is
supplied. The full data remain essential computational evidence.

## Building the manuscript

From this package's directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=paper/build paper/manuscript.tex
```

The source is standalone and includes its bibliography. No other mathematical
source or proof supplement is required to compile or read it.

## Sources and AI use

The strip reduction and original conjecture are credited to Bohnert and
Springer, *Discrete & Computational Geometry* 76 (2026), 1238-1265,
[doi:10.1007/s00454-026-00822-0](https://doi.org/10.1007/s00454-026-00822-0),
Proposition 3.5 and Conjecture 3.7. Exact cone-enumeration semantics are
described by Bruns, Ichim and Söger,
[arXiv:1206.1916v4](https://arxiv.org/abs/1206.1916v4), Section 5.3,
and the versioned Normaliz manual cited in the manuscript.

OpenAI Codex helped develop the argument, implement and run the computations,
check the proof and write the manuscript. The accompanying
[manuscript-only AI review](AI_REVIEW.md) identifies the reviewed source/PDF
version and its actual scope. The review does not inspect the computational
artifacts. AI review,
compilation and passing code tests do not constitute independent human
certification or repository acceptance.
