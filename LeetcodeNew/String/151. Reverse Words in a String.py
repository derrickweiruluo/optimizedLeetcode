
class Solution:  # O(1) space, optimized
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = s.split()[::-1]
        for i in range(1, len(s)):
            s[i] = ' ' + s[i]
        
        return ''.join(s)
        
        
class Solution2:   # O(N) space and time    
    def reverseWords(self, s: str) -> str:
        queue = collections.deque(s.split())
        l = len(s.split())
        res = []
        
        for _ in range(l):
            w = queue.pop()
            res.append(w + ' ')
        return ''.join(res)[:-1]