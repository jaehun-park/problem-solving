from sys import stdin

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, field):
    queue = [(x, y)]
    field[y][x] = 0
    
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(field[0]) or ny < 0 or ny >= len(field):
                continue

            if field[ny][nx] == 1 :
                queue.append((nx, ny))
                field[ny][nx] = 0
        
# main
T = int(stdin.readline())
answers = []

for _ in range(T):
    width, height, cabbage_num = map(int, stdin.readline().split())
    field = [[0 for i in range(width)] for j in range(height)]
    answer = 0
    
    for _ in range(cabbage_num):
        x, y = map(int, stdin.readline().split())
        field[y][x] = 1
    
    for k in range(width * height):
        x, y = k % width, k // width
        if field[y][x] == 1:
            bfs(x, y, field)
            answer += 1
    
    answers.append(answer)

for answer in answers:
    print(answer)