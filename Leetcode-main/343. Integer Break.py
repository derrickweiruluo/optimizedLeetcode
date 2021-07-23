class Solution:
    def integerBreak(self, n: int) -> int:
        
        # corner cases, when n is < 4:
        if n == 2: return 1
        if n == 3: return 2
        
        res = 1
        
        # general cases: for any number > 4:
        while n > 4:
            res *= 3
            n -= 3
        
        # after rounds n -= 3 --> n == 4
        res *= n
        return res
