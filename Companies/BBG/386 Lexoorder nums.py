'''
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Input: n = 2
Output: [1,2]
'''


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = [None] * n
        cur = 1
        for i in range(n):
            res[i] = cur
            
            if cur * 10 <= n:
                cur = cur * 10
            else:
                if cur + 1 > n:
                    cur = cur // 10
                cur += 1
                while cur % 10 == 0:
                    cur = cur // 10
        return res