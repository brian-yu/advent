from hashlib import md5





def hasTriple(s):
	for i in range(len(s)):
		char = s[i]

		if s[i+1:i+3] == 2 * char:
			return char

	return False

def findKeys(salt):
	keys = []
	needs = {}

	i = 0
	while len(keys) < 64:
		hex = md5((salt+str(i)).encode()).hexdigest()

		for _ in range(2016):
			hex = md5(hex.encode()).hexdigest()
		
		trip = hasTriple(hex)

		for need in needs:
			# idx, hashes = needs[need]
			if need*5 in hex:
				for pair in needs[need]:
					if i < pair[0] + 1000 and len(keys) < 64:
						keys.append(pair)
						print(pair)

		if trip:
			if trip in needs:
				needs[trip].append((i, hex))
			else:
				needs[trip] = [(i, hex)]

		


		i += 1

	#[print(pair) for pair in sorted(keys)]
	print("--")
	print(sorted(keys)[63])
	return keys



keys = findKeys("ihaygndm")
#keys = findKeys("abc")