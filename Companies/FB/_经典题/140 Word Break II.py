'''
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
'''


# time O(2^n) in the worse case scenario where all combinations of the string are correct (e,g, s=aaa, dic=[a, aa, aaa]).
# Space O(2^n) for the same reason - every partition is stored in memory


# Same worst case time complexity as below, but with DP Pruning
class Solution:  # 1st-BEST from Tony
    def wordBreak(self, s, wordDict):
        res = []
        self.dfs(s, wordDict, '', res)
        return res

    def dfs(self, s, dic, path, res):
    # Before we do dfs, we check whether the remaining string
    # can be splitted by using the dictionary,
    # in this way we can decrease unnecessary computation greatly.
        if self.check(s, dic): # prunning
            if not s:
                res.append(path[:-1])  # get rid of trailing space
                return # backtracking
            for i in range(1, len(s)+1):
                if s[:i] in dic:
                    # dic.remove(s[:i])
                    self.dfs(s[i:], dic, path + s[:i] + " ", res)

    # DP code to check whether a string can be splitted by using the
    # dic, this is the same as word break I.
    def check(self, s, dic):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]
# *--------------------------------

class Solution:
    class Trie:
        def __init__(self):
            self.root = {}
            self.WORD_DELIM = '$'
            
        def addWord(self, word):
            cur = self.root
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur[self.WORD_DELIM] = word
            
        def addWords(self, words):
            for word in words:
                self.addWord(word)
                
        def getValidSentences(self, word, res = ''):            
            res = []
            def dfs(word=word, temp=[]):
                cur = self.root
                for i,char in enumerate(word):
                    if self.WORD_DELIM in cur:
                        dfs(word[i:], temp + [cur[self.WORD_DELIM]])
                    if char not in cur:
                        break
                    cur = cur[char]
                else:
                    if self.WORD_DELIM in cur:
                        res.append(' '.join(temp + [cur[self.WORD_DELIM]]))
            dfs()
            return res
                
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = self.Trie()
        trie.addWords(wordDict)
        return trie.getValidSentences(s)



#* ---------------------------------
class Solution:  # 2nd-BEST
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}
        
        def dfs(s, wordSet):
            if s in memo:
                return memo[s]
            
            res = []
            if s in wordSet:
                res.append(s)
            for i in range(1, len(s)):
                right = s[i:]
                if right in wordSet:
                    res += [word + " " + right for word in dfs(s[0:i], wordSet)]
            
            memo[s] = res
            return memo[s]
        
        return dfs(s, wordSet)









# Additional Note
    # my solution with comments and test cases
    # https://leetcode.com/submissions/detail/608597792/
    # this is huahua's shorter codes