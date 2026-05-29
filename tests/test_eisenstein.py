"""Tests for eisenstein_triples.py — Eisenstein integer triple generation and properties."""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from eisenstein_triples import (
    norm, is_eisenstein_triple, is_primitive, weyl_orbit,
    generate_triples, primitive_triples, density_comparison,
    multiplication_closure, parametric_form,
)


class TestNorm:
    """Test the Eisenstein norm a² - ab + b²."""

    def test_basic_values(self):
        assert norm(1, 0) == 1
        assert norm(0, 1) == 1
        assert norm(1, 1) == 1
        assert norm(0, 0) == 0

    def test_known_triples(self):
        # (3, 5): 9 - 15 + 25 = 19, not a perfect square
        assert norm(3, 5) == 19
        # (3, 8): 9 - 24 + 64 = 49 = 7²
        assert norm(3, 8) == 49
        assert is_eisenstein_triple(3, 8, 7)

    def test_norm_nonnegative(self):
        for a in range(-10, 11):
            for b in range(-10, 11):
                assert norm(a, b) >= 0

    def test_norm_symmetry(self):
        """norm(a,b) = norm(b,a) = norm(a-b,a) for D₆ symmetry."""
        assert norm(3, 7) == norm(7, 3)
        assert norm(3, 7) == norm(-4, -7)


class TestIsTriple:
    def test_known_triples(self):
        assert is_eisenstein_triple(3, 8, 7)
        assert is_eisenstein_triple(5, 8, 7)
        assert is_eisenstein_triple(7, 15, 13)

    def test_non_triples(self):
        assert not is_eisenstein_triple(1, 2, 3)
        assert not is_eisenstein_triple(2, 3, 4)


class TestPrimitivity:
    def test_unit_is_primitive(self):
        assert is_primitive(1, 0)
        assert is_primitive(0, 1)

    def test_zero_zero_not_primitive(self):
        assert not is_primitive(0, 0)

    def test_scaled_not_primitive(self):
        # (2, 2) = 2 * (1, 1), norm = 4
        assert not is_primitive(2, 2)

    def test_primitive_triple(self):
        assert is_primitive(3, 8)


class TestWeylOrbit:
    def test_orbit_rotation_preserves_norm(self):
        """The 6 rotations (multiplication by units) preserve the norm."""
        # The first 6 elements are the unit multiples, which should all have same norm
        a, b = 3, 8
        unit_multiples = [
            (a, b),           # identity
            (-b, a - b),      # ×ω
            (b - a, -a),      # ×ω²
            (-a, -b),         # ×(-1)
            (b, b - a),       # ×(-ω)
            (a - b, a),       # ×(-ω²)
        ]
        norms = set(norm(x, y) for x, y in unit_multiples)
        assert len(norms) == 1

    def test_orbit_contains_original(self):
        orbit = weyl_orbit(3, 8)
        assert (3, 8) in orbit

    def test_orbit_size_at_most_12(self):
        orbit = weyl_orbit(3, 8)
        assert len(orbit) <= 12

    def test_orbit_size_exactly_12(self):
        """For nonzero (a,b) with a≠b, orbit should have exactly 12 elements."""
        orbit = weyl_orbit(3, 8)
        assert len(orbit) == 12


class TestGeneration:
    def test_generate_small(self):
        triples = generate_triples(10)
        # All should have c <= 10 and c > 0
        for a, b, c in triples:
            assert c <= 10
            assert c > 0
            assert norm(a, b) == c * c

    def test_primitive_subset(self):
        """Primitive triples should be a subset of all triples."""
        all_t = set(generate_triples(30))
        prim_t = set(primitive_triples(30))
        assert prim_t.issubset(all_t)

    def test_generation_increasing(self):
        """More triples at higher max_c."""
        t10 = len(generate_triples(10))
        t50 = len(generate_triples(50))
        assert t50 > t10


class TestParametricForm:
    def test_parametric_produces_triples(self):
        count = 0
        for m in range(2, 15):
            for n in range(1, m):
                a, b, c, ok = parametric_form(m, n)
                if ok:
                    assert is_eisenstein_triple(a, b, c)
                    count += 1
        assert count > 0

    def test_parametric_verification(self):
        """Every valid parametric form should pass the norm check."""
        for m in range(2, 20):
            for n in range(1, m):
                a, b, c, ok = parametric_form(m, n)
                if ok:
                    assert norm(a, b) == c * c


class TestDensityComparison:
    def test_density_runs(self):
        result = density_comparison(50)
        assert result['eisenstein_count'] > 0
        assert result['pythagorean_count'] > 0
        assert result['ratio'] > 0


class TestMultiplicationClosure:
    def test_closure(self):
        result = multiplication_closure(30)
        assert result['closed'] > 0
        assert result['failed'] == 0
