# Weak existence for adaptive porous flow with a negative drag jump

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This package proposes a complete resolution of [AIM 527](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/527-negative-jump-adaptive-flow.md), at statement revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Theorem 1 proves weak existence for every bounded connected Lipschitz domain
in dimension at least two, every finite growth exponent `r >= 2`, and all the
original mixed pressure and normal-flux data. The drag at speed one is an
arbitrary vector field in the conjugate Lebesgue space, exactly as in the
problem. The constructed velocity has speed at least one almost everywhere.
This is an existence statement for that free transition law; it does not
assert energy minimization, uniqueness or a selected threshold drag.

The complete argument is in the manuscript. Finite divergence-free/gradient
oscillations reduce graph defects on bounded pair ranges. Exact monotone
cutoff equations preserve the rough data and permit summable corrections
in the original conjugate norms.

- [Complete manuscript](paper/main.pdf)
- [Editable standalone LaTeX source](paper/main.tex)
- [Original-target comparison](TARGET_COMPARISON.md)
- [AI use and review scope](AI_USE.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The result is submitted as a full solution claim for independent mathematical
review. Catalogue classification is left to the maintainers.

To rebuild the manuscript, run the following from `paper/` with a standard
TeX installation containing the AMS packages, `hyperref`, `cleveref`,
`aliascnt`, `lmodern`, `microtype` and `geometry`:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The proof is analytic. Document compilation verifies the source builds;
it is not a mathematical proof checker.
