"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.



X X X X
X O O X
X X O X
X O X X


After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

"""


# 题意： # 沉默所有岛屿，除了挨着四条边上的陆地
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in (0, m - 1):
            for j in range(n):
                if board[i][j] == 'O':
                    self.dfs(board, i, j)
        
        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == 'O':
                    self.dfs(board, i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    
    def dfs(self, grid, i, j):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != 'O':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)