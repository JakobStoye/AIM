# A polynomial obstruction to binary expansion

This package contains a proposed counterexample to
[AIM 640: Coboundary expansion of random balanced Cayley complexes](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/640-random-balanced-cayley-expansion.md).

For every fixed simplicial dimension k>=2, the elementary abelian groups
G_d=(F2)^d have the following deterministic obstruction. For every allowed
set A, the dimension of H^{k-1}(Y_{A,k};F2) is at least
sum_{j=0}^{min(k,d)} binom(d,j)-|A|. A positive lower bound forces the
original unnormalized coboundary expansion constant to be zero.
Since D(G_d)=2^d, every set of the prescribed logarithmic size
ceil(C log D(G_d)) has zero expansion for all sufficiently large d,
for every fixed C>0. The requested success probability is therefore
eventually zero along this group sequence, for any positive expansion threshold.

- [Complete manuscript](paper/main.pdf)
- [Editable LaTeX source](paper/main.tex)
- [Comparison with every original requirement](TARGET_COMPARISON.md)
- [AI-use disclosure](AI_USE.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

The manuscript gives the complete analytic proof. Its argument uses Boolean
polynomial functions, finite linear algebra and the literal common skeleton
of the specified complexes. No computation or private supplement is needed
to establish the result.

To rebuild with a standard LaTeX installation, run the following commands
from the `paper/` directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The governing construction and conjecture are credited to Roy Meshulam,
[Random Balanced Cayley Complexes, arXiv:2211.02085v1](https://arxiv.org/abs/2211.02085v1),
Sections 1–2 and Conjecture 8.1. Independent mathematical review is requested.
Catalogue classification is left to the maintainers.

