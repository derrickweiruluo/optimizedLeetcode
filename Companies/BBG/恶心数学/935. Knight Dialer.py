'''
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
'''



# https://leetcode.com/problems/knight-dialer/discuss/189252/O(logN)
# O(N)
class Solution:
    def knightDialer(self, N: int) -> int:
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for i in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
                x6 + x8, x7 + x9, x4 + x8, \
                x3 + x9 + x0, 0, x1 + x7 + x0, \
                x2 + x6, x1 + x3, x2 + x4, \
                x4 + x6
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)