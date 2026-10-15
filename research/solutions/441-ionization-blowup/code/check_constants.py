"""Replay the finite rational inequalities in the accompanying ionization note.

The published scalar inverse theorem remains an external dependency.
"""

from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
import platform


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "data"
EXPECTED_INPUTS = {
    "Re_Pstar.dat": "a020445a9830aebbceebdda17f6771e33d0a3a714ab11d89aa00959e09b4970b",
    "Im_Pstar.dat": "de553121fc460e50f7a7246fd262f0bcb0c77ebbbdc5057521eaf56e31a3879c",
}


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def scale(z, a):
    return z[0] * a, z[1] * a


def polynomial_value(poly, x):
    result = F(0)
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result


def main():
    if not __debug__:
        raise RuntimeError("Verification requires assertions: do not use python -O")
    re_path, im_path = SOURCE / "Re_Pstar.dat", SOURCE / "Im_Pstar.dat"
    re_coeff = [F(line) for line in re_path.read_text().splitlines() if line.strip()]
    im_coeff = [F(line) for line in im_path.read_text().splitlines() if line.strip()]
    assert len(re_coeff) == len(im_coeff) == 51
    coeff = list(zip(re_coeff, im_coeff))

    for name, expected in EXPECTED_INPUTS.items():
        actual = hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError("Published coefficient input changed: " + name)

    zero = F(0), F(0)
    plus, minus, derivative = zero, zero, zero
    for n, z in enumerate(coeff):
        plus = add(plus, z)
        minus = add(minus, scale(z, (-1) ** n))
        derivative = add(derivative, scale(z, n * n))

    # An independent polynomial recurrence checks T_n(+-1) and T_n'(1).
    chebyshev = [[F(1)], [F(0), F(1)]]
    for n in range(2, 51):
        current = [F(0)] * (n + 1)
        for k, value in enumerate(chebyshev[-1]):
            current[k + 1] += 2 * value
        for k, value in enumerate(chebyshev[-2]):
            current[k] -= value
        chebyshev.append(current)
    independent = []
    for component in (re_coeff, im_coeff):
        poly = [F(0)] * 51
        for n, value in enumerate(component):
            for k, monomial in enumerate(chebyshev[n]):
                poly[k] += value * monomial
        independent.append(
            (
                polynomial_value(poly, F(1)),
                polynomial_value(poly, F(-1)),
                polynomial_value([k * poly[k] for k in range(1, 51)], F(1)),
            )
        )
    assert plus == (independent[0][0], independent[1][0])
    assert minus == (independent[0][1], independent[1][1])
    assert derivative == (independent[0][2], independent[1][2])

    beta = F(772201763088846, 841768781900003)
    h = F(1, 10**10)
    beta_min, beta_max = beta - h, beta + h
    assert F(9, 10) < beta_min < beta_max < 1
    phi = -2 * beta * beta / (1 + beta * beta), 2 * beta / (1 + beta * beta)
    f_minus_center = add(add(minus, scale(plus, -1)), mul(phi, derivative))
    derivative_abs_upper = abs(derivative[0]) + abs(derivative[1])
    f_minus_re_upper = f_minus_center[0] + 2 * h * derivative_abs_upper
    radius = F(12, 10**7)
    assert f_minus_re_upper + radius < -1
    derivative_sq = derivative[0] ** 2 + derivative[1] ** 2
    f_plus_sq_lower = 4 * beta_min**2 / (1 + beta_min**2) * derivative_sq
    assert f_plus_sq_lower > F(1, 100)
    assert radius < F(1, 1000)

    coefficient_abs_upper = sum(abs(z[0]) + abs(z[1]) for z in coeff)
    weighted_abs_upper = sum(n * n * (abs(z[0]) + abs(z[1])) for n, z in enumerate(coeff))
    polynomial_envelope = 2 * coefficient_abs_upper + 2 * weighted_abs_upper + radius
    assert polynomial_envelope < 50

    cj, cpsi = F(232), F(13)
    error = F(5, 10**6)
    residual = F(5, 10**9)
    g_lip = error + 20 * radius + 6 * radius**2
    perturb_norm, perturb_lip = F(1, 10**13), F(1, 10**6)
    selfmap = cj * (error * radius + 10 * radius**2 + 3 * radius**3 + residual + perturb_norm)
    contraction = cj * (g_lip + perturb_lip)
    original_sign_margin = F(4, 10**10) - cpsi * (
        error * radius + 10 * radius**2 + 3 * radius**3
    )
    obstruction_change = cpsi * (1 + g_lip * cj / (1 - contraction)) * perturb_norm
    assert selfmap < radius
    assert contraction < F(1, 100)
    assert original_sign_margin > F(1, 10**10)
    assert obstruction_change < F(1, 10**11)

    # M<50 follows from the exact triangle envelope (which is below 42).
    perturbation_envelope = 2 * F(50) ** 3 + 4 * F(50) ** 5 / beta_min
    perturbation_lipschitz = 6 * F(50) ** 2 + 20 * F(50) ** 4 / beta_min
    alpha4_bound = min(perturb_norm / perturbation_envelope, perturb_lip / perturbation_lipschitz)
    assert alpha4_bound > F(1, 10**23)

    result = {
        "status": "PASS",
        "scope": "Finite exact coefficient, endpoint and strict-margin inequalities only.",
        "source": "arXiv:2406.16597v3, Appendix A, polynomial P_*",
        "arithmetic": "fractions.Fraction; no rounded comparisons",
        "python_version": platform.python_version(),
        "coefficient_count": len(coeff),
        "input_sha256": EXPECTED_INPUTS,
        "independent_endpoint_check": "Chebyshev monomial recurrence",
        "exact_values": {
            "polynomial_envelope": str(polynomial_envelope),
            "left_endpoint_real_upper": str(f_minus_re_upper + radius),
            "right_endpoint_modulus_squared_lower": str(f_plus_sq_lower),
            "selfmap_upper": str(selfmap),
            "contraction_upper": str(contraction),
            "original_obstruction_margin_lower": str(original_sign_margin),
            "obstruction_change_upper": str(obstruction_change),
            "alpha4_profile_envelope_lower": str(alpha4_bound),
        },
        "claims_checked": [
            "9/10 < beta_* +/- 10^-10 < 1",
            "polynomial envelope < 50",
            "left endpoint including correction radius < -1",
            "right endpoint approximate-profile modulus squared > 1/100",
            "self-map upper bound < 1.2e-6",
            "contraction upper bound < 1/100",
            "original obstruction margin > 1e-10",
            "new obstruction change < 1e-11",
            "0 < alpha4 <= 1e-23 satisfies the profile forcing envelopes",
        ],
        "limitations": [
            "Does not recertify the published scalar inverse/residual theorem.",
            "Does not simulate the PDE or supply an explicit Cauchy threshold or initial datum.",
        ],
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
