'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Input: s = "aba"
Output: true
s
Input: s = "abca"
Output: true

Input: s = "abc"
Output: false
'''
# O(N), O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isValid(s, left + 1, right) or self.isValid(s, left, right - 1)
        return True
            
    
    def isValid(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True