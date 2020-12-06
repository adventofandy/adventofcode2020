import re
import sys

def separate_passports(data):
    return data.split('\n\n')

def parse_passport(pass_str):
    elements = re.split(' |\n', pass_str)
    elements = list(filter(None, elements))
    print(elements)
    el_tuples = [tuple(e.split(':')) for e in elements]
    pass_dict = dict(el_tuples)
    return pass_dict

def is_hgt_valid(height):
    regex = re.compile(
            r'^(?P<mag>\d*)(?P<meas>(in|cm))$')
    match = regex.search(height)
    if not match:
        print(f'Bad Height: {height}')
        return False

    result_dict = match.groupdict()
    try:
        mag_int = int(result_dict["mag"])
    except ValueError:
        print(f'Bad Height: {height}')
        return False
    
    if result_dict["meas"] == "cm":
        return mag_int >=150 and mag_int <=193
    elif result_dict["meas"] == "in":
        return mag_int >= 59 and mag_int <= 76
    else:
        print(f'Bad Height Unit: {height}')
        return False

def is_hcl_valid(hcl):
    match = re.match('^#[0-9a-f]{6}$',hcl)
    if not match:
        print(f'Bad HCL: {hcl}')
        return False
    else:
        return True

def is_ecl_valid(ecl):
    match = re.match('^(amb|blu|brn|gry|grn|hzl|oth)$',ecl)
    if not match:
        print(f'Bad ecl: {ecl}')
        return False
    else:
        return True

def is_pid_valid(pid):
    match = re.match('^[0-9]{9}$', pid)
    if not match:
        print(f'Bad pid: {pid}')
        return False
    else:
        return True

def is_byr_valid(byr):
    try:
        byr_int = int(byr)
    except ValueError:
        print(f'Bad byr: {byr}')
        return False

    return byr_int >= 1920 and byr_int <=2002

def is_iyr_valid(iyr):
    try:
        iyr_int = int(iyr)
    except ValueError:
        print(f'Bad iyr: {iyr}')
        return False

    return iyr_int >= 2010 and iyr_int <=2020

def is_eyr_valid(eyr):
    try:
        eyr_int = int(eyr)
    except ValueError:
        print(f'Bad eyr: {eyr}')
        return False

    return eyr_int >= 2020 and eyr_int <=2030

def is_valid_passport(pass_dict, pt):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = pass_dict.keys()
    all_fields = all(item in fields for item in req_fields)
    if pt == 1 or all_fields == False:
        return all_fields

    # Part 2
    else:
        return (is_byr_valid(pass_dict["byr"]) and
                is_iyr_valid(pass_dict["iyr"]) and
                is_eyr_valid(pass_dict["eyr"]) and
                is_hgt_valid(pass_dict["hgt"]) and
                is_hcl_valid(pass_dict["hcl"]) and
                is_ecl_valid(pass_dict["ecl"]) and
                is_pid_valid(pass_dict["pid"]))

if __name__ == "__main__":
    file_data = None
    with open(sys.argv[1]) as f:
        file_data = f.read()

    pt = int(sys.argv[2])

    passports = separate_passports(file_data)
    pass_dicts = [parse_passport(p) for p in passports]

    valid = len([p for p in pass_dicts if is_valid_passport(p, pt)])
    print(valid)

