lines = [line.rstrip() for line in open('input.txt').readlines()]

lines.sort()

print('\n'.join(lines))

guards = [i for i in range(len(lines)) if 'Guard' in lines[i]]

print(guards)
guards.append(len(lines))
minutes = {}
time = {}
for i in range(len(guards)-1):
    guard_id = lines[guards[i]].split("#")[1].split()[0]
    for j in range(guards[i]+1, guards[i+1], 2):
        minutes.setdefault(guard_id, {})
        time.setdefault(guard_id, 0)
        start = int(lines[j].split(":")[1][:2])
        end = int(lines[j+1].split(":")[1][:2])
        time[guard_id] += end - start
        for minute in range(start, end):
            minutes[guard_id].setdefault(minute, 0)
            minutes[guard_id][minute] += 1

maxMin = 0
maxGuard = 0

for guard in time:
    if time[guard] > maxMin:
        maxMin = time[guard]
        maxGuard = guard

print(maxGuard, maxMin)
maxMin = 0
maxMinute = 0

for minute in minutes[maxGuard]:
    if minutes[maxGuard][minute] > maxMin:
        maxMin = minutes[maxGuard][minute]
        maxMinute = minute

print(int(maxMinute) * int(maxGuard))


maxMin = 0
maxGuard = 0
maxMinute = 0

for guard in minutes:
    for minute in minutes[guard]:
        if minutes[guard][minute] > maxMin:
            maxMin = minutes[guard][minute]
            maxMinute = minute
            maxGuard = guard
print(int(maxGuard) * int(maxMinute))


