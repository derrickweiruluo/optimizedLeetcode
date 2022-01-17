'''
n 个 硬币
ith row can only store i coins
could be imcomplete in the last row

return # of complete row
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
        
        # if target is 5, l = r = 5, --> left + 1 = 6, return right
        # if target is 5, l = r =6, --> right = mid - 1 = 5, return right
        return right