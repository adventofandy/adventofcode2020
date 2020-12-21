import sys
class Ship:
    cardinals = ['N', 'E', 'S', 'W']
    x = 0
    y = 0
    direction = 'E'

    def __init__(self, x=0, y=0, direction='E'):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        if(other.x == self.x and
                other.y == self.y and
                other.direction == self.direction
                ):
            return True
        else:
            return False

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
            if in_dir == 'L':
                in_num = 360-in_num

            in_ticks = int(in_num/90)
            self.direction = self.cardinals[
                    (self.cardinals.index(self.direction)+in_ticks) % len(self.cardinals)
                ]
        else:
            raise ValueError(f'Bad direction {in_dir} from {inp})')

    def get_man_dist(self):
        return abs(self.x) + abs(self.y)
    
    def __repr__(self):
        return f'X: {self.x} Y: {self.y} Direction: {self.direction}'

if __name__ == "__main__":
    filename = sys.argv[1]
    part = int(sys.argv[2])

    with open(filename) as f:
        data = f.read()
        lines = data.rstrip('\n').split('\n')
    
    ship = Ship()
    for l in lines:
        ship.move(l)
    
    print(ship)
    print(f'Manhatten Distance:{ship.get_man_dist()}')

