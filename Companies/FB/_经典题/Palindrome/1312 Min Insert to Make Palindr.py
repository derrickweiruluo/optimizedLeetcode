'''

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
'''

# Time O(N^2)
# Space O(N^2)





class Solution:
    def minInsertions(self, s: str) -> int:
        
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i < j:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]


# Intuition
# Split the string s into to two parts,
# and we try to make them symmetrical by adding letters.

# The more common symmetrical subsequence they have,
# the less letters we need to add.

# Now we change the problem to find the length of longest common sequence.
# This is a typical dynamic problem.


# Explanation
# Step1.
# Initialize dp[n+1][n+1],
# wheredp[i][j] means the length of longest common sequence between
# i first letters in s1 and j first letters in s2.

# Step2.
# Find the the longest common sequence between s1 and s2,
# where s1 = s and s2 = reversed(s)

# Step3.
# return n - dp[n][n]

class Solution:  # LEE 215
    def minInsertions(self, s: str) -> int:
        
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                if s[i] == s[-j - 1]: 
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1]  = max(dp[i][j + 1], dp[i + 1][j])
        
        return n - dp[n][n]