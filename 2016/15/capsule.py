

class Disk:

	def __init__(self, numPos, startPos):
		self.numPos = numPos
		self.startPos = startPos

	def __str__(self):
		return "{} positions. Starts at {}.".format(self.numPos, self.startPos)

	def getPosAtTime(self, time):
		return (time + self.startPos) % self.numPos


class Machine:

	def __init__(self, fname):
		self.disks = []
		for line in open(fname):
			tok = line.strip().strip(".").split()
			self.disks.append(Disk(int(tok[3]), int(tok[-1])))
		[print(disk) for disk in self.disks]

	def findTime(self):
		time = 0
		while True:
			posAtTimes = [self.disks[i].getPosAtTime(time+i+1) for i in range(len(self.disks))]
			if posAtTimes.count(0) == len(posAtTimes):
				return time
			time += 1



M = Machine("input2.txt")

# print(M.disks[0].getPosAtTime(1))
# print(M.disks[1].getPosAtTime(2))

print(M.findTime())