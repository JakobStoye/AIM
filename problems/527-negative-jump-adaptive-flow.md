# 527. Existence for adaptive porous flow with a negative drag jump

**Area:** Numerical PDEs and porous-media flow

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

Let $`d\ge2`$ and let $`\Omega\subset\mathbb R^d`$ be bounded, connected and Lipschitz. Partition its boundary, up to surface measure zero, into relatively open pressure and flux parts $`\Sigma_p,\Sigma_v`$. Let $`2\le r<\infty`$ and $`s=r/(r-1)`$. Suppose $`\phi_1:[0,1]\to[0,\infty)`$ and $`\phi_2:[1,\infty)\to[0,\infty)`$ are continuous and nondecreasing, with

```math
c a^{(r-2)/2}\le\phi_2(a)\le C(1+a^{(r-2)/2})\quad(a\ge1),\qquad 0<\phi_2(1)<\phi_1(1),
```

for constants $`c,C>0`$. The last inequality is a negative jump in inverse permeability (drag) at the normalized speed threshold one.

For $`u\in L^r(\Omega;\mathbb R^d)`$ define the multivalued constitutive law

```math
\Lambda(u)=\left\{\phi_1(|u|^2)u\,\mathbf1_{\{|u|<1\}}+\phi_2(|u|^2)u\,\mathbf1_{\{|u|>1\}}+h\,\mathbf1_{\{|u|=1\}}:h\in L^s(\Omega;\mathbb R^d)\right\}.
```

The transition law is free on $`\{|u|=1\}`$; it is neither a prescribed branch value nor a prescribed convex combination.

Take $`q\in L^r(\Omega)`$, $`f\in L^s(\Omega;\mathbb R^d)`$ and $`u_0\in L^r(\Sigma_v)`$. If $`\Sigma_p`$ has positive surface measure, prescribe pressure through an extension $`P\in W^{1,s}(\Omega)`$ and put

```math
V=\{\psi\in W^{1,s}(\Omega):\mathop{\mathrm{Tr}}\nolimits\psi=0\text{ on }\Sigma_p\}.
```

If $`\Sigma_p=\varnothing`$, put $`P=0`$, $`V=\{\psi\in W^{1,s}(\Omega):\int_\Omega\psi=0\}`$ and impose $`\int_\Omega q=\int_{\partial\Omega}u_0`$.

Does every such choice of domain, laws and data admit $`u\in L^r(\Omega;\mathbb R^d)`$, $`p\in P+V`$ and $`\zeta\in\Lambda(u)`$ satisfying

```math
\zeta=f-\nabla p\quad\text{a.e. in }\Omega,\qquad
\int_\Omega u\cdot\nabla\psi=-\int_\Omega q\psi+\int_{\Sigma_v}u_0\psi\quad(\psi\in V)?
```

Prove this existence assertion or construct admissible data for which it fails. The target is a weak solution of the stated law, without an additional requirement that it minimize an energy.

## Application

Adaptive porous-flow models switch constitutive laws according to the computed speed, reserving a more expensive nonlinear law for selected regions. Existence is needed to determine whether such a switch defines a solvable continuum model before assessing a numerical method.

## References

1. A. Fumagalli and F. S. Patacchini, [Model adaptation for non-linear elliptic equations in mixed form: existence of solutions and numerical strategies](https://doi.org/10.1051/m2an/2022016), *ESAIM: Mathematical Modelling and Numerical Analysis* 56 (2022), 565–592, §§3–4 and conclusion; [full text](https://www.numdam.org/item/10.1051/m2an/2022016.pdf).
2. A. Fumagalli and F. S. Patacchini, [Well-posedness and variational numerical scheme for an adaptive model in highly heterogeneous porous media](https://doi.org/10.1016/j.jcp.2022.111844), *Journal of Computational Physics* (2023); [preprint](https://arxiv.org/abs/2206.07970), nonmonotone existence discussion and conclusion.
3. [Numerical validation of an adaptive model for the determination of nonlinear-flow regions in highly heterogeneous porous media](https://arxiv.org/abs/2405.02094), preprint (2024), §§2.4–2.7.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/kaiwen-jin-527-negative-jump-flow/paper/main.pdf) establishes the full original target. Weak existence for every original higher-dimensional free-transition porous-flow datum, with speed at least one almost everywhere.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/527-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #86](https://github.com/MColbrook/AIM/pull/86) at `adbe6891d9441d819df9d6acc614fc747f5821a3`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
