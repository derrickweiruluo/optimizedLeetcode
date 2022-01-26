'''
Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

打破一个回文串 且 最小

'''



#  Complexity
# Time O(N)
# Space O(N)

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        Check half of the string,
        replace a non 'a' character to 'a'.

        If only one character, return empty string.
        Otherwise repalce the last character to 'b'
        """
        n = len(palindrome)
        if n == 1:
            return ''
        
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b'