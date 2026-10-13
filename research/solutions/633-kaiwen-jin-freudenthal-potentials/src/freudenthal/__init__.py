"""Continuous vector polynomial potentials with continuous curl.

The degree argument is the potential degree d=k+1. Coordinates used by
the assembler are integer cube coordinates; evaluation uses [0,1]^3.
"""

from .basis import PotentialBasis, construct_basis, dimension
from .geometry import BernsteinSpace, Mesh

__all__ = ["BernsteinSpace", "Mesh", "PotentialBasis", "construct_basis", "dimension"]
