# Artifact reproduction record

This is an analytic theorem. Compilation and artifact checks validate the delivered document and its references; they do not establish mathematical correctness.

## Document build

The standalone source was built with latexmk 4.86a and pdfTeX 1.40.27 (TeX Live 2025):

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex

The build completed successfully and produced 12 pages, with no LaTeX warning, undefined reference, or overfull/underfull box. The paper has an inline bibliography and no external manuscript assets or data. A separate build in the public delivery checkout used only the exported manuscript and standard TeX distribution; its twelve rendered pages and extracted text matched the delivered PDF exactly.

Every page of the delivered PDF has content and visual inspection coverage. The final added formula locator was inspected on its page, and all other pages render identically to the checked preceding revision. The theorem, numbered statements, prescribed recurrence, citation keys and bibliography were preserved during these exposition revisions.

## Mathematical evidence

The proof is the complete argument in the manuscript and its cited public dependencies. It includes every Hurst parameter, the Brownian value, zero initial conditions, zero crossings, degenerate coefficients and mesh-independent constants. No numerical experiment, computer certificate or formal proof is used. Independent mathematical review is requested.

## File integrity

The manifest records byte lengths and SHA-256 hashes. SHA256SUMS covers every delivered file except itself. Build output belongs in the ignored build directory.
