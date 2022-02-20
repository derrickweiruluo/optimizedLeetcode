'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

# O(n^2) time, O(1) space

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            odd = self.extend(s, i, i)
            even = self.extend(s, i, i + 1)
            print(odd, even)
            res = max(res, odd, even, key = len)
        return res
    
    def extend(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
