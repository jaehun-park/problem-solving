from sys import stdin

N, M, A, B = map(int, stdin.readline().split())
CONSTRAINT = set()
for _ in range(M):
    start, end = map(int, stdin.readline().split())
    CONSTRAINT.update(range(start, end + 1))

visit = set()
queue = [(N, 0)]
found = False
while queue:
    temp, depth = queue.pop(0)
    if temp in CONSTRAINT or temp < 0 or temp in visit:
        continue
    elif temp == 0:
        found = True
        break
    visit.add(temp)
    queue.extend([(temp - A, depth + 1), (temp - B, depth + 1)])

print(depth if found else -1)
