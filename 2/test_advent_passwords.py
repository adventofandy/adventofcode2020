import pytest
import advent_passwords


TESTFILE = "test_passwords.txt"

@pytest.fixture
def test_passwords():
    lines = None
    with open(TESTFILE) as f:
        lines = f.readlines()
    
    assert lines
    return lines

def test_parse_password_line(test_passwords):
    for p in test_passwords:
        parsed = advent_passwords.parse_password_line(p)

