lines = [line.rstrip() for line in open('input.txt').readlines()]

coords = [tuple([int(x) for x in line.split(', ')]) for line in lines]

xmax = max(coord[0] for coord in coords) + 1
ymax = max(coord[1] for coord in coords) + 1

grid = [[0 for j in range(ymax)] for i in range(xmax)]

def man_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for x in range(xmax):
    for y in range(ymax):
        minDist = xmax+ymax
        minCoord = coords[0]
        dists = {}
        for coord in coords:
            dist = man_dist(coord, (x, y))
            dists.setdefault(dist, 0)
            dists[dist] += 1
            if dist < minDist:
                minDist = dist
                minCoord = coord
        if dists[minDist] > 1:
            grid[x][y] = "."
        else:
            grid[x][y] = minCoord

print(grid)

def adjacent(grid, pos):
    x, y = pos
    adj = []
    if x + 1 < len(grid) and grid[x+1][y] != ".":
        adj.append((x+1, y))
    if x - 1 >= 0 and grid[x-1][y] != ".":
        adj.append((x-1, y))
    if y + 1 < len(grid[0]) and grid[x][y+1] != ".":
        adj.append((x, y+1))
    if y - 1 >= 0 and grid[x][y-1] != ".":
        adj.append((x, y-1))

    return adj

from collections import deque
def findArea(grid, coord):
    q = deque([coord])
    visited = set([coord])
    area = 0
    while len(q) > 0:
        pos = q.popleft()
        area += 1
        if pos[0] == 0 or pos[0] == xmax-1 or pos[1] == 0 or pos[1] == ymax-1:
            return 0
        for n in adjacent(grid, pos):
            if grid[n[0]][n[1]] == coord and n not in visited:
                visited.add(n)
                q.append(n)
    print(len(visited))
    return area

print(xmax, ymax)
print(len(grid), len(grid[0]))
print(adjacent(grid, (346, 348)))
print(findArea(grid, (346, 348)))

def maxArea(grid, coords):
    maxA = 0
    for coord in coords:
        area = findArea(grid, coord)
        print(coord, area)
        if area > maxA:
            maxA = area
    return maxA

print(maxArea(grid, coords))

        
grid = [[0 for j in range(ymax)] for i in range(xmax)]

for x in range(xmax):
    for y in range(ymax):
        totalDist = 0
        for coord in coords:
            dist = man_dist(coord, (x, y))
            totalDist += dist
        if totalDist < 10000:
            grid[x][y] = 1


def findArea(grid, coord):
    q = deque([coord])
    visited = set([coord])
    area = 0
    while len(q) > 0:
        pos = q.popleft()
        area += 1
        for n in adjacent(grid, pos):
            if grid[n[0]][n[1]] == 1 and n not in visited:
                grid[n[0]][n[1]] = 0
                visited.add(n)
                q.append(n)
    return area

maxA = 0
for x in range(xmax):
    for y in range(ymax):
        if grid[x][y] == 1:
            area = findArea(grid, (x,y))
            if area > maxA:
                maxA = area
print(maxA)



