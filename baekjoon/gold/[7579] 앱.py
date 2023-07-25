from sys import stdin

N, M = map(int, stdin.readline().split())
memory = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))
total_cost = sum(cost)
min_cost = total_cost
dp = [[0 for _ in range(sum(cost))] for _ in range(N + 1)]

for i in range(1, N + 1):
    for c in range(min_cost):
        if c < cost[i - 1]:
            dp[i][c] = dp[i - 1][c]
        else:
            dp[i][c] = max(dp[i - 1][c - cost[i - 1]] + memory[i - 1], dp[i - 1][c])

        if dp[i][c] >= M:
            min_cost = c
            break

print(min_cost)
