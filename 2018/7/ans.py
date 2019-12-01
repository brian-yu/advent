
lines = [line.rstrip() for line in open('input.txt').readlines()]

g = {}
posts = set()
steps = set()
prereqs = {}

for line in lines:
    pre = line[5]
    post = line[36]
    g.setdefault(pre, set())
    g[pre].add(post)
    prereqs.setdefault(post, set())
    prereqs[post].add(pre)
    steps |= {pre, post}
    posts.add(post)

noDeps = steps - posts
print(noDeps)

from heapq import heappush, heappop
heap = []

for step in noDeps:
    heappush(heap, step)

order = []
visited = set()
while len(heap) > 0:
    step = heappop(heap)
    order.append(step)
    if step in g:
        for post in g[step]:
            prereqs[post].remove(step)
            if post not in visited and len(prereqs[post]) == 0:
                heappush(heap, post)
                visited.add(post)

print("".join(order))

