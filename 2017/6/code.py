

s = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"
#s = "0 2 7 0"
s = tuple([int(i) for i in s.split()])

print(s)

print(len(s))

seen = set()
visited = {}
count = 0
while s:
	l = list(s)
	maxI = l.index(max(l))
	i = (maxI + 1) % len(l)
	a = l[maxI]
	l[maxI] = 0
	while a > 0:
		l[i] += 1
		a -= 1
		i = (i+1)%len(l)
	seen.add(s)
	if s not in visited:
		visited[s] = count
	else:
		print(count - visited[s])
		visited[s] = count
		break
	s = tuple(l)
	count += 1


print(count)




