class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # breaking the recursive search on a substring
        if len(s) < k:
            return 0
        
        for char in set(s):
            if s.count(char) < k:
                return max(self.longestSubstring(subString,k) for subString in s.split(char))
            
        return len(s)
