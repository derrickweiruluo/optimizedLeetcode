"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
x = 2.00000, n = 10 -> res = 1024.000
Example 2:
x = 2.10000, n = 3  -> res = 9.26100
Output: 9.26100
Example 3:
x = 2.00000, n = -2 -> res =  0.25000
"""


class Solution:
    """
    conditions:
    * n is an integer.
    * Either x is not zero or n > 0.
    """
    def myPow(self, x: float, n: int) -> float:
        # Either x is not zero or n > 0.
        if x == 0:
            return 0
        if n == 1:
            return x
        # pre-processing for negative n case
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:  # while n != 0
            if n % 2 == 1:
                res *= x
            x = x * x
            n = n // 2
        return res
