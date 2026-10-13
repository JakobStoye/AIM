"""Dense, symmetric Fourier storage with ordinary linear convolution.

An array of length 2K+1 represents modes -K,...,K. No Nyquist convention,
circular convolution or intermediate projection is used.
"""
from dataclasses import dataclass
import numpy as np
from scipy.fft import fft, ifft, next_fast_len


@dataclass(frozen=True)
class Fourier:
    coefficients: np.ndarray

    def __post_init__(self):
        a = np.asarray(self.coefficients)
        if a.ndim != 1 or a.size % 2 != 1 or a.size == 0:
            raise ValueError("Expected a nonempty odd-length one-dimensional array")
        if not np.all(np.isfinite(a)):
            raise ValueError("Fourier coefficients must be finite")
        dtype = np.clongdouble if a.dtype.itemsize > 16 else np.complex128
        object.__setattr__(self, "coefficients", np.array(a, dtype=dtype, copy=True))

    @property
    def cutoff(self):
        return self.coefficients.size // 2

    @property
    def modes(self):
        return np.arange(-self.cutoff, self.cutoff + 1, dtype=np.int64)

    def project(self, cutoff):
        if not isinstance(cutoff, (int, np.integer)) or cutoff < 0:
            raise ValueError("cutoff must be a nonnegative integer")
        a = np.zeros(2 * cutoff + 1, dtype=self.coefficients.dtype)
        m = min(cutoff, self.cutoff)
        a[cutoff-m:cutoff+m+1] = self.coefficients[self.cutoff-m:self.cutoff+m+1]
        return Fourier(a)

    def nonzero(self):
        a = self.coefficients.copy()
        a[self.cutoff] = 0
        return Fourier(a)

    def airy(self, time):
        if not np.isfinite(time):
            raise ValueError("time must be finite")
        real = np.longdouble if self.coefficients.dtype == np.clongdouble else float
        phase = np.asarray(self.modes, dtype=real)**3 * real(time)
        return Fourier(self.coefficients * np.exp(1j * phase))

    def inverse_derivative(self, order=1):
        if order not in (1, 2):
            raise ValueError("Only inverse derivative orders 1 and 2 are supported")
        a = np.zeros_like(self.coefficients)
        nz = self.modes != 0
        a[nz] = self.coefficients[nz] / (1j * self.modes[nz])**order
        return Fourier(a)

    def scale(self, scalar):
        return Fourier(self.coefficients * scalar)

    def add(self, other):
        cutoff = max(self.cutoff, other.cutoff)
        return Fourier(self.project(cutoff).coefficients + other.project(cutoff).coefficients)


def convolve(left, right, *, method="auto"):
    """Full polynomial product; output cutoff is the sum of input cutoffs."""
    a, b = left.coefficients, right.coefficients
    if method not in ("auto", "direct", "fft"):
        raise ValueError("Unknown convolution method")
    if method == "direct" or (method == "auto" and min(a.size, b.size) <= 193):
        return Fourier(np.convolve(a, b))
    size = a.size + b.size - 1
    padded = next_fast_len(size)
    return Fourier(ifft(fft(a, padded) * fft(b, padded))[:size])


def l2_norm(f):
    """L2 norm for the measure dx/(2 pi)."""
    return float(np.sqrt(np.sum(np.abs(f.coefficients)**2)))


def sobolev_norm(f, exponent):
    return float(np.sqrt(np.sum((1.0 + f.modes**2)**exponent * np.abs(f.coefficients)**2)))
