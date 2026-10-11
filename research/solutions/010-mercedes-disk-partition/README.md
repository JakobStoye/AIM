# The Mercedes-star partition of a disk

Proposed resolution of [AIM 010](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/010-mercedes-disk-partition.md), at statement revision `c9929805cece044705abaaebe1cebddac1ba11a6`.

Author: Kaiwen Jin. Contact: yui.ui.siki@gmail.com.

Theorem 1 in the [manuscript](paper/mercedes_partition.pdf) asserts that, for every triple of pairwise disjoint nonempty connected open subsets of the unit disk, the largest first Dirichlet eigenvalue is at least the square of the first positive zero of the Bessel function of order 3/2. Three equal sectors attain this value. The statement covers the full admissible class in AIM 010, including cells with arbitrary topology and boundary regularity and triples that need not cover the disk. It makes no uniqueness claim.

The proof uses the known sharp spherical three-partition theorem in the arbitrary-open formulation of Soave and Terracini, arXiv:1404.7288v2, Definition 1, equation (10) and Theorem 1.10 at N=3. A common radial map matches the angular terms of the disk and sphere after division by positive reference profiles. A Wronskian comparison proves that the remaining radial term is nonnegative. A logarithmic cutoff handles tests meeting the origin, and explicit sector cutoffs establish attainment. All these steps are included in the five-page paper.

The [target comparison](TARGET_COMPARISON.md) maps each original requirement to the manuscript. The [editable source](paper/mercedes_partition.tex) has an inline bibliography and no external figure or data inputs. This is an analytic proof claim; no numerical calculation or software certificate is a proof premise.

To compile from this directory with a standard LaTeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/mercedes_partition.tex
```

The source uses article, fontenc, lmodern, amsmath, amssymb, amsthm, geometry and hyperref. `PUBLIC_MANIFEST.json` records the four payload files and their SHA-256 hashes. `SHA256SUMS` covers those files and the manifest, excluding itself.

OpenAI Codex assisted proof exploration, source checks, symbolic calculations and drafting. Another fresh Codex context read the complete manuscript and checked the cited primary-source passages; the final notation and layout changes were then checked during recompilation. No separate detailed AI report is submitted. Human or formal verification has not been performed. Independent mathematical review is requested, and repository acceptance remains pending.
