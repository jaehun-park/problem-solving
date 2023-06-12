N, M = map(int, input().split())
BOARD = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if BOARD[i][j] == "R":
            red_loc = [i, j]
        if BOARD[i][j] == "B":
            blue_loc = [i, j]
        if BOARD[i][j] == "O":
            HOLE_LOC = [i, j]

DIRECTIONS = {(0, 1), (0, -1), (-1, 0), (1, 0)}


def move(red_loc, blue_loc, dy, dx):
    relative_direct = [int((blue_loc[i] - red_loc[i]) / (abs(blue_loc[i] - red_loc[i]) - 0.001)) for i in range(2)]
    next_loc = [red_loc[:], blue_loc[:]]

    order = [1, 0] if dy == relative_direct[0] and dx == relative_direct[1] else [0, 1]
    game_over, is_equal = False, False

    for i in order:
        while BOARD[next_loc[i][0] + dy][next_loc[i][1] + dx] != "#":
            if BOARD[next_loc[i][0] + dy][next_loc[i][1] + dx] == "O":
                game_over = True
            next_loc[i][0] += dy
            next_loc[i][1] += dx
            if next_loc[0] == next_loc[1]:
                next_loc[i][0] -= dy
                next_loc[i][1] -= dx
                break
    if next_loc == [red_loc, blue_loc]:
        is_equal = True

    return next_loc, game_over, is_equal


def check(red_loc, blue_loc):
    red_direct = [int((HOLE_LOC[i] - red_loc[i]) / (abs((HOLE_LOC[i] - red_loc[i])) - 0.001)) for i in range(2)]
    blue_direct = [int((HOLE_LOC[i] - blue_loc[i]) / (abs((HOLE_LOC[i] - blue_loc[i])) - 0.001)) for i in range(2)]

    if 0 not in red_direct:
        return False

    while red_loc != HOLE_LOC:
        red_loc[0] += red_direct[0]
        red_loc[1] += red_direct[1]
        if BOARD[red_loc[0]][red_loc[1]] == "#":
            return False

    if red_direct == blue_direct:
        while blue_loc != HOLE_LOC:
            blue_loc[0] += red_direct[0]
            blue_loc[1] += red_direct[1]
            if BOARD[blue_loc[0]][blue_loc[1]] == "#":
                return True
        return False
    return True


def bfs(red_loc, blue_loc):
    queue = [[red_loc, blue_loc, set(), 1]]
    answer = -1
    while queue:
        red_loc, blue_loc, pre_action, depth = queue.pop(0)
        if check(red_loc[:], blue_loc[:]):
            return depth
        if depth == 10:
            continue

        for option in DIRECTIONS - pre_action:
            pre_action = {(0, 1), (0, -1)} if option in [(0, 1), (0, -1)] else {(1, 0), (-1, 0)}
            (next_red_loc, next_blue_loc), game_over, is_equal = move(red_loc[:], blue_loc[:], option[0], option[1])
            if game_over or is_equal:
                continue
            queue.append([next_red_loc, next_blue_loc, pre_action, depth + 1])
    return answer


print(bfs(red_loc, blue_loc))
