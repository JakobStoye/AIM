# A half-power vanishing-noise estimate for a quadratic kinetic mean-field game

This note presents a complete analytic solution claim for
[AIM problem 405](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/405-kinetic-mfg-vanishing-viscosity-rate.md).
Independent mathematical review is requested.

For every dimension $`d\geq1`$, horizon $`T>0`$, and smooth, nonnegative,
compactly supported probability datum on
$`Q=\mathbb T^d\times\mathbb R^d`$, Theorem 1 proves

```math
\|m_\nu-m_0\|_{L^2((0,T)\times Q)}^2+
\|m_\nu(T)-m_0(T)\|_{L^2(Q)}^2\leq4L\nu,
\qquad 0<\nu\leq1.
```

The densities minimize the prescribed quadratic acceleration, local density,
and terminal density costs in the original weak kinetic admissible class.
The constant $`L`$ is explicit and depends only on the datum, $`d`$, and $`T`$.
Thus the requested exponent can be chosen as $`\eta(d)=1/2`$.

- [Complete manuscript](paper/main.pdf)
- [Editable standalone LaTeX source](paper/main.tex)
- [Correspondence with the original target](TARGET_COMPARISON.md)
- [AI use and review](AI_USE.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The argument uses kinetic Gaussian averaging, a weak entropy identity for a
positive convolution commuting with kinetic transport, and strict convexity.
The current-velocity identity is credited to its earlier elliptic use.
The proof includes the noncompact velocity tails, recovery of the initial
datum, and finite limiting action at vacuum.

The paper concerns the stated minimizing pairs. It does not assert a new
existence theorem, a classical value-function theory, optimality of the
exponent, or a result for different costs.
The contribution is analytic; no numerical results or formal proof project
are part of this package.

To rebuild the manuscript using a standard TeX installation:

~~~sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/main.tex
~~~

The bibliography is embedded in the source. No additional manuscript assets
are required. Author: Kaiwen Jin, yui.ui.siki@gmail.com.
