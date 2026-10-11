# Comparison with the full target of AIM 555

Original statement: [Problem 555 at revision c9929805cece044705abaaebe1cebddac1ba11a6](https://github.com/MColbrook/AIM/blob/c9929805cece044705abaaebe1cebddac1ba11a6/problems/555-nonadaptive-randomization-gain.md).
Manuscript: [The maximal gain of nonadaptive randomization](paper/main.pdf).
References below use the manuscript's theorem and equation numbering.
This is a complete solution claim awaiting independent mathematical review.

| Original requirement | Manuscript evidence | Coverage |
|---|---|---|
| Real Banach spaces and a bounded linear operator | Section 3 defines X_q, Y and S_q in (5), proves completeness and the norm bound | Same class; a family inside the permitted supremum |
| Closed unit-ball inputs | Section 1 and the summed-norm estimate in Section 3 | Every unit-ball input |
| Fixed continuous deterministic functionals, arbitrary reconstruction | Section 1; Lemma 2 uses indistinguishable x and -x and imposes no condition on reconstruction | Full deterministic algorithm class |
| Continuous randomized linear measurements | Section 2 specifies grouped linear measurements; Section 3 extends each from a finite block | No nonlinear measurement or unbounded information |
| Complete list and reconstruction chosen independently of input | Section 2 hashes/signs and Section 3 choices depend only on n, q and seed | Nonadaptive for every input |
| At most n measurements for every realization | Section 3: prefix costs at most n/2 and the remaining block budget costs at most n/2 | Strict realization-wise budget |
| Worst-input expected norm | Section 1 definition; Proposition 3 and (11) | Expected norm, with input supremum outside expectation |
| Error jointly measurable | Section 3: finite seed space and continuous realized reconstruction give continuous scalar norm error in x | The target's scalar error condition; no separability assumption on Y |
| Inputs distributed over infinitely many blocks | Section 3 expectation estimate bounded by epsilon times the complete X_q norm | Every mixed input, not only single-block test vectors |
| One fixed operator and spaces throughout each n-limit | Section 3 fixes q,p,s,X_q,Y,S_q before n is introduced | No dimension-dependent operator substitution |
| Both rates finite | Theorem 4: deterministic lower bound (8) and universal comparison (12) exclude infinite randomized rate | Every family member belongs to the supremum's admissible class |
| Polynomial rate is the supremum of Big-O exponents | Section 1 definition; logarithmic factor in (11) is absorbed for every smaller exponent | No unproved endpoint Big-O estimate |
| Maximal increase randomized minus deterministic | (1), Theorem 4 and (7) | Gain at least 1-3/(2q)+1/q^2 for even q >= 4 |
| Determine the full supremum | Proof of Theorem 1: universal upper one and admissible family gains tending to one | G=1; in particular gain strictly above 1/2 is possible |
| Constants and quantifiers | Section 3 fixes D by (10) for each fixed q; all n-estimates use that same D | Dependence on the chosen operator is allowed; no uniform-in-q estimate claimed |

## Imported results and their roles

- Kunsch--Wnuk, arXiv:2410.23067v2, Proposition 4.1: the finite-dimensional
  nonadaptive CountSketch expected-infinity-norm estimate for 1 <= p <= 2,
  with explicit grouped-measurement cost. Manuscript Proposition 3 states the
  specialization, and Section 3 checks its parameters and homogeneous scaling.
- Krieg--Novak--Ullrich, arXiv:2406.07108v2, symmetric case of Corollary 14,
  with the continuous-information formulation in Section 6.3: manuscript
  equation (12). The adaptive randomized error on its right is bounded by
  the manuscript's nonadaptive randomized error. This proves finite-rate
  admissibility and the universal upper gain one.
- Krieg--Ullrich, arXiv:2602.02066v2, Section 10.2, equation (10.10): the
  original interval and question, used for positioning rather than as a proof
  of the new lower construction.

All version-specific locators are identified explicitly in the bibliography.
The manuscript contains the complete publishable argument. No conclusion is
based on tests, finite numerical experiments, or undisclosed supplementary
proof material. Exact individual rates and attainment by a single operator
are outside the claims of this note.
