from sys import stdin

N, M = map(int, stdin.readline().split())
orders = [list(map(int, stdin.readline().split()))[1:] for _ in range(M)]

pre_cnt = [0 for _ in range(N)]
next_num = [[] for _ in range(N)]

for order in orders:
    for i in range(len(order) - 1):
        next_num[order[i] - 1].append(order[i + 1] - 1)
        pre_cnt[order[i + 1] - 1] += 1

queue = [i for i in range(N) if pre_cnt[i] == 0]
result = []

while queue:
    temp = queue.pop(0)
    result.append(temp + 1)
    for i in next_num[temp]:
        pre_cnt[i] -= 1
        if pre_cnt[i] == 0:
            queue.append(i)

if len(result) == N:
    for res in result:
        print(res)
else:
    print(0)
