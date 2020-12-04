import sys

# Generator that yields . or # as Tobagan slides down slope
def slide(slope, slope_x, slope_y):
    cur_x = 0
    cur_y = 0
    width = len(slope[0])
    while cur_y < len(slope):
        print(f'{cur_x} {cur_y} {slope[cur_y][cur_x]}')
        yield slope[cur_y][cur_x]
        cur_x = (cur_x+slope_x) % width
        cur_y = cur_y + slope_y

def main(slope_file, start_x, start_y, slope_x, slope_y):
    slope_data = None

    with open(slope_file, "rb") as f:
        slope_data = f.read().splitlines()
        slope_data_str = [l.decode("ascii") for l in slope_data]
        print(slope_data_str)
        assert slope_data_str

    run = [t for t in slide(slope_data_str, slope_x, slope_y)]
    print(run)
    print(f"Trees: {run.count('#')}")

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
