timers = [0] * 9

for fish in open('src/day6/input.txt').read().strip().split(","):
    timers[int(fish)] += 1

for _day in range(256):
    new_timers = [0] * 9
    for i in range(1, 9):
        new_timers[i - 1] = timers[i]
    new_timers[8] = timers[0]
    new_timers[6] += timers[0]
    timers = new_timers

print(sum(timers))
