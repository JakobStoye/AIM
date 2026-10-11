"""Logarithmically rescaled analytic propagation through radial shells."""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np
from numpy.typing import ArrayLike, NDArray
from .spectral import _dimension, _integer


@dataclass(frozen=True)
class RadialCoefficient:
    """Piecewise radial and tangential coefficients.

    radii[i] is the outer edge of coefficient interval i. Interval zero is
    (0,radii[0]); later intervals are (radii[i-1],radii[i]).
    A = radial e_r e_r^T + tangential (I-e_r e_r^T) almost everywhere.
    Values at interfaces and at the origin do not affect weak solutions.
    """

    radii: ArrayLike
    radial: ArrayLike
    tangential: ArrayLike

    def __post_init__(self) -> None:
        arrays = [np.array(x, dtype=float, copy=True) for x in (
            self.radii, self.radial, self.tangential,
        )]
        if any(x.ndim != 1 or not len(x) for x in arrays):
            raise ValueError("radii and coefficients must be nonempty vectors")
        if len({len(x) for x in arrays}) != 1:
            raise ValueError("one coefficient pair is required per outer edge")
        if any(not np.all(np.isfinite(x)) or np.any(x <= 0) for x in arrays):
            raise ValueError("radii and coefficients must be positive and finite")
        if np.any(np.diff(arrays[0]) <= 0):
            raise ValueError("radii must be strictly increasing")
        for key, value in zip(("radii", "radial", "tangential"), arrays):
            value.setflags(write=False)
            object.__setattr__(self, key, value)

    @property
    def alpha(self) -> float:
        return float(min(np.min(self.radial), np.min(self.tangential)))

    @property
    def beta(self) -> float:
        return float(max(np.max(self.radial), np.max(self.tangential)))


def _log_ratio(end: float, start: float) -> float:
    relative = (end - start) / start
    return math.log1p(relative) if math.isfinite(relative) else math.log(end) - math.log(start)


def _radial_rates(offset: int, angular: int, radial: float, tangential: float) -> tuple[float, float]:
    """Reject unsupported dynamic ranges before dividing or taking logarithms."""
    ratio = tangential / radial
    if not math.isfinite(ratio) or ratio <= 0:
        raise FloatingPointError("coefficient ratio is not representable")
    gap = math.sqrt(offset * offset + 4 * ratio * angular)
    if not math.isfinite(gap) or gap <= 0:
        raise FloatingPointError("radial spectral gap is not representable")
    growing = 2 * ratio * angular / (gap + offset)
    if not math.isfinite(growing) or growing <= 0:
        raise FloatingPointError("regular radial exponent is not representable")
    return gap, growing


def log_radial_spectrum(
    dimension: int, coefficient: RadialCoefficient,
    inner_radius: float, max_degree: int,
) -> NDArray[np.float64]:
    """Return log energy restriction singular values for degrees 1,...,L.

    The regular radial solution starts as r^gamma in the core. At each
    interface f and q=a_r*r*f' are continuous. In t=log(r),
    (f,q)' = [[0,1/a_r],[a_t*l*(l+d-2),-(d-2)]] (f,q).
    The energy at r is r^(d-2)*f*q for a unit L2 spherical harmonic.
    We remove the growing exponential and normalize each two-vector.
    The inner radius can lie in the core, in a shell, or on an interface.
    No finite element grid or time discretization is used.
    """
    dimension = _dimension(dimension)
    max_degree = _integer(max_degree, "max_degree")
    if not isinstance(coefficient, RadialCoefficient):
        raise ValueError("coefficient must be a RadialCoefficient")
    outer_radius = float(coefficient.radii[-1])
    inner_radius = float(inner_radius)
    if not math.isfinite(inner_radius) or not 0 < inner_radius < outer_radius:
        raise ValueError("require finite 0 < inner_radius < outer_radius")
    first_radius = float(coefficient.radii[0])
    logs = np.empty(max_degree, dtype=float)
    offset = dimension - 2
    for index in range(max_degree):
        degree = index + 1
        angular = degree * (degree + offset)
        a0 = float(coefficient.radial[0])
        b0 = float(coefficient.tangential[0])
        _, gamma = _radial_rates(offset, angular, a0, b0)
        core_flux = a0 * gamma
        if not math.isfinite(core_flux) or core_flux <= 0:
            raise FloatingPointError("regular core flux is not representable")
        state = np.array([1.0, core_flux])
        norm = float(np.max(state))
        if not math.isfinite(norm) or norm <= 0 or not math.isfinite(gamma):
            raise FloatingPointError("core exponent is not representable")
        state /= norm
        scale = math.log(norm)
        initial_energy = offset * math.log(first_radius) + math.log(core_flux)
        inner_energy = None
        if inner_radius <= first_radius:
            inner_energy = initial_energy + (2 * gamma + offset) * _log_ratio(inner_radius, first_radius)
        outer_energy = initial_energy
        for shell in range(1, len(coefficient.radii)):
            start = float(coefficient.radii[shell - 1])
            end = float(coefficient.radii[shell])
            a = float(coefficient.radial[shell])
            b = float(coefficient.tangential[shell])
            gap, growing = _radial_rates(offset, angular, a, b)
            decaying = -offset - growing
            matrix = np.array([[0.0, 1 / a], [b * angular, -offset]])
            if not np.all(np.isfinite(matrix)):
                raise FloatingPointError("radial propagation matrix is not representable")
            projector = (matrix - decaying * np.eye(2)) / gap
            targets = [inner_radius, end] if start < inner_radius < end else [end]
            previous = start
            for target in targets:
                delta = _log_ratio(target, previous)
                weight = -math.expm1(-gap * delta)
                stable = (1 - weight) * np.eye(2) + weight * projector
                state = stable @ state
                if np.any(state <= 0) or not np.all(np.isfinite(state)):
                    raise FloatingPointError("nonpositive or nonfinite radial state")
                norm = float(np.max(state))
                state /= norm
                scale += growing * delta + math.log(norm)
                energy = offset * math.log(target) + math.log(state[0]) + math.log(state[1]) + 2 * scale
                if target == inner_radius:
                    inner_energy = energy
                outer_energy = energy
                previous = target
        if inner_energy is None:
            raise RuntimeError("inner energy was not sampled")
        logs[index] = (inner_energy - outer_energy) / 2
    if not np.all(np.isfinite(logs)):
        raise FloatingPointError("nonfinite spectrum")
    return logs
