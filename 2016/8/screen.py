

class Screen:

	def __init__(self, w, h):
		self.screen = [[" " for i in range(w)] for j in range(h)]
		self.width = w
		self.height = h

	def rect(self, w, h):
		for r in range(h):
			for c in range(w):
				self.screen[r][c] = "#"

	def rotateCol(self, c, n):
		# prev = self.screen[-n%self.height][c]
		# for r in range(self.height):
		# 	temp = self.screen[r][c]
		# 	self.screen[r][c] = prev
		# 	prev = temp
		oldCol = [self.screen[r][c] for r in range(self.height)]
		for r in range(self.height):
			self.screen[r][c] = oldCol[(r-n)%self.height]

	def rotateRow(self, r, n):
		oldRow = [self.screen[r][c] for c in range(self.width)]
		for c in range(self.width):
			self.screen[r][c] = oldRow[(c-n)%self.width]

	def display(self):
		for row in self.screen:
			for item in row:
				print(item, end="")
			print()
		print()

	def parse(self, file):
		for line in file:
			words = line.strip().split()

			if words[0] == "rect":
				w, h = [int(i) for i in words[1].split("x")]
				self.rect(w, h)
			else:
				n = int(words[-1])
				pos = int(words[-3].split("=")[1])

				if words[1] == "column":
					self.rotateCol(pos, n)
				else:
					self.rotateRow(pos, n)

	def numOn(self):
		num = 0
		for row in self.screen:
			num += row.count("#")
		return num




f = open("input.txt")


s = Screen(50, 6)

s.parse(f)
s.display()
print(s.numOn())