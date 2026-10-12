# Uniform covariance bounds for constrained Ising replicas

This package contains a complete analytic solution claim for
[AIM problem 576](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/576-ising-replica-covariance.md).
Independent mathematical review is requested.

Theorem 1.1 proves a finite covariance bound for every fixed real symmetric
interaction matrix and every partition of the sites, simultaneously for all
replica counts, all feasible conserved totals and all replica/site-dependent
external fields. The norm is the ordinary Euclidean operator norm of all
spins. The constant depends on the fixed interaction and partition, and is
independent of the replica count, totals and fields. Its dependence on the
interaction and dimension is not optimized.

The proof conditions two independent copies on their coordinatewise sum.
Their disagreement orientations then have no external field and zero
conserved totals. Pairing identical symmetric block laws gives a lower bound
for the conditioning probability; a centered Fourier expansion bounds the
second-moment numerator at the same scale. Sections 2--3 contain the entire
argument.

- [Manuscript (PDF)](paper/ising_replica_covariance.pdf)
- [Editable LaTeX source](paper/ising_replica_covariance.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [AI use and review disclosure](AI_USE.md)
- [File manifest](PUBLIC_MANIFEST.json)

The argument is purely analytic. There are no proof-critical computations,
experimental data, numerical claims or supplementary proof inputs.
To rebuild the manuscript with a standard LaTeX installation:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build paper/ising_replica_covariance.tex
```

The source is standalone and uses standard LaTeX packages. Compilation checks
format and references; it does not establish mathematical correctness.
Verify the distributed file hashes with:

```sh
shasum -a 256 -c SHA256SUMS
```

This package does not change the catalogue classification. Maintainer review
and acceptance remain separate from the submitted solution claim.
