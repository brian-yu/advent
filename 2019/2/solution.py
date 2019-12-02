




def run(program, noun, verb):
    program[1] = noun
    program[2] = verb

    pc = 0
    while pc < len(program):
        opcode = program[pc]
        if opcode == 99:
            break
        elif opcode == 1:
            program[program[pc + 3]] = program[program[pc + 1]] + program[program[pc + 2]]
        elif opcode == 2:
            program[program[pc + 3]] = program[program[pc + 1]] * program[program[pc + 2]]
        else:
            print("Oops!")
        pc += 4
    return program[0]


def search(program, target):
    for noun in range(100):
        for verb in range(100):
            output = run(program.copy(), noun, verb)
            
            if output == target:
                return 100 * noun + verb

program = [int(line.rstrip('\n')) for line in open('input.txt').read().split(',')]


print(run(program.copy(), 12, 2))

print(search(program, 19690720))
