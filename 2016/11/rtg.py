from collections import deque

class Facility:

	def __init__(self, filename):
		self.floors = []
		self.itemIndex = {"e": 0}
		self.indexItem = {0: "e"}
		self.current = 1

		num = 0
		for line in open(filename):
			for word in line.rstrip().strip(".").replace(",", "").split():
				if word in {"generator", "microchip"}:
					num += 1
		for line in open(filename):
			words = line.rstrip().strip(".").replace(",", "").split()
			floorItems = set()
			for i in range(len(words)):
				if words[i] in {"generator", "microchip"}:
					item = words[i-1][0] + words[i][0]
					if item not in self.itemIndex:
						self.itemIndex[item] = len(self.itemIndex)
						self.indexItem[len(self.indexItem)] = item
					floorItems.add(item)
			
			l = ["e"] if not self.floors else ["."]
			for i in range(1, num+1):
				if i in self.indexItem and self.indexItem[i] in floorItems:
					l.append(self.indexItem[i])
				else:
					l.append(".")
			self.floors.append(tuple(l))
		self.floors = tuple(self.floors)
		self.display(self.floors)

	def __str__(self):
		return "\n".join(reversed([str(i) for i in self.floors]))

	def validateFloor(self, floor): #floor is a tuple of strings
		valid = True
		#print(floor)
		for item in floor:
			if "m" in item:
				valid = valid and (item[0]+"g" in floor) or (True not in ["g" in i for i in floor])
		return valid

	def isSolved(self, floors):
		return len(self.itemIndex) == len([i for i in floors[-1] if i in self.itemIndex])

	def display(self, floors):
		print("\n".join(reversed([str(i) for i in floors])))
		print("---")

	def move(self, floors, current, new, item):
		floors[current][self.itemIndex[item]] = "."
		floors[new][self.itemIndex[item]] = item

	def permutations(self, floors):

		current = [i for i in range(len(floors)) if floors[i][0] == "e"][0]

		perms = []

		newFloors = [i for i in range(current-1, current+2, 2) if i >= 0 and i <= 3]

		items = list([item for item in floors[current] if item in self.itemIndex and item != "e"])


		for newFloor in newFloors:
			for i in range(len(items)):
				a = items[i]
				perm = [list(floor) for floor in floors]
				self.move(perm, current, newFloor, a)
				self.move(perm, current, newFloor, "e")
				perm = tuple([tuple(floor) for floor in perm])
				if (self.validateFloor(perm[current]) and self.validateFloor(perm[newFloor])):
					perms.append(perm)
				for j in range(i, len(items)):
					b = items[j]
					if a != b:
						perm = [list(floor) for floor in floors]
						self.move(perm, current, newFloor, a)
						self.move(perm, current, newFloor, b)
						self.move(perm, current, newFloor, "e")
						
						perm = tuple([tuple(floor) for floor in perm])
						if (self.validateFloor(perm[current]) and self.validateFloor(perm[newFloor])):
							perms.append(perm)
		return perms

	def BFS(self, floors):

		q = deque([(floors, 0)])
		visited = set()

		while q:
			node, steps = q.popleft()

			if self.isSolved(node):
				print(steps)
				print("!!!!!!!SOLVED~~~~~")
				f.display(floors)
				return steps

			perms = self.permutations(node)

			for perm in perms:
				if perm not in visited:
					q.append((perm, steps+1))
					visited.add(perm)

	def solve(self):
		return self.BFS(self.floors)





f = Facility("input2.txt")
print(f.solve())
