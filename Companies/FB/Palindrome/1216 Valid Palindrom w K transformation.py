'''
# 1216 
Valid Palindrome III

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

'''

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        '''
        dp[i][j]: the longest palindromic subsequence's length of substring(i, j), where i, j are left, right indices of the string.
        State transition:
        if s.charAt(i) == s.charAt(j):
        dp[i][j] = dp[i+1][j-1] + 2
        otherwise,
        dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]).
        dp[i][i] Initialized to 1.'''
        
        for i in range(n - 2, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return n - dp[0][n - 1] <= k