"""
Vollständige Test-Suite für die Vector-Klasse
Speichere dies als test_vector.py
"""
import pytest
import math
from vector import Vector


class TestVectorConstruction:
    """Tests für Vektorkonstruktion und Eigenschaften"""
    
    def test_empty_vector(self):
        v = Vector([])
        assert len(v) == 0
    
    def test_from_list(self):
        v = Vector([1, 2, 3])
        assert len(v) == 3
        assert list(v) == [1.0, 2.0, 3.0]
    
    def test_from_tuple(self):
        v = Vector((1, 2, 3))
        assert len(v) == 3
    
    def test_from_range(self):
        v = Vector(range(5))
        assert len(v) == 5
    
    def test_invalid_components(self):
        with pytest.raises(TypeError):
            Vector(["a", "b"])


class TestVectorArithmetic:
    """Tests für arithmetische Operationen"""
    
    @pytest.fixture
    def vectors_2d(self):
        return Vector([1, 2]), Vector([3, 4])
    
    def test_addition(self, vectors_2d):
        v1, v2 = vectors_2d
        assert v1 + v2 == Vector([4, 6])
    
    def test_subtraction(self, vectors_2d):
        v1, v2 = vectors_2d
        assert v2 - v1 == Vector([2, 2])
    
    def test_scalar_multiplication(self):
        v = Vector([1, 2, 3])
        assert v * 2 == Vector([2, 4, 6])
        assert 2 * v == Vector([2, 4, 6])
    
    def test_element_wise_multiplication(self, vectors_2d):
        v1, v2 = vectors_2d
        assert v1 * v2 == Vector([3, 8])
    
    def test_dot_product(self, vectors_2d):
        v1, v2 = vectors_2d
        assert v1 @ v2 == 11.0
    
    def test_division(self):
        v = Vector([2, 4, 6])
        assert v / 2 == Vector([1, 2, 3])
    
    def test_division_by_zero(self):
        v = Vector([1, 2, 3])
        with pytest.raises(ValueError):
            v / 0


class TestVectorComparison:
    """Tests für Vergleichsoperationen"""
    
    def test_equality(self):
        assert Vector([1, 2]) == Vector([1, 2])
        assert Vector([1, 2]) != Vector([2, 1])
    
    def test_magnitude_comparison(self):
        short = Vector([1, 0])
        long = Vector([3, 4])
        assert short < long
        assert long > short
    
    def test_hashable(self):
        v1 = Vector([1, 2])
        v2 = Vector([1, 2])
        assert hash(v1) == hash(v2)
        assert len({v1, v2}) == 1


class TestVectorAdvanced:
    """Tests für fortgeschrittene Operationen"""
    
    def test_magnitude(self):
        assert abs(Vector([3, 4])) == 5.0
        assert abs(Vector([1, 1, 1])) == pytest.approx(math.sqrt(3))
    
    def test_normalization(self):
        v = Vector([3, 4])
        normalized = v.normalize()
        assert abs(normalized) == pytest.approx(1.0)
        assert normalized == Vector([0.6, 0.8])
    
    def test_normalize_zero_raises(self):
        with pytest.raises(ValueError):
            Vector([0, 0]).normalize()
    
    def test_distance(self):
        v1 = Vector([0, 0])
        v2 = Vector([3, 4])
        assert v1.distance_to(v2) == pytest.approx(5.0)
    
    @pytest.mark.parametrize("v1,v2,expected_angle", [
        (Vector([1, 0]), Vector([0, 1]), math.pi/2),
        (Vector([1, 0]), Vector([1, 0]), 0.0),
        (Vector([1, 1]), Vector([1, 1]), 0.0),
    ])
    def test_angle(self, v1, v2, expected_angle):
        assert v1.angle_to(v2) == pytest.approx(expected_angle, abs=1e-7) # TODO: adjust vector angle precision


class TestVectorEdgeCases:
    """Tests für Edge Cases"""
    
    @pytest.mark.parametrize("dim", [1, 2, 3, 10, 100])
    def test_various_dimensions(self, dim):
        v = Vector([1] * dim)
        assert len(v) == dim
    
    def test_zero_vector_is_false(self):
        assert not bool(Vector([0, 0, 0]))
    
    def test_non_zero_vector_is_true(self):
        assert bool(Vector([1, 0, 0]))
    
    def test_negative_components(self):
        v = Vector([-1, -2, -3])
        assert -v == Vector([1, 2, 3])


# Führe Tests aus
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
    
    