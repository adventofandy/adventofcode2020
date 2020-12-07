import sys

def dec_intersections(l):
    sets = [set(e) for e in l]
    intersection = set.intersection(*sets)
    return len(intersection)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        dec_groups = f.read().split('\n\n')
        decs = [set(list(d.replace('\n', ''))) for d in dec_groups]
        dec_nums = [len(s) for s in decs]
        dec_sum = sum(dec_nums)
        print(f'Part1: {dec_sum}')

        dec_group_lists = [g.rstrip('\n').split('\n') for g in dec_groups]
        dec_group_intersections = [dec_intersections(l) for l in dec_group_lists]
        dec_int_sum = sum(dec_group_intersections)
        print(f'Part2: {dec_int_sum}')
        
