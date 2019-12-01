

def conditionMet(registers, arr):
	if arr[0] not in registers:
		registers[arr[0]] = 0
	condReg = registers[arr[0]]
	op = arr[1]
	value = int(arr[2])

	if op == ">":
		return condReg > value
	elif op == "<":
		return condReg < value
	elif op == "==":
		return condReg == value
	elif op == "<=":
		return condReg <= value
	elif op == ">=":
		return condReg >= value
	elif op == "!=":
		return condReg != value


file = open("input.txt")

lines = [line.strip().split() for line in file]

registers = {}

maxEnc = float("-inf")

for line in lines:
	reg = line[0]
	condReg = line[4]

	if reg not in registers:
		registers[reg] = 0
	
	if conditionMet(registers, line[4:]):
		if line[1] == "inc":
			registers[reg] += int(line[2])
		else:
			registers[reg] -= int(line[2])
		if registers[reg] > maxEnc:
				maxEnc = registers[reg]

print(registers)

print(max([registers[i] for i in registers]))
print(maxEnc)