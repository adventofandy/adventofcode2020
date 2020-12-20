import sys
class Ship:
    cardinals = {'N', 'E', 'S', 'W'}
    x = 0
    y = 0
    direction = 'E'

    def __init__(self):
        x = 0
        y = 0
        direction = 'E'

    def move(self, inp):
        in_dir = inp[:1]
        in_num = int(inp[1:])

        if in_dir in {'F','N','S','E','W'}:
            if in_dir == 'F':
                m_dir = self.direction
            else:
                m_dir = in_dir

            if m_dir == 'N':
                self.y += in_num
            elif m_dir == 'E':
                self.x += in_num
            elif m_dir == 'S':
                self.y -= in_num
            elif m_dir == 'W':
                self.x -= in_num
            else:
                raise ValueError
        elif in_dir in {'L', 'R'}:
            
        else:
            raise ValueError(f'Bad direction {in_dir} from {inp})



if __name__ == "__main__":
    filename = sys.argv[1]
    part = int(sys.argv[2])

    with open(filename) as f:
        data = f.read()
        lines = data.rstrip('\n').split('\n')
        

