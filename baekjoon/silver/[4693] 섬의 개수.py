from sys import stdin

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def search(matrix, visit, temp):
    result = []
    m, n = temp // len(matrix[0]), temp % len(matrix[0])
    for d in DIRECTIONS:
        i, j = m + d[0], n + d[1]
        if min(i, j) >= 0 and i < len(matrix) and j < len(matrix[0]) and matrix[i][j] == 1 and i * len(matrix[0]) + j not in visit:
            result.append(i * len(matrix[0]) + j)
    return result


maps = []
map_size = list(map(int, stdin.readline().split()))
while map_size != [0, 0]:
    maps.append([list(map(int, stdin.readline().split())) for _ in range(map_size[1])])
    map_size = list(map(int, stdin.readline().split()))

for map_matrix in maps:
    cnt = 0
    islands = list(range(len(map_matrix) * len(map_matrix[0])))
    stack = []
    visit = set()

    while islands:
        start = islands.pop()
        if start in visit or map_matrix[start // len(map_matrix[0])][start % len(map_matrix[0])] == 0:
            continue
        cnt += 1
        stack.append(start)
        while stack:
            temp = stack.pop()
            if temp in visit:
                continue
            visit.add(temp)
            stack.extend(search(map_matrix, visit, temp))
    print(cnt)
