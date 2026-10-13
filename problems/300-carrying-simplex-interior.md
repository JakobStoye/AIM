# 300. Interior smoothness of carrying simplices in competitive population maps

**Area:** Mathematical biology and dynamical systems

**Status:** ✅ SOLVED

**Last checked:** 2026-10-13

## Problem statement

For an integer $`d\ge3`$, set $`C=[0,\infty)^d`$ and consider the population map $`F_i(x)=x_i f_i(x)`$. Suppose $`f`$ is $`C^1`$ on an open neighborhood of $`C`$, $`f_i(x)>0`$ and $`\partial f_i/\partial x_j(x)<0`$ on $`C`$ for all $`i,j`$. Each positive coordinate axis has a fixed point $`q_i e_i`$, with $`q_i>0`$. For $`q=(q_1,\ldots,q_d)`$ assume

```math
\rho(M(x))<1\quad(x\in[0,q]),\qquad
M_{ij}(x)=-\frac{x_i}{f_i(x)}\frac{\partial f_i}{\partial x_j}(x),
```

where $`\rho`$ denotes spectral radius and $`[0,q]=\prod_i[0,q_i]`$. These hypotheses guarantee a carrying simplex $`\Sigma\subset C\setminus\{0\}`$: a compact invariant unordered hypersurface to whose trajectories every nonzero trajectory is asymptotic. Here unordered means that no two distinct points are comparable coordinatewise.

Is $`\Sigma\cap(0,\infty)^d`$ necessarily a $`C^1`$ embedded $`(d-1)`$-dimensional submanifold for every such map? Equivalently, write $`\Sigma=\{R(u)u:u\in\Delta\}`$, where $`\Delta=\{u\in C:\sum_i u_i=1\}`$ and $`R:\Delta\to(0,\infty)`$ is its continuous radial representation: must $`R`$ be $`C^1`$ on the relative interior of $`\Delta`$? Only interior regularity is requested; no smoothness or transverse embedding at extinction faces is assumed.

## Application

Competition maps describe populations whose per-capita growth decreases with every population density. Their carrying simplex contains the long-term nonzero dynamics. Interior $`C^1`$ regularity would justify smooth geometric reduction when analyzing coexistence, invariant manifolds and changes of stability.

## References

1. Stephen Baigent, *Carrying Simplices for Competitive Maps*, ICDEA 2017 proceedings (2019), 3–29. [Author manuscript](https://www.homepages.ucl.ac.uk/~ucess29/resources/ICDEA_RPS.pdf), Theorem 1 (hypotheses) and §6 (open interior regularity).
2. Janusz Mierczyński, Lei Niu and Alfonso Ruiz-Herrera, *Linearization and invariant manifolds on the carrying simplex for competitive maps*, Journal of Differential Equations (2019), DOI [10.1016/j.jde.2019.08.001](https://doi.org/10.1016/j.jde.2019.08.001). [Accepted manuscript](https://arxiv.org/abs/1902.08914), §1, Corollaries 4.8–4.9 and Theorem 4.12.
3. Janusz Mierczyński, *The C1 property of convex carrying simplices for competitive maps*, DOI [10.1017/etds.2018.85](https://doi.org/10.1017/etds.2018.85). [Manuscript](https://arxiv.org/abs/1801.01032), §2 assumptions and §3 Main Theorem.
4. Janusz Mierczyński and Stephen Baigent, *Existence of the carrying simplex for a retrotone map*, Journal of Difference Equations and Applications 30 (2024), 287–319. [Published paper](https://doi.org/10.1080/10236198.2023.2285394), Theorem 3.1 and property (ix).
5. Stephen Baigent and Janusz Mierczyński, *Time-periodic carrying simplex for a competitive system of Carathéodory ODEs* (2026). [Preprint](https://arxiv.org/abs/2605.01287), Theorems 6.4–6.5 and 7.2.

6. Michel Benaïm, *On Invariant Hypersurfaces of Strongly Monotone Maps*, Journal of Differential Equations 137 (1997), 302–319. [Institutional full text](https://libra.unine.ch/server/api/core/bitstreams/c6fe2a93-8853-4641-820e-5b23656b0077/content), §§1–2.
7. Janusz Mierczyński, *On smoothness of carrying simplices*, Proceedings of the American Mathematical Society 127 (1999), 543–551. [Author repost](https://arxiv.org/abs/1708.05195), §1, manuscript p. 3, and Theorems A–B.

## Status review

**Resolution reviewed 2026-10-13:** [Kaiwen Jin's manuscript](../research/solutions/300-carrying-simplex-interior/paper/interior_smoothness.pdf) establishes the full original target. Interior C1 carrying-simplex regularity for every map in the original class, without a permanence or convexity assumption.

**Independent review:** the [complete per-problem audit](../research/solution_reviews/2026-10-13-yui-prs/300-review.md) reconstructs the argument, compares its hypotheses and quantifiers with the original statement, and checks the cited sources and accompanying materials. The review was carried out by independent Codex AI agents during maintainer processing; it does not assert human peer review or Lean verification.

The reviewed submission is [PR #67](https://github.com/MColbrook/AIM/pull/67) at `efb5c003723b01af6090482c58330db2da99e86b`. The original problem statement at `c9929805cece044705abaaebe1cebddac1ba11a6` was compared with its unchanged current form. The proof and documented independent audit meet the repository's **Solved** criterion; the original problem page and ID are retained.
