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