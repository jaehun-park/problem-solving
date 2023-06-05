from sys import stdin
import heapq

V, E = map(int, stdin.readline().split())
edges = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, stdin.readline().split())
    edges[A].append([C, B])
    edges[B].append([C, A])
    
heap = [[0, 1]]
visit = set()
answer = 0

while len(visit) < V:
    c, b = heapq.heappop(heap)
    if b not in visit:
        visit.add(b)
        answer += c
        for edge in edges[b]:
            heapq.heappush(heap, edge)

print(answer)