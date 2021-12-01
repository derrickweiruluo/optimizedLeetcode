"""
trunctated int result

--> next greater - 1
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0: return 0
        if x == 1: return 1
        
        left, right = 1, x
        while left < right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        
        return left - 1