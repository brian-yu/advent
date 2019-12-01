class Program:

	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
		self.parent = None

	def setParent(self, parent):
		self.parent = parent

	def __str__(self):
		return "{} ({}){}".format(self.name, self.weight, "-> {}".format([child.name for child in self.children]) if self.children else "")

	def subSum(self):
		if not self.children:
			return self.weight
		return self.weight + sum(child.subSum() for child in self.children)

	def childrenBalanced(self):
		sums = [child.subSum() for child in self.children]
		mode = max(sums, key=sums.count)
		return False not in [child.subSum() == mode for child in self.children]

	def findImbalance(self):
		if self.children:
			sums = [child.subSum() for child in self.children]
			mode = max(sums, key=sums.count)
			for child in self.children:
				if child.subSum() != mode:
					if child.childrenBalanced():
						print(mode - child.subSum() + child.weight)
					else:
						child.findImbalance()
	__repr__ = __str__



class Tower:
	def __init__(self, filename):
		lines = [line.strip().split() for line in open(filename)]
		self.programs = {}
		for line in lines:
			self.programs[line[0]] = Program(line[0], int(line[1].strip("(").strip(")")), [child.strip(",") for child in line[3:]])
		for name in self.programs:
			program = self.programs[name]
			program.children = [self.programs[child] for child in program.children]
			if program.children:
				for child in program.children:
					child.setParent(name)
		for program in self.programs:
			if not self.programs[program].parent:
				self.root = self.programs[program]
				break
		print(self.root)
		self.root.findImbalance()

		#print([self.programs[node] for node in self.programs])

	# def imbalance(self):



t = Tower("input.txt")
