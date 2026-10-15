# Scope of the domain clarification

The statement under discussion is
[AIM 423 at revision a153f469ee0ea64e876b2ad97c79d252c19a3e22](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/423-magnetic-airy-half-plane-spectrum.md),
which asks for nonempty spectrum at every real nonzero parameter, including
all intermediate magnitudes.

The note concerns the literal ordinary H1_0 domain in that statement. It
does not resolve the intended spectral question for the different natural
closed magnetic Dirichlet realization.

The [original problem sheet](https://nsa.fjfi.cvut.cz/problems/04_AIM_2015/2015-02/2015-02_AIM_Almog_2.pdf)
reports known nonemptiness for sufficiently small and sufficiently large
nonzero magnitudes of the parameter. The remaining intended spectral
question concerns intermediate magnitudes. This note does not extend those
closed-realization spectral results.

| Requirement or interpretation | Result in the note | Scope |
|---|---|---|
| Half-plane y>0 and complex L2 | Section 1 fixes exactly this space and geometry | Same |
| Magnetic expression -partial_x^2-(partial_y-i x^2/2)^2+i c y | Equation (1), with no replacement by a nonmagnetic expression | Same |
| Printed ordinary H1_0 and distributional operator expression | Equation (2) defines the restriction T_c | Same literal domain |
| Every real c different from zero, including intermediate magnitudes | Proposition 1 and Section 2 apply for each fixed real c, without a sign or size assumption | All nonzero c covered for the literal restriction; c=0 also satisfies the stated domain result |
| Parameter dependence and convergence | Equation (7) permits a constant C_c depending on the fixed parameter; equations (10)--(11) give strong L2 convergence of functions and operator images | No estimate uniform in c is claimed or needed |
| Closedness of the printed restriction | Section 2 gives an explicit strong graph limit outside its domain | The restriction is nonclosed |
| Spectrum defined by bounded inverse of a bijective shift | Section 3 proves that this inverse property forces closedness | Spectrum of the printed nonclosed restriction is the whole complex plane under this convention |
| Spectrum defined only for closed operators | The printed restriction is nonclosed | The prerequisite is not met |
| Natural closed magnetic Dirichlet realization | Section 3 distinguishes its magnetic Sobolev form domain | Spectral nonemptiness, eigenvalues and a physical threshold are not established here |
| Public imported facts | Brezis, Corollaries 4.23 and 4.24, supply density and uniqueness of locally integrable distributions; Almog--Helffer, pp.6 and12, equations (2.3), (2.4), (2.24), supplies the distinct magnetic-domain prescription | The note states the applications and writes out its graph-limit and bounded-inverse arguments |

The spectrum conclusion does not claim that every spectral point is an
eigenvalue. The distinction between ordinary and covariant derivatives is
part of the result and must be retained in any description of this package.
The note makes no novelty or priority claim.
