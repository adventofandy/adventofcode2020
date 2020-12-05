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

def invalid_height(height):
    if len(height) < 2:
        return False

    if height[:-2] == '' or height[-2:] == '':
        return False
    mag = int(height[:-2])
    meas = height[-2:]

    if meas == 'cm':
        return mag < 150 or mag > 193
    elif meas == 'in':
        return mag < 59 or mag > 76
    else:
        return False

def invalid_hair_color(hcl):
    return not re.match('#[0-9a-f]{6}$',hcl)

def invalid_eye_color(ecl):
    return not re.match('amb|blu|brn|gry|grn|hzl|oth',ecl)

def invalid_pid(pid):
    return not re.match('[0-9]{9}', pid)

def is_valid_passport(pass_dict):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    fields = pass_dict.keys()
    all_fields = all(item in fields for item in req_fields)
    
    return all_fields

if __name__ == "__main__":
    file_data = None
    with open(sys.argv[1]) as f:
        file_data = f.read()

    passports = separate_passports(file_data)
    pass_dicts = [parse_passport(p) for p in passports]

    valid = len([p for p in pass_dicts if is_valid_passport(p)])
    print(valid)

