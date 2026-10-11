# Proposed counterexample for AIM 387

The manuscript proves failure of the stated local controllability property for
the normalized Saint--Venant tank at **T = 21/10**. Its explicit compatible
terminal states tend to the flat equilibrium in C1, while no trajectory in one
fixed small neighborhood can reach them from equilibrium. Tank velocity and
displacement are zero at both endpoints. This answers the question asking for
sufficiency at every T > 2 negatively; it does not determine the eventual
positive controllability time.

- [Complete manuscript](paper/obstruction.pdf)
- [Editable LaTeX source](paper/obstruction.tex)
- [Comparison with the original target](TARGET_COMPARISON.md)
- [Original problem at the fixed source revision](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/387-shallow-water-tank-sharp-control-time.md)

Author: Kaiwen Jin. Manuscript contact: `yui.ui.siki@gmail.com`.

The result is an analytic counterexample claim. No numerical computation or
formal proof is a premise. OpenAI Codex assisted with developing and checking
the argument, source retrieval and writing. The same AI checked its own
argument. No separate detailed AI review is submitted; independent
mathematical review is requested. Publication of these materials does not
establish acceptance of the claim.

To rebuild with a standard TeX Live installation containing `latexmk`, run:

```sh
sh build.sh
```

The generated PDF is `build/obstruction.pdf`. The supplied manuscript was
built with pdfTeX 3.141592653-2.6-1.40.27 (TeX Live 2025) and LaTeX2e; rebuilding may change PDF
timestamps while preserving its mathematical content. The source is standalone
and needs only the listed standard LaTeX packages. File hashes for the
distributed snapshot are in `SHA256SUMS`; `PUBLIC_MANIFEST.json` describes
the mathematical files. Those two inventory files do not hash themselves.
