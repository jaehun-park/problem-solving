N, M = map(int, input().split())
woks = list(map(int, input().split())) + [0]
combinations = list(set([woks[i] + woks[j] for i in range(M + 1) for j in range(i + 1, M + 1)]))
dp = [0] + [-1] * N

for i in range(1, N + 1):
    pre_states = [dp[i - k] for k in combinations if i >= k and dp[i - k] != -1]
    dp[i] = min(pre_states) + 1 if pre_states else dp[i]

print(dp[N])
