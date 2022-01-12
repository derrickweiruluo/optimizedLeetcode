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
        memo = {}
        m, n = len(board), len(board[0])
        
        # do a fast check first, before the expensive DFS
        if m * n < len(word): return False
        counter = collections.Counter(word)
        for i in range(m):
            for j in range(n):
                counter[board[i][j]] -= 1
        if max(counter.values()) > 0: return False
        
        # Start of DFS
        for i in range(m):
            for j in range(n):
                if self.getWords(board, word, i, j, memo, 0):
                    return True

        return False

    def getWords(self, board, word, i, j, memo, pos):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or memo.get((i, j)) or word[pos] != board[i][j]:
            return False

        memo[(i, j)] = True
        res = self.getWords(board, word, i, j + 1, memo, pos + 1) \
              or self.getWords(board, word, i, j - 1, memo, pos + 1) \
              or self.getWords(board, word, i + 1, j, memo, pos + 1) \
              or self.getWords(board, word, i - 1, j, memo, pos + 1)
        memo[(i, j)] = False

        return res