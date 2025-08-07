from typing import Any, Sequence, Union, Iterator, Iterable
from functools import total_ordering
import numbers
import math


@total_ordering  # This decorator will automatically provide the __le__ and __gt__ methods based on __lt__ and __eq__
class Vector:
    """
    A class to represent a mathematical vector in arbitrary dimensions.

    This class provides basic vector operations such as addition, 
    scalar multiplication, element-wise multiplication, dot product, 
    magnitude calculation, and ordering comparisons based on the vector's 
    magnitude.

    Comparison operators (==, <, <=, >, >=) compare vectors based on 
    their Euclidean norm (magnitude). The ordering methods are 
    automatically completed using the `functools.total_ordering` decorator.

    Attributes:
        _components (tuple): The components of the vector stored as an immutable tuple.

    Example usage:
        >>> v1 = Vector(1, 2, 3)
        >>> v2 = Vector(4, 5, 6)
        >>> v1 + v2
        Vector(5.0, 7.0, 9.0)
        >>> v1 * 3
        Vector(3.0, 6.0, 9.0)
        >>> v1 * v2  # Element-wise multiplication
        Vector(4.0, 10.0, 18.0)
        >>> v1 @ v2  # Dot product
        32.0
        >>> abs(v1)
        3.7416573867739413

    Methods:
        __init__(*components):
            Initialize the vector with the given components.

        __iter__():
            Return an iterator over the vector's components.

        __repr__():
            Return the official string representation of the vector.

        __str__():
            Return the nicely printable string representation.

        __eq__(other):
            Return True if the vectors have the same components.

        __lt__(other):
            Compare vectors based on their magnitude.

        __add__(other):
            Add two vectors component-wise.

        __mul__(other):
            If other is a scalar, multiply each component by the scalar.
            If other is a vector, perform element-wise multiplication.

        __matmul__(other):
            Compute the dot product of two vectors.

        __abs__():
            Return the Euclidean norm (magnitude) of the vector.

        __array__(dtype=None):
            Convert the vector to a NumPy ndarray.

    Notes:
        - The class assumes immutable vectors; modification of components 
          after creation is not supported.
        - When using the multiplication operator (`*`):
            * `vector * scalar` performs scalar multiplication.
            * `vector * vector` performs element-wise multiplication.
            * `vector @ vector` computes the dot product, following NumPy convention.

    """

    def __init__(
        self, *components: Union[numbers.Real, Sequence[numbers.Real]]
    ) -> None:
        """
        Initialize a vector with given components.
        Accepts either individual components or a sequence of components.
        
        If no components are provided, an empty vector is created.

        >>> Vector(1, 2.5, 3.0)
        Vector(1.0, 2.5, 3.0)
        >>> Vector([1.0, 2.0, 3.0])
        Vector(1.0, 2.0, 3.0)
        >>> Vector()  # Empty vector
        Vector()
        """
        if len(components) == 1 and isinstance(components[0], Sequence):
            if all(isinstance(c, numbers.Real) for c in components[0]):
                components = components[0]
        if not all(isinstance(c, numbers.Real) for c in components):
            raise TypeError("All components must be real.")
        
        
        self._components = tuple(float(c) for c in components)
        

    def __repr__(self) -> str:
        """
        Unambiguous string representation for debugging.
        Should ideally allow reconstructing the object.
        This method is used by the `repr()` function.

        >>> repr(Vector(1.0, 2.0, 3.0))
        'Vector(1.0, 2.0, 3.0)'
        >>> repr(Vector(1.0))
        'Vector(1.0)'
        """
        return f"Vector({', '.join(str(c) for c in self._components)})"

    def __str__(self) -> str:
        """
        User-friendly string representation.
        This method is used by the `str()` and `print()` function.

        >>> str(Vector(1.0, 2.0, 3.0))
        '<1.0, 2.0, 3.0>'
        >>> str(Vector(1.0))
        '<1.0>'
        >>> print(Vector(1.0, 2.0, 3.0))
        <1.0, 2.0, 3.0>
        """
        return f"<{', '.join(str(c) for c in self._components)}>"

    # container protocol methods
    def __len__(self) -> int:
        """
        Return the number of components (dimensionality) in the vector.

        This method is used by the `len()` function.

        >>> len(Vector(1.0, 2.0, 3.0))
        3
        >>> len(Vector(1.0))
        1
        """
        return len(self._components)

    def __getitem__(self, index: Union[int, slice]) -> Union[float, "Vector"]:
        """
        Return component at index, or a new Vector for a slice.

        >>> v = Vector(1.0, 2.0, 3.0)
        >>> v[0]
        1.0
        >>> v[1]
        2.0
        >>> v[-1]
        3.0
        >>> v[1:3]
        Vector(2.0, 3.0)
        >>> v[:2]
        Vector(1.0, 2.0)
        >>> v[1:1]
        Vector()
        """
        result = self._components[index]
        if isinstance(index, slice):
            return Vector(result)
        
        return result

    def __setitem__(self, index: int, value: float) -> None:
        """
        Prevent item assignment to maintain immutability.
        Raises an error if an attempt is made to set a component.

        >>> v = Vector(1.0, 2.0, 3.0)
        >>> v[0] = 5.0
        Traceback (most recent call last):
        TypeError: Vector objects are immutable and cannot be modified.
        """
        raise TypeError("Vector objects are immutable and cannot be modified.")

    def __iter__(self) -> Iterator[float]:
        """
        Return an iterator over the components of the vector.
        This allows iteration over the vector's components.

        >>> v = Vector(1.0, 2.0, 3.0)
        >>> list(v)
        [1.0, 2.0, 3.0]
        >>> for component in v:
        ...     print(component)
        1.0
        2.0
        3.0
        """
        return iter(self._components)
    

    def __contains__(self, item: float) -> bool:
        """
        Check if a component is in the vector.
        This allows using the `in` keyword to check for component existence.

        >>> v = Vector(1.0, 2.0, 3.0)
        >>> 2.0 in v
        True
        >>> 4.0 in v
        False
        """
        return item in self._components

    # Equality, inequality, and hash methods

    def __eq__(self, other: Any) -> bool:
        """
        Check if two vectors are equal.
        Two vectors are considered equal if they have the same components.

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> v2 = Vector(1.0, 2.0, 3.0)
        >>> v1 == v2
        True
        >>> v3 = Vector(1.0, 2.0, 4.0)
        >>> v1 == v3
        False
        """
        if not isinstance(other, Vector):
            return NotImplemented
        
        return self._components == other._components



    def __lt__(self, other: "Vector") -> bool:
        """
        Compare vectors based on their magnitude.
        
        

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> v2 = Vector(3.0, 4.0)
        >>> v1 < v2
        True
        >>> v2 < v1
        False
        """
        return abs(self) < abs(other)

    def __hash__(self) -> int:
        """
        Return a hash value for the vector.
        This allows vectors to be used as keys in dictionaries or sets.

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> type(hash(v1))
        <class 'int'>
        """
        pass


    # other comparison methods
    # not needed due to @total_ordering decorator
    # Note: The ordering of vectors by their magnitude is not consistent with other collections of python objects,
    # where the default behavior is to compare by the first differing component.
    
    
    # def __le__(self, other: "Vector") -> bool:
    #     """
    #     Check if this vector is less than or equal to another vector based on magnitude.

    #     >>> v1 = Vector(1.0, 2.0, 3.0)
    #     >>> v2 = Vector(3.0, 4.0)
    #     >>> v1 <= v2
    #     True
    #     >>> v2 <= v1
    #     False
    #     """
    #     if not isinstance(other, Vector):
    #         return NotImplemented
    #     return abs(self) <= abs(other)

    # def __gt__(self, other: "Vector") -> bool:
    #     """
    #     Compare vectors based on their magnitude.

    #     >>> v1 = Vector(1.0, 2.0, 3.0)
    #     >>> v2 = Vector(3.0, 4.0)
    #     >>> v1 > v2
    #     False
    #     >>> v2 > v1
    #     True
    #     """
    #     if not isinstance(other, Vector):
    #         return NotImplemented
    #     return abs(self) > abs(other)

    # def __ge__(self, other: "Vector") -> bool:
    #     """
    #     Check if this vector is greater than or equal to another vector based on magnitude.

    #     >>> v1 = Vector(1.0, 2.0, 3.0)
    #     >>> v2 = Vector(3.0, 4.0)
    #     >>> v1 >= v2
    #     False
    #     >>> v2 >= v1
    #     True
    #     """
    #     if not isinstance(other, Vector):
    #         return NotImplemented
    #     return abs(self) >= abs(other)

    # Arithmetic operations
    
    
    def __neg__(self) -> "Vector":
        """
        Negate the vector (multiply by -1).

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> -v1
        Vector(-1.0, -2.0, -3.0)
        """
        pass

    def __pos__(self) -> "Vector":
        """
        Return the vector itself (unary plus).

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> +v1
        Vector(1.0, 2.0, 3.0)
        """
        pass
    
    def __abs__(self) -> float:
        """
        Return the magnitude (length) of the vector.

        >>> abs(Vector(3.0, 4.0))
        5.0
        >>> abs(Vector(1.0, 2.0, 2.0))
        3.0
        """
        return math.sqrt(sum(c**2 for c in self._components))
    
    
    def __add__(self, other: "Vector") -> "Vector":
        """
        Add two vectors component-wise.

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> v2 = Vector(4.0, 5.0, 6.0)
        >>> v1 + v2
        Vector(5.0, 7.0, 9.0)
        """
        pass

    def __radd__(self, other: "Vector") -> "Vector":
        """
        Right-hand addition for vector addition.

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> v2 = Vector(4.0, 5.0, 6.0)
        >>> v2 + v1
        Vector(5.0, 7.0, 9.0)
        """
        pass

    def __sub__(self, other: "Vector") -> "Vector":
        """
        Subtract two vectors component-wise.

        >>> v1 = Vector(4.0, 5.0, 6.0)
        >>> v2 = Vector(1.0, 2.0, 3.0)
        >>> v1 - v2
        Vector(3.0, 3.0, 3.0)
        """
        pass

    def __rsub__(self, other: "Vector") -> "Vector":
        """
        Right-hand subtraction for vector subtraction.

        >>> v1 = Vector(4.0, 5.0, 6.0)
        >>> v2 = Vector(1.0, 2.0, 3.0)
        >>> v2 - v1
        Vector(-3.0, -3.0, -3.0)
        """
        pass

    def __mul__(self, other: Union[numbers.Real, "Vector"]) -> Union["Vector", float]:
        """
        Multiply a vector by a scalar or another vector (pairwise multiplication).

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> v2 = Vector(4.0, 5.0, 6.0)
        >>> v1 * 2
        Vector(2.0, 4.0, 6.0)
        >>> v1 * v2
        Vector(4.0, 10.0, 18.0)
        """
        pass

    def __rmul__(self, other: Union[numbers.Real, "Vector"]) -> Union["Vector", float]:
        """
        Right-hand multiplication for scalar multiplication.

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> v2 = Vector(4.0, 5.0, 6.0)
        >>> 2 * v1
        Vector(2.0, 4.0, 6.0)
        """
        pass

    def __matmul__(self, other: "Vector") -> float:
        """
        Calculate the dot product of two vectors.

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> v2 = Vector(4.0, 5.0, 6.0)
        >>> v1 @ v2
        32.0
        """
        pass

    def __truediv__(self, scalar: numbers.Real) -> "Vector":
        """
        Divide a vector by a scalar.

        >>> v1 = Vector(2.0, 4.0, 6.0)
        >>> v1 / 2
        Vector(1.0, 2.0, 3.0)
        """
        pass



    def __bool__(self) -> bool:
        """
        Return True if the vector is not zero (i.e., has non-zero components).

        >>> bool(Vector(1.0, 2.0, 3.0))
        True
        >>> bool(Vector(0.0, 0.0, 0.0))
        False
        """
        pass

    # Additional methods for advanced functionality

    def normalize(self) -> "Vector":
        """
        Normalize the vector (make it a unit vector).

        >>> v1 = Vector(3.0, 4.0)
        >>> v1.normalize()
        Vector(0.6, 0.8)
        """
        pass

    def distance_to(self, other: "Vector") -> float:
        """
        Calculate the Euclidean distance to another vector.

        >>> v1 = Vector(1.0, 2.0, 3.0)
        >>> v2 = Vector(4.0, 5.0, 6.0)
        >>> v1.distance_to(v2)
        5.196152422706632
        """
        pass

    def angle_to(self, other: "Vector") -> float:
        """
        Calculate the angle (in radians) between this vector and another vector.

        >>> v1 = Vector(1.0, 0.0)
        >>> v2 = Vector(0.0, 1.0)
        >>> v1.angle_to(v2)
        1.5707963267948966
        """
        pass


