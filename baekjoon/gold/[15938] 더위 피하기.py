from sys import stdin

DIRECTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MOD = 10**9 + 7

sx, sy = map(int, stdin.readline().split())
T = int(stdin.readline())
home_loc = list(map(int, stdin.readline().split()))
N = int(stdin.readline())
obstacles_loc = [list(map(int, stdin.readline().split())) for _ in range(N)]
dp = [[[0 for _ in range(201)] for _ in range(401)] for _ in range(401)]


def go_home(x, y, t):
    print(x, y, t)
    if [x, y] == home_loc:
        return 1
    if abs(home_loc[0] - x) + abs(home_loc[1] - y) > t:
        return 0
    for dx, dy in DIRECTION:
        args = [x + dx, y + dy, t - 1]
        if args[:2] not in obstacles_loc:
            dp[x - home_loc[0]][y - home_loc[1]][t] += go_home(*args) % MOD
    return dp[x - home_loc[0]][y - home_loc[1]][t] % MOD


print(go_home(sx, sy, T))
