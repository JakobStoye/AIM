# Two positive equilibria outside two disks for a monostable reaction

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

This package submits a proposed analytic counterexample to [AIM problem 384](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/384-reaction-two-obstacle-uniqueness.md), frozen at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Theorem 3.1 constructs one admissible positive monostable reaction and two equal disjoint disks in dimension two whose full exterior admits two distinct bounded positive classical Dirichlet equilibria. On the same finite neck region, the first has squared mass at most 4500 and the second has squared mass strictly greater than 5000. This one example negates the question's universal uniqueness assertion. All reaction and geometry parameters are explicit and finite.

- [Complete manuscript](paper/main.pdf) and [editable source](paper/main.tex).
- [Target comparison](TARGET_COMPARISON.md).
- `PUBLIC_MANIFEST.json` records the selected files and their hashes; `SHA256SUMS` also covers the manifest.

## Reading and building

The paper contains the full analytic argument, including exhaustion, nonvanishing, boundary and regularity details. No numerical experiment, formal proof project or external proof supplement is required by the construction. The cited primary analytic sources are identified in the manuscript.

From this package directory, with a standard TeX Live installation:

```sh
shasum -a 256 -c SHA256SUMS
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/main.tex
```

The distributed source was compiled with pdfTeX 1.40.27 (TeX Live 2025). Compilation checks document integrity, not mathematical correctness. PDF metadata timestamps may make a local rebuild differ bytewise; the checksums identify the distributed files before rebuilding.

## AI involvement and review

OpenAI Codex contributed mathematical development, source checking and manuscript drafting. One fresh Codex context simulated a PDE reader and another reviewed the same anonymous draft as a mathematical referee, including its cited sources. The author then made one revision, adding two notation reminders and a short acknowledgment of earlier nonuniqueness results. The referee found no major objection within that draft review. These were AI reviews within one model provider. No separate detailed review report is submitted; independent mathematical review is requested.

This is a complete counterexample claim offered for independent mathematical review. No independent human review, Lean verification, journal acceptance, upstream acceptance or novelty certification is claimed. This package adds submission materials and leaves catalogue classification to the maintainers.
