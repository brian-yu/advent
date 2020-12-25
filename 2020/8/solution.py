import re

file = open('input.txt')
instructions = [line.rstrip('\n') for line in file.readlines()]

def parse(instruction):
    match = re.match(r'([a-z]+) ([\-+]\d+)', instruction)

    return match.group(1), int(match.group(2))

def execute_boot_code(instructions):
    executed_instructions = set()
    idx = 0
    accumulator = 0
    while idx < len(instructions):
        if idx in executed_instructions:
            return accumulator, False

        instruction = instructions[idx]
        op, argument = parse(instruction)

        executed_instructions.add(idx)

        if op == 'jmp':
            idx += argument
        elif op == 'acc':
            accumulator += argument
            idx += 1
        elif op == 'nop':
            idx += 1
        else:
            raise Exception('invalid operation')
    
    return accumulator, True

print(execute_boot_code(instructions))

swap_map = {
    'jmp': 'nop',
    'nop': 'jmp',
    'acc': 'acc',
}

for i in range(len(instructions)):
    instruction = instructions[i]
    op, _ = parse(instruction)

    instructions[i] = swap_map[op] + instruction[3:]
    
    accumulator_val, uncorrupted = execute_boot_code(instructions)
    if uncorrupted:
        print(accumulator_val)
    
    instructions[i] = instruction