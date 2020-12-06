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
TESTFILE1 = "test_passports_pt1.txt"
TESTFILE2v = "test_passports_pt2_valid.txt"
TESTFILE2i = "test_passports_pt2_invalid.txt"

NUMPASS1 = 4

test_byr_data = [("2002", True), ("2003", False)]
test_hgt_data = [("60in", True), ("190cm", True),
        ("190in", False), ("190", False)]
test_hcl_data = [("#123abc", True), ("#123abz", False), ("123abc", False)]
test_ecl_data = [("brn", True), ("wat", False)]
test_pid_data = [("000000001", True), ("0123456789", False)]

@pytest.fixture
def test_file():
    lines = None
    with open(TESTFILE1) as f:
        lines = f.read()
    
    assert lines
    return lines

@pytest.fixture
def test_file_pt2_invalid():
    lines = None
    with open(TESTFILE2i) as f:
        lines = f.read()
    
    assert lines
    return lines

@pytest.fixture
def test_file_pt2_valid():
    lines = None
    with open(TESTFILE2v) as f:
        lines = f.read()
    
    assert lines
    return lines

def test_num_passports(test_file):
    passports = passport.separate_passports(test_file)
    assert len(passports) == NUMPASS1

@pytest.mark.parametrize("byr_in, byr_exp", test_byr_data)
def test_byr_valid(byr_in, byr_exp):
    assert passport.is_byr_valid(byr_in) == byr_exp

@pytest.mark.parametrize("hgt_in, hgt_exp", test_hgt_data)
def test_hgt_valid(hgt_in, hgt_exp):
    assert passport.is_hgt_valid(hgt_in) == hgt_exp

@pytest.mark.parametrize("hcl_in, hcl_exp", test_hcl_data)
def test_hcl_valid(hcl_in, hcl_exp):
    assert passport.is_hcl_valid(hcl_in) == hcl_exp

@pytest.mark.parametrize("ecl_in, ecl_exp", test_ecl_data)
def test_ecl_valid(ecl_in, ecl_exp):
    assert passport.is_ecl_valid(ecl_in) == ecl_exp

@pytest.mark.parametrize("pid_in, pid_exp", test_pid_data)
def test_pid_valid(pid_in, pid_exp):
    assert passport.is_pid_valid(pid_in) == pid_exp

@pytest.mark.parametrize("inp,exp",
        [(PASS1, PASSDICT1), (PASS2, PASSDICT2), (PASS3, PASSDICT3),
        (PASS4, PASSDICT4)])
def test_parse_passport_param(inp, exp):
    assert passport.parse_passport(inp) == exp

@pytest.mark.parametrize("inp_valid, exp_valid",
        [(PASSDICT1, True), (PASSDICT2, False), (PASSDICT3, True),
        (PASSDICT4, False)])
def test_valid_passport_pt1(inp_valid, exp_valid):
    assert passport.is_valid_passport(inp_valid, 1) == exp_valid
