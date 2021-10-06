'''
Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

https://github.com/Taoge123/OptimizedLeetcode/blob/master/LeetcodeNew/DynamicProgramming/LC_140_Word_Break_II.py
'''

class Solution1:  # DFS_SubString Slicing
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, wordSet, memo)
    
    def dfs(self, s, wordSet, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        
        res = []
        for word in wordSet:
            if not s.startswith(word):
                continue
            if s == word:
                res.append(word)
            else:
                restOfTheResults = self.dfs(s[len(word):], wordSet, memo)
                for item in restOfTheResults:
                    res.append(word + ' ' + item)
        
        memo[s] = res
        return res

class Solution2:  # DFS whole string Indexing
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, 0, wordSet, memo)
    
    def dfs(self, s, idx, wordSet, memo):
        if s[idx:] in memo:
            return memo[s[idx:]]
        if not s:
            return []
        
        res = []
        for word in wordSet:
            if not s[idx:].startswith(word):
                continue
            if s[idx:] == word:
                res.append(word)
            else:
                restOfTheResults = self.dfs(s, idx + len(word), wordSet, memo)
                for item in restOfTheResults:
                    res.append(word + ' ' + item)
        
        memo[s[idx:]] = res
        return res