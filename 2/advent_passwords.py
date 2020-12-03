import sys
import re

def parse_password_line(line):
    regex = re.compile(
            r'^(?P<min>\d*)-(?P<max>\d*) (?P<letter>\w*): (?P<password>\w*)')
    print(line)
    match = regex.search(line)
    
    result_dict = match.groupdict()
    result_dict["min"] = int(result_dict["min"])
    result_dict["max"] = int(result_dict["max"])
    print(result_dict)
    return result_dict

if __name__ == "__main__":
    lines = None
    with open(sys.argv[1], "rb") as f:
        lines = f.readlines()
    
    assert lines
