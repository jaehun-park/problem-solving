class Game():
    def __init__(self, board, m, n):
        self.m, self.n = m, n
        self.init_board(board)
        self.remove_cnt = 0
    
    def init_board(self, board):
        board = [list(line) for line in board[::-1]]
        self.board = [[] for i in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                self.board[j].append(board[i][j])
    
    def search(self):
        result = set()
        for x in range(self.n-1):
            h = min(len(self.board[x]), len(self.board[x+1]))
            for y in range(h-1):
                if self.board[x][y] == self.board[x][y+1] == self.board[x+1][y] == self.board[x+1][y+1]:
                    result.update([(x,y), (x+1,y), (x,y+1), (x+1,y+1)])
        return list(result)
    
    def update(self):
        removable_list = self.search()
        if not removable_list:
            return False
        removable_list.sort(reverse=True, key=lambda idx: idx[1])
        self.remove_cnt += len(removable_list)
        for x, y in removable_list:
            del self.board[x][y]
        return True
        
                
def solution(m, n, board):
    game = Game(board, m, n)
    while game.update():
        continue
    answer = game.remove_cnt
    
    return answer