
FLIP = {"0": "1", "1": "0"}

def reverseFlip(state):
	global FLIP
	return "".join([FLIP[i] for i in state[::-1]])

def generate(state, size):
	if len(state) > size:
		return state[:size]
	return generate(state + "0" + reverseFlip(state), size)

def pairReduce(state):
	return "".join(["1" if state[i] == state[i+1] else "0" for i in range(0, len(state)-1, 2)])

def checksum(initial, size):
	state = generate(initial, size)

	s = pairReduce(state)

	while len(s) % 2 == 0:
		s = pairReduce(s)

	return s


print(checksum("11011110011011101", 35651584))

#print(checksum("10000", 20))