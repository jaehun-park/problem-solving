from sys import stdin

N, M, X = map(int, stdin.readline().split())
adj_matrix = [[float("inf") if i != j else 0 for j in range(N)] for i in range(N)]
rvs_adj_matrix = [[float("inf") if i != j else 0 for j in range(N)] for i in range(N)]
for _ in range(M):
    start, end, time = map(int, stdin.readline().split())
    adj_matrix[start - 1][end - 1] = time
    rvs_adj_matrix[end - 1][start - 1] = time


def dijkstra(start, matrix):
    distance = matrix[start]
    fixed = [start]
    while len(fixed) != N:
        next_node = sorted([em for em in list(enumerate(distance)) if em[0] not in fixed], key=lambda x: x[1])[0][0]
        for i in range(N):
            if distance[i] > distance[next_node] + matrix[next_node][i]:
                distance[i] = distance[next_node] + matrix[next_node][i]
        fixed.append(next_node)
    return distance


to_home_times = dijkstra(X - 1, adj_matrix)
from_home_times = dijkstra(X - 1, rvs_adj_matrix)
total_times = [to_home_times[i] + from_home_times[i] for i in range(N)]
print(max(total_times))
