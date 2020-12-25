import re

file = open('input.txt')
program = [line.rstrip('\n') for line in file.readlines()]

def get_mask_fn(mask):
    zeros_mask = 0
    ones_mask = 0

    for i, digit in enumerate(reversed(mask)):
        if digit == 'X':
            zeros_mask += 2**i
        elif digit == '0':
            pass
        elif digit == '1':
            ones_mask += 2**i
            zeros_mask += 2**i
    
    return lambda x: x & zeros_mask | ones_mask

def parse_program(program):
    memory = {}
    mask_fn = lambda x: Exception('no mask fn')
    for line in program:
        if line.startswith('mask'):
            match = re.match(r'mask = ([X01]+)', line)
            mask_fn = get_mask_fn(match.group(1))
        elif line.startswith('mem'):
            match = re.match(r'mem\[(\d+)\] = (\d+)', line)
            address = int(match.group(1))
            value = int(match.group(2))

            memory[address] = mask_fn(value)
    
    print(sum(memory.values()))

parse_program(program)

def get_addresses(mask, address):
    addresses = [0]
    reversed_mask = reversed(mask)
    for i, mask_digit in enumerate(reversed_mask):
        if mask_digit == '0':
            for j in range(len(addresses)):
                addresses[j] += (address & 1) * 2**i
        elif mask_digit == '1':
            for j in range(len(addresses)):
                addresses[j] += 2**i
        elif mask_digit == 'X':
            new_addresses = []
            for j in range(len(addresses)):
                new_addresses.append(addresses[j] + 2**i)
            addresses.extend(new_addresses)
        address >>= 1
    
    return addresses

def parse_program_v2(program):
    memory = {}
    mask = None
    for line in program:
        if line.startswith('mask'):
            match = re.match(r'mask = ([X01]+)', line)
            mask = match.group(1)
        elif line.startswith('mem'):
            match = re.match(r'mem\[(\d+)\] = (\d+)', line)
            address = int(match.group(1))
            value = int(match.group(2))

            addresses = get_addresses(mask, address)
            for address in addresses:
                memory[address] = value
    
    print(sum(memory.values()))

parse_program_v2(program)