
numbers = [0,14,1,3,7,9]

def find_nth_number(numbers, n):
    first_seen = {num: idx for idx, num in enumerate(numbers)}
    last_seen = {num: idx for idx, num in enumerate(numbers)}

    prev_number = numbers[-1]
    for turn in range(len(numbers), n):
        if first_seen[prev_number] == turn - 1:
            number = 0
        else:
            number = turn - 1 - last_seen[prev_number]
        
        last_seen[prev_number] = turn - 1
        
        if number not in first_seen:
            first_seen[number] = turn
        
        prev_number = number
    
    return prev_number

print(find_nth_number(numbers, 2020))

print(find_nth_number(numbers, 30000000))


