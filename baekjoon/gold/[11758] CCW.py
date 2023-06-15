x, y = zip(*[list(map(int, input().split())) for _ in range(3)])
answer = (x[1] - x[0]) * (y[2] - y[0]) - (x[2] - x[0]) * (y[1] - y[0])
print(int(answer > 0) - int(answer < 0))
