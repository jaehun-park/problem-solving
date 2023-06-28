from bisect import bisect_left
from sys import stdin

N = int(stdin.readline())
lines = [list(map(int, stdin.readline().split())) for _ in range(N)]
lines.sort()
seq = [line[1] for line in lines]
last_num = []
orders = [0 for _ in seq]
max_order = 0

for i, num in enumerate(seq):
    if not last_num or last_num[-1] < num:
        last_num.append(num)
        orders[i] = max_order
        max_order += 1
    else:
        insert_idx = bisect_left(last_num, num)
        last_num[insert_idx] = num
        orders[i] = insert_idx

result = []
loc = max_order - 1
for i, order in enumerate(orders[::-1]):
    if loc == order:
        loc -= 1
        result.append(N - i - 1)

print(N - max_order)
for i, (a, b) in enumerate(lines):
    if i not in result:
        print(a)
