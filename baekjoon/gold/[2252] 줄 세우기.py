from sys import stdin

N, M = map(int, stdin.readline().split())

graph = [[] for _ in range(N)]
from_cnt = [0 for _ in range(N)]

for _ in range(M):
    front, back = map(int, stdin.readline().split())
    from_cnt[back - 1] += 1
    graph[front - 1].append(back - 1)

queue = [i for i in range(N) if from_cnt[i] == 0]
while queue:
    temp = queue.pop()
    for i in graph[temp]:
        from_cnt[i] -= 1
        if from_cnt[i] == 0:
            queue.append(i)
    print(temp + 1, end=" ")
