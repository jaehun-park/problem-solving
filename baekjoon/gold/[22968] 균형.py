from bisect import bisect_left
from sys import stdin

T = int(stdin.readline())
V = [int(stdin.readline()) for _ in range(T)]
maximum = max(V)
d = [1, 2]
while d[-1] < maximum:
    depth = len(d)
    d.append(d[depth - 1] + d[depth - 2] + 1)

V = [(v, bisect_left(d, v)) for v in V]
print(*[depth + 1 if d[depth] <= v else depth for v, depth in V], sep="\n")
