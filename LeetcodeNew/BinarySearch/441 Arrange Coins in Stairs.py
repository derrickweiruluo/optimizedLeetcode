'''
n coins, arrange them in rows
row_i has i coins, i start from 1 (1-indexed)

Asked, how many complete rows

'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        r = n
        
        left, right = 1, r
        while left <= right:
            mid = (left + right) // 2
            val = mid * (mid + 1) // 2
            if val == n:
                return mid
        
            #当left right 下一步要break while loop == 要产生解
            elif val > n:   # 还有剩余, (right - 1) 个完整的rows
                right = mid - 1
            else:           # 没有剩余, (right)     个完整的rows
                left = mid + 1
        
        return right