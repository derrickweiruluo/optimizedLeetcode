'''
Input: s = "aacecaaa"
Output: "aaacecaaa"

Input: s = "abcd"
Output: "dcbabcd"
'''

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