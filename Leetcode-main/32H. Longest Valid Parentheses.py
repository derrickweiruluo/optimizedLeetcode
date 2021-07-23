# 超高频 FAANG

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        
        dp = [0] * len(s)
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue     # skip to next iteration
            
            if stack:
                prev = stack.pop()  # get the most recent '('
                dp[i] = i - prev + 1 + dp[prev - 1]  # distance of curr () + the value of the previous(adjcent) one
        
        return max(dp)
