# AIM 636: a uniform Kolmogorov bound for Jack measures

This package submits a complete solution claim for [AIM 636](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/636-jack-normal.md), at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

For the Jack law and normalized statistic in that statement, Theorem 1.1 proves

```math
d_{\mathrm K}(W_{n,\alpha},Z)\le 10\max\{n^{-1/2},\sqrt\alpha/n\}
```


for every integer $`n\ge3`$ and every real $`\alpha\ge1`$, with one constant independent of both parameters. The estimate includes $`\alpha\asymp n`$ and has no logarithmic factor.

- [Complete manuscript](paper/jack_normal.pdf)
- [Editable LaTeX source](paper/jack_normal.tex)
- [Correspondence with the frozen target](TARGET_COMPARISON.md)
- [Build instructions](BUILD.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The proof computes the signed conditional third moment of a Jack-growth exchangeable pair and expresses it in three orthogonal Jack characters. It then applies the normal-approximation inequality of Shao and Zhang. The manuscript credits the growth kernels of Kerov, the low-content identities of Lassalle, and the relevant earlier approximation results. Its mathematical argument is analytic and does not depend on numerical experiments.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

AI use and review: OpenAI Codex assisted with literature retrieval, proof development, symbolic checks and exposition. Separate fresh contexts of OpenAI Codex reviewed the frozen manuscript; this is AI review in a shared computing environment. No human or formal verification is claimed. No detailed AI review report is included. Independent mathematical review is requested.

This package is a solution claim pending maintainer review; it does not change the catalogue classification.
