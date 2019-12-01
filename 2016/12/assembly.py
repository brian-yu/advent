



class Assembly:

	def __init__(self, filename):
		f = open(filename)

		self.instructions = [line.strip().split() for line in f]

		#print(self.instructions)

		self.registers = {"a": 0, "b": 0, "c": 1, "d": 0}

	def execute(self):
		print(self.registers)
		i = 0

		while i < len(self.instructions):

			instruction = self.instructions[i]
			print(i)
			print(instruction)
			cmd = instruction[0]
			if cmd == "cpy":
				if instruction[1] in self.registers:
					self.registers[instruction[2]] = self.registers[instruction[1]]
				else:
					self.registers[instruction[2]] = int(instruction[1])
			if cmd == "inc":
				self.registers[instruction[1]] += 1
			if cmd == "dec":
				self.registers[instruction[1]] -= 1
			if cmd == "jnz":
				arg1 = self.registers[instruction[1]] if instruction[1] in self.registers else int(instruction[1])
				if arg != 0:
					i += int(instruction[2])
				else:
					i += 1
			else:
				i += 1
			# if i > len(self.instructions)-1:
			# 	break
			print(self.registers)

		print(self.registers)



a = Assembly("input.txt")
a.execute()