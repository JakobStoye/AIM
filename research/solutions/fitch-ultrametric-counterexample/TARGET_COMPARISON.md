# Comparison with AIM Problem 328

Frozen statement: [328, revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/328-fitch-ultrametric-ancestral-accuracy.md).

The original assertion is universal over every integer r>=5 and every finite
rooted strictly binary tree with at least two leaves, finite nonnegative edge
lengths and equal root-to-leaf height H. Under the specified rate-one symmetric
Neyman model, uniform root and uniform final Fitch tie breaking, it asks whether
accuracy is at least q_r(H)=1/r+(r-1)exp(-rH/(r-1))/r.

Theorem 1 supplies an admissible r=20 counterexample, hence negates that universal
assertion. No positive theorem or failure classification for other alphabets
is claimed.

| Original clause | Manuscript location and exact fulfillment |
|---|---|
| Integer r>=5 | Theorem 1 chooses r=20. |
| Finite tree; at least two leaves; two children at each internal vertex | Theorem 1 specifies rho with children a,v and v with children b,c. |
| Finite nonnegative lengths | Equation (3) specifies four strictly positive logarithmic lengths. |
| Equal root-to-leaf heights | Theorem 1 and start of proof give log16+log(5/4)=log20 and H=(19/20)log20. |
| Exact generator and rate | Equation (1) has diagonal -1 and off-diagonal 1/19 at r=20; equation (5) preserves that normalization. |
| Uniform root and conditional branch independence | Section 1 states the model; Section 2 conditions on root state 1, uses parent-conditioned terminal independence and branch independence, then removes root conditioning by label symmetry. |
| Literal Fitch recursion and uniform final tie | Section 1 defines the sets and final choice; equations (7)-(9) use the full cherry set and exact singleton/union cases. |
| One character on a known tree | The entire calculation uses the three observed states on one specified finite tree, with no sequence or topology-estimation limit. |
| Compare against any one leaf | Equations (2)-(4), equal heights and equation (5) give q_20(H)=39/400 for every leaf. |
| Strict failure | Equations (4) and (9) give 38829/400000 <39000/400000, deficit 171/400000. |

The proposed resolution is analytic and self-contained. The supplementary exact
verifier checks the finite arithmetic; it is not a substitute for the written
proof. Submission of this package does not establish upstream acceptance,
human peer review or formal verification.
