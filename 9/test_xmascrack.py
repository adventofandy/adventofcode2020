import pytest
from xmascrack import XmasCrack

pt1_test_file = "pt1_test.txt"
pt1_test_pre = 5
pt1_test_list = [
        35, 20, 15, 25, 47,
        40, 62, 55, 65, 95,
        102, 117, 150, 182,
        127, 219, 299, 277,
        309, 576
        ]

@pytest.fixture
def test_pt1_fix():
    cracker = XmasCrack(pt1_test_pre)
    cracker.load_message_file(pt1_test_file)
    return cracker

def test_load_message(test_pt1_fix):
    cracker = test_pt1_fix
    assert cracker.message_list == pt1_test_list

def test_find_invalid(test_pt1_fix):
    cracker = test_pt1_fix
    inv = cracker.find_invalid()
    assert inv == 127

def test_find_weakness(test_pt1_fix):
    cracker = test_pt1_fix
    weakness = cracker.find_weakness(127)
    assert weakness == 62
