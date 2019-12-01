

f = open("input.txt")

freqs = []

for line in f:
	for i in range(len(line)):
		letter = line[i].strip()
		if len(freqs) < i + 1:
			freqs.append({})
		if letter not in freqs[i]:
			freqs[i][letter] = 0
		freqs[i][letter] += 1

s = ""

for freq in freqs:
	maxL = list(freq.keys())[0]
	for letter in freq:
		if freq[letter] > freq[maxL]:
			maxL = letter
	s += maxL
print(s)

s = ""
for freq in freqs:
	minL = list(freq.keys())[0]
	for letter in freq:
		if freq[letter] < freq[minL]:
			minL = letter
	s += minL
print(s)
