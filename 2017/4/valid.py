
valid = 0

for line in open("input.txt"):
	words = line.strip().split()
	if len(words) == len(set(words)):
		valid += 1

print(valid)



valid = 0

for line in open("input.txt"):
	words = line.strip().split()

	sort = ["".join(sorted(word)) for word in words]
	if len(sort) == len(set(sort)):
		valid += 1

print(valid)