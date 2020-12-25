from collections import defaultdict

file = open('input.txt')

entries = list(map(lambda x: int(x.rstrip('\n')), file.readlines()))

print(len(entries))
print(len(set(entries)))

def find_pair_that_sums_to_target(entries, target, excluded_indices=set()):
    # type: (List[int], int, [Set[int]]) -> Optional[Tuple[int, int]]
    
    entry_map = defaultdict(set)
    for idx, entry in enumerate(entries):
        entry_map[entry].add(idx)

    for idx, entry in enumerate(entries):
        if idx in excluded_indices:
            continue

        if target - entry in entry_map:
            indices = entry_map[target - entry]
            if len(indices - {idx} - excluded_indices) > 0:
                return entry, target - entry
    
    return None

a, b = find_pair_that_sums_to_target(entries, 2020)
print(a, b)
print(a * b)


for idx, entry in enumerate(entries):
    maybe_pair = find_pair_that_sums_to_target(entries, 2020 - entry, {idx})
    if maybe_pair:
        a, b = maybe_pair
        print(entry, a, b)
        print(entry * a * b)
