

def freqDict(letters):
	freq = {}

	for letter in letters:
		if letter not in freq:
			freq[letter] = 1
		else:
			freq[letter] += 1
	return freq

def decrypt(wordList, ID):
	alpha = [chr(i) for i in range(97, 123)]
	words = []
	for word in wordList:
		s = ""
		for letter in word:
			s += alpha[(alpha.index(letter) + ID) % 26]
		words.append(s)
	return "-".join(words)

def isValid(code):
	sections = code.split("-")
	wordList = [str(i) for i in sections[:-1]]
	letters = "".join(wordList)
	ID = int(sections[-1].split("[")[0])
	check = sections[-1].split("[")[1].split("]")[0]

	freq = freqDict(letters)

	for letter in check:
		if letter not in freq:
			return 0
		if freq[letter] != max(freq.values()):
			return 0
		del freq[letter]

	decrypted = decrypt(wordList, ID)
	if "stor" in decrypted:
		print(ID, decrypted)

	return ID


f = open("input.txt")

IDsum = 0
for code in f:
	IDsum += isValid(code)

print(IDsum)
