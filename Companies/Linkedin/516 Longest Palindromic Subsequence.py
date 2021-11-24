

class Solution: # 2D DP
    def longestPalindromeSubseq(self, s: str) -> int:        
        '''
        Idea:
        dp[i][j] = longest palindrome subsequence of s[i to j].
        If s[i] == s[j], dp[i][j] = 2 + dp[i+1][j - 1]
        Else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        '''
        # Solutuon 1
        n = len(s)
        dp = [[1] * 2 for _ in range(n)]
        for j in range(1, len(s)):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j % 2] = 2 + dp[i + 1][(j - 1) % 2] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j % 2] = max(dp[i + 1][j % 2], dp[i][(j - 1) % 2])
        return dp[0][(n - 1) % 2]



class Solution:  # TOO advance DP, 1D
    def longestPalindromeSubseq(self, s: str) -> int:
        # https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99129/Python-DP-O(n)-space-O(n2)-time
        
        n = len(s)
        dp = [1] * n
        for j in range(1, len(s)):
            prev = dp[j]
            for i in range(j - 1, -1, -1):
                temp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + prev if i + 1 < j else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                prev = temp
                    
        return dp[0]
        
        
        
