from sys import stdin

N = int(stdin.readline())
lines = [list(map(int, stdin.readline().split())) for _ in range(N)]
lines.sort()
seq = [line[1] for line in lines]
increase_num = [1 for _ in range(N)]

for i in range(N - 1, -1, -1):
    cnt = 0
    for j in range(i, N):
        if seq[i] < seq[j]:
            cnt = max(cnt, increase_num[j])
    increase_num[i] += cnt
    
print(N - max(increase_num))