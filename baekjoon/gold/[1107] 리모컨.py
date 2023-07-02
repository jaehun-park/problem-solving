from bisect import bisect_left
from itertools import product
from sys import stdin

N = int(stdin.readline())
error_cnt = int(stdin.readline())
error_num = list(map(int, stdin.readline().split())) if error_cnt else []
button = [num for num in range(10) if num not in error_num]

if error_cnt != 10:
    possible_change = (
        [int("".join(str(x) for x in p)) for p in list(product(button, repeat=len(str(N)) - 1))] if len(str(N)) - 1 > 0 else []
    )
    possible_change.extend([int("".join(str(x) for x in p)) for p in list(product(button, repeat=len(str(N))))])
    possible_change.extend([int("".join(str(x) for x in p)) for p in list(product(button, repeat=min(len(str(N)) + 1, 6)))])
    adjacency_idx = bisect_left(possible_change, N)
    ch1 = possible_change[min(len(possible_change) - 1, adjacency_idx)]
    ch2 = possible_change[adjacency_idx - 1]
    channel = ch1 if abs(ch1 - N) < abs(ch2 - N) else ch2
else:
    channel = 100

print(min(abs(channel - N) + len(str(channel)), abs(N - 100)))
