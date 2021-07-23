class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.test(mid, index, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1
        
    def test(self, val, index, n):
        b = max(val - index, 0)
        res = (b + val) * (val - b + 1) / 2
        b = max(val - ((n - 1) - index), 0)
        res += (b + val) * (val - b + 1) / 2
        return res - val
