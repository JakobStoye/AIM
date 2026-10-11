# Exact algebra library

The package uses Python integers, rational numbers and a prime field. It has
no runtime dependency outside the standard library. `aim519.core` re-exports
the low-level algebra routines; paper drivers use `audit`, `polynomial` and
`certificates` directly.

| Module | Mathematical contract |
|---|---|
| `magmatic` | A leaf is `()`. Products are sorted pairs of binary trees, so they are commutative and nonassociative. `magmatic(n)` enumerates all trees with exactly n leaves. `A=('A',)` and `Y(t)=('Y',t)` are independent free Lie letters. |
| `associative` | Integer dictionaries map words of generator tuples to coefficients. `lie_expansion` takes a Lyndon word with standard bracketing. `adjoint_x` returns PBW pairs `(word,potential)`, where `None` denotes absence of a potential factor. Its input must be a Lie polynomial for the paper's PBW-purity statements. |
| `mechanical` | Canonical simple unrooted trees record the number of momentum leaves at each vertex; `None` represents kinetic energy. `mechanical_bracket` uses the paper's Poisson sign and counts isomorphic contributions with multiplicity. Graphs passed to `canonical` must be connected trees with symmetric adjacency. |
| `linear` | `sparse_rank` performs exact modular column elimination and rejects a nonprime modulus. Its rank is a modular rank; a deficiency alone does not imply rational dependence. |
| `certificates` | `verify_block` independently checks a supplied integer matrix, block hash and saved pivots. It does not certify that its columns were constructed from the intended brackets. |
| `polynomial` | Sparse exponents follow `(q_1,...,q_d,p_1,...,p_d)`; coefficients use `Fraction`. Calibration compares direct Poisson differentiation with tree contraction. Optional details retain exact input and output values. |
| `audit` | `run_audit` reconstructs every input column and checks its image, lowering formulas and full modular rank. Its cutoff is 2--18 and its output directory must not exist. |

For degree-one word decoding the marker leaf count exceeds the sum of all
side-label leaf counts. For higher-degree retraction its count strictly
exceeds every old label, so its new generator is absent from the input. These
are mathematical preconditions, not general promises for arbitrary words.
The paper drivers choose valid markers automatically.

Cached sparse mapping results are copied before return; callers cannot poison
the cache by modifying a returned dictionary. Such caches keep at most 4096
entries per function. Exact coefficients can grow rapidly, so higher cutoffs
require a separate resource assessment.

Run the reference identities, known dimensions, graph relabelling and corrupt
certificate checks with `python3 -m unittest discover -s test -v` from the
repository root. The suite also passes with `python3 -O`.
