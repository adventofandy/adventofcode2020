import sys

filename = sys.argv[1]
part = int(sys.argv[2])

if part == 1:
    with open(filename) as f:
        data = f.read()
        joltage_list = [int(i) for i in data.rstrip('\n').split('\n')]

    joltage_list.append(0)
    joltage_list.append(max(joltage_list) + 3)
    joltage_list.sort()
    print(joltage_list)
    diffs = [joltage_list[a] - joltage_list[a-1] for a in range(1, len(joltage_list))]
    print(f'1: {diffs.count(1)}\t3: {diffs.count(3)}')

if part == 2:
    with open(filename) as f:
        data = f.read()
        joltage_list = [int(i) for i in data.rstrip('\n').split('\n')]
        joltage_list.append(0)
        joltage_list.append(max(joltage_list) + 3)

    joltage_list.sort()

    a = 1 if 1 in joltage_list else 0
    b = a + 1 if 2 in joltage_list else 0
    c = a + b + 1 if 3 in joltage_list else 0
    for i in range(4, max(joltage_list) + 1):
        a, b, c = b, c, a + b + c if i in joltage_list else 0
    print(c)


