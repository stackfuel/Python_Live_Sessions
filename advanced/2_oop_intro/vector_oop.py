# vector_oop.py

from math import acos, sqrt


class Vector2D:
    def __init__(self, x=0, y=0):
        """Initialize a vector with x and y coordinates."""
        self.components = (x, y)

    def __getitem__(self, index):
        """Get the x or y coordinate by index."""
        return self.components[index]

    def __repr__(self):
        """Return a string representation of the vector."""
        return f"Vector2D({self.components[0]}, {self.components[1]})"

    def __add__(v1, v2):
        """Add two vectors."""
        return Vector2D(v1[0] + v2[0], v1[1] + v2[1])

    def __sub__(v1, v2):
        """Subtract two vectors."""
        return Vector2D(v1[0] - v2[0], v1[1] - v2[1])

    def __mul__(v, factor):
        """Multiply a vector by a scalar or a Vector2D object."""
        if isinstance(factor, Vector2D):
            return Vector2D(v[0] * factor[0], v[1] * factor[1])

        return Vector2D(v[0] * factor, v[1] * factor)

    def dot_product(v1, v2):
        """Calculate the dot product of two vectors."""
        return v1[0] * v2[0] + v1[1] * v2[1]

    def __abs__(v):
        """Calculate the magnitude of a vector."""
        return sqrt(v[0] ** 2 + v[1] ** 2)

    def normalize(v):
        """Normalize a vector to unit length."""
        mag = abs(v)
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector2D(v[0] / mag, v[1] / mag)

    def angle_with(v1, v2):
        """Calculate the angle in radians between two vectors."""
        # Berechnen von Kosinus des Winkels
        cos_angle = v1.dot_product(v2) / (abs(v1) * abs(v2))
        
        # Einschränken auf den Bereich [-1, 1]
        cos_angle = max(-1, min(1, cos_angle))

        return acos(cos_angle)
