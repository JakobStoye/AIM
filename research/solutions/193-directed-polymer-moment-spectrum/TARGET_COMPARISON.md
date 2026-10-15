# Comparison with AIM problem 193

Target: [A continuous strictly decreasing moment spectrum for Gaussian polymers](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/193-directed-polymer-moment-spectrum.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

The submitted Theorem 1.1 makes a complete-solution claim for this exact target.
The paper and this comparison are offered for independent mathematical review;
repository classification and acceptance remain with the maintainers.

| Target requirement | Manuscript location and argument |
|---|---|
| Simple random walk from zero on Z^3, with six equally likely neighbors | Introduction and equation (1.1) |
| iid standard Gaussian disorder independent of the walk | Introduction before (1.1) |
| Normalization by beta^2/2 at every time | Equation (1.1) |
| Original threshold p*(beta), using all real p>=1 and moments bounded uniformly over every length | Equation (1.2), the paragraph following (1.3), and the all-length estimate (3.24) |
| Original beta_c defined by almost sure positivity of the martingale limit | Equation (1.3); the martingale argument at the start of Section 2 |
| Nonempty finite domain (0,beta_c] | Equation (2.2), using the positive weak-disorder/L2 interval and a Gaussian fractional-moment estimate |
| Finite p*(beta) for each beta>0 | Diagonal path bound (2.3) |
| Strict decrease for every pair 0<b<beta<=beta_c | Proposition 2.1, especially (2.7), from the exact Gaussian identity (2.8) and Nelson hypercontractivity |
| Critical value p*(beta_c)=5/3 | Equation (2.4), citing Junk-Lacoin, arXiv:2502.04113v2, Corollary 2.5; critical weak disorder uses its Theorem 2.1 and simple-walk discussion |
| Interior left continuity | Equation (2.5), citing Junk-Lacoin, arXiv:2405.04335v3, Corollary 2.11(i) |
| Interior right continuity when p*(beta)<=2, including equality 2 | Final proof in Section 3.5; strictness gives p*>5/3 there, so Junk, arXiv:2307.05097v3, Theorem 1.2(i) applies |
| Interior right continuity when p*(beta)>2 | Proposition 3.1 and Section 3.5; each fixed real 2<s<p*(beta) persists on an upward temperature-parameter interval |
| Continuity at beta_c from the left | Critical weak disorder plus (2.5), applied explicitly in Section 3.5 |
| Divergence of p*(beta) as beta decreases to zero | Proposition 2.1, using an actually bounded second moment at a positive parameter |
| Every finite real value in [5/3,infinity) is attained exactly once | Theorem 1.1 and the intermediate-value argument in Section 3.5 |
| No assumed boundedness of the moment at p=p*(beta) | Explicit after (1.3); the stability proof fixes strict gaps 2<s<p<q<p*(beta_0) in (3.2) |

The finite probability-vector supports in Section 3 represent the exact endpoint
laws at each finite polymer length. They may grow without bound with the length.
The constants in (3.22)-(3.24) do not depend on those support sizes. This does
not impose a finite-support assumption on the Gaussian disorder or restrict
the uniform-in-length claim to a finite range.

The source question is the Gaussian three-dimensional instance of Berger's
Conjecture 3.32. The paper does not claim the corresponding general-disorder
or arbitrary-dimension conjecture. The critical, left-continuity and low-moment
right-continuity results are credited to their actual sources; the paper supplies
the high-moment local stability argument. The result is analytic and uses no
numerical experiment, finite certificate or formal-proof artifact.
