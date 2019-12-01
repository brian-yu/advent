lines = [line.rstrip() for line in open('input.txt')]



seen = {}
overlap = set()
safe = None
for line in lines:
    split = line.split()
    r, c = split[2][:-1].split(",")
    l, w = split[-1].split("x")
    r,c,l,w=int(r),int(c),int(l),int(w)
    for x in range(r, r+l):
        for y in range(c, c+w):
            if (x, y) in seen:
                overlap.add((x, y))
            seen.setdefault((x, y), 0)
            seen[(x,y)] += 1

print(len(overlap))
for line in lines:
    split = line.split()
    r, c = split[2][:-1].split(",")
    l, w = split[-1].split("x")
    r,c,l,w=int(r),int(c),int(l),int(w)
    cut = False
    for x in range(r, r+l):
        for y in range(c, c+w):
            if seen[(x,y)] > 1:
                cut = True
    if not cut:
        safe = line
print(safe)
