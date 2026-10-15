# Positive harmonic profiles outside convex cones

This package contains a proposed analytic solution of [AIM problem 460](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/460-singular-stable-cone-positive-solution-uniqueness.md), at repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

[The manuscript](paper/manuscript.pdf), by Kaiwen Jin, proves proportionality of the two positive harmonic profiles in the complete stated class. The spectral measure can be singular, including finite directional support. The cone is proper, closed and convex with nonempty interior; each globally continuous profile is zero on the cone and has its own polynomial growth exponent strictly below the operator order. See Theorem 1.1 and the [target comparison](TARGET_COMPARISON.md).

The main estimate bounds the entire polynomial growth norm by one interior value. Normalization at a maximizing scale, boundary compactness and a supporting-ball barrier give this bound. An annular comparison and dilation then bound the ratio globally; an extremal nonnegative difference proves proportionality.

The package supplies the [editable LaTeX source](paper/manuscript.tex). It uses an analytic proof and the cited public mathematical sources. There is no proof-critical computation or numerical experiment. AI assistance is disclosed at the end of the manuscript. Independent mathematical review is requested.

To rebuild from this package with a standard TeX installation, run the following command three times from the package root:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=paper paper/manuscript.tex
```

No additional source or asset is required. Compilation checks the document, while the mathematical claims remain subject to review. `PUBLIC_MANIFEST.json` identifies the selected content files; `SHA256SUMS` records their hashes and the manifest hash.
