from heapq import heappush, heappop

def isOpen(pos):
	x, y = pos
	return bin(x*x + 3*x + 2*x*y + y + y*y + MAGIC).count("1") % 2 == 0


#state would be position

def heuristic(pos, goal):
	return ((pos[0]-goal[0])**2+(pos[1]-goal[1])**2)**0.5

def neighbors(pos):
	x = [0, 0, 1, -1]
	y = [1, -1, 0, 0]

	coords = [(pos[0]+x[i], pos[1]+y[i]) for i in range(len(x)) if pos[0] + x[i] >= 0 and pos[1] + y[i] >=0]

	return {coord for coord in coords if isOpen(coord)}

def shortestPath(x, y):
	goal = (x, y)
	start = (1, 1)
	visited = set()
	heap = []

	g = {start: 0}
	heappush(heap, (0, start))

	while heap:
		f, pos = heappop(heap)

		if pos == goal:
			return f

		visited.add(pos)

		for neighbor in neighbors(pos):
			if neighbor in visited:
				continue

			neighborG = g[pos] + 1

			if neighbor not in g:
				g[neighbor] = float("inf")

			if neighborG >= g[neighbor]:
				continue
			
			g[neighbor] = neighborG
			neighborF = g[neighbor] + heuristic(neighbor, goal)
			heappush(heap, (neighborF, neighbor))


	return -1

from collections import deque

def bfs():
	# goal = (x, y)
	start = (1, 1)
	q = deque([start])
	distances = {start: 0}


	while q:
		curr = q.popleft()

		if distances[curr] < 50:
			for n in neighbors(curr):
				if n not in distances:
					q.append(n)
					distances[n] = distances[curr] + 1

	# return sum([len(distances[i]) for i in distances if i <= 50])
	return len(distances)





MAGIC = 1350

print(shortestPath(31, 39))
print(bfs())