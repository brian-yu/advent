class Keypad:

	keypad = [["1", "2", "3"],
			  ["4", "5", "6"],
			  ["7", "8", "9"]]

	keypad = [["0", "0", "1", "0", "0"],
			  ["0", "2", "3", "4", "0"],
			  ["5", "6", "7", "8", "9"],
			  ["0", "A", "B", "C", "0"],
			  ["0", "0", "D", "0", "0"]]

	def __init__(self):
		self.r = 1
		self.c = 1
		self.code = ""

	def processFile(self, file):
		for line in file:
			self.code += self.processLine(line)

	def processLine(self, line):
		for s in line:
			if s == "U":
				self.changeRow(-1)
			elif s == "R":
				self.changeCol(1)
			elif s == "L":
				self.changeCol(-1)
			elif s == "D":
				self.changeRow(1)
		return self.keypad[self.r][self.c]

	def changeRow(self, n):
		if self.r + n < len(self.keypad) and self.r + n >= 0:
			if self.keypad[self.r + n][self.c] != "0":
				self.r += n

	def changeCol(self, n):
		if self.c + n < len(self.keypad[0]) and self.c + n >= 0:
			if self.keypad[self.r][self.c + n] != "0":
				self.c += n


f = open("input.txt")

keypad = Keypad()

keypad.processFile(f)

print(keypad.code)
