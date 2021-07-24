class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # MAX_INT = 2147483647          2**31 - 1
        # MIN_INT = -2147483648        -2**31
        # HALF_MIN_INT = -1073741824    MIN_INT // 2

        
        if dividend == -2147483648 and divisor == -1:    # python corner case
            return 2147483647
        
        a, b = abs(dividend), abs(divisor)   # 先只考虑绝对值 （正数）
        res = 0
        
        for x in range(32)[::-1]:       # 从大到小 2^x 开始搜索可以整除的 x
            if (a >> x) - b >= 0:       # 如果可以整除
                res += 1 << x           #      (2 ^ x)
                a -= b << x             #  b * (2 ^ x)
        
        return res if (dividend > 0) == (divisor > 0) else -res    # 同号res 异号-res
