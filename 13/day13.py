import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    part = int(sys.argv[2])

    with open(filename) as f:
        lines = f.read().rstrip('\n').split('\n')
    
    if part == 1:
        tgt_time = int(lines[0])
        busses_raw = lines[1].split(',')
        busses = [int(i) for i in busses_raw if i != 'x']
        print(busses)
        mods = {b-((tgt_time+b) % b):b for b in busses}
        print(mods)

        min_time = min(mods.keys())
        print(min_time)
        print(mods[min_time])

        print(f'Part 1: {min_time*mods[min_time]}')

