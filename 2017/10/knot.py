

def reverseWrap(l, start, length):
	a = start
	b = (start + length) % len(l)
	if start + length < len(l):
		return l[:a] + l[a:b][::-1] + l[b:]
	else:
		sub = (l[a:] + l[:b])[::-1]
		return sub[-b:] + l[b:a] + sub[:-b]

def knot(num, lengths, l=None, i=0, skip=0):
	if not l:
		l = [i for i in range(num)]

	for length in lengths:
		l = reverseWrap(l, i, length)
		i = (i + length + skip) % len(l)
		skip += 1

	return l, i, skip

def sparseHash(num, lengths):
	l = [i for i in range(num)]
	i = 0
	skip = 0

	for _ in range(64):
		l, i, skip = knot(num, lengths, l, i, skip)

	return l

def hexify(n):
	h = hex(n).split('x')[-1]
	if len(h) < 2:
		h = "0" + h
	return h

def denseHash(text):

	lengths = [ord(char) for char in text] + [17, 31, 73, 47, 23]

	l = sparseHash(256, lengths)

	dense = []

	for i in range(16):
		temp = l[i*16]
		for j in range(i*16+1, i*16+16):
			temp ^= l[j]
		dense.append(temp)

	return "".join([hexify(i) for i in dense])

print(knot(5, [3, 4, 1, 5]))
l = knot(256, [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110])
print(l[0][0] * l[0][1])


f = open("input.txt")
text = f.read().strip()


print(denseHash(""))
print(denseHash("AoC 2017"))
print(denseHash("1,2,3"))
print(denseHash("1,2,4"))

print()

print(denseHash(text))
