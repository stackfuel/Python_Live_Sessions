# vector_functional.py

from math import sqrt


def add(v1: tuple, v2: tuple) -> tuple:
    """Add two vectors."""
    return (v1[0] + v2[0], v1[1] + v2[1])

def sub(v1, v2):
    """Subtract two vectors."""
    return (v1[0] - v2[0], v1[1] - v2[1])

def mul(v, factor):
    """Multiply a vector by a scalar or a tuple of scalars."""
    if isinstance(factor, tuple):
        if len(factor) != 2:
            raise ValueError("Factor must be a scalar or a tuple of two scalars.")
        return (v[0] * factor[0], v[1] * factor[1])
    
    return (v[0] * factor, v[1] * factor)

def dot_product(v1, v2):
    """Calculate the dot product of two vectors."""
    return v1[0] * v2[0] + v1[1] * v2[1]

def abs(v):
    """Calculate the magnitude of a vector."""
    return sqrt(v[0] ** 2 + v[1] ** 2)

def normalize(v):
    """Normalize a vector to unit length."""
    mag = abs(v)
    if mag == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return (v[0] / mag, v[1] / mag)
