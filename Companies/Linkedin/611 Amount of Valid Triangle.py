'''
给你一堆数组，求可以组成valid 三角形的数量

'''

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        res = 0
        nums.sort()
        
        for i in range(2, len(nums)):
            # iterate the 3rd number and treat like a 2-sum problem
            # left 是三角形最小的边
            # right 是三角形中间的边
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1

        return res