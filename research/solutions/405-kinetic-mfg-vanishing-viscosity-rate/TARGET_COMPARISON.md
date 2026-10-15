# Correspondence with AIM problem 405

Target: [An algebraic vanishing-noise rate for kinetic mean-field games](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/405-kinetic-mfg-vanishing-viscosity-rate.md),
repository revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.

The manuscript presents a complete solution claim for this fixed variational
target. Its Theorem 1 gives the requested exponent $`\eta(d)=1/2`$ for every
dimension, and additionally bounds the terminal density difference.
The claim awaits independent mathematical review.

| Original requirement | Manuscript location | Scope |
| --- | --- | --- |
| $`Q=\mathbb T^d\times\mathbb R^d`$, without a bounded velocity truncation | Section 1 defines $`Q,S,D`$; Sections 2–4 work on the full velocity space | Same domain; the unit-period torus convention is explicit |
| Every integer $`d\geq1`$ and every $`T>0`$ | Theorem 1 | All prescribed dimensions and horizons |
| Smooth, nonnegative, compactly supported probability datum | Section 1 and Theorem 1 | Same data class; no strict positivity imposed |
| Every $`0<\nu\leq1`$, compared with the zero-diffusivity minimizer | Theorem 1, equation (4), and the closing proof | Every prescribed diffusivity, not only a selected sequence |
| Quadratic acceleration perspective, local density-square cost, and terminal density-square cost | Equation (1) | Exactly the prescribed three costs |
| Velocity diffusion and acceleration flux in the kinetic equation | Equations (2)–(3) | Exactly the prescribed sign, diffusion block, transport, and initial datum |
| Narrowly continuous probability curves with finite second velocity moments | Section 1; Lemma 1; equations (11) and (15) | Original weak class; uniform moments are derived |
| Distributional equation with actual initial and terminal traces | Equation (3); Sections 3–4; equation (21) | Smoothed initial data converge back to the original datum before minimality is used |
| Finite action and the zero/infinite perspective convention at vacuum | Section 1; equations (23)–(24) | The limiting flux is zero at vacuum and has finite original action |
| Constant independent of $`\nu`$ | Equation (5) and the closing proof | Explicit $`L`$ depends only on $`d,T,\lVert m_{\mathrm{in}}\rVert_2`$, initial moment and entropy |
| Spacetime $`L^2`$ density estimate with some positive exponent | Theorem 1, equation (4) | $`\lVert m_\nu-m_0\rVert_{L^2(S)}\leq2\sqrt L\,\nu^{1/2}`$ |

Here $`m_{\mathrm{in}}`$ denotes the original initial density and $`S=(0,T)\times Q`$.
The row containing $`\lVert m_{\mathrm{in}}\rVert_2`$ uses the $`L^2(Q)`$ norm.

The main value comparison is proved in Sections 2–4. Kinetic Gaussian
averaging gives $`E_\nu\leq E_0`$. For fixed $`\nu`$, the entropy calculation
and removal of the positive convolution produce an inviscid pair with
the same density $`m_\nu`$ and cost at most $`E_\nu+L\nu`$.
The exact midpoint square identity yields equation (4).
The weak entropy argument explicitly treats the noncompact velocity tails.

The research references supply the kinetic question, first-order variational
lineage, and credit for the earlier elliptic entropy/current-velocity identity.
They are not used to impose extra regularity on the minimizing pairs.
The cited functional-analysis inputs from Brezis are the one-dimensional
Sobolev chain rule, reflexive weak compactness, continuous-function density,
and Hilbert representation; the kinetic and weighted-action arguments are
given in the manuscript.

The conclusion is for the minimizing pairs stipulated by the target.
It does not claim a new existence theorem, optimality of the exponent, or
rates for general Hamiltonians or different couplings.
