# Comparison with AIM 485

Original target: [Optimal obstacle regularity for stable jump kernels with only angular integrability](https://github.com/MColbrook/AIM/blob/a153f469ee0ea64e876b2ad97c79d252c19a3e22/problems/485-general-stable-obstacle-optimal-regularity.md), revision `a153f469ee0ea64e876b2ad97c79d252c19a3e22`.

Submitted claim: Theorem 1.1 of [the manuscript](paper/main.pdf). All locations below refer to this manuscript. The original target prescribes its unique finite-energy minimizer. Theorem 1.1 is an a priori estimate for every minimizer in exactly that class; Lemma 4.1 also shows uniqueness through the energy zero-space argument. No additional regularity of the minimizer is assumed.

| Original requirement | Manuscript location and argument | Coverage |
| --- | --- | --- |
| Every n >= 2 and 0 < s < 1 | Theorem 1.1; Section 2 fixes precisely these ranges | Full |
| Nonnegative even a in L1 on the sphere; total mass <= Lambda | Equation (1.1) and Theorem 1.1; Section 2 identifies the density operator with the spectral formula | Full |
| Every quadratic directional moment >= lambda | Equation (1.1); Section 2 computes the general elliptic-class constants, and Appendix A derives directional cap mass | Full |
| Every nonnegative phi in C_c^infinity | Theorem 1.1 and Section 4 | Full |
| The prescribed energy and L^{2n/(n-2s)} finite-energy minimizer | Equations (1.2)--(1.3); Section 4 proves comparisons with admissible positive-part tests in that same homogeneous class | Full |
| Positive principal-value operator and its normalization | Introduction and equation (2.2); Section 4 uses energy = B(u,u)/2 | Full |
| Uniform full global C^{1,s} norm | Theorem 1.1; Proposition 4.3 gives separation from contact, and the closing proof covers all gradient pairs and the two supremum norms | Full |
| Constants only C(n,s,lambda,Lambda), without obstacle support radius | Theorem 1.1; compactness over the mass/moment class in Sections 2--3; fixed normalizations and support-independent forcing bound in Section 4 | Full |
| No stronger angular Lp assumption or positivity in every direction | Theorem 1.1; Appendix A uses cap mass and total mass, and Proposition 4.2 invokes only the density mass/moment flatness result | Full |

## Public inputs

The bibliography gives exact public source versions. The linear estimates, maximum principle, Liouville theorem and stable barrier come from Fernandez-Real and Ros-Oton, arXiv:2411.12455v1, Theorem 2.4.3, Lemma 2.3.5, Theorem 2.4.15(b), Corollary 2.4.14 and Lemma 2.6.2. The ball Hopf bound uses Grube, arXiv:2410.00829v1, Proposition 1.7(3) and Proposition 6.7; a smooth tangent ball and global nonnegativity satisfy its geometric and exterior assumptions. The half-line uniqueness input is Grube and Ros-Oton, arXiv:2605.18711v1, Theorem 1.1. The final flatness input is Ros-Oton and Weidner, arXiv:2308.01695v1, Proposition 5.8, applied only to angular densities. Its small forcing gradient, semiconvexity, actual free-boundary point, growth and Lipschitz profile approximation are checked in Section 4.

The necessary additional argument is the convex-primitive cone rigidity in Proposition 3.1, followed by the classification and radius-normalized approximation in Section 3. Appendix A supplies measure-uniform compactness instead of assuming that a density theorem automatically holds for singular measures.

## Scope and evidence

This is a complete analytic claim for the density-class target above. The auxiliary classification permits singular spectral measures, but the endpoint obstacle estimate for all such measures is not asserted. There are no numerical or computer-assisted proof claims. No separate detailed AI review is submitted; independent mathematical review is requested.
