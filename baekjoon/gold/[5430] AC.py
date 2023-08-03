from collections import deque
from sys import stdin

T = int(stdin.readline())
result = []
for _ in range(T):
    actions = stdin.readline().strip()
    length = int(stdin.readline())
    arr = stdin.readline().strip()[1:-1].split(",")
    arr = deque(arr) if length > 0 else deque()
    is_reverse, is_error = False, False

    for c in actions:
        if c == "R":
            is_reverse = False if is_reverse else True
        elif len(arr) > 0:  # D
            if is_reverse:
                arr.pop()
            else:  # forward
                arr.popleft()
        else:
            is_error = True
            break
    if is_error:
        result.append("error")
    else:
        if is_reverse:
            arr.reverse()
        arr = "[" + ",".join(arr) + "]"
        result.append(arr)
print(*result, sep="\n")
