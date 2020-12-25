file = open('input.txt')
adapters = [int(line.rstrip('\n')) for line in file.readlines()]

source = 0
device_adapter = max(adapters) + 3

adapters.extend([source, device_adapter])

sorted_adapters = list(sorted(adapters))

def count_gaps(sorted_arr, gap_size):
    count = 0

    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] - sorted_arr[i - 1] == gap_size:
            count += 1
    
    return count

gaps_of_one = count_gaps(sorted_adapters, 1)
gaps_of_three = count_gaps(sorted_adapters, 3)

print(gaps_of_one * gaps_of_three)

def count_adapter_arrangements(sorted_adapters, i=0, memo={}):
    if i == len(sorted_adapters) - 1:
        return 1
    
    if i in memo:
        return memo[i]
    
    count = 0
    adapter = sorted_adapters[i]
    for j in range(i + 1, len(sorted_adapters)):
        if sorted_adapters[j] - adapter > 3:
            break
        count += count_adapter_arrangements(sorted_adapters, j, memo)
    
    memo[i] = count
    
    return count

print(count_adapter_arrangements(sorted_adapters))
