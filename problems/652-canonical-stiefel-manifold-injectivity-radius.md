# 652. Injectivity radius of the canonical Stiefel manifold

**Area:** Imaging, control, geometry and dynamics

**Status:** 🔵 OPEN

**Last checked:** 2026-10-16

## Problem statement

The injectivity radius of a complete Riemannian manifold is the largest $`r`$ such that every geodesic of length less than or equal to $`r`$ is a shortest curve between its endpoints. For $`2\leq p\leq n-2`$, what is the injectivity radius of the compact Stiefel manifold 
```math
\mathrm{St}(n,p) := \{U\in\mathbb{R}^{n\times p}|U^\top U = I_p\}
```
equipped with the canonical metric $`g^\mathrm{can}`$ defined by $`g^\mathrm{can}_U(\xi,\zeta) = \mathrm{trace}(\xi^\top (I_n - \frac12 U U^\top) \zeta)`$?

## Application

The knowledge of the injectivity radius is an asset in several computational problems on manifolds. If, between two given points, one finds a geodesic whose length is less than or equal to the injectivity radius, then the length of the geodesic gives the Riemannian distance between the two points. The injectivity radius also defines the largest ball on which geodesic normal coordinates may be used. It is involved in optimization, consensus, statistics and data fitting.

## References

1. P.-A. Absil and S. Mataigne, [The Ultimate Upper Bound on the Injectivity Radius of the Stiefel Manifold](https://doi.org/10.1137/24M1644808), *SIAM Journal on Matrix Analalysis and Applications* 46(2):1145–1167, 2025.
2. R. Zimmermann and J. Stoye, [High Curvature Means Low Rank: On the Sectional Curvature of Grassmann and Stiefel Manifolds and the Underlying Matrix Trace Inequalities](https://doi.org/10.1137/24M1655755), *SIAM Journal on Matrix Analysis and Applications* 46(1):748–779, 2025.
3. J. Stoye, S. Mataigne, P.-A. Absil, and R. Zimmermann, [Shortest geodesic loops, sectional curvature, and injectivity radius of the Stiefel manifold](https://doi.org/10.1007/s10543-026-01141-9), *BIT Numerical Mathematics* 66, 2026.
4. W. Klingenberg, Riemannian Geometry, *vol. 1 of de Gruyter Studies in Mathematics*, Walter de Gruyter & Co., Berlin, 1982.
5. T. Sakai, Riemannian Geometry, *Fields Institute Communications*, American Mathematical Society, Providence, 1996.
   
## Status review

**Literature check:** Current searches found no matching solution or announced proof for this problem.

A result due to Klingenberg [4] (see also [5, Chapter III, Proposition 4.13]) states that the injectivity radius is given by the minimum between the conjugate radius and half the length of a shortest (nontrivial) geodesic loop. Moreover, if the sectional curvature of $`\mathrm{St}(n,p)`$ is globally bounded from above by $`K>0`$, it follows that the conjugate radius is bounded from below by $`\frac{\pi}{\sqrt{K}}`$.
An upper bound on the conjugate radius is given in [1] by finding explicit conjugate points at a geodesic length of $`\sqrt{2} t_\mathrm{r}`$, where $`t_\mathrm{r}`$ is the smallest positive root of $`\frac{\sin (t)}{t} + \cos (t)`$. A lower bound is given in [2, Theorem 8] by determining that the sectional curvatures are (sharply) bounded by $`K = \frac54`$. The shortest geodesic loops have a length of $`2\pi`$, see [1, Theorem 6.1]. 
Hence, we obtain that the injectivity radius is determined by the conjugate radius and lies in the range
```math
0.894\pi<\sqrt{\frac{4}{5}}\pi\leq \mathrm{inj}(\mathrm{St}(n,p)) \leq \sqrt{2}t_\mathrm{r}< 0.914 \pi.
```
We strongly believe that the injectivity radius is given by its upper bound (as the numerical experiments in [1] and the explicit *first* conjugate point on $`\mathrm{St}(4,2)`$ in [3] suggest), but we are lacking a proof.

For a proof one needs to perform a detailed analysis on when conjugate points first occur. 
Conjugate points are characterized by the existence of (nontrivial) directions for which the directional derivative of the Riemannian exponential vanishes. By [1, Proposition 3.2], the question of finding first conjugate points on the canonical Stiefel manifold boils down to determining matrices $`A\in\mathrm{skew}(p)`$, $`B\in\mathbb{R}^{(n-p)\times p}`$ with the smallest value $`(\frac{1}{2}\|A\|_\mathrm{F}^2 + \|B\|_\mathrm{F}^2)^{\frac12}`$ such that there exist matrices $`A_\omega \in\mathrm{skew}(p)`$, $`B_\omega\in\mathbb{R}^{(n-p)\times p}`$ (not both zero) for which the first $`p`$ columns of the directional derivative of the matrix exponential at $`\Omega :=`$$`\begin{bmatrix}
        A & -B^\top\\B & 0
    \end{bmatrix}`$ in the direction $`\check\Omega :=`$$`\begin{bmatrix}
        A_\omega & -B_\omega^\top\\B_\omega & 0
    \end{bmatrix}`$ vanish, i.e.,
```math
\left(\mathrm{d}\exp_\mathrm{m}(\Omega)[\check{\Omega}]\right)\begin{bmatrix}
        I_p\\0
    \end{bmatrix} = 0.
```
Solving this problem determines the injectivity radius of the canonical Stiefel manifold. 
