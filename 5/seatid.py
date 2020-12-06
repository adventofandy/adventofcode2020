import sys

def get_seatid(seat):
    row = seat[:7].replace('F', '0').replace('B', '1')
    column = seat[7:].replace('L', '0').replace('R', '1')

    seatid = int(row, 2)*8 + int(column, 2)
    return seatid

if __name__ == "__main__":
    seat = sys.argv[1]

    with open(sys.argv[1]) as f:
        seat_lines = f.readlines()
        seats = [l.rstrip('\n') for l in seat_lines]
        assert seats

    seatids = [get_seatid(s) for s in seats]

    print(f'Max SeatID: {max(seatids)}')

    your_seat = [s+1 for s in seatids if s+2 in seatids and not s+1 in seatids]
    print(your_seat)
