'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p1 = n -1
        
        while p1 and nums[p1 -1] >= nums[p1]:
            p1 -= 1
        
        p2 = n -1
        while p1 and p2 > p1 and nums[p2] <= nums[p1 - 1]:
            p2 -= 1
            
        nums[p1 - 1], nums[p2] = nums[p2], nums[p1 - 1]
        
        p3 = n - 1
        while p3 > p1:
            nums[p3], nums[p1] = nums[p1], nums[p3]
            p1 += 1
            p3 -= 1
        