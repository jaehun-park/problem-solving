def solution(N, road, K):
    graph = [[500001 for _ in range(N)] for _ in range(N)]
    
    for start, end, dist in road:
        graph[start-1][end-1] = min(graph[start-1][end-1], dist)
        graph[end-1][start-1] = min(graph[end-1][start-1], dist)
    
    min_dist = [[i, graph[0][i]] for i in range(N)]
    heap = [[i, graph[0][i]] for i in range(N)]

    while heap:
        heap.sort(reverse=True, key=lambda x: x[1])
        tmp, dist = heap.pop()
        if dist > K:
            break
        for i in range(1, len(min_dist)):
            if min_dist[i][1] > min_dist[tmp][1] + graph[tmp][i]:
                min_dist[i][1] = min_dist[tmp][1] + graph[tmp][i]
        for i in range(len(heap)):
            heap[i][1] = min(min_dist[heap[i][0]][1], heap[i][1])
                
    answer = len([node for node in min_dist if node[1] <= K]) + 1
    return answer