'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
'''
class Solution:  #BEST
    
    # time: N^3, N is for substring method, N^2 is DFS + MEMO
    # Space O(N)
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)
        return self.dfs(s, 0, wordSet, memo)
    
    def dfs(self, s, i, wordSet, memo):
        if i == len(s):
            return True
        if s[i:] in memo:
            return memo[s[i:]]
        
        for j in range(i + 1, len(s) + 1):
            if s[i: j] in wordSet and self.dfs(s, j, wordSet, memo):
                memo[s[i: j]] = True
                return True
        
        memo[s[i:]] = False
        return False


        # Examples: 
        # s = "applepenapple", wordDict = ["apple","pen"]
        # apple, pen, apple -> True
        
        # s = "catsandog", ["cats","dog","sand","and","cat"]
        # cat - sand - og





class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # s = "applepenapple", wordDict = ["apple","pen"]
        # apple, pen, apple -> True
        
        # s = "catsandog", ["cats","dog","sand","and","cat"]
        # cat - sand - og
        
        memo = {} # hashmap {substring : Boolean}
        wordSet = set(wordDict)
        return self.dfs(s, 0, wordSet, memo)  # Boolean
    
    
    # s = "applepenapple"
    
    #s = 'apple' + dfs('penapple')
    #s = 'pen' + dfs('apple')

    
    # 这一步是搜索 s[idx:] 的subarray
    def dfs(self, s, idx, wordSet, memo):
        if idx == len(s):
            return True
        if s[idx:] in memo:
            return memo[s[idx:]]
        
        for i in range(idx + 1, len(s) + 1):
            # s[idx: i] 在字典里 AND dfs s[i:] 也是 True
            if s[idx:i] in wordSet and self.dfs(s, i, wordSet, memo):
                memo[s[idx:]] = True
                return True
        
        memo[s[idx:]] = False
        return False
            