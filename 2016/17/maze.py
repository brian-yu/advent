
from collections import deque
from hashlib import md5


def neighbors(state, pos):
	hex = md5(state.encode()).hexdigest()[0:4]
	#print(state)
	possible = []
	x, y = pos
	valid = {"b", "c", "d", "e", "f"}
	if y > 0 and hex[0] in valid:
		possible.append((state + "U", (x, y-1)))
	if y < 3 and hex[1] in valid:
		possible.append((state + "D", (x, y+1)))
	if x > 0 and hex[2] in valid:
		possible.append((state + "L", (x-1, y)))
	if x < 3 and hex[3] in valid:
		possible.append((state + "R", (x+1, y)))
	return possible

def bfs(passcode):

	visited = set([passcode])
	q = deque([(passcode, (0,0))])

	paths = []

	while q:
		state, pos = q.popleft()
		if pos == (3,3):
			#return state[len(passcode):]
			paths.append(state[len(passcode):])
			continue

		for nstate, npos in neighbors(state, pos):
			if nstate not in visited:
				visited.add(nstate)
				q.append((nstate, npos))
	return max([len(i) for i in paths])


print(bfs("mmsxrhfx"))

# print(neighbors("ihgpwlahD", (0,1)))