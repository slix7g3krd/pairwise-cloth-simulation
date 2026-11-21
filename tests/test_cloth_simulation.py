import pytest
import math
from render import cloth_simulation as mod

CASES = [
    ("sub", 'm.substeps(0.05, 0.01) == 5'),
    ("iter", 'm.constraint_iterations(0.2, 4) == 6'),
    ("wind", 'm.wind_scale(2, 3) == 6'),
    ("hash", 'm.hash_cell((1.2, 2.3), 1) == (1, 2)'),
    ("pin", 'm.pinned_target((0, 0), (1, 2)) == (1, 2)'),
    ("fric", 'm.friction(5, 2) == 3'),
    ("lod", "m.lod_state(2, 'run') == (2, 'run')"),
    ("read", 'm.readback_interp(0, 10, 0.5) == approx(5.0)'),
    ("pause", 'm.pause_wind(3, True) == 0'),
    ("stretch", 'm.stretch_ratio(2, 1) == approx(2.0)'),
    ("integ", 'm.integrate((0, 0), (1, 1), 2) == (2, 2)'),
    ("damp", 'm.damping(10, 0.2) == approx(8.0)'),
    ("ctime", 'm.collision_time(0.5, 0.2) == approx(0.7)'),
    ("rest", 'm.rest_length(2, 3) == 6'),
    ("id", 'm.cloth_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
