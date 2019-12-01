

class Spiral:

	def __init__(self, goal):
		self.value = 1
		self.x = 0
		self.y = 0
		self.radius = 1
		self.goal = goal
		self.graph = {}
		self.found = False
		self.goalx = None
		self.goaly = None
		self.addToGraph()

	def generate(self):
		while not self.found:
			self.x = self.radius
			self.y = 1 - self.radius

			while self.y < self.radius:
				self.addToGraph()
				self.y += 1
			while self.x > -self.radius:
				self.addToGraph()
				self.x -= 1
			while self.y > -self.radius:
				self.addToGraph()
				self.y -= 1
			while self.x < self.radius:
				self.addToGraph()
				self.x += 1
			while self.y < 1 - self.radius:
				self.addToGraph()
				self.y += 1

			self.radius += 1

	def distanceToGoal(self):
		dist = 0
		self.x = self.goalx
		self.y = self.goaly
		while self.x != 0 or self.y != 0:
			if self.x != 0:
				self.x += -self.x/abs(self.x)
				dist += 1
			if self.y != 0:
				self.y += -self.y/abs(self.y)
				dist += 1
		return dist


	def neighborSum(self):
		total = 0
		for i in range(self.x-1, self.x+2):
			for j in range(self.y-1, self.y+2):
				try:
					total += self.graph[i][j]
				except:
					pass

		return total

	def addToGraph(self):

		if self.x == 0 and self.y == 0:
			self.value = 1
		else:
			self.value = self.neighborSum()
		print(self.x, self.y, self.value)

		if self.x not in self.graph:
			self.graph[self.x] = {}
		self.graph[self.x][self.y] = self.value

		if self.value > self.goal and not self.found:
			self.found = True
			self.goalx = self.x
			self.goaly = self.y
		# self.value += 1



s = Spiral(325489)
s.generate()
# print(s.graph[s.goalx][s.goaly])
# print(s.graph[0][0])
# print(s.graph[0][1])
# print(s.graph[1][1])
# print(s.graph[0][1])
# print(s.graph[-1][1])