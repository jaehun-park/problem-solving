def find_block(matrix, i, j, TARGET):
    directions = ((1,0), (-1,0), (0,1), (0,-1))
    pieces = []
    q = [(i, j)]
    while q:
        tmp = q.pop()
        if tmp not in pieces: 
            pieces.append(tmp)
        for d in directions:
            if min(tmp[0]+d[0], tmp[1]+d[1]) < 0 or max(tmp[0]+d[0], tmp[1]+d[1]) > len(matrix) - 1:
                continue
            if matrix[tmp[0]+d[0]][tmp[1]+d[1]] == TARGET and (tmp[0]+d[0], tmp[1]+d[1]) not in pieces:
                q.append((tmp[0]+d[0], tmp[1]+d[1]))
    result = list(zip(*pieces))
    start = min(result[0]), min(result[1])
    end = max(result[0]), max(result[1])
    size = len(pieces)
    
    block = []
    for i in range(start[0], end[0] + 1):
        row = []
        for j in range(start[1], end[1] + 1):
            if (i, j) in pieces:
                row.append(1)
            else:
                row.append(0)
        block.append(row)
    
    for piece in pieces:
        matrix[piece[0]][piece[1]] = 0 if TARGET == 1 else 1
                  
    return block, size

    
def rotate(block):
    n = len(block)
    m = len(block[0])
    rotated_block = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            rotated_block[j][n - 1 - i] = block[i][j]
    return rotated_block
    

def search(matrix, TARGET):
    result = []
    for i, row in enumerate(matrix):
        for j, em in enumerate(row):
            if em == TARGET:
                block, size = find_block(matrix, i, j, TARGET)
                for _ in range(4):
                    result.append([block, size])
                    block = rotate(block)
    return result


def solution(game_board, table):
    blocks = search(table, 1)
    emptys = search(game_board, 0)
    answer = 0
    for block in blocks:
        if block in emptys:
            emptys.remove(block)
            answer += block[1]
    return answer / 4


game_board = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], 
              [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], 
              [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], 
              [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], 
              [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], 
              [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], 
              [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 
              [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], 
              [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], 
              [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], 
              [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], 
              [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

table = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], 
         [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], 
         [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], 
         [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], 
         [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], 
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
         [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], 
         [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], 
         [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], 
         [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], 
         [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], 
         [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]

print(solution(game_board, table))