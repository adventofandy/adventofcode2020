import pytest
import passport

PASS1 = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm'
PASSDICT1 = {'ecl':'gry', 'pid':'860033327', 'eyr':'2020', 'hcl':'#fffffd', 'byr':'1937', 'iyr':'2017', 'cid':'147', 'hgt':'183cm'}
PASS2 = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929'
PASSDICT2 = {'iyr':'2013', 'ecl':'amb', 'cid':'350', 'eyr':'2023', 'pid':'028048884', 'hcl':'#cfa07d', 'byr':'1929'}
PASS3 = 'hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm'
PASSDICT3 = {'hcl':'#ae17e1', 'iyr':'2013', 'eyr':'2024', 'ecl':'brn', 'pid':'760753108', 'byr':'1931', 'hgt':'179cm'}
PASS4 = 'hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in\n'
PASSDICT4 = {'hcl':'#cfa07d', 'eyr':'2025', 'pid':'166559648','iyr':'2011', 'ecl':'brn', 'hgt':'59in'}
TESTFILE = "test_passports.txt"
NUMPASS = 4

@pytest.fixture
def test_file():
    lines = None
    with open(TESTFILE) as f:
        lines = f.read()
    
    assert lines
    return lines

def test_num_passports(test_file):
    passports = passport.separate_passports(test_file)
    assert len(passports) == NUMPASS

def test_parse_passport1():
    assert passport.parse_passport(PASS1) == PASSDICT1

def test_parse_passport2():
    assert passport.parse_passport(PASS2) == PASSDICT2

def test_parse_passport3():
    assert passport.parse_passport(PASS3) == PASSDICT3

def test_parse_passport4():
    assert passport.parse_passport(PASS4) == PASSDICT4

def test_valid_passport1():
    assert passport.is_valid_passport(PASSDICT1)

def test_valid_passport2():
    assert not passport.is_valid_passport(PASSDICT2)

def test_valid_passport3():
    assert passport.is_valid_passport(PASSDICT3)

def test_valid_passport4():
    assert not passport.is_valid_passport(PASSDICT4)