'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note::  that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 
Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''


class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        memo = {}
        return self.dfs(s, 0, wordSet, memo)
    
    def dfs(self, string, idx, wordSet, memo):
        if idx == len(string):
            return True
        
        if string[idx:] in memo:
            return memo[string[idx:]]
        
        for i in range(idx + 1, len(string) + 1):
            if string[idx: i] in wordSet and self.dfs(string, i, wordSet, memo):
                memo[string[idx:]] = True
                return True
        
        memo[string[idx:]] = False
        return False

'''https://leetcode.com/problems/word-break/discuss/43995/A-Simple-Python-DP-solution'''
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        
        dp = [True] + [False] * len(s)
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i: j + 1] in wordSet:
                        dp[j + 1] = True
        
        return dp[-1]