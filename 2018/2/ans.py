from collections import Counter

lines = [line.rstrip() for line in open('input.txt')]

threes = 0
twos = 0

for line in lines:
    counter = Counter(line)
    vals = set(counter.values())
    print(vals)
    if 3 in vals:
        threes += 1
    if 2 in vals:
        twos += 1

print(threes * twos)


seen = {}
for line in lines:
    for i in range(len(line)):
        stub = line[:i] + "*" + line[i+1:]
        if stub in seen:
            print(line)
            print(seen[stub])
            print(stub)
            break
        seen[stub] = line
