
def findNextLayer(s):
	groups = []
	inGarbage = False
	currGroup = []
	depth = 0
	isCanceled = False
	numInGarbage = 0

	i = 0
	while i < len(s):
		if not inGarbage:
			if s[i] == "{":
				if not currGroup:
					currGroup.append(i)
				depth += 1
			if s[i] == "}":
				depth -= 1
				if depth == 0:
					currGroup.append(i)
					groups.append(currGroup)
					currGroup = []
			if s[i] == "<":
				inGarbage = True
		else:
			if s[i] == ">" and not isCanceled:
				inGarbage = False
			
			if s[i] != "!" and s[i] != ">" and not isCanceled:
				numInGarbage += 1

			if s[i] == "!":
				isCanceled = not isCanceled
			else:
				isCanceled = False

		i += 1
	return groups, numInGarbage


def countGroups(s, depth=0):
	groups, _ = findNextLayer(s)

	if not groups:
		return 0

	total = 0

	for group in groups:
		total += 1 + depth + countGroups(s[group[0]+1:group[1]], depth + 1)

	return total


f = open("input.txt")
s = [line for line in f][0].strip()

print(countGroups(s))

_, num = findNextLayer(s)

print(num)