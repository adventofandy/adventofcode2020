import sys
class Ship:
    class Waypoint:
        def __init__(self, x=10, y=1):
            self.x = x
            self.y = y
    # class Waypoint

    def __init__(self, x=0, y=0, wpx=10, wpy=1):
        self.x = x
        self.y = y
        self.wp = Ship.Waypoint(x=wpx, y=wpy)

    def __eq__(self, other):
        if(other.x == self.x and
                other.y == self.y and
                other.wp.x == self.wp.x and
                other.wp.y == self.wp.y
                ):
            return True
        else:
            return False

    def move(self, inp):
        in_dir = inp[:1]
        in_num = int(inp[1:])

        if in_dir == 'F':
            self.x += self.wp.x*in_num
            self.y += self.wp.y*in_num

        elif in_dir in {'N','S','E','W'}:
            if in_dir == 'N':
                self.wp.y += in_num
            elif in_dir == 'E':
                self.wp.x += in_num
            elif in_dir == 'S':
                self.wp.y -= in_num
            elif in_dir == 'W':
                self.wp.x -= in_num
            else:
                raise ValueError
        
        elif in_dir in {'L', 'R'}:
            print(f'{in_dir} {in_num}')
            # Normalize to mod 360 degrees
            in_num = in_num % 360 

            # Normalize to clock-wise direction
            if in_dir == 'L':
                in_num = 360-in_num
            
            print(in_num)
            if in_num == 90:
                temp_x = self.wp.x
                self.wp.x = self.wp.y
                self.wp.y = -temp_x
            elif in_num == 180:
                self.wp.x = -self.wp.x
                self.wp.y = -self.wp.y
            elif in_num == 270:
                temp_x = self.wp.x
                self.wp.x = -self.wp.y
                self.wp.y = temp_x
            elif in_num == 0:
                print('Passing 0/360 degree rotation')
                pass
            else:
                raise ValueError(f'Bad degree {in_num} from {inp}')
        else:
            raise ValueError(f'Bad direction {in_dir} from {inp})')

    def get_man_dist(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return f'X: {self.x} Y: {self.y} WPX: {self.wp.x} WPY: {self.wp.y}'

if __name__ == "__main__":
    filename = sys.argv[1]
    part = int(sys.argv[2])

    with open(filename) as f:
        data = f.read()
        lines = data.rstrip('\n').split('\n')
    
    ship = Ship()
    for l in lines:
        ship.move(l)
        print(l)
        print(ship)

    print(ship)
    print(f'Manhatten Distance: {ship.get_man_dist()}')

