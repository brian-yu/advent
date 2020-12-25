file = open('input.txt')

lines = [line.rstrip('\n') for line in file.readlines()]

def partition(s, lo_char, hi_char, num):
    lo = 0
    hi = num - 1

    for char in s:
        mid = (lo + hi) // 2
        # print(lo, hi, mid)

        if char == lo_char:
            hi = mid
        elif char == hi_char:
            lo = mid
        else:
            raise Exception('invalid char')
    # print(lo, hi, mid)
    return hi

# print(partition("BBFFBBF", "F", "B", 128))

seat_ids = set()
for line in lines:
    row = partition(line[:7], 'F', 'B', 128)
    col = partition(line[7:], 'L', 'R', 8)
    
    seat_id = row * 8 + col
    
    seat_ids.add(seat_id)

print(max(seat_ids))

print({i for i in range(max(seat_ids) + 1)} - seat_ids)
