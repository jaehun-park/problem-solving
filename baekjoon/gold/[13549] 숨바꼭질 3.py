from collections import deque

start, end = map(int, input().split())
queue = deque([[start, 0]])
visit = set()

while queue:
    loc, depth = queue.popleft()

    if loc in visit:
        continue
    visit.add(loc)

    if loc == end:
        break
    elif loc > end:
        queue.append([loc - 1, depth + 1])
    else:
        queue.extend([[loc * 2, depth], [loc - 1, depth + 1], [loc + 1, depth + 1]])

print(depth)
