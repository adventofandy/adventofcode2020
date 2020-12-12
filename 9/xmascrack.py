from itertools import combinations

class XmasCrack:
    preamble_size = 0
    message_list = []

    def __init__(self, preamble):
        self.preamble_size = preamble

    def load_message_str(self, string):
        self.message_list = [int(s) for s in string.rstrip('\n').split('\n')]

    def load_message_file(self, fil):
        with open(fil) as f:
            data = f.read()
            self.load_message_str(data)
    
    def is_num_valid(self, pos):
        if pos < self.preamble_size:
            raise ValueError(f'Invalid position {pos} (less than preamble {self.preamble_size})')

        preamble = self.message_list[pos-self.preamble_size:pos]
        cur_num = self.message_list[pos]
        pairs = combinations(preamble, 2)
        sums = [a + b for a,b in [tuple(l) for l in pairs]]
        return cur_num in sums

    def find_invalid(self):
        for pos in range(self.preamble_size, len(self.message_list)):
            if not self.is_num_valid(pos):
                return self.message_list[pos]

    def find_weakness(self, target):
        for s in range(len(self.message_list)):
            for e in range(s+1, len(self.message_list)):
                window = self.message_list[s:e+1]
                summ = sum(window)
                if summ == target:
                    return min(window) + max(window)
                elif summ > target:
                    break

        return None
