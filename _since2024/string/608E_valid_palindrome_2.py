"""
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
"""

# s consists of lowercase English letters.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def _is_valid_palindrone(substring, i, j):
            while i < j:
                if substring[i] == substring[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True


        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return _is_valid_palindrone(s, left + 1, right) or _is_valid_palindrone(s, left, right - 1)
        return True