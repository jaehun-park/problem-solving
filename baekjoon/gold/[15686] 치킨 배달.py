from itertools import combinations
from sys import stdin

N, M = map(int, stdin.readline().split())
city = [list(map(int, stdin.readline().split())) for _ in range(N)]

houses = [[i, j] for i in range(N) for j in range(N) if city[i][j] == 1]
chickens = [[i, j] for i in range(N) for j in range(N) if city[i][j] == 2]

dists = [[abs(chicken[0] - house[0]) + abs(chicken[1] - house[1]) for chicken in chickens] for house in houses]

total_dists = []
for selected in combinations(range(len(chickens)), M):
    total_dists.append(sum([min([dists[i][j] for j in selected]) for i in range(len(houses))]))

print(min(total_dists))
