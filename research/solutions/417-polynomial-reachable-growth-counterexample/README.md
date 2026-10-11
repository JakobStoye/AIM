# Small-time controllability without polynomial reachable neighborhoods

Kaiwen Jin · yui.ui.siki@gmail.com

This package proposes a counterexample to [AIM Problem 417](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/417-analytic-reachable-set-polynomial-growth.md) at revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

The [complete paper](paper/main.pdf), with [editable LaTeX source](paper/main.tex), gives a five-dimensional polynomial system with two measurable controls in `[-1,1]`. It reaches a full Euclidean neighborhood of the origin in every positive time. Yet a reachable point `-r e_4`, with `r > 0`, must satisfy

```math
r<\frac{t^{11}}4e^{-1/(6t)}
```

when its duration is at most `t`. Consequently no constants `C,T > 0` and integer `N >= 1` can give `B(0,Ct^N)` inside the reachable set for every `0 < t < T`.

The proof is self-contained in the paper: a critical quartic identity, a logarithmic estimate valid for all admissible controls, explicit concentration curves, exact signed coordinate loops, and linear steering to a full neighborhood. The axis upper bound and the full-dimensional neighborhood have different scopes, both stated explicitly. The result does not claim a counterexample in each prescribed dimension.

[Target comparison](TARGET_COMPARISON.md) maps the original statement to Theorem 1 and its proof. [Reproduction instructions](REPRODUCTION.md) cover typesetting and an optional exact rational check of Lemma 3's polynomial coefficients and moments. That check uses only Python's standard library and does not certify the general controllability theorem.

AI use: OpenAI Codex assisted with literature retrieval, mathematical development, exact arithmetic checks and manuscript drafting. No separate detailed AI report is submitted. Independent mathematical review is requested; this package is a complete solution claim for maintainer assessment.
