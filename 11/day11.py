import sys
import copy

def can_see_occ_in_dir(grid, x, y, dx, dy):
    count = 1
    
    while(x+(dx*count) in range(len(grid[y])) 
            and y+(dy*count) in range(len(grid))):
        next_loc = grid[y+(dy*count)][x+(dx*count)]
        if next_loc == '#':
            return '#'
        elif next_loc == 'L':
            return 'L'
        else:
            count+=1

    return '.'

def get_adjacent_seats(grid, x, y, tol):
    adj = []
    if tol == 4:
        adj = [grid[y+dy][x+dx] 
                for dx in range(-1, 2) 
                for dy in range(-1, 2) 
                if (dx != 0 or dy != 0) and
                x+dx in range(len(grid[y])) and
                y+dy in range(len(grid))]
    
    elif tol == 5:
        adj = [can_see_occ_in_dir(grid, x, y, dx, dy)
                for dx in range(-1, 2) 
                for dy in range(-1, 2) 
                if (dx != 0 or dy != 0) and
                x+dx in range(len(grid[y])) and
                y+dy in range(len(grid))]
    return adj
    
def get_new_seat_status(grid, x, y, tol):
    if grid[y][x] == '.':
        return '.'
    else:
        adj = get_adjacent_seats(grid, x, y, tol)
        if grid[y][x] == 'L' and '#' not in adj:
            return '#'
        elif grid[y][x] == '#' and adj.count('#') >= tol:
            return 'L'
        else:
            return grid[y][x]

def shuffle_seats(grid, part):
    if part == '1':
        tol = 4
    else:
        tol = 5

    last_grid = []
    new_grid = grid

    while(new_grid != last_grid):
        last_grid = copy.deepcopy(new_grid)
        for y in range(len(last_grid)):
            for x in range(len(last_grid[0])):
                new_grid[y][x] = get_new_seat_status(last_grid, x, y, tol)
        #print(new_grid)
    return new_grid

if __name__ == "__main__":
    filename = sys.argv[1]
    part = sys.argv[2]

    with open(filename) as f:
        data = f.read()
        lines = data.rstrip('\n').split('\n')
        grid = [list(l) for l in lines]

    final_grid = shuffle_seats(grid, sys.argv[2])
    print('\n'.join([''.join(l) for l in final_grid]))
    occupied = sum([l.count('#') for l in final_grid])
    print(f'Occupied: {occupied}')

