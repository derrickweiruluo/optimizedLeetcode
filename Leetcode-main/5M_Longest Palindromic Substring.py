class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, maxLen = 0, 1
        
        for i in range(len(s)):
            diff = i - maxLen
            if diff >= 1 and self.isPalindrome(i - maxLen - 1, i, s):
                start = i - maxLen - 1
                maxLen += 2
                continue
            if diff >= 0 and self.isPalindrome(i - maxLen, i, s):
                start = i - maxLen
                maxLen += 1
            
        return s[start: start + maxLen]
    
    def isPalindrome(self, start, end, s):
        return s[start: end + 1] == s[start: end + 1][::-1]
