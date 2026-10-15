# Comparison with AIM 162

Target: [An extreme solitary wave for the bidirectional Whitham system](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/162-extreme-bidirectional-solitary-wave.md),
revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.
Paper: [An extreme solitary wave for the bidirectional Whitham system](paper/manuscript.pdf),
Kaiwen Jin, 15 October 2026.

This comparison uses the finished manuscript and the public problem statement.
It presents a complete affirmative solution claim for mathematical review.

| Original requirement | Result and location in the paper | Scope |
|---|---|---|
| Real-line convolution kernel with Fourier symbol `tanh(xi)/xi`, continuously extended by 1 at zero | Equations (2) and (6); Fourier convention at the end of Section 1 | Exact symbol and mass-one normalization |
| Existence of a speed `c>1` | Theorem 1.1 and Lemma 4.3 | One speed, also satisfying `c<sqrt(3(sqrt(3)-1))` |
| An even continuous profile from the real line to the positive reals | Theorem 1.1; Lemmas 4.1 and 4.4 | Entire real line; strict positivity |
| Smoothness away from zero and strict decrease for positive x | Lemma 4.4 and Theorem 1.1 | Smooth on the punctured line; strict decrease on the whole positive half-line |
| Tending to zero at infinity | Lemma 4.3, using the balance in Lemma 4.2 | Both tails vanish; profile integrability is not assumed |
| Cubic equation `K*v=c^2 v-(3c/2)v^2+v^3/2` and crest `v(0)=c(1-1/sqrt(3))` | Equation (3), Proposition 3.3, Lemma 4.1 and Theorem 1.1 | Pointwise equation on the whole line, including the crest |
| Surface profile `eta=cv-v^2/2` with `eta(0)=c^2/3` | Theorem 1.1 and its closing proof | Exact profile reconstruction and crest identity |
| Both printed conservative PDEs for the traveling pair | Equations (1) and (23), and the proof of Theorem 1.1 | Globally in distributions; classically away from the moving crest |
| Estimates adequate for the growing-period construction | Lemma 2.2 and Proposition 2.5; Propositions 3.2--3.3 and Lemma 4.1 | Common modulus and drop; fixed-period smoothing constants may depend on the period |

The argument for highest positive waves at every sufficiently large period
is supplied in Section 3. Its global continuation uses Constantin--Strauss--
Varvaruca, Theorem 4, Remarks 3--4 and Figure 2 in preprint NI14051, pp.14--15;
the paper checks the full trivial line, transversality, Fredholm condition and
compact exhaustion there. The unique distinguished continuation is the source
input for the same-arm return argument, which is proved in Proposition 3.2.

The fixed-period multiplier, nodal and local smoothing inputs come from
Ehrnström--Johnson--Claassen, Proposition 2.7, Theorem 4.2 and Lemma 4.1,
with numbering tied to arXiv:1610.02603v2. Their Appendix B is credited for
positive highest waves at its fixed period. The real analytic implicit-function
input is Fučík--Nečas--Souček--Souček, Lemma 3R, printed p.57. The normalized
kernel and the stated extreme-solitary question are in Ehrnström--Mæhlen--
Varholm, Section 4.2 and Remark 4.8. All entries and public links appear in the
manuscript bibliography.

Nilsson--Wang's small solitary waves and Ehrnström--Nik--Walker's construction
for the unidirectional square-root multiplier are background comparisons. The
manuscript supplies the large-period positive construction and the zero-tail
argument for the bidirectional cubic itself. It makes no uniqueness, stability,
all-speed, integrable-tail or full Euler-wave claim.
