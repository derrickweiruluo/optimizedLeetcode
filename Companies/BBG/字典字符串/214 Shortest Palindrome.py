'''
Input: s = "aacecaaa"
Output: "aaacecaaa"

Input: s = "abcd"
Output: "dcbabcd"
'''

class Solution: # recursive
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        j = 0
        for i in reversed(range(len(s))):
            if s[i] == s[j]:
                j += 1
        return s[::-1][:len(s)-j] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]



class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        cur = s + '|' + s[::-1]
        lps = [-1] + [0] * len(cur)
        left, right = -1, 0
        
        while right < len(cur):
            while left >= 0 and cur[left] != cur[right]:
                left = lps[left]
            left += 1
            right += 1
            lps[right] = left
                
        return s[lps[-1]:][::-1] + s


# Brute Force
class Solution:
    def shortestPalindrome(self, s: str) -> str:

        re = s[::-1]
        i = len(s)
        
        while not s[:i] == re[len(s) - i:]:
            i -= 1
        
        return re[:len(s) - i] + s