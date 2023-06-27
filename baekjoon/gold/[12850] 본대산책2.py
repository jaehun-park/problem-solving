import copy


def matmul(mat1, mat2):
    size = len(mat1)
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000000007
    return result


graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]
d = int(input())
result = None

while d > 0:
    if d % 2 == 1:
        result = matmul(result, graph) if result is not None else copy.deepcopy(graph)
    graph = matmul(graph, graph)
    d //= 2

print(result[0][0])
