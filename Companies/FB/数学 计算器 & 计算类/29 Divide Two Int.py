# 给两个整数， 可正可负， 用bit操作求truncated的商

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        # [-2^31, 2^31 - 1], 所以需要下面的corner case check
        if dividend == -2147483648 and divisor == -1:
            return 2147483647


        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        # Note: a >> n == floor(a / 2^n)
        
        # 19/3 -->  3 * 2^2 + 3 * 2^1, 所以我们要尝试不断right shift dividend， 递减的方式
        for x in range(31, -1, -1):
            if dividend >> x >= divisor:
                res += 1 << x
                dividend -= divisor << x
        
        return res * sign