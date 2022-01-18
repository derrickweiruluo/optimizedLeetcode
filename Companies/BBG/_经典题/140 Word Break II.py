
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        # my solution with comments and test cases
        # https://leetcode.com/submissions/detail/608597792/
        # this is huahua's shorter codes
        
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

#* ---------------------------------


#Important solution

class Solution:  # from Tony
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