# AIM 518: removing the logarithmic loss in the Li-Wu KdV integrator

**Author:** Kaiwen Jin, <yui.ui.siki@gmail.com>  
**Submission:** complete solution claim, requesting independent mathematical review.  
**Target:** [AIM problem 518 at commit c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/518-kdv-integrator-logarithmic-loss.md).

The [paper](paper/main.pdf) proves a logarithm-free L2 error bound for the
specified unfiltered Li-Wu time-semidiscrete method, for real mean-zero
H^gamma initial data, 0 < gamma <= 1. The constants and admissible timestep
are uniform on each bounded H^gamma ball. See the [target comparison](TARGET_COMPARISON.md)
for the precise scope and proof locations. The numerical experiments are
finite Fourier diagnostics; they are not premises of the analytic proof.

## Materials

- [Complete manuscript and editable standalone LaTeX source](paper/README.md).
- [Target-to-theorem comparison](TARGET_COMPARISON.md).
- [Numerical library and conventions](src/README.md), with [meaningful tests](test/README.md).
- [Case configurations, generators and plotting instructions](numerical_case/README.md).
- [Small measured summaries](numerical_case/summary/README.md) and [vector figures](paper/figures/).
- [Reproduction checks and their limits](REPRODUCTION_REPORT.md).
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS).

The code is delivered as files in this submission package. No separate code
repository is needed. Generated Fourier arrays, trajectories and per-step
files remain local in `numerical_case/results/`, which is ignored. The
supplied scripts regenerate them.

## Install and test

Run these commands from this package directory using Python 3.11 or later:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python -m pip install --no-deps -e .
python -m pytest -q
```

The locked versions record the tested Python 3.13.3 macOS/arm64 environment;
they do not promise identical floating-point bytes on other systems. The
campaign uses the Unix `resource` module to record process memory. The
library and tests use NumPy, SciPy, Matplotlib, pytest and mpmath.

## Reproduce the paper's numerical cases

To redraw the figures directly from the supplied scalar summaries:

```bash
python numerical_case/make_figures.py
```

To regenerate all case data and supplemental checks, then refresh the
summaries and figures:

```bash
python numerical_case/run_study.py
python numerical_case/validate_rough_ode.py
python numerical_case/check_frequency_bounds.py
python numerical_case/export_publication_summary.py
python numerical_case/make_figures.py
```

The main campaign is fixed by `numerical_case/config.json`: 48 global rows
and 48 local remainder cases, with two timestep references and selected
spatial, dtype and independent-ODE checks. One numerical worker is used;
the evolution scripts cap numerical-library threads at one. On the recorded
runtime the original main campaign took 84.3 seconds and peaked at 390 MB
resident memory. Regenerated metadata and PDF timestamps may differ.

The manuscript is standalone: bibliography, tables and plot coordinates
are embedded in `paper/main.tex`. A conventional LaTeX installation with
the packages named in its preamble can compile it with two `pdflatex` runs.
The numerical package needs no TeX installation.

## AI use and review status

ChatGPT and Codex assisted with argument development, exposition, source
checks and numerical implementation, as disclosed in the manuscript's final
AI use declaration. No separate detailed AI review report is submitted.
The reproduction report records software and artifact checks only. This
submission requests independent review of the complete manuscript; it does
not claim human peer review, formal verification or AIM acceptance.

The manifest describes the delivered scientific files. `SHA256SUMS` also
covers the manifest; the checksum file itself is excluded from its own list.
