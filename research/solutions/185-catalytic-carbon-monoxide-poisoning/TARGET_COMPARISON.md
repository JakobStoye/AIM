# Correspondence with AIM Problem 185

Original target:
[Selection of the carbon-monoxide poisoning phase](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/185-catalytic-carbon-monoxide-poisoning.md),
revision a153f469ee0ea64e876b2ad97c79d252c19a3e22.

The submitted manuscript is *CO phase selection for a stirred catalytic
surface model*, by Kaiwen Jin. Its Theorem 1 claims the entire target.

| Original requirement | Location in the manuscript | Correspondence |
| --- | --- | --- |
| States vacant, CO and oxygen on the infinite lattice Z2 | Section 1 model; Appendix A construction | Same process and domain |
| A vacant site becomes CO at rate p | Section 1 transition table; equation (4) | Same site rate |
| Each unordered vacant neighbor pair becomes two oxygen atoms at rate q/4 | Section 1 table and O(t) in Section 2 | Same pair convention and rate |
| An unordered mixed CO/oxygen pair becomes vacant at rate r/4 | Section 1 table; equation (3) and R(t) | Same pair convention and rate |
| Each pair exchanges states at finite positive rate gamma | Section 1 table; Lemma 2 and equation (9) | All effective exchanges are included |
| Every p>q>0 and every finite positive r,gamma | Section 1 hypotheses, equations (7)--(9), Theorem 1 | No additional parameter threshold or limiting regime |
| Every iid initial law with positive CO density | Theorem 1 and its proof in Section 3 | No lower positive-density bound |
| Every finite K, with all-CO probability tending to one as real time tends to infinity | Theorem 1, equation (1), final proof paragraph | Same quantifiers and conclusion |

Theorem 1 also proves that every site eventually remains CO almost surely.
The sitewise random times need not have a finite maximum over the infinite
lattice. This additional conclusion is not a claim of simultaneous global
absorption at a finite time.

Durrett and Swindle's *Coexistence results for catalysts* (1994),
Theorem 1 and its proof on pp. 490--492, supply the model and the
signed-density/vacancy estimate credited in Section 2. The manuscript supplies
the reaction count, finite-change and marked-field phase-selection argument.
The pinned Durrett book's Open Problem 5.4.6 is cited for the question;
the result here is stated for the iid initial-law class specified by this
AIM target, without asserting its broader initial-data formulation.

This is a full solution claim offered for mathematical review. It is not an
announcement of upstream acceptance or a formal proof certificate.
