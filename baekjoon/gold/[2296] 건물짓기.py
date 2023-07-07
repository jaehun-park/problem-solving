from sys import stdin

N = int(stdin.readline())
buildings = sorted([list(map(int, stdin.readline().split())) for _ in range(N)])
increase_dp, decrease_dp = [b[2] for b in buildings], [b[2] for b in buildings]

for i in range(N):
    for j in range(i):
        if buildings[i][1] < buildings[j][1]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + buildings[i][2])
        else:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + buildings[i][2])

print(max(increase_dp + decrease_dp))