# Demonstration of the Vector class
def demonstrate_vector_class():
    """
    Comprehensive demonstration of all Vector class features.
    """
    print("=== Vector Class Demonstration ===\n")

    # Construction and representation
    print("1. Construction and String Representation:")
    v1 = Vector(3, 4)
    v2 = Vector(1, 2, 3)
    print(f"v1 = {v1!r}")  # Uses __repr__
    print(f"v1 = {v1}")  # Uses __str__
    print(f"v2 = {v2}")
    print()

    # Container operations
    print("2. Container Operations:")
    print(f"Length of v1: {len(v1)}")
    print(f"First component of v1: v1[0] = {v1[0]}")
    print(f"Components of v1: {list(v1)}")  # Uses __iter__
    print(f"Is 3.0 in v1? {3.0 in v1}")  # Uses __contains__
    x, y = v1  # Unpacking works due to __iter__
    print(f"Unpacked v1: x={x}, y={y}")
    print()

    # Arithmetic operations
    print("3. Arithmetic Operations:")
    v3 = Vector(1, 1)
    v4 = Vector(2, 3)
    print(f"v3 = {v3}")
    print(f"v4 = {v4}")
    print(f"v3 + v4 = {v3 + v4}")
    print(f"v3 - v4 = {v3 - v4}")
    print(f"2 * v3 = {2 * v3}")  # Scalar multiplication
    print(f"v3 * v4 = {v3 * v4}")  # Pairwise multiplication
    print(f"v3 * v4 = {v3 @ v4}")  # Dot product
    print(f"v3 / 2 = {v3 / 2}")
    print(f"-v3 = {-v3}")
    print(f"+v3 = {+v3}")

    print()

    # Magnitude and boolean operations
    print("4. Magnitude and Boolean Operations:")
    print(f"|v1| = {abs(v1)}")
    print(f"bool(v1) = {bool(v1)}")
    zero_vector = Vector(0, 0)
    print(f"zero_vector = {zero_vector}")
    print(f"bool(zero_vector) = {bool(zero_vector)}")
    print()

    # Comparison operations
    print("5. Comparison Operations:")
    short_vec = Vector(1, 1)
    long_vec = Vector(3, 4)
    print(f"short_vec = {short_vec} (magnitude: {abs(short_vec):.2f})")
    print(f"long_vec = {long_vec} (magnitude: {abs(long_vec):.2f})")
    print(f"short_vec < long_vec: {short_vec < long_vec}")
    print(f"short_vec == long_vec: {short_vec == long_vec}")
    print(f"short_vec == Vector(1, 1): {short_vec == Vector(1, 1)}")
    print()

    # Hash and set operations
    print("6. Hashing and Set Operations:")
    vectors = {Vector(1, 2), Vector(3, 4), Vector(1, 2)}  # Duplicate will be removed
    print(f"Set of vectors: {vectors}")
    vector_dict = {Vector(1, 0): "unit x", Vector(0, 1): "unit y"}
    print(f"Vector as dictionary key: {vector_dict[Vector(1, 0)]}")
    print()

    # Advanced vector operations
    print("7. Advanced Vector Operations:")
    a = Vector(3, 4, 0)
    b = Vector(1, 2, 0)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"Distance from a to b: {a.distance_to(b):.2f}")
    print(f"Angle between a and b: {math.degrees(a.angle_to(b)):.2f}°")
    print(f"a normalized: {a.normalize()}")

    # Error handling demonstration
    print("8. Error Handling:")
    try:
        Vector(1, 2) + Vector(1, 2, 3)  # Different dimensions
    except ValueError as e:
        print(f"Dimension mismatch error: {e}")

    try:
        v1[0] = 5  # Attempt to modify immutable vector
    except TypeError as e:
        print(f"Immutability error: {e}")

    try:
        zero_vector.normalize()  # Normalize zero vector
    except ValueError as e:
        print(f"Zero vector normalization error: {e}")


if __name__ == "__main__":
    demonstrate_vector_class()
