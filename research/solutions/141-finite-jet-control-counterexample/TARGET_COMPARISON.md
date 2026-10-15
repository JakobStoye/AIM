# Comparison with the original target

Target: [AIM 141 at a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/141-finite-jet-small-time-control.md).
The paper gives a negative answer by an analytic counterexample.

| Original requirement | Paper result and location | Scope |
|---|---|---|
| All real-analytic systems in dimensions n>=3 | Theorem 1 uses one polynomial system in R^5 | One admissible counterexample negates the universal implication; no n=3/4 classification |
| Equilibrium drift at zero | Displayed original and perturbed drifts vanish at zero | Same hypothesis |
| Measurable controls in the fixed cube | Theorem 1 and proof use (u,v) in [-1,1]^2 throughout | Same control class and bounds |
| Original small-time local controllability | Theorem 1 invokes the exact full-neighborhood result in Jin's earlier Theorem 1; Section 2 identifies its signed-loop and four-coordinate steering proof | Full Euclidean neighborhood, not an axis-only premise |
| One original tuple before choosing N | The system in equation (1) remains fixed | Original tuple independent of N |
| Every prescribed finite Taylor order N | Choose k>=1 with 2k>N | All finite N, not a finite computational range |
| Every field and multi-index derivative through total order N | Controlled fields are unchanged; the drift difference is x_5^(2k)e_4 | Complete matching N-jet |
| The matched tuple should retain controllability | Equations (5)--(9) prove that every fourth-axis endpoint in all sufficiently small durations has nonnegative fourth coordinate | The perturbed tuple is not small-time locally controllable |
| Reachability in time at most t | The proof explicitly takes the union over every duration 0<=T<=t<=tau_k | Same at-most-time definition |
| External theorem applicability | Section 2 states Jin's Lemma 2 with C^2/Lipschitz/third-derivative bounds and all six zero endpoint jets before applying it | Exact credited mathematical inputs |

The original system and its logarithmic estimate are prior results. The added
argument establishes an obstruction for each high-order positive drift
perturbation uniformly over every admissible control, then matches the full
finite jet. The package does not claim human peer review, formal verification
or a result for each individual dimension n>=3.
