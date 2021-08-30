"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 
Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 
Follow up: Could you use search pruning to make your solution faster with a larger board?

#######思路：
loop 每一个点，如果从这个点出发的DFS有解， return True， 都没有， False

DFS:
如果测完了, return True
如果出界或者当前idx != word[idx], return False

DFS前， 沉没当前idx, where board[i][j] == word[idx
Boolean = dfs 上下左右，如有一个true， reture
DFS后， 还原当前idx


"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        
        return False
    
    def dfs(self, board, i, j, word, idx):
        if len(word) == idx:
            return True
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or word[idx] != board[i][j]:
            return False
        
        board[i][j] = '#'
        
        found = self.dfs(board, i + 1, j, word, idx + 1) \
                    or self.dfs(board, i - 1, j, word, idx + 1) \
                    or self.dfs(board, i, j + 1, word, idx + 1) \
                    or self.dfs(board, i, j - 1, word, idx + 1)
        
        board[i][j] = word[idx]
        return found
