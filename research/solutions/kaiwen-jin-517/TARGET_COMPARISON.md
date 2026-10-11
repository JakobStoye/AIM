# Target comparison: AIM Problem 517

Submitted manuscript: Kaiwen Jin, *Local approximation widths for elliptic
equations with measurable coefficients* (11 October 2026).

Original statement: [517. Sharp local approximation widths for rough elliptic
equations](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/517-sharp-local-elliptic-widths.md),
at commit c9929805cece044705abaaebe1cebddac1ba11a6.

This is a complete solution claim submitted for independent mathematical
review. The complete argument is in [the manuscript](paper/main.pdf), with
[editable source](paper/main.tex). Its validity does not depend on numerical
experiments or an additional proof supplement.

| Target requirement | Manuscript statement or proof | Relation |
|---|---|---|
| Dimensions d=2,3 | Introduction; Theorem 1.1 | Identical range |
| Concentric open cubes omega compactly contained in omega-star | Introduction; Section 3 | Identical domain class; the proof uses a fixed finite ball covering inside omega-star |
| Real symmetric measurable A with alpha I <= A <= beta I and 0 < alpha <= beta < infinity | Equation (1); Theorem 1.1 | Identical coefficient and ellipticity assumptions; no continuity, periodicity or scale separation |
| Nonzero chi in W1-infinity(omega) intersect H10(omega) | Introduction; Section 3 | Identical cutoff class; the product lies in H10 and its zero extension is justified |
| H1 solutions tested against every H10(omega-star) function | Introduction; Lemma 2.1 and Section 3 | Identical weak solution concept |
| Normalization a_omega(chi u,chi)=0 | Introduction; Section 3 normalization | Identical representative condition; the cutoff identity makes it a positive weighted mean |
| T u = chi times the restriction of u to omega | Equation (2) | Identical operator and target |
| Outer source energy at most one and target a_omega energy | Equations (1)--(2) | Identical seminorm/norm conventions; normalization removes constant ambiguity |
| Approximation by linear V contained in H10(omega), dim V <= n | Equation (2); Section 3 | Identical width convention; every local constant is included in the dimension count |
| d_n(T) <= C exp(-c n^(1/(d-1))) for every integer n >= 1 | Theorem 1.1 and its proof in Section 3 | Full proposed conclusion, including n smaller than the fixed covering size |
| Constants may depend on the fixed coefficient, geometry and cutoff | Theorem 1.1; Section 3 | Exactly the allowed dependence; contrast independence is not claimed |

The decisive result is Lemma 2.3: expanding-ball energy Gram matrices satisfy
a determinant estimate from an ordinary harmonic extension and tangential
boundary energy. The argument uses almost-everywhere Sobolev slices, handles
singular Gram matrices directly, and does not require unique continuation.
Spherical harmonic counting and compact restriction yield Theorem 2.4.
Section 3 transfers its approximation spaces to the prescribed cutoff while
preserving the target energy norm and the dimension budget.

The exact constant-coefficient ball spectrum in Section 4 explains the
boundary-dimension exponent. It is not presented as a matching lower bound
for every cutoff or a solution of all abstract PDE cases in Ma's framework.
The computations in Section 4 are ordinary numerical checks of selected
radial models and finite-dimensional form comparisons. They do not certify
the theorem for every coefficient. No formal verification or independent
human review is claimed.

AI use: ChatGPT supplied an initial proof candidate and literature notes.
Codex expanded the proof, checked cited primary passages, prepared and tested
the numerical code, and assisted with writing and typesetting. The manuscript
ends with the same factual disclosure. No separate detailed AI report is
submitted; independent mathematical review is requested.
