'''
使用相同的digit， 找出next greater

这题和 I II 不是一个类型，属于 two-pointer
'''

# Input: n = 12
# Output: 21


# Input: n = 21
# Output: -1

class Solution: # BEST, same complexity
    def nextGreaterElement(self, n: int) -> int:
        
        if int(n) < 12: return -1
        
        nums = list(str(n))
        n = len(nums)
        p1 = n -1
        
        # 第一步, p1： 从右往左找到第一个向下dip的上一位(悬崖边)
        while p1 and nums[p1 -1] >= nums[p1]:
            p1 -= 1
        
        # 第二步, p2 从右走到第一个 比p1 - 1 (第一个dip)要大的
        # worst case p2 == p1
        #  conrner case: if p1 == 0, already the greatest
        p2 = n -1
        while p1 != 0 and p2 > p1 and nums[p2] <= nums[p1 - 1]:
            p2 -= 1
        
        # 第三步， swap p1 - 1, p2
        # similar to 让最开始dip往上抬升一点点
        if p1 - 1 < 0: return -1
        nums[p1 - 1], nums[p2] = nums[p2], nums[p1 - 1]
        

        # [不用管的前部半段] + [p1: p3 + 1]
        # 因为p1:p3这一段就是mono-increasing的，直接指针排序
        p3 = n - 1
        while p3 > p1:
            nums[p3], nums[p1] = nums[p1], nums[p3]
            p1 += 1
            p3 -= 1
        
        res = int("".join(nums))
        if res == int(n): return -1
        return res if res < 2 ** 31 else -1