"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board, word):
        memo = {}  # memo of false result
        m, n = len(board), len(board[0])
        
        # Two Sanity Check:
        if m * n < len(word): return False   
        counter = collections.Counter(word)
        for i in range(m):
            for j in range(n):
                counter[board[i][j]] -= 1
        if max(counter.values()) > 0: return False
        
        for i in range(m):
            for j in range(n):
                if self.getWord(board, i, j, memo, word, 0):
                    return True
        return False

    def getWord(self, board, i, j, memo, word, pos):
        if pos == len(word):
            return True
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or memo.get((i, j)) or word[pos] != board[i][j]:
            return False
        memo[(i, j)] = True
        if self.getWord(board, i, j + 1, memo, word, pos + 1) \
              or self.getWord(board, i, j - 1, memo, word, pos + 1) \
              or self.getWord(board, i + 1, j, memo, word, pos + 1) \
              or self.getWord(board, i - 1, j, memo, word, pos + 1):
            return memo[(i, j)]
        
        memo[(i, j)] = False
        return memo[(i, j)]