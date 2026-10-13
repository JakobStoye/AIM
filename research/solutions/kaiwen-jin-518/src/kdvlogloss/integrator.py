"""Literal Li-Wu (1.4) with complete 2K/3K intermediate support.

The finite realization projects only the final single-step output. Its cutoff
is a fixed spatial discretization parameter, never a function of the timestep.
Endpoint differences can lose accuracy for very small timesteps; extended
precision and independent reference checks are supplied for that regime.
"""
import numpy as np
from .fourier import Fourier, convolve


def quadratic_stage(f, step):
    d = f.inverse_derivative()
    sd = d.airy(step)
    return convolve(sd, sd).nonzero().add(
        convolve(d, d).nonzero().airy(step).scale(-1)).scale(1/6)


def li_wu_step(f, step, cutoff=None):
    """Advance mean-zero Fourier data, retaining full intermediates.

    Input: Fourier data of cutoff K, finite step >=0, optional final cutoff.
    Output: the projection of the fixed polynomial scheme to the final cutoff.
    """
    if not np.isfinite(step) or step < 0:
        raise ValueError("step must be finite and nonnegative")
    if f.coefficients[f.cutoff] != 0:
        raise ValueError("The scheme requires exactly mean-zero input")
    cutoff = f.cutoff if cutoff is None else cutoff
    if step == 0:
        return f.project(cutoff)
    d = f.inverse_derivative()
    sd = d.airy(step)
    quadratic = quadratic_stage(f, step)
    h1 = convolve(sd, quadratic.inverse_derivative()).nonzero().scale(1/3)
    mean_square = np.sum(f.coefficients * f.coefficients[::-1])
    h2 = sd.scale(step * mean_square / 9)
    cube1 = convolve(convolve(sd, sd), sd).inverse_derivative()
    cube0 = convolve(convolve(d, d), d).inverse_derivative().airy(step)
    h3 = cube1.add(cube0.scale(-1)).scale(-1/54)
    a = quadratic.inverse_derivative(2)
    end1 = convolve(a, sd).inverse_derivative(2)
    end0 = convolve(a.airy(-step), d).inverse_derivative(2).airy(step)
    h4 = end1.add(end0.scale(-1)).scale(-1/(27*step))
    return f.airy(step).add(quadratic).add(h1).add(h2).add(h3).add(h4).project(cutoff).nonzero()


def twisted_rhs(time, coefficients):
    """Independent Galerkin ODE: v'=S_-t partial_x[(S_t v)^2]/2."""
    f = Fourier(coefficients)
    sf = f.airy(time)
    product = convolve(sf, sf).project(f.cutoff)
    return product.airy(-time).coefficients * (0.5j * f.modes)


def integrate(f, final_time, steps, *, snapshots=True):
    if not isinstance(steps, (int, np.integer)) or steps <= 0:
        raise ValueError("steps must be a positive integer")
    if not np.isfinite(final_time) or final_time <= 0:
        raise ValueError("final_time must be positive and finite")
    step = final_time / steps
    state = f
    trajectory = np.empty((steps+1, f.coefficients.size), dtype=f.coefficients.dtype) if snapshots else None
    if snapshots:
        trajectory[0] = state.coefficients
    for n in range(steps):
        state = li_wu_step(state, step)
        if snapshots:
            trajectory[n+1] = state.coefficients
    return trajectory if snapshots else state
