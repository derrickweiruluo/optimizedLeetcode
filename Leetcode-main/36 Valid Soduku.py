class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        return self.validSquare(board) and self.validRow(board) and self.validColumn(board)
        
    def validSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValid(square):
                    return False
        return True

    def validRow(self, board):
        for row in board:
            if not self.isValid(row):
                return False
        return True

    def validColumn(self, board):
        for col in zip(*board):
            if not self.isValid(col):
                return False
        return True

    def isValid(self, lst):
        numList = [val for val in lst if val != "."]
        return len(numList) == len(set(numList))
        
        
        
