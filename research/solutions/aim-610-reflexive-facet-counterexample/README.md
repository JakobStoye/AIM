# A counterexample to the facet bound for reflexive polytopes

This package submits an analytic counterexample to [AIM Problem 610](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/610-reflexive-polytope-facet-bound.md).
The [complete manuscript](paper/manuscript.pdf), [editable source](paper/manuscript.tex), and [target comparison](TARGET_COMPARISON.md) specify and prove the claim.

The construction gives a 45-dimensional reflexive lattice polytope with

```math
f_{44}(P)=2^{32}\binom{40}{8}+5=330303106984181765>6^{45/2}.
```

Section 2 derives the vertices and polar of a cube cut by a sum-of-absolute-coordinates constraint, and the exact polar identity for a pyramid with base at height 1 and apex at height -1. Section 3 applies five pyramids to the 40-dimensional base with sum bound 32, proves that both polytopes are integral with the origin in their interiors, and counts the dual facets. Every point family is specified symbolically; enumeration of its members is unnecessary.

Author: Kaiwen Jin. Contact: [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com).

This is a complete counterexample claim submitted for independent mathematical review. No smallest counterexample dimension or independent priority certification is asserted. Catalogue classification is left to the maintainers.

## Reproduction

Compile the self-contained source with a TeX installation containing the standard AMS, Latin Modern, geometry, microtype, and hyperref packages:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error paper/manuscript.tex
```

The final inequality can be reproduced using Python's standard library and arbitrary-precision integers:

```python
from math import comb

F = 2**32 * comb(40, 8) + 5
print(F)
print(F**2)
print(6**45)
print(F**2 - 6**45)
assert F**2 > 6**45
```

Expected output:

```text
330303106984181765
109100142483403824664737926558515225
103945637534048876111514866313854976
5154504949354948553223060244660249
```

The manuscript supplies the geometric proof. The integer calculation is a check of its concluding arithmetic, and no numerical simulation or external certificate is a premise. `PUBLIC_MANIFEST.json` lists the four mathematical/document files; `SHA256SUMS` covers those files and the manifest. The checksum file excludes itself.

## Sources and AI use

The references are [Nill's vertex conjecture](https://arxiv.org/abs/math/0405448v1), [Mori, Mori and Ohsugi's facet conjecture and twinned-chain result](https://doi.org/10.1007/s00454-026-00879-x), and [Haase and Melnikov's reflexive embedding result](https://arxiv.org/abs/math/0406485v1). They provide context and attribution; the construction and its proof are included in the manuscript.

OpenAI Codex assisted the mathematical exploration, proof development, drafting, source checks, and arithmetic checks. A fresh-context AI review examined the complete argument and cited references; two local definition glosses were then added. The reviewers shared the host filesystem, so physical isolation was not established. No separate detailed review report is included in this package. Independent mathematical review is requested.
