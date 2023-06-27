import heapq
from sys import stdin

N, M = map(int, stdin.readline().split())
pre_cnt = [0 for _ in range(N + 1)]
next_num = [[] for _ in range(N + 1)]
for _ in range(M):
    first, second = map(int, stdin.readline().split())
    pre_cnt[second] += 1
    next_num[first].append(second)

hq = []
for i in range(1, N + 1):
    if pre_cnt[i] == 0:
        heapq.heappush(hq, i)
result = []

while hq:
    temp = heapq.heappop(hq)
    result.append(temp)
    for i in next_num[temp]:
        pre_cnt[i] -= 1
        if pre_cnt[i] == 0:
            heapq.heappush(hq, i)

print(*result)
