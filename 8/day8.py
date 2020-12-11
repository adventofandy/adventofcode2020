import adventcpu
import sys
import re

def flip(data, index):
    instr = data[index:index+3]
    if instr == "jmp":
        pre = data[:index]
        post = data[index+3:]
        ret = pre + "nop" + post
    elif instr == "nop":
        pre = data[:index]
        post = data[index+3:]
        ret = pre + "jmp" + post
    else:
        raise ValueError(f'Bad instruction {instr}')
    return ret

def permute_prgm(data):
    j_n_in = [m.start() for m in re.finditer('(jmp|nop)', data)]
    perms = [flip(data, i) for i in j_n_in]
    return perms

cpu = adventcpu.CPU()

if(sys.argv[2] == '1'):
    cpu.load_prgm_file(sys.argv[1])
    cpu.execute_prgm()
else:
    with open(sys.argv[1]) as f:
        data = f.read()
        perms = permute_prgm(data)
        for p in perms:
            cpu.load_prgm_str(p)
            cpu.execute_prgm()

