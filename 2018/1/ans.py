
lines = [line.rstrip() for line in open('input.txt').readlines()]

freq = 0

for delta in lines:
    sign = -1 if delta[0] == "-" else 1
    delta = sign * int(delta[1:])
    freq += delta

print(freq)

freq = 0
seen = set([0])
i = 0

while True:
    delta = lines[i]
    sign = -1 if delta[0] == "-" else 1
    delta = sign * int(delta[1:])
    freq += delta
    if freq in seen:
        print(freq)
        break
    seen.add(freq)
    i = (i+1) % len(lines)

