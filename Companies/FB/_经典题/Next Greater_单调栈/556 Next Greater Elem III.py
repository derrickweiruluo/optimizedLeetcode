'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
'''

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
        
        





class Solution:  # BEST, same complexity
    def nextGreaterElement(self, n: int) -> int:
        
        if int(n) < 12: return -1

        arr = list(str(n))
        n = len(arr)
        i, j = n - 2, n - 1
        while i >= 0 and arr[i + 1] <= arr[i]:
            i -= 1
        
        if i == -1: return -1
        
        while arr[j] <= arr[i]:
            j -= 1
        
        arr[i], arr[j] = arr[j], arr[i]
        
        res = int("".join(arr[:i + 1] + arr[i + 1:][::-1]))
        
        return res if res < 2 ** 31 else -1