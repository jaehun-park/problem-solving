from sys import stdin

N = int(stdin.readline())
mat = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[float("inf") if i != j else 0 for j in range(N)] for i in range(N)]

for i in range(1, N):
    for m in range(N - i):
        for k in range(m, i + m):
            dp[m][i + m] = min(dp[m][i + m], dp[m][k] + dp[k + 1][i + m] + mat[m][0] * mat[k][1] * mat[i + m][1])

print(dp[0][N - 1])
