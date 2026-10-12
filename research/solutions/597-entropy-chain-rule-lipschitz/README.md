# An entropy chain rule on bounded Lipschitz domains

Proposed complete solution to [AIM problem 597](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/597-entropy-chain-rule-lipschitz.md), at target revision `c9929805cece044705abaaebe1cebddac1ba11a6`. Independent mathematical review is requested.

Author: Kaiwen Jin. Contact: [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com).

[Complete manuscript](paper/manuscript.pdf) · [Editable LaTeX source](paper/manuscript.tex) · [Target comparison](TARGET_COMPARISON.md).

Theorem 1.1 proves absolute continuity of the weighted entropy on the closed time interval and its exact chain rule for the prescribed flux on every bounded Lipschitz domain. It assumes precisely weak continuity in time, fixed positive mass, the no-flux weak continuity equation, finite initial entropy, finite kinetic action and finite Fisher information. Vacuum is allowed. The theorem covers nonsmooth nonconvex domains without density bounds or a smooth-gradient approximation condition.

The proof combines a local truncated entropy identity with reflection across Lipschitz boundary graphs. The density, actual flux and square-root gradient are transformed together; their scalar pairing is preserved because the graph reflection is an involution. A partition of unity is summed while the entropy derivative remains bounded. Removing the truncation then gives the formula at every pair of times, including both endpoints.

The manuscript includes the complete analytic argument and exact locators for its public sources. OpenAI Codex was used for proof development, source searches, drafting and checks of the manuscript, cited statements and PDF. No separate detailed AI review is submitted. Independent mathematical review remains outstanding.

To rebuild the manuscript from this directory with a TeX installation providing the listed standard packages, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -output-directory=paper paper/manuscript.tex
```

The six-page PDF and source were compiled and checked, including all displayed formulas and references. This is an analytic theorem submission. [PUBLIC_MANIFEST.json](PUBLIC_MANIFEST.json) records the four payload files, and [SHA256SUMS](SHA256SUMS) binds those files and the manifest.
