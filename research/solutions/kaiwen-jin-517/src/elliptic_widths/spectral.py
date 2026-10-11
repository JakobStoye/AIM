"""Sphere multiplicities, determinant bounds, and symmetric form comparisons."""

from __future__ import annotations

import math
import operator
import numpy as np
from numpy.typing import ArrayLike, NDArray


def _integer(value: int, name: str, minimum: int = 1) -> int:
    if isinstance(value, (bool, np.bool_)):
        raise ValueError(f"{name} must be an integer >= {minimum}")
    try:
        value = operator.index(value)
    except TypeError as error:
        raise ValueError(f"{name} must be an integer >= {minimum}") from error
    if value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def _dimension(dimension: int) -> int:
    dimension = _integer(dimension, "dimension")
    if dimension not in (2, 3):
        raise ValueError("dimension must be 2 or 3")
    return dimension


def multiplicity(dimension: int, degree: int) -> int:
    """Multiplicity of a nonconstant degree on S^(dimension-1)."""
    dimension = _dimension(dimension)
    degree = _integer(degree, "degree")
    return 2 if dimension == 2 else 2 * degree + 1


def spherical_degrees(dimension: int, count: int) -> NDArray[np.int64]:
    """First count positive degrees, in increasing order with multiplicity."""
    dimension = _dimension(dimension)
    count = _integer(count, "count", 0)
    if count == 0:
        return np.empty(0, dtype=np.int64)
    maximum = (count + 1) // 2 if dimension == 2 else math.ceil(math.sqrt(count + 1))
    degrees = np.arange(1, maximum + 1, dtype=np.int64)
    repetitions = np.full(maximum, 2) if dimension == 2 else 2 * degrees + 1
    return np.repeat(degrees, repetitions)[:count]


def _bound_inputs(dimension, count, inner_radius, outer_radius, alpha, beta):
    dimension = _dimension(dimension)
    count = _integer(count, "count")
    values = np.asarray([inner_radius, outer_radius, alpha, beta], dtype=float)
    if not np.all(np.isfinite(values)):
        raise ValueError("radii and ellipticity bounds must be finite")
    if not 0 < inner_radius < outer_radius or not 0 < alpha <= beta:
        raise ValueError("require 0 < inner < outer and 0 < alpha <= beta")
    return dimension, count


def log_determinant_bound(
    dimension: int, count: int, inner_radius: float, outer_radius: float,
    alpha: float, beta: float,
) -> NDArray[np.float64]:
    """Upper bounds for log(product(s_j^2)), for all prefixes 1,...,count."""
    dimension, count = _bound_inputs(
        dimension, count, inner_radius, outer_radius, alpha, beta,
    )
    sums = np.cumsum(spherical_degrees(dimension, count) + dimension - 2, dtype=float)
    return (alpha / beta) * (math.log(inner_radius) - math.log(outer_radius)) * sums


def log_singular_bound(
    dimension: int, count: int, inner_radius: float, outer_radius: float,
    alpha: float, beta: float,
) -> NDArray[np.float64]:
    """Individual upper bounds deduced by taking prefix geometric means."""
    return log_determinant_bound(
        dimension, count, inner_radius, outer_radius, alpha, beta,
    ) / (2 * np.arange(1, count + 1))


def expanded_spectrum(dimension: int, log_by_degree: ArrayLike) -> NDArray[np.float64]:
    """Sort a finite set of radial modes by singular value with multiplicity.

    This is the spectrum of the supplied finite-degree subspace. It does not
    certify that uncomputed degrees cannot interlace.
    """
    dimension = _dimension(dimension)
    values = np.asarray(log_by_degree, dtype=float)
    if values.ndim != 1 or not np.all(np.isfinite(values)):
        raise ValueError("log_by_degree must be a finite one-dimensional array")
    degrees = np.arange(1, len(values) + 1)
    repeats = np.full(len(values), 2) if dimension == 2 else 2 * degrees + 1
    return np.sort(np.repeat(values, repeats))[::-1]


def generalized_eigenvalues(numerator: ArrayLike, denominator: ArrayLike) -> NDArray:
    """Ascending eigenvalues of Q x = lambda G x for symmetric Q, positive G.

    Cholesky whitening avoids forming G^(-1)Q, which is not symmetric.
    """
    q = np.asarray(numerator, dtype=float)
    g = np.asarray(denominator, dtype=float)
    if q.ndim != 2 or q.shape[0] != q.shape[1] or q.shape != g.shape or not len(q):
        raise ValueError("forms must be nonempty square matrices of equal shape")
    if not np.all(np.isfinite(q)) or not np.all(np.isfinite(g)):
        raise ValueError("forms must be finite")
    for form in (q, g):
        scale = max(float(np.linalg.norm(form, ord=np.inf)), 1.0)
        if np.max(np.abs(form - form.T)) > 1e-12 * scale:
            raise ValueError("forms must be symmetric")
    try:
        factor = np.linalg.cholesky((g + g.T) / 2)
    except np.linalg.LinAlgError as error:
        raise ValueError("denominator must be positive definite") from error
    left = np.linalg.solve(factor, (q + q.T) / 2)
    whitened = np.linalg.solve(factor, left.T).T
    return np.linalg.eigvalsh((whitened + whitened.T) / 2)
