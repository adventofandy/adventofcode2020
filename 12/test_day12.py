import pytest
from day12 import Ship

move_tests = [("N10", Ship(x=0, y=10, direction='E')),
    ("W10", Ship(x=-10, y=0, direction='E')),
    ("S10", Ship(x=0, y=-10, direction='E')),
    ("E10", Ship(x=10, y=0, direction='E')),
    ("F10", Ship(x=10, y=0, direction='E')),
    ("L90", Ship(x=0, y=0, direction='N')),
    ("L180", Ship(x=0, y=0, direction='W')),
    ("L270", Ship(x=0, y=0, direction='S')),
    ("R90", Ship(x=0, y=0, direction='S')),
    ("R180", Ship(x=0, y=0, direction='W')),
    ("R270", Ship(x=0, y=0, direction='N'))]

@pytest.fixture
def test_file_lines():
    with open("test.txt") as f:
        lines = f.read().rstrip('\n').split('\n')
        return lines

@pytest.mark.parametrize("inp,exp_ship", move_tests)
def test_move(inp, exp_ship):
    test_ship = Ship()
    test_ship.move(inp)
    assert test_ship == exp_ship

def test_trip(test_file_lines):
    test_ship = Ship()
    for line in test_file_lines:
        test_ship.move(line)

    assert test_ship.get_man_dist() == 25

