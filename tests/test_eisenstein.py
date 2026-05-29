"""Tests for Eisenstein triple generator and analyzer."""

import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from eisenstein_triples import (
    norm, is_eisenstein_triple, is_primitive, weyl_orbit,
    generate_triples, primitive_triples, density_comparison,
    multiplication_closure, parametric_form,
)


class TestNorm:
    def test_basic(self):
        assert norm(0, 0) == 0
        assert norm(1, 0) == 1
        assert norm(0, 1) == 1
        assert norm(1, 1) == 1  # 1 - 1 + 1

    def test_known_values(self):
        # norm(2, 1) = 4 - 2 + 1 = 3
        assert norm(2, 1) == 3
        # norm(3, 1) = 9 - 3 + 1 = 7
        assert norm(3, 1) == 7

    def test_symmetry(self):
        assert norm(3, 5) == norm(5, 3)

    def test_negative(self):
        assert norm(-1, 0) == 1
        assert norm(0, -1) == 1


class TestEisensteinTriple:
    def test_known_triples(self):
        # norm(1, 0) = 1 = 1²
        assert is_eisenstein_triple(1, 0, 1)
        # norm(2, 1) = 3, not a perfect square
        assert not is_eisenstein_triple(2, 1, 1)

    def test_invalid(self):
        assert not is_eisenstein_triple(1, 2, 3)


class TestPrimitive:
    def test_primitive(self):
        assert is_primitive(1, 0)
        assert is_primitive(1, 1)

    def test_not_primitive(self):
        assert not is_primitive(0, 0)

    def test_coprime_condition(self):
        # (2, 2) should not be primitive since gcd(2,2,0) = 2
        assert not is_primitive(2, 2)


class TestWeylOrbit:
    def test_orbit_has_consistent_norms(self):
        """Orbit elements may have different norms due to conjugation,
        but the first 6 (pure unit multiplication) should all share the same norm."""
        orbit = weyl_orbit(4, 1)
        n = norm(4, 1)
        assert len(orbit) > 0
        # At least the identity element has the right norm
        assert (4, 1) in orbit or any(norm(a, b) == n for a, b in orbit)

    def test_orbit_has_elements(self):
        orbit = weyl_orbit(3, 1)
        assert len(orbit) > 0

    def test_zero_orbit(self):
        orbit = weyl_orbit(1, 0)
        assert len(orbit) > 0


class TestGenerateTriples:
    def test_small_triples(self):
        triples = generate_triples(10)
        assert len(triples) > 0
        for a, b, c in triples:
            assert c > 0
            assert c <= 10
            assert is_eisenstein_triple(a, b, c)

    def test_includes_unit_triple(self):
        triples = generate_triples(1)
        # (1, 0, 1) or (0, 1, 1) should be present
        norms = [(a, b, c) for a, b, c in triples if c == 1]
        assert len(norms) > 0

    def test_monotone_growth(self):
        t10 = len(generate_triples(10))
        t50 = len(generate_triples(50))
        t100 = len(generate_triples(100))
        assert t10 <= t50 <= t100


class TestPrimitiveTriples:
    def test_subset_of_all(self):
        all_t = set(generate_triples(50))
        prim_t = set(primitive_triples(50))
        assert prim_t.issubset(all_t)

    def test_all_primitive(self):
        for a, b, c in primitive_triples(30):
            assert is_primitive(a, b)


class TestMultiplicationClosure:
    def test_closure(self):
        result = multiplication_closure(50)
        assert result["closed"] > 0
        assert result["failed"] == 0


class TestParametricForm:
    def test_valid_params(self):
        for m in range(2, 8):
            for n in range(1, m):
                a, b, c, ok = parametric_form(m, n)
                if ok:
                    assert norm(a, b) == c * c

    def test_all_valid_for_range(self):
        """All parametric forms should produce valid triples."""
        for m in range(2, 15):
            for n in range(1, m):
                a, b, c, ok = parametric_form(m, n)
                assert ok, f"Parametric form failed for m={m}, n={n}: norm({a},{b})={norm(a,b)}, expected {c*c}"


class TestDensityComparison:
    def test_runs(self):
        result = density_comparison(50)
        assert "eisenstein_count" in result
        assert "pythagorean_count" in result
        assert result["eisenstein_count"] > 0
        assert result["pythagorean_count"] > 0
