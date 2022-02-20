'''
扫雷游戏， 按下一个格子之后 返回board的状态
'''


# board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
# board[clickr][clickc] is either 'M' or 'E'.
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        i, j = click[0], click[1]
        
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        self.dfs(board, i, j)
        return board
    
    
    def dfs(self, board, x, y):
        if board[x][y] != 'E':  #返回条件 One，被摁过了，就返回
            return
        
        dirs = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1), (0, 0)]
        count = 0
        
        for dx, dy in dirs:  # 数一个点上下左右有几个雷
            xi, yi = x + dx, y + dy
            if 0 <= xi < len(board) and 0 <= yi < len(board[0]) and board[xi][yi] == 'M':
                count += 1
         
        if count:            # 返回条件 Two，如果周边有雷，不搜索了，返回
            board[x][y] = str(count)
            return
        
        board[x][y] = 'B'
        
        for dx, dy in dirs:
            if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                self.dfs(board, x + dx, y + dy)