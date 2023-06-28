from sys import stdin


def find(x):
    if x == cycle[x]:
        return x
    else:
        temp = find(cycle[x])
        cycle[x] = temp
        return temp


def union(x, y):
    x, y = find(x), find(y)
    if cycle[x] < cycle[y]:
        cycle[y] = cycle[x]

    else:
        cycle[x] = cycle[y]


N = int(stdin.readline())
planets = [list(map(int, stdin.readline().split())) for _ in range(N)]

x_distance = sorted([[planets[i][0], i] for i in range(N)])
y_distance = sorted([[planets[i][1], i] for i in range(N)])
z_distance = sorted([[planets[i][2], i] for i in range(N)])

x_distance = [[abs(x_distance[i][0] - x_distance[i + 1][0]), x_distance[i][1], x_distance[i + 1][1]] for i in range(N - 1)]
y_distance = [[abs(y_distance[i][0] - y_distance[i + 1][0]), y_distance[i][1], y_distance[i + 1][1]] for i in range(N - 1)]
z_distance = [[abs(z_distance[i][0] - z_distance[i + 1][0]), z_distance[i][1], z_distance[i + 1][1]] for i in range(N - 1)]

tunnels = sorted(x_distance + y_distance + z_distance)

total_cost = 0
connected_sets = [set([i]) for i in range(N)]
cycle = list(range(N))

for cost, m, n in tunnels:
    if find(m) != find(n):
        union(m, n)
        total_cost += cost

print(total_cost)
