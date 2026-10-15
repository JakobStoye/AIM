# Sharp Weyl remainder for constant-index transmission eigenvalues

This package contains Kaiwen Jin's manuscript claiming the sharp Weyl
remainder for the constant-index interior transmission problem. The theorem
covers every dimension at least two, every bounded connected smooth domain
and every fixed constant refractive index greater than one. It counts all
nonzero complex energies with the Riesz multiplicity of the original
transmission operator, at every sufficiently large exact radius.

Independent mathematical review of the claim is requested. It is not a claim
of journal publication, formal verification or repository acceptance.

| File | Purpose |
| --- | --- |
| [weyl_remainder.pdf](weyl_remainder.pdf) | Complete manuscript, proof and references |
| [weyl_remainder.tex](weyl_remainder.tex) | Standalone editable LaTeX source |
| [TARGET_COMPARISON.md](TARGET_COMPARISON.md) | Comparison with the full AIM429 target |
| [PUBLIC_MANIFEST.json](PUBLIC_MANIFEST.json) | File purposes and SHA-256 hashes |
| [SHA256SUMS](SHA256SUMS) | Checksums of the delivered files |

Build the manuscript with a standard TeX installation containing LaTeX,
AMS packages, mathtools, Latin Modern, geometry, microtype, hyperref, cleveref and
aliascnt:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error weyl_remainder.tex
```

The source is self-contained as a document. The external mathematical inputs
are the public sources cited and identified in its references. No numerical
experiment or separate software implementation is needed for the analytic
argument.

OpenAI Codex assisted substantially with source review, argument development
and checking, and writing. The manuscript includes a factual AI-use
disclosure. No separate detailed AI report is submitted; independent
mathematical review is requested.

Author contact: [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com).
