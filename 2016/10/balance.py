class Bot:

	def __init__(self, id, rules, system):
		self.id = id
		self.values = []
		self.rules = rules
		self.system = system

	def __str__(self):
		return "Bot {} has values: {} and rules: low to {}, high to {}".format(self.id, self.values, " ".join(self.rules[:2]), " ".join(self.rules[2:]))

	def addValue(self, value): #TODO - ADD rule checking

		self.values.append(value)

		if 17 in self.values and 61 in self.values:
			print(self)

		if len(self.values) == 2:
			self.execute()

	def execute(self):
		lowdest, lowid, highdest, highid = self.rules
		if lowdest == "output":
			self.system.setOutput(lowid, self.popLow())
		else:
			self.system.addToBot(lowid, self.popLow())
		
		if highdest == "output":
			self.system.setOutput(highid, self.popHigh())
		else:
			self.system.addToBot(highid, self.popHigh())

	def popLow(self):
		low = min(self.values)
		self.values.remove(low)
		return low

	def popHigh(self):
		high = max(self.values)
		self.values.remove(high)
		return high

class System:

	def __init__(self, filename):
		file = open(filename)
		self.commands = [line.strip().split() for line in open(filename)]
		self.output = {}
		self.bots = {}

		self.initialize()
		self.run()

	def addToBot(self, botId, value):
		self.bots[botId].addValue(value)

	def setOutput(self, id, value):
		self.output[id] = value

	def initialize(self):
		for command in self.commands:
			if command[0] == "bot":
				botNum = command[1]
				rules = command[5:7] + command[10:]
				self.bots[botNum] = Bot(botNum, rules, self)

	def run(self):
		for command in self.commands:
			if command[0] == "value":
				botNum = command[5]
				bot = self.bots[botNum]
				value = int(command[1])
				bot.addValue(value)


s = System("input.txt")
s.initialize()
s.run()

print(s.output["0"] * s.output["1"] * s.output["2"])

[print("({}: {}) ".format(i, s.output[i]), end="") for i in sorted(s.output.keys())]
print()