import sys

def find_by_sum(entries, goal_nums, goal_sum):
    # Base Case
    if goal_nums == 1:
        try:
            l = [entries.index(goal_sum)]
            return l
        except ValueError:
            return None

    for i in range(0, len(entries)):
        entry = entries[i]

        inds = find_by_sum(entries, goal_nums - 1, goal_sum - entry)
        
        # No sum found or duplicate in sum
        if (not inds) or (i in inds):
            continue
        
        # Sum found
        else:
            return inds + [i]

    return None

def calculate_product(entries, indexes):
    product = 1
    for i in indexes:
        product *= entries[i]

    return product

if __name__ == "__main__":
    input_file = sys.argv[1]

    entries = None
    with open(input_file, "rb") as f:
        byte_entries = f.readlines()
        entries = [int(e) for e in byte_entries]

    assert entries
    print(f'Read {len(entries)} entries')
    
    print(f'=== Part 1 ===')
    entry_indexes = find_by_sum(entries, 2, 2020)
    print(f'Matching Entries:')
    print(f'{int(entries[entry_indexes[0]])} ({entry_indexes[0]})')
    print(f'{int(entries[entry_indexes[1]])} ({entry_indexes[1]})')

    product = calculate_product(entries, entry_indexes)
    print(f'Product: {product}')
    
    print(f'=== Part 2 ===')
    entry_indexes = find_by_sum(entries, 3, 2020)
    print(f'Matching Entries:')
    print(f'{int(entries[entry_indexes[0]])} ({entry_indexes[0]})')
    print(f'{int(entries[entry_indexes[1]])} ({entry_indexes[1]})')

    product = calculate_product(entries, entry_indexes)
    print(f'Product: {product}')

