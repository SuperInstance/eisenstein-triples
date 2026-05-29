# eisenstein-triples

Eisenstein integer triples — the hexagonal analog of Pythagorean triples — with D₆ orbit computation, parametric generation, and statistical analysis.

## Overview

Eisenstein triples are integer solutions to **a² − ab + b² = c²**, where the left side is the norm form of the Eisenstein integer ring Z[ω] with ω = e^{2πi/3}. Just as Pythagorean triples arise from the Gaussian integers Z[i], Eisenstein triples arise from the hexagonal lattice — the densest packing in 2D.

This library provides generators, verifiers, and analysis tools for exploring the structure of these triples and their symmetries.

## Key Concepts

- **Eisenstein norm**: N(a + bω) = a² − ab + b², the fundamental quadratic form on the hexagonal lattice
- **D₆ Weyl orbit**: Each Eisenstein triple generates up to 12 related triples under the symmetries of Z[ω] (6 rotations × conjugation)
- **Parametric form**: For coprime m > n > 0 with 3 ∤ (m−n): a = m² − n², b = 2mn − n², c = m² − mn + n²
- **Primitivity**: gcd(|a|, |b|, |a−b|) = 1, the Eisenstein ring analog of coprime Pythagorean triples

## Files

| File | Description |
|------|-------------|
| [`eisenstein_triples.py`](eisenstein_triples.py) | Core library: triple generation, D₆ orbit computation, primitivity testing |
| [`analyze.py`](analyze.py) | Statistical analysis comparing Eisenstein vs Pythagorean triple distributions |
| [`verify_proofs.py`](verify_proofs.py) | Comprehensive verification of claimed mathematical results |
| [`verify_eisenstein_snap_falsification.py`](verify_eisenstein_snap_falsification.py) | Falsification tests for snap-lattice alignment claims |
| [`eisenstein-prime-norms.md`](eisenstein-prime-norms.md) | Analysis of Eisenstein prime norms and their factorization structure |
| [`EISENSTEIN-VS-Z2-BENCHMARK.md`](EISENSTEIN-VS-Z2-BENCHMARK.md) | Benchmark comparing Eisenstein Z[ω] vs Z² lattice properties |

## Usage

```python
from eisenstein_triples import generate_triples, weyl_orbit, norm

# Generate all Eisenstein triples with c ≤ 100
triples = generate_triples(100)

# Compute the full D₆ orbit of a triple
orbit = weyl_orbit(3, 5)
print(f"({3},{5}) has {len(orbit)} distinct D₆ images")

# Compute Eisenstein norm
print(norm(3, 5))  # 19
```

## Connection to Conservation Spectral Analysis

Eisenstein triples connect to the conservation spectral ecosystem through the hexagonal lattice's role as the optimal 2D packing. The D₆ symmetry group governing triple orbits is the same Weyl group that appears in the root-system decompositions underlying conservation spectral signatures. The parametric structure of Eisenstein triples — where norms factorize according to the arithmetic of Z[ω] — parallels how conservation laws decompose physical systems into spectral components along lattice-theoretic lines.

## Provenance

Extracted from the [forgemaster](https://github.com/SuperInstance/forgemaster) `retro-sunset-plato` branch. Developed as part of the Retro Sunset Plato research program.
