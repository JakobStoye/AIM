# Proposed resolution of AIM 639

Kaiwen Jin, *Strong convergence of the fractional WIS Euler integrator for Lipschitz drifts*.

For every fixed $`T>0`$, $`H\in(0,1)`$, real $`\alpha,\beta,x_0`$, and autonomous globally Lipschitz drift $`a`$ of at most linear growth, Theorem 2.1 establishes the terminal root mean-square estimate
```math
\bigl(\mathbb E|X_T-X_n|^2\bigr)^{1/2}
 \le C(T/n)^{\min\{H+1/2,1\}},
```
where $`C`$ is independent of $`n`$. The approximation is the prescribed GfBm_EM recurrence, with exact samples of the same fractional Brownian path. The theorem includes $`H=1/2`$, zero initial values, and crossings of zero, without derivative assumptions on $`a`$.

- [Complete manuscript](paper/main.pdf)
- [Editable source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [Build and artifact validation](REPRODUCTION_RECORD.md)
- [File manifest](MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

The target is [AIM 639 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/639-wis-fractional-euler-rate.md). The exact integrating-factor representation and numerical recurrence are due to Erdoğan, Lord and Schieven, cited as reference [1] in the manuscript. Sections 3 and 4 supply the fractional and Brownian quadrature estimates needed for the sharper convergence bound.

This submission is a complete analytic solution claim awaiting independent mathematical review. Catalogue classification is left to the maintainers.

## Build

From this directory, with a TeX distribution and latexmk:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex

The paper is standalone, with its bibliography in the source and no figure or data dependency. The argument is analytic; no numerical experiment, computer certificate or formal proof is relied on.

## AI use

OpenAI Codex assisted proof development, source checking and manuscript drafting. Independent mathematical review is requested. No separate detailed AI review report is submitted.
