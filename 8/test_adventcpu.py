import pytest
from adventcpu import Instruction
from adventcpu import CPU

nop_test = "nop +0"
acc_test = "acc +1"
jmp_test = "jmp +4"
acc_neg_test = "acc -3"

instr_gen_test_data = [
        ("nop +0", {"opcode":"nop", "op1_sign":"+", "op1":"0"}),
        ("acc +1", {"opcode":"acc", "op1_sign":"+", "op1":"1"}),
        ("jmp +4", {"opcode":"jmp", "op1_sign":"+", "op1":"4"}),
        ("acc +3", {"opcode":"acc", "op1_sign":"+", "op1":"3"}),
        ("jmp -3", {"opcode":"jmp", "op1_sign":"-", "op1":"3"})
        ]

instr_test_data = [
        ("nop +0", {"opcode":Instruction.Opcode["NOP"], "op1":0}),
        ("acc +1", {"opcode":Instruction.Opcode["ACC"], "op1":1}),
        ("jmp +4", {"opcode":Instruction.Opcode["JMP"], "op1":4}),
        ("acc +3", {"opcode":Instruction.Opcode["ACC"], "op1":3}),
        ("jmp -3", {"opcode":Instruction.Opcode["JMP"], "op1":-3})
        ]

day8_pt1_test_file = "pt1_test.txt"

@pytest.fixture
def test_cpu():
    return CPU()

@pytest.mark.parametrize("instr_str,exp_dict", instr_gen_test_data)
def test_instr_gen(instr_str, exp_dict):
    i_dict = Instruction.parse_instruction(instr_str)
    assert i_dict == exp_dict

@pytest.mark.parametrize("instr_str,exp_dict", instr_test_data)
def test_instr(instr_str, exp_dict):
    i = Instruction(instr_str)
    assert i.opcode == exp_dict['opcode']
    assert i.op1 == exp_dict['op1']
    
def test_cpu_init(test_cpu):
    assert test_cpu.get_pc() == 0
    assert test_cpu.get_acc() == 0
    assert test_cpu.get_executed() == []

def test_nop(test_cpu):
    test_cpu.load_prgm_str(nop_test)
    test_cpu.execute_prgm()
    assert test_cpu.get_pc() == 1
    assert test_cpu.get_acc() == 0
    assert test_cpu.get_executed() == [0]

def test_acc(test_cpu):
    test_cpu.load_prgm_str(acc_test)
    test_cpu.execute_prgm()
    assert test_cpu.get_pc() == 1
    assert test_cpu.get_acc() == 1
    assert test_cpu.get_executed() == [0]

def test_acc_neg(test_cpu):
    test_cpu.load_prgm_str(acc_neg_test)
    test_cpu.execute_prgm()
    assert test_cpu.get_pc() == 1
    assert test_cpu.get_acc() == -3
    assert test_cpu.get_executed() == [0]

def test_jmp(test_cpu):
    test_cpu.load_prgm_str(jmp_test)
    test_cpu.execute_prgm()
    assert test_cpu.get_pc() == 4
    assert test_cpu.get_acc() == 0
    assert test_cpu.get_executed() == [0]

def test_day8_pt1(test_cpu):
    test_cpu.load_prgm_file(day8_pt1_test_file)
    test_cpu.execute_prgm()
    assert test_cpu.get_pc() == 1
    assert test_cpu.get_acc() == 5
    assert test_cpu.get_executed() == [0,1,2,6,7,3,4]

