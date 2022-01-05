'''
# 1216 
Valid Palindrome III

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

'''

# wis's  comment

# 想要将一个字符串s变成一个回文串（无论是通过增加还是删除），一个技巧就是构造另一个字符串t是s的逆序。于是，如果要求增加字符，那么s和t的shorted common supersequence就是需要增加的最少字符；如果要求删除字符，那么s和t的longest common subsequence就对应着需要删除的最少字符。

# 本题求出s和t的LCS后，只需要判断s的长度减去LCS的长度（即对于s而言最少需要删除的字符）是否小于等于k即可。
# DP
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