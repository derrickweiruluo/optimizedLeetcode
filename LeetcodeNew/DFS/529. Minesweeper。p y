"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


#######
DFS两个返回条件 
    1. 假如当前格子不为 empty
    2. 假如已经计算出相邻8个方向有多少颗雷

"""

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        self.dfs(board, i, j)
        return board
    
    def dfs(self,board, x, y):
        '''
        两个返回条件 
        1. 假如当前格子不为 empty
        2. 假如已经计算出相邻8个方向有多少颗雷
        '''
        if board[x][y] != 'E':
            return
        dirs = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
        count = 0
        for dx, dy in dirs:
            if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]) and board[x + dx][y + dy] == 'M':
                count += 1
        
        if count:
            board[x][y] = str(count)
            return
        else:
            board[x][y] = 'B'
            
        for dx, dy in dirs:
            if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                self.dfs(board, x + dx, y + dy)
