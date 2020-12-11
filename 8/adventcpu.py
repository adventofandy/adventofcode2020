from enum import Enum
import re

class Instruction:
    class Opcode(Enum):
        BAD = -1
        NOP = 0
        ACC = 1
        JMP = 2

    opcode = Opcode.BAD
    op1 = 0
    
    def __init__(self, instr_str):
        i_dict = Instruction.parse_instruction(instr_str)
        if not i_dict:
            return
        else:
            self.opcode = Instruction.Opcode[i_dict['opcode'].upper()]
            self.op1 = int(i_dict['op1'])
            if i_dict['op1_sign'] == '-':
                self.op1 *= -1
    
    def get_opcode(self):
        return self.opcode
    
    def get_op1(self):
        return self.op1

    def parse_instruction(instr_str):
        required_elems = ["opcode", "op1_sign", "op1"]
        regex = re.compile(
            r'^(?P<opcode>.*) (?P<op1_sign>(-|\+))(?P<op1>\d*)$')
        instr_dict = regex.search(instr_str).groupdict()
        
        keys = instr_dict.keys()
        if not all(x in keys for x in required_elems):
            print(f'Instruction {i_dict} did not contain required elements {required_elems}')
            return None

        return instr_dict

    def __repr__(self):
        return f'{self.opcode.name} {self.op1}'

class CPU:
    program = []
    pc = 0
    acc = 0
    executed = []

    def __init__(self):
        return

    def get_pc(self):
        return self.pc

    def get_acc(self):
        return self.acc

    def get_executed(self):
        return self.executed

    def clear_state(self):
        self.pc = 0
        self.acc = 0
        self.executed = []
        self.program = []

    def load_prgm_file(self,file_name):
        with open(file_name) as f:
            data = f.read()
            return self.load_prgm_str(data)
        return False

    def load_prgm_str(self, prgm_str):
        self.clear_state()

        lines = prgm_str.rstrip('\n').split('\n')
        self.program = [Instruction(l) for l in lines]
        bad_instr = [self.program.index(i) for i in self.program if i.get_opcode() == 
                Instruction.Opcode.BAD]
        if bad_instr:
            print(f'Bad Instructions at {bad_instr}')
            print(f'Program:\n{program}')
            return False

        return True

    def execute_prgm(self):
        if not self.program:
            print(f'ERROR: Program not initialized')
            return -1

        while(self.pc not in self.executed and self.pc < len(self.program)):
            self.executed.append(self.pc)
            self.execute_instr(self.program[self.pc])
        
        print(f'***Program Halted***')
        if(self.pc >= len(self.program)):
            print("Reached end of prgm")
        else:
            print("Infinite loop")
        print(f'PC:\t\t{self.pc}')
        print(f'ACC:\t\t{self.acc}')
        #print(f'Instrs:\t\t{self.executed}')
        #print(f'Program:\n{self.program}')
        return 0

    def execute_instr(self, instr):
        op = instr.get_opcode()
        if op == Instruction.Opcode.NOP:
            self.pc += 1
        elif op == Instruction.Opcode.ACC:
            self.pc += 1
            self.acc += instr.get_op1()
        elif op == Instruction.Opcode.JMP:
            self.pc += instr.get_op1()
        else:
            raise ValueError(f'Tried to execute unknown opcode {op} at {self.pc}')


        


            


