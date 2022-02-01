'''
Note that you are allowed to reuse a dictionary word.


Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

'''
# Time O(N^2 + Trie Time), Space O(N + T)
# There are total N dp states, they are dp[0], dp[1],.., dp[n], each dp state needs a loop O(N) to calculate the result.
# Plus with the time to build the Trie, which is O(T).
# So total complexity is: O(N * N + T) = O(N^2 + T).
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            curr = curr.child[c]
        curr.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        root = TrieNode()
        for word in wordDict:
            root.addWord(word)
            
        memo = {}

        def dp(start):
            if start == n:  # Found a valid way to break words
                return True
            if start in memo:
                return memo[start]

            curr = root
            for end in range(start + 1, n + 1):  # O(N)
                c = s[end-1]
                if c not in curr.child: break
                curr = curr.child[c]
                if curr.isWord and dp(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return dp(0)



# s = "applepenapple", wordDict = ["apple","pen"]
# apple, pen, apple -> True

# s = "catsandog", ["cats","dog","sand","and","cat"]
# cat - sand - og


# time: N^3, N is for substring method, N^2 is DFS + MEMO
# Space O(N)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {} # hashmap {substring : Boolean}
        wordSet = set(wordDict)
        return self.dfs(s, 0, wordSet, memo)  # Boolean
    
    # 这一步是搜索 s[idx:] 的subarray
    def dfs(self, s, i, wordSet, memo):
        if i == len(s):
            return True
        if s[i:] in memo:
            return memo[s[i:]]
        
        for j in range(i + 1, len(s) + 1):
            # s[idx: i] 在字典里 AND dfs s[i:] 也是 True
            if s[i:j] in wordSet and self.dfs(s, j, wordSet, memo):
                memo[s[i:]] = True
                return True
        
        memo[s[i:]] = False
        return False





