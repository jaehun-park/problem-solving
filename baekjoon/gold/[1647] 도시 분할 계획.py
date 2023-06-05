from sys import stdin
import heapq

N, M = map(int, stdin.readline().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, stdin.readline().split())
    edges[A].append((C, B))
    edges[B].append((C, A))
    
heap = [(0, 1)]
visit = set()
answer = 0
max_cost = 0

while len(visit) < N:
    c, b = heapq.heappop(heap)
    if b not in visit:
        visit.add(b)
        answer += c
        max_cost = max(max_cost, c)
        for edge in edges[b]:
            if edge[1] not in visit:
                heapq.heappush(heap, edge)

print(answer - max_cost)