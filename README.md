# eisenstein-triples

Eisenstein integer triples with **D₆ symmetry** and hexagonal lattice applications.

## Overview

Eisenstein triples are the hexagonal analog of Pythagorean triples. Where Pythagorean triples satisfy `a² + b² = c²` over the Gaussian integers, Eisenstein triples satisfy the norm equation:

```
a² - ab + b² = c²
```

This is the norm form of the Eisenstein integer ring **Z[ω]** where `ω = e^{2πi/3}`, the ring of integers of the 6th cyclotomic field.

## D₆ Orbit Symmetry

Each primitive Eisenstein triple generates a **12-element orbit** under the D₆ action (6 hexagonal rotations × sign). The `weyl_orbit()` function in `eisenstein_triples.py` computes all elements of this orbit.

## Contents

| File | Description |
|------|-------------|
| [`eisenstein_triples.py`](eisenstein_triples.py) | Core library: norm, orbit, triple generation, primitivity testing |
| [`analyze.py`](analyze.py) | Analysis tools: distribution, symmetry classification, statistics |
| [`verify_proofs.py`](verify_proofs.py) | Automated proof verification for triple properties |
| [`eisenstein-prime-norms.md`](eisenstein-prime-norms.md) | Notes on Eisenstein prime norms |

## Quick Start

```python
from eisenstein_triples import norm, is_eisenstein_triple, weyl_orbit

# Check a triple
assert is_eisenstein_triple(3, 8, 7)  # 9 - 24 + 64 = 49

# Compute full D₆ orbit
orbit = weyl_orbit(3, 8)
print(f"Orbit has {len(orbit)} elements")
```

## Provenance

Extracted from the [forgemaster](https://github.com/SuperInstance/forgemaster) `retro-sunset-plato` branch.
