import math
from sys import stdin


def distance(idx1, idx2):
    x1, y1 = STARS[idx1]
    x2, y2 = STARS[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


N = int(stdin.readline())
STARS = [list(map(float, stdin.readline().split())) for _ in range(N)]
edges = [(distance(i, j), i, j) for j in range(N) for i in range(N) if i != j]
edges.sort()

star_set = [set([i]) for i in range(N)]
result = 0
for edge in edges:
    cost, node1, node2 = edge
    for k in range(len(star_set)):
        if node1 in star_set[k]:
            i = k
        if node2 in star_set[k]:
            j = k
    if i == j:
        continue
    star_set[i] = star_set[i].union(star_set[j])
    del star_set[j]
    result += cost
    if len(star_set) == 1:
        break

print(result)
