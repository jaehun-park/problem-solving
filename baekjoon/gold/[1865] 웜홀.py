from sys import stdin


def has_cycle(graph, distance, N):
    for i in range(N):
        for node in range(N):
            for neighbor, time in graph[node]:
                if distance[node] + time < distance[neighbor]:
                    if i == N - 1:
                        return True
                    distance[neighbor] = distance[node] + time

    return False


TC = int(stdin.readline())
for _ in range(TC):
    N, M, W = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        s, e, t = map(int, stdin.readline().split())
        graph[s - 1].append([e - 1, t])
        graph[e - 1].append([s - 1, t])
    for _ in range(W):
        s, e, t = map(int, stdin.readline().split())
        graph[s - 1].append([e - 1, -t])
    distance = [0] + [10001 for _ in range(N - 1)]

    print("YES" if has_cycle(graph, distance, N) else "NO")
