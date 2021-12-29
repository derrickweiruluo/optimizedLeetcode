'''
检查一个 数独 棋盘看是不是valid

Followup: N * N 的 数独棋盘
'''


class Solution:  # General N * N 的数独棋盘
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validSquare(board) and self.validRow(board) and self.validCol(board)
    
    def validSquare(self, board):
        n = int(sqrt(len(board)))
        for i in range(0, (n - 1) * n + 1, n):
            for j in range(0, (n - 1) * n + 1, n):
                square = [board[x][y] for x in range(i, i + n) for y in range(j, j + n)]
                if not self.valid(square):
                    return False
        return True
    
    def validRow(self, board):
        for row in board:
            if not self.valid(row):
                return False
        return True
    
    def validCol(self, board):
        for col in zip(*board):
            if not self.valid(col):
                return False
        return True
    
    def valid(self, nums):
        vals = [num for num in nums if num != '.']
        return len(vals) == len(set(vals))




class Solution:  # Specific 3 * 3 的数独棋盘
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validSquare(board) and self.validRow(board) and self.validCol(board)
    
    # def validSquare(self, board):
    #     n = int(sqrt(len(board)))
    #     for i in range(0, (n - 1) * n, n):
    #         for j in range(0, (n - 1) * n, n):
    #             square = [board[x][y] for x in range(i, i + n) for y in range(j, j + n)]
    #             if not self.valid(square):
    #                 return False
    #     return True
    
    def validSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.valid(square):
                    return False
        return True
    
    def validRow(self, board):
        for row in board:
            if not self.valid(row):
                return False
        return True
    
    def validCol(self, board):
        for col in zip(*board):
            if not self.valid(col):
                return False
        return True
    
    def valid(self, nums):
        vals = [num for num in nums if num != '.']
        return len(vals) == len(set(vals))