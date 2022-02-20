'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".




""" Explainations:

Idea is start from each index and try to extend palindrome for both odd and even length.
for each idx, speadout left and right together until not palidrome or out of range
"""

# O(N^2) Time, O(1) Space 
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        
        for i in range(len(s)):
            count += self.extractPalindrome(s, i, i)       # odd-length palidrome
            count += self.extractPalindrome(s, i, i + 1)   # Even-length palidrome
            
        return count
    
    def extractPalindrome(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        return count


# O(N^2) Time, O(N^2) Space
def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        res = 0 
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
        return res