'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # bit
        if n == 0: return False
        return n & (n - 1) == 0
        
        # binary search
        left, right = 0, 32
        while left <= right:
            mid = (left + right) // 2
            cur = 2 ** mid
            if cur == n:
                return True
            elif cur < n:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
                