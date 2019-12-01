
def isTrap(seg):
	return seg in {"^^.", ".^^", "^..", "..^"}

def nextRow(row):
	row = "." + row + "."
	return "".join(["^" if isTrap(row[i-1:i+2]) else "." for i in range(1, len(row)-1)])



def generate(row, num):
	maze = [row]

	while len(maze) < num:
		row = nextRow(row)
		maze.append(row)

	return maze

init = "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."

print("".join(generate(init, 400000)).count("."))
