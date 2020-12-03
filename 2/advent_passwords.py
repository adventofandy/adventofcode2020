import sys
import re

# Second arg denotes which section of the Day 2's challenge we're doing
def is_password_valid(entry, sec):
    def xor(a, b):
        return (a and not b) or (b and not a)
    let = entry["letter"]
    mini = entry["min"]
    maxi = entry["max"]
    password = entry["password"]

    num_let = password.count(let)
    
    if sec == 1:
        return num_let >= mini and num_let <= maxi
    elif sec == 2:
        mini_let = password[mini-1] == let
        maxi_let = password[maxi-1] == let
        return xor(mini_let, maxi_let)
    else:
        raise ValueError("Invalid section number %i" % (sec))

def parse_password_line(line):
    regex = re.compile(
            r'^(?P<min>\d*)-(?P<max>\d*) (?P<letter>\w*): (?P<password>\w*)')
    #print(line)
    match = regex.search(line)
    
    result_dict = match.groupdict()
    result_dict["min"] = int(result_dict["min"])
    result_dict["max"] = int(result_dict["max"])
    #print(result_dict)
    return result_dict

if __name__ == "__main__":
    lines = None
    with open(sys.argv[1], "rb") as f:
        lines = f.readlines()
    
    assert lines

    sec = int(sys.argv[2])

    entries = [parse_password_line(l.decode("ascii")) for l in lines]
    valid_entries = [e for e in entries if is_password_valid(e, sec)]

    print(f"There are {len(valid_entries)} valid entries out of {len(entries)}")
