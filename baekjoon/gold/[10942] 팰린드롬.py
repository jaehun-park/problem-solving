from sys import stdin

N = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
queries = [list(map(int, stdin.readline().split())) for _ in range(M)]

dp = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i, min(i + 2, N)):
        if seq[i] == seq[j]:
            dp[i][j] = True

for i in range(N - 1, -1, -1):
    for j in range(i + 2, N):
        if seq[i] == seq[j] and dp[i + 1][j - 1]:
            dp[i][j] = True

for start, end in queries:
    print(1 if dp[start - 1][end - 1] else 0)
