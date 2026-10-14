# Uniform vanishing-viscosity convergence for a local quadratic mean field game

This package presents a proposed analytic resolution of [Problem 404: Uniform convergence of value functions in local mean-field games](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/404-local-mfg-uniform-vanishing-viscosity.md). The complete proof is in the manuscript; independent mathematical review is requested.

For the local quadratic Hamiltonian and linear density coupling on the volume-one flat torus, Theorem 1.1 proves that the entire family of viscous value functions converges to one continuous function, uniformly on every interior time slab. The result holds in dimensions one, two and three, for every fixed positive time horizon, smooth nonnegative probability initial density and smooth fixed terminal cost. Initial vacuum is allowed. The theorem makes no quantitative rate claim.

A density-gradient identity and averaged finite-energy perturbations of optimal trajectories give continuity independent of viscosity. An initial-preserving heat recovery identifies the common density and flux; calibrated paths identify the occupied-region value, and homogeneous Hamilton-Jacobi comparison determines the value in vacuum.

- [Complete manuscript, 12 pages](paper/main.pdf)
- [Editable, standalone TeX source](paper/main.tex)
- [Exact target comparison](TARGET_COMPARISON.md)
- [Build and integrity checks](BUILD.md)
- [File manifest](PUBLIC_MANIFEST.json) and [checksums](SHA256SUMS)

Author: Kaiwen Jin. Contact: [yui.ui.siki@gmail.com](mailto:yui.ui.siki@gmail.com).

AI tools were used to develop the argument, draft and revise the exposition, check references and validate the document. Two additional AI contexts reviewed a frozen draft for reader comprehension and mathematical objections. No separate detailed review report is submitted. Publication of this package does not establish maintainer acceptance; independent mathematical review is requested.

The package is an analytic manuscript and its documentation. Its proof uses the public sources cited in the paper. The prescribed Hamiltonian, coupling, dimensions and data class are collected in Theorem 1.1; general models and a convergence rate remain outside that statement.
