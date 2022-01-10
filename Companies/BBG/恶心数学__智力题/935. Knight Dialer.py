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


# 电话键盘里面，纯数字的 键盘matching

class Solution:
    def knightDialer(self, N: int) -> int:
        mod = 10 ** 9 + 7
        res = [1] * 10
        mapping = {0:(4,6), 1:(6,8), 2:(7,9), 3:(4,8), 4:(0,3,9), \
                   5:(), 6:(0,1,7), 7:(2,6), 8:(1,3), 9:(2,4)}
        
        for _ in range(N - 1):
            cur = [0,0,0,0,0,0,0,0,0,0]
            for num in range(10):
                for nextNum in mapping[num]:
                    cur[nextNum] = (cur[nextNum] + res[num]) % mod
            res = cur
        
        return sum(res) % mod



class Solution:
    def knightDialer(self, N: int) -> int:
        # mapping = {0:(4,6), 1:(6,8), 2:(7,9), 3:(4,8), 4:(0,3,9), \
                #    5:(), 6:(0,1,7), 7:(2,6), 8:(1,3), 9:(2,4)}
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for i in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \
                x6 + x8, x7 + x9, x4 + x8, \
                x3 + x9 + x0, 0, x1 + x7 + x0, \
                x2 + x6, x1 + x3, x2 + x4, \
                x4 + x6
            
            x1 = x1 % (10**9 + 7)
            x2 = x2 % (10**9 + 7)
            x3 = x3 % (10**9 + 7)
            x4 = x4 % (10**9 + 7)
            x5 = x5 % (10**9 + 7)
            x6 = x6 % (10**9 + 7)
            x7 = x7 % (10**9 + 7)
            x8 = x8 % (10**9 + 7)
            x9 = x9 % (10**9 + 7)
            x0 = x0 % (10**9 + 7)


        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10**9 + 7)



# LEE LogN 解法

# if N = 1, return 10.
# if N > 1, return sum of [1,1,1,1,1,1,1,1,1,1] * M ^ (N - 1)
import numpy as np
class Solution:
    def knightDialer(self, N: int) -> int:
        mod = 10**9 + 7
        if N == 1: return 10
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res, N = 1, N - 1
        while N:
            if N % 2: res = res * M % mod
            M = M * M % mod
            N /= 2
        return int(np.sum(res)) % mod