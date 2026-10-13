# Symmetric four-color laws on a branched ray

This package claims a complete computer-assisted nonexistence proof for
[AIM Problem 584 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/584-four-color-branched-ray.md).
The graph has a root, two adjacent leaves, and an infinite ray from the root.
There is no proper four-coloring with the color symmetry, one-dependence,
and common ordered-path law required in that statement. The stationary,
reflection-invariant line law is arbitrary.

The claim is submitted for independent mathematical review. No human or
formal certification, or upstream acceptance, is claimed.

- [Paper (PDF)](paper/main.pdf) and [editable TeX source](paper/main.tex)
- [Target comparison](TARGET_COMPARISON.md)
- [Exact certificate](certificate/farkas.json)
- [Verifier](src/verify_certificate.py) and [probability rules](src/probability_rules.py)
- [Tests](test/test_certificate.py)
- [Reproduction case and actual output](numerical_case/README.md)
- [Environment and build instructions](ENVIRONMENT.md)
- [File manifest](PUBLIC_MANIFEST.json) and [SHA-256 checksums](SHA256SUMS)

## Proof and verification

An analytic recurrence on the infinite ray shows that the probability of
any specified one-step extension is at most half its prefix probability.
Finite marginal and deletion identities determine 78 short cylinder
probabilities in terms of two parameters. At the required lengths their
products use only the parameters, their square, and their mixed product.
The certificate combines 8,245 identities and 7,244 valid nonnegative
expressions. All 8,298 probability and moment coefficients cancel exactly,
leaving the negative constant

```text
-4663173554073621650668701/229601458397122150289899520 < -1/50.
```

The verifier reconstructs each identity from its geometry and color word;
it does not trust a stored coefficient matrix. It uses Python's exact
`fractions.Fraction` arithmetic. The displayed decimal approximation and
elapsed time are informational; no floating-point tolerance or optimizer
is used to decide validity.

Run from this directory with the Python standard library:

```sh
python3 src/verify_certificate.py certificate/farkas.json
python3 -m unittest discover -s test -v
python3 numerical_case/replay_certificate.py
```

The exported package was replayed successfully, and all 12 tests passed.
Tests include corrupted-certificate rejection, ordered-leaf and reflection
checks, independent-set bounds, short-cylinder values, and separate line-law
and star-neighbor controls. The analytic derivation of the constraints is
part of the paper and must also be reviewed.

The certificate SHA-256 is
`c64ca628b2ea2b324a840827ef7571b9d68f2a8fd4039c7c0baab43581bf4f67`.

## Scope and attribution

The theorem retains all the symmetries and arbitrary-set one-dependence
in the original question. It uses the infinite continuation and makes no
nonexistence claim for a fixed finite truncation. Restriction also rules
out the corresponding graph when either finite arm is lengthened.

Holroyd and Liggett's [*Finitely dependent coloring*, arXiv:1403.2448v4](https://arxiv.org/abs/1403.2448v4)
provides the known symmetric one-dependent line coloring. Liggett and Tang's
[*One-dependent colorings of the star graph*, arXiv:1804.06877v3](https://arxiv.org/abs/1804.06877v3)
proves nonextension for that prescribed line law in Proposition 1.4 and
distinguishes the arbitrary-law question. These are background references;
the present contradiction derives its necessary identities directly from
the stated assumptions.

The manuscript author is Kaiwen Jin, contact `yui.ui.siki@gmail.com`.
OpenAI Codex assisted with literature retrieval, exploration, proof and
certificate development, code verification, and writing. An additional
fresh-context review by the same AI vendor examined the manuscript, cited
sources, and certificate implementation, including a separate exact
reconstruction. This is AI review and is not independent human or formal
verification. Independent mathematical review is requested.
