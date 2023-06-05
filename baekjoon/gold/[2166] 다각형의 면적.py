from sys import stdin

N = int(stdin.readline())
points = [list(map(int, stdin.readline().split())) for _ in range(N)]

answer = 0
for i in range(len(points)):
    (x1, y1), (x2, y2) = points[i - 1], points[i]
    answer += x1 * y2 - x2 * y1
print(round(abs(answer) / 2, 1))