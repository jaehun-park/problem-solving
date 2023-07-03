from sys import stdin


def matmul(mat1, mat2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += mat1[i][k] * mat2[k][j]
            result[i][j] %= 1000000007
    return result


coef = [[1, 1], [1, 0]]
result = [[1, 0], [0, 1]]
N = int(stdin.readline()) - 1

while N > 0:
    if N % 2 == 1:
        result = matmul(coef, result)
    coef = matmul(coef, coef)
    N //= 2

print((result[1][0] + result[1][1]) % 1000000007)
