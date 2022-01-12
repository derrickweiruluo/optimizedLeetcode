'''
Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.


Input:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Output: ["eat","oath"]
'''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        res = set()
        for word in words:
            t = trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t["#"] = "#"

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, "", res)
        return list(res)
    
    
    def dfs(self, board, i, j, trie, path, res):
        if "#" in trie:
            res.add(path)
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie:
            return
        
        cur_char = board[i][j]
        board[i][j] = "$"
        
        self.dfs(board, i+1, j, trie[cur_char], path + cur_char, res)
        self.dfs(board, i-1, j, trie[cur_char], path + cur_char, res)
        self.dfs(board, i, j+1, trie[cur_char], path + cur_char, res)
        self.dfs(board, i, j-1, trie[cur_char], path + cur_char, res)
        
        board[i][j] = cur_char