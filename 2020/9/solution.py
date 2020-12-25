from collections import Counter

file = open('input.txt')

numbers = [int(line.rstrip('\n')) for line in file.readlines()]

def any_pair_sums_to_target(preamble, target):
    for number in preamble:
        if target - number in preamble:
            return True
    return False

def find_invalid_number(numbers, preamble_length=25):
    preamble = Counter(numbers[:preamble_length])

    for i, next_number in enumerate(numbers[preamble_length:], start=preamble_length):
        if not any_pair_sums_to_target(preamble, next_number):
            return next_number
        
        preamble[next_number] += 1

        to_remove = numbers[i - preamble_length]
        preamble[to_remove] -= 1
        if preamble[to_remove] == 0:
            preamble.pop(to_remove)

def contiguous_range_sums_to_target(numbers, start, target):
    for i, num in enumerate(numbers[start:], start=start):
        target -= num
        if target == 0 and i != start:
            return numbers[start:i+1]
        elif target < 0:
            return None
    
    return None

def find_encryption_weakness(numbers, invalid_number):
    for i in range(len(numbers)):
        contiguous_range = contiguous_range_sums_to_target(numbers, i, invalid_number)
        if not contiguous_range:
            continue
        return min(contiguous_range) + max(contiguous_range)
    return None



invalid_number = find_invalid_number(numbers)
print(invalid_number)

print(find_encryption_weakness(numbers, invalid_number))
