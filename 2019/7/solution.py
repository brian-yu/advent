




def run(program):
    opcode_params = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}

    pc = 0
    while pc < len(program):
        instr = str(program[pc])
        opcode = int("".join(instr[-2:]))
        parameter_modes = instr[:-2][::-1]

        params = []
        for i in range(opcode_params[opcode]):
            val = program[pc + i + 1]
            if i < len(parameter_modes) and parameter_modes[i] == "1":
                params.append(val)
            else:
                params.append(program[val])
        
        if opcode == 99:
            break
        elif opcode == 1:
            program[program[pc + 3]] = params[0] + params[1]
        elif opcode == 2:
            program[program[pc + 3]] = params[0] * params[1]
        elif opcode == 3:
            int_input = int(input("Input: "))
            program[program[pc + 1]] = int_input
        elif opcode == 4:
            print(params[0])
        elif opcode == 5:
            if params[0] != 0:
                pc = params[1]
                continue
        elif opcode == 6:
            if params[0] == 0:
                pc = params[1]
                continue
        elif opcode == 7:
            if params[0] < params[1]:
                program[program[pc + 3]] = 1
            else:
                program[program[pc + 3]] = 0
        elif opcode == 8:
            if params[0] == params[1]:
                program[program[pc + 3]] = 1
            else:
                program[program[pc + 3]] = 0
        else:
            print("Oops!")
        pc += opcode_params[opcode] + 1
    return program[0]

program = [int(line.rstrip('\n')) for line in open('input.txt').read().split(',')]

print(run(program))
