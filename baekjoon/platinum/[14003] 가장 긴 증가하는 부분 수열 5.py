from bisect import bisect_left
from sys import stdin

N = int(stdin.readline())
sequence = list(map(int, stdin.readline().split()))
last_num_list = []
orders = [0 for _ in range(N)]
max_length = 0

for i, num in enumerate(sequence):
    if not last_num_list or last_num_list[-1] < num:
        last_num_list.append(num)
        orders[i] = max_length
        max_length += 1
    else:
        orders[i] = bisect_left(last_num_list, num)
        last_num_list[orders[i]] = num

result = []
loc = max_length - 1
for i, order in enumerate(orders[::-1]):
    if loc == order:
        result.append(sequence[-(i + 1)])
        loc -= 1
print(len(result))
print(*result[::-1])
