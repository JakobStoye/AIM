# 517. Sharp local approximation widths for rough elliptic equations

**Area:** Numerical PDE analysis and multiscale approximation

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`d\in\{2,3\}`$, let $`\omega\Subset\omega^*\subset\mathbb R^d`$ be concentric open cubes, and let $`A\in L^\infty(\omega^*;\mathbb R^{d\times d})`$ be symmetric with

```math
\alpha|\xi|^2\le\xi^TA(x)\xi\le\beta|\xi|^2
```

for almost every $`x`$, every $`\xi`$, and fixed $`0<\alpha\le\beta<\infty`$. Write

```math
a_D(u,v)=\int_D A\nabla u\cdot\nabla v,\qquad \|u\|_{a,D}=a_D(u,u)^{1/2}.
```

Choose a nonzero cutoff $`\chi\in W^{1,\infty}(\omega)\cap H_0^1(\omega)`$. Define the local harmonic space and its normalization by

```math
\mathcal H_A=\{u\in H^1(\omega^*):a_{\omega^*}(u,v)=0\text{ for every }v\in H_0^1(\omega^*)\},
```



```math
\mathcal H_A^0=\{u\in\mathcal H_A:a_\omega(\chi u,\chi)=0\}.
```

The normalization removes the constant kernel of the energy seminorm. Let $`Tu=\chi(u|_\omega)`$ and set

```math
d_n(T)=\inf_{\substack{V\subset H_0^1(\omega)\text{ linear}\\\dim V\le n}}\ \sup_{\substack{u\in\mathcal H_A^0\\\|u\|_{a,\omega^*}\le1}}\ \inf_{v\in V}\|Tu-v\|_{a,\omega}.
```

Prove or refute that, for every such fixed choice of data, there are $`C,c>0`$, independent of $`n`$, such that

```math
d_n(T)\le C\exp\!\left(-c n^{1/(d-1)}\right)\qquad(n\ge1).
```

No smoothness or scale separation of $`A`$ is assumed. The constants may depend on $`A`$, the cubes and $`\chi`$; contrast-independent constants are not part of the question. This is the scalar elliptic specialization of the local-width conjecture in reference [1].

## Application

In porous-media flow and diffusion through heterogeneous materials, a coarse finite-element method can use basis functions adapted to the local coefficient. The width measures the best error achievable with $`n`$ local functions after oversampling on a larger region. The sharper exponent would quantify how many local basis functions suffice for a prescribed accuracy, even when the material has unresolved fine scales.

## References

1. C. Ma, [A Unified Framework for Multiscale Spectral Generalized FEMs and Low-Rank Approximations to Multiscale PDEs](https://doi.org/10.1007/s10208-025-09711-z), Foundations of Computational Mathematics **26**, 1699–1758 (2026), equations (2.20)–(2.22), Theorem 3.8, §6.1 and §7, p.1752. [Preprint](https://arxiv.org/abs/2311.08761v3).
2. C. Alber, P. Bastian, M. Hauck and R. Scheichl, [Optimal Spectral Approximation in the Overlaps for Generalized Finite Element Methods](https://arxiv.org/abs/2507.12226v1), 2025, Theorem 5.3.
3. C. Ye, [An Order-One Lower Bound on the Error of Scalable Generalized Multiscale Finite Element Space Constructions](https://arxiv.org/abs/2607.13888v1), 2026, §§2, 8–9.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/kaiwen-jin-517/paper/main.pdf) establishes the full original target. Affirmative: sharp local elliptic widths with exponent1/(d-1) for arbitrary measurable symmetric elliptic coefficients in d=2,3.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/517-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #39](https://github.com/MColbrook/AIM/pull/39) at `c5902207726a88e2f2922c7ffb1189272e755cdb`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
