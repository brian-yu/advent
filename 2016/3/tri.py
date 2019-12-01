

def isValid(a, b, c):
	if (a + b > c) and (b + c > a) and (a + c > b):
		return True




f = open("input.txt")

valid = 0

triangles = []
for line in f:
	triangles.append([int(i) for i in line.split()])


for c in range(len(triangles[0])):
	for r in range(0, len(triangles), 3):
		if (isValid(triangles[r][c],triangles[r+1][c],triangles[r+2][c])):
			valid += 1


print(valid)