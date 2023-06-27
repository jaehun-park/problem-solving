from sys import stdin

N = int(stdin.readline())
costs = [list(map(int, stdin.readline().split())) for _ in range(N)]
k = ((1, 2), (0, 2), (0, 1))

d = [[float("inf") for _ in range(3)] for _ in range(3)]
for i in range(3):
    d[i][i] = costs[0][i]

for cost in costs[1:-1]:
    for i in range(3):
        indices = [m if d[i][m] < d[i][n] else n for m, n in k]
        for j in range(3):
            d[i].append(d[i][indices[j]])
            d[i][-1] += cost[j]
        d[i] = d[i][3:]

answer = float("inf")

for i in range(3):
    for j in range(3):
        for k in range(3):
            if k not in [i, j]:
                answer = min(answer, d[i][j] + costs[-1][k])

print(answer)
