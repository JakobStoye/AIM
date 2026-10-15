# Target comparison: AIM 379

Target: [Uniqueness of strong-KPP equilibria on general unbounded domains](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/379-strong-kpp-unbounded-uniqueness.md), repository revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Result: Theorem 1 of [the manuscript](paper/main.pdf) is an analytic counterexample to the universal assertion. The following map is based on that finished manuscript and the public target.

| Original requirement | Manuscript location and supplied object | Scope |
| --- | --- | --- |
| Dimension d >= 2 | Theorem 1 and Section 3 use d=21, with x in R^20 and y in R | One allowed dimension suffices for a counterexample |
| Connected, unbounded domain | Section 4, equation (11); a strip between two graphs, connected through y=0 | Exact domain class |
| Common-radius uniformly bounded C^{2,gamma} boundary charts | Section 4: global graphs, bounded derivatives through order 3 and graph separation at least pi | gamma=1/2, common chart radius and uniform norms |
| Homogeneous f in C^{1,gamma}([0,infinity)) | Section 1, equation (2); bounded reaction with bounded Lipschitz derivative | gamma=1/2, including the global bounded-norm convention |
| f(0)=f(1)=0, f'(0)>0, positive on (0,1), negative above 1 | Equation (2) and the following verification | Every sign clause holds |
| f(s)/s strictly decreasing on (0,1] | Equation (2): ratio 1-s on this interval | Exact required interval |
| Fixed beta in [0,1) | Section 1 after Theorem 1 takes beta=0, zero Dirichlet trace | An admitted parameter; no other Robin claim |
| Bounded positive classical solutions | Theorem 1; Lemma 2; Section 4 constructs U and T, locally C^{2,1/2} up to the true boundary and between 0 and 1 | Exact solution concept |
| At most one such solution | Equations (12) and (14) and the last comparison in Section 4: U(x,0)>=q^{-1}>Bq^{-2}>=T(x,0) for sufficiently large fixed q | Uniqueness fails on the same domain with the same reaction and boundary parameter |
| No periodicity or spectral-gap condition | Lemma 2 uses bounded exhaustions and fixed-patch estimates; Sections 3-4 give explicit barriers | No such extra hypothesis is imposed |
| Uniform constants and behavior at infinity | Section 3 fixes R=10^6 and b=20000; Section 4 fixes finite B from one compact collar before choosing separation points | One domain and fixed constants, not a changing-domain limit |
| Imported elliptic theory | Lemma 2 cites Gilbarg-Trudinger Theorem 8.9, Corollary 8.36, Theorem 9.19 (k=1), Lemma 6.18, Corollaries 6.3/6.7; Section 2 cites its weak chain rule | Identity principal coefficients, bounded forces, zero true-boundary data and fixed local patches meet the stated conditions |

The quantifier conclusion is a negation: existence of one admissible (d, domain, f, beta) with two distinct equilibria disproves uniqueness asserted for every admissible choice. It does not classify all remaining choices.

The introduction credits Berestycki-Graham's original conjecture and conditional uniqueness theorem, their later open-question formulation, and Rossi-Tough's dimension results and shrinking-obstacle counterexamples. The paper's added construction is the uniformly smooth graph domain and its explicit barrier argument. Independent mathematical review is pending.
