'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''

# O(1) space requirement, inplace
# 问清楚 321 是否变成 123
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = n -1
        
        # 第一步, p1： 从右往左找到第一个向下dip的上一位(悬崖边)
        while p1 and nums[p1 -1] >= nums[p1]:
            p1 -= 1
        
        # 第二步, p2 从右走到第一个 比p1 - 1 (第一个dip)要大的
        # worst case p2 == p1
        p2 = n -1
        while p1 != 0 and p2 > p1 and nums[p2] <= nums[p1 - 1]:
            p2 -= 1
        
        # 第三步， swap p1 - 1, p2

        # corner case
        # if arr is [3,2,1], non-decreasing, nothing happend in the p1, p2 swap
        # but p1 will be at 0, which will be perform the wrap around permuation
        nums[p1 - 1], nums[p2] = nums[p2], nums[p1 - 1]
        

        # [不用管的前部半段] + [p1: p3 + 1]
        # 因为p1:p3这一段就是mono-increasing的，直接指针排序
        p3 = n - 1
        while p3 > p1:
            nums[p3], nums[p1] = nums[p1], nums[p3]
            p1 += 1
            p3 -= 1

        
# sample test case:
# i:0,1,2,3,4,5,6,7
# --------------------
#  [1,2,3,4,6,5,1,0]
# 右边数起第一个dip
# p1 (从右边扫悬崖边), idx = 4, num = 6
# p2 (从右边扫比第一个dip大): idx = 5, num = 5
# p1 - 1 <--> p2
#  [1,2,3,5,6,4,1,0]
# 把 p1 到 p3 的 互换顺序
# 因为 p1 是第一个悬崖点，意味着 p1开始的有半段 保证 non-increasing

# [1,2,3,5] + [6,4,1,0]

# [1,2,3,5] = [0,1,4,6]