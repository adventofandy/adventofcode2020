import pytest
import toboggan


TESTFILE = "test_slope.txt"
SLOPE_X = 3
SLOPE_Y = 1

good_run = ['.','.','#','.','#','#','.','#','#','#','#']

@pytest.fixture
def test_slope():
    lines = None
    with open(TESTFILE) as f:
        lines = f.read().splitlines()
    
    assert lines
    return lines

def test_slide(test_slope):
    toboggan_run = [t for t in toboggan.slide(test_slope, SLOPE_X, SLOPE_Y)]
    assert toboggan_run == good_run
