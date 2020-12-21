import pytest
from day12pt2 import Ship

move_tests = [("N10", Ship(x=0, y=0, wpx=10, wpy=11)),
    ("W10", Ship(x=0, y=0, wpx=0, wpy=1)),
    ("S10", Ship(x=0, y=0, wpx=10, wpy=-9)),
    ("E10", Ship(x=0, y=0, wpx=20, wpy=1)),
    ("F10", Ship(x=100, y=10, wpx=10, wpy=1)),
    ("L90", Ship(x=0, y=0, wpx=-1, wpy=10)),
    ("L180", Ship(x=0, y=0, wpx=-1, wpy=-10)),
    ("L270", Ship(x=0, y=0, wpx=1, wpy=-10)),
    ("R90", Ship(x=0, y=0, wpx=1, wpy=-10)),
    ("R180", Ship(x=0, y=0, wpx=-1, wpy=-10)),
    ("R270", Ship(x=0, y=0, wpx=-1, wpy=10))]

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

    assert test_ship.get_man_dist() == 286

