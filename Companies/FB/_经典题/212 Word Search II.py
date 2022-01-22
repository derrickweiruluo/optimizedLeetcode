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
class TrieNode():  # Pass on 01/20/22
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        self.word = None


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True
        node.word = word

class Solution:  
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, res)
        return res
    
    def dfs(self, board, parent, x, y, res):
        char = board[x][y]
        node = parent.children[char]
        if node.isWord:
            res.append(node.word)
            node.isWord = False         # avoid 同一个word 的重复搜索
            # Don't RETURN since child.word can be a prefix of other words, e.g., 'ane' and 'aneis'

        board[x][y] = '#'               # avoid 同一个 char的死循环
        for xi, yi in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if 0 <= xi < len(board) and 0 <= yi < len(board[0]) and board[xi][yi] in node.children:
                self.dfs(board, node, xi, yi, res)
        board[x][y] = char


        # hit the end of trie leaf node, if already checking "abcd" in trie leaf, (whether it works or not)
        # we don't need to spend time checking "abcde" word 
        # speed optimization only
        if not node.children:
            parent.children.pop(char)




# *-------------------------------
class Solution:  # TLE 42/62
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