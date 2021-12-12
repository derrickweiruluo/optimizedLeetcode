'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''

# O(1) space requirement, inplace
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = n -1
        
        # 第一步, p1(left) 从右走到第一个 降落点(mono-increasing)
        while p1 and nums[p1 -1] >= nums[p1]:
            p1 -= 1
        
        # 第二步, p2(right) 从右走到第一个 比当前p1 dip要大的
        p2 = n -1
        while p1 and p2 > p1 and nums[p2] <= nums[p1 - 1]:
            p2 -= 1
        
        # 第三步， swap p1 - 1, p2
        nums[p1 - 1], nums[p2] = nums[p2], nums[p1 - 1]
        

        # [不用管的前部半段] + [p1: p3 + 1]
        # 因为p1:p3这一段就是mono-increasing的，直接指针排序
        p3 = n - 1
        while p3 > p1:
            nums[p3], nums[p1] = nums[p1], nums[p3]
            p1 += 1
            p3 -= 1
        