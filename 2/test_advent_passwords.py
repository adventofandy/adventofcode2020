import pytest
import advent_passwords


TESTFILE = "test_passwords.txt"

good_parse_0 = {'min': 1, 'max': 3, 'letter': 'a', 'password': 'abcde'}
good_parse_1 = {'min': 1, 'max': 3, 'letter': 'b', 'password': 'cdefg'}
good_parse_2 = {'min': 2, 'max': 9, 'letter': 'c', 'password': 'ccccccccc'}

@pytest.fixture
def test_passwords():
    lines = None
    with open(TESTFILE) as f:
        lines = f.readlines()
    
    assert lines
    return lines

def test_parse_password_line_0(test_passwords):
    p = test_passwords[0]
    parsed = advent_passwords.parse_password_line(p)
    assert parsed == good_parse_0 

def test_parse_password_line_1(test_passwords):
    p = test_passwords[1]
    parsed = advent_passwords.parse_password_line(p)
    assert parsed == good_parse_1

def test_parse_password_line_2(test_passwords):
    p = test_passwords[2]
    parsed = advent_passwords.parse_password_line(p)
    assert parsed == good_parse_2

def test_is_password_valid_0():
    assert advent_passwords.is_password_valid(good_parse_0, 1)
    assert advent_passwords.is_password_valid(good_parse_0, 2)

def test_is_password_valid_1():
    assert not advent_passwords.is_password_valid(good_parse_1, 1)
    assert not advent_passwords.is_password_valid(good_parse_1, 2)

def test_is_password_valid_2():
    assert advent_passwords.is_password_valid(good_parse_2, 1)
    assert not advent_passwords.is_password_valid(good_parse_2, 2)
