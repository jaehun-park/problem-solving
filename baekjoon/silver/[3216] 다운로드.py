from sys import stdin

N = int(stdin.readline())
answer, remain_playtime = 0, 0

for _ in range(N):
    music_len, load_time = map(int, stdin.readline().split())
    remain_playtime -= load_time
    if remain_playtime < 0:
        answer += abs(remain_playtime)
        remain_playtime = 0
    remain_playtime += music_len

print(answer)