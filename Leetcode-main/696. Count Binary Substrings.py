class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        res = 0
        
        prevCount, curCount = 0, 1
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curCount += 1
            else:
                res += min(prevCount, curCount)
                prevCount = curCount
                curCount = 1
        
        return res + min(prevCount, curCount)
