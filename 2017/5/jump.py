



dirs = [int(line.strip()) for line in open("test.txt")]
#print(dirs)
i = 0
steps = 0
while i >= 0 and i < len(dirs):
	#print(dirs)
	jump = dirs[i]
	if jump < 3:
		dirs[i] += 1
	else:
		dirs[i] -= 1
	i += jump
	steps += 1

print(steps)