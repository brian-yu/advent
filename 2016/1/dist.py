
f = open("input.txt")

l = []
for t in f:
 	l = t.rstrip().split(", ")

height = 0
width = 0

headings = ["N","E","S","W"]
mult = [1, 1, -1, -1]
h = 0

visited = {}

def checkOrAdd(w, h):
	if w in visited:
		if h in visited[w]:
			return True
		else:
			visited[w].add(h)
	else:
		visited[w] = {h}
	return False

def turn(heading, turn):
	if turn == "L":
		if heading == 0:
			return 3
		else:
			return heading - 1
	elif heading == 3:
		return 0
	else:
		return heading + 1

def move(heading, distance):
	global width, height, visited
	distance *= mult[heading]
	if heading in {0, 2}:
		for h in range(height, height+distance, mult[heading]):
			if(checkOrAdd(width, h)):
				print(width, h)
				print("hq found {}".format(abs(h)+abs(width)))
				return True
		height += distance
	else:
		for w in range(width, width+distance, mult[heading]):
			if (checkOrAdd(w, height)):
				print(w, height)
				print("hq found {}".format(abs(height)+abs(w)))
				return True
		width += distance
	return False

for d in l:
	h = turn(h, d[0])
	num = int(d[1:])
	if(move(h, num)):
		break

	# print("{} {}".format(d, headings[h]), end="")
	# print("\th: {} min h: {} max h: {}".format(height, minh, maxh), end = "")
	# print(" w: {} min w: {} max w: {}".format(width, minw, maxw))
#print("{} {} {} {}".format(maxh, minh, maxw, minw))

print(width, height)
print(height + width)

