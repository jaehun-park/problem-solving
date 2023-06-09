from sys import stdin

N = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
reduce_num = [1 for _ in range(N)]

for i in range(N - 1, -1, -1):
    cnt = 0
    for j in range(i, N):
        if seq[i] > seq[j]:
            cnt = max(cnt, reduce_num[j])
    reduce_num[i] += cnt
    
print(max(reduce_num))