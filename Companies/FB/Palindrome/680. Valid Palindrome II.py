'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.isValidPalidrome(s, left, right - 1) or self.isValidPalidrome(s, left + 1, right)
        
        return True
            
    def isValidPalidrome(self, s, i, j):
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True