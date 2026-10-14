# Quadratic barrier parameters for hyperbolic balls

This package submits an analytic resolution claim for [AIM 540](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/540-hyperbolic-ball-barrier-parameter.md), at the indicated immutable problem revision.

The manuscript proves, for every \(R>1\),

\[
\frac{(R-1)^2}{256}\leq\theta_*(R)\leq1+2R^2,
\]

where \(\theta_*(R)\) is the infimum over all barriers in the original arbitrary-triple covariant-derivative definition on a radius-\(R\) ball in the hyperbolic plane of curvature \(-1\). The optimal order is \(R^2\), so an \(O(\sqrt R)\) parameter is impossible. The lower bound imposes no rotational symmetry and the barrier can depend on \(R\).

The upper construction is credited to Hirai, Nieuwboer and Walter. The lower bound uses the curvature identity at circle maxima, a scalar comparison for the maximum profile, and the gradient inequality along every radial geodesic. The manuscript distinguishes full self-concordance from the weaker condition along geodesics.

- [Complete manuscript](paper/hyperbolic_ball_barriers.pdf)
- [Standalone editable TeX source](paper/hyperbolic_ball_barriers.tex)
- [Correspondence with the original target](TARGET_COMPARISON.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

Author: Kaiwen Jin. Manuscript contact: yui.ui.siki@gmail.com.

OpenAI Codex assisted with the argument, checking and manuscript preparation, as disclosed in the paper. This package is offered as a complete solution claim for independent mathematical review; repository classification is left to the maintainers.

The source is a standalone LaTeX document with its bibliography included. It was built with TeX Live 2025. From the package directory, compile twice:

    pdflatex -no-shell-escape -halt-on-error -interaction=nonstopmode -output-directory paper paper/hyperbolic_ball_barriers.tex
    pdflatex -no-shell-escape -halt-on-error -interaction=nonstopmode -output-directory paper paper/hyperbolic_ball_barriers.tex

The mathematical contribution is analytic and uses no numerical or certificate input.
