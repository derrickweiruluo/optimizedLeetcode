"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board[0]) == 0: return
        self.solve(board)
        
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for char in "123456789":
                        if self.isValid(board, i, j, char):
                            board[i][j] = char
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                                
                    return False  # if no "True" after trying all numbers
        
        return True   # if no "False" after trying every spot
    
    def isValid(self, board, x, y, char):
        for i in range(9):
            if board[i][y] == char:
                return False
        
        for j in range(9):
            if board[x][j] == char:
                return False
            
        for i in range(3):
            for j in range(3):
                if board[(x // 3) * 3 + i][(y // 3) * 3 + j] == char:
                    return False
        
        return True
