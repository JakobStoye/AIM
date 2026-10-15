# Superlinear SKT localization

Kaiwen Jin — yui.ui.siki@gmail.com

This package submits a complete analytic solution claim for [AIM problem 469](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/469-superlinear-skt-nonlocal-to-local-limit.md), at revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`. Independent mathematical review is requested.

For every admissible smooth bounded connected domain, every dimension, every number of species at least two, and every fixed exponent greater than one, Theorem 1.1 proves subsequential convergence of the given regional strong solutions to a global local weak solution. The subsequence works on every finite time interval. Densities converge strongly in every space-time Lp below the exponent 2s; nonlinear pressures and reactions converge strongly in L1. The pressure has an integrable weak gradient, so the limiting equation retains its original initial data and the homogeneous Neumann pressure flux in the first-order weak sense.

The power entropy gives spatial compactness and higher integrability. A regularized logarithmic entropy also controls weighted square-root differences, giving an Lr pressure difference quotient with r = 4s/(3s+1) > 1. The proof includes the one-dimensional spatial compactness hypothesis, nonlinear time compactness, and testing with arbitrary boundary values.

- [Complete manuscript](paper/localization.pdf)
- [Editable standalone LaTeX source](paper/localization.tex)
- [Original-target comparison](TARGET_COMPARISON.md)
- [Build instructions](BUILD.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

The result is analytic; no numerical computation or computational certificate is a premise. It does not assert local uniqueness, a rate, whole-family convergence, or the endpoint s = 1. The manuscript credits the source nonlocal theory, the linear-rate benchmark, and Ponce's spatial compactness results. No priority certificate is claimed.

AI use: the argument and manuscript were developed with OpenAI Codex. Internal AI proof checks and one fresh-context reader and one fresh-context referee review assisted preparation; they share the same vendor and host. They are not independent human review or formal verification. No detailed internal review reports are submitted. This package leaves catalogue classification to maintainer review.
