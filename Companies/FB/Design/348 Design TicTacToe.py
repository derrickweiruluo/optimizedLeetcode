'''
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

1.  A move is guaranteed to be valid and is placed on an empty block.
2.  Once a winning condition is reached, no more moves are allowed.
3.  A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

'''

# Clarifications:
# 1: Garantee valid move


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0] * n
        self.col = [0] * n
        self.diagOne = 0
        self.diagTwo = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:

        
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # step 1: fill the row, col, diagonal_one and diagonal_two accordingly
        self.row[row] += 1 if player == 1 else -1
        self.col[col] += 1 if player == 1 else -1
        if row + col == self.n - 1:
            self.diagOne += 1 if player == 1 else -1
        if row - col == 0:
            self.diagTwo += 1 if player == 1 else -1
            
        # check all four types of winning condiitons, if winner, return it
        # 
        # 下面的abs() 代码要注意括号的位置，很容易写错位置，bug-check    
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n \
            or abs(self.diagOne) == self.n or abs(self.diagTwo) == self.n:
            if player == 1: 
                return 1
            else: 
                return 2
        return 0