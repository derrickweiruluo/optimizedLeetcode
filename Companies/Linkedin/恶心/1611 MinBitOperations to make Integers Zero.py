'''
Example 2:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
Example 3:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.

'''

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # 2^k needs 2^(k+1)-1 operations.
        # https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/877798/JavaC%2B%2BPython-3-Solutions-with-Prove-O(1)-Space
        '''Solution 1: Recursion
        1XXXXXX -> 1100000 -> 100000 -> 0

        1XXXXXX -> 1100000 needs minimumOneBitOperations(1XXXXXX ^ 1100000),
        because it needs same operations 1XXXXXX ^ 1100000 -> 1100000 ^ 1100000 = 0.

        1100000 -> 100000 needs 1 operation.
        100000 -> 0, where 100000 is 2^k, needs 2^(k+1) - 1 operations.

        In total,
        f(n) = f((b >> 1) ^ b ^ n) + 1 + b - 1,
        where b is the maximum power of 2 that small or equals to n.

        Time O(logn)
        Space O(logn)
        '''
        
        ''' Solution 3, improve from Sol2, tail recursion
        Inspired by @endlesscheng, can be proved based on solution 2.
        We iterate the binary format of n,
        whenever we meet bit 1 at ith position,
        we increment the result by (1 << (i + 1)) - 1.

        Time O(logn)
        Space O(1)
        '''
        sign, res = 1, 0
        while n > 0:
            res += n ^ (n - 1) * sign
            n &= n - 1
            sign *= -1
        
        return abs(res)