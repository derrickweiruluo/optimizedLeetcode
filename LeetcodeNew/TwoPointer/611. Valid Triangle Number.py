'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

 

Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

'''
class Solution:  # 11/2021
    def triangleNumber(self, nums: List[int]) -> int:
        
        res = 0
        nums.sort()
        
        for i in range(2, len(nums)): # iterate the 3rd number and treat like a 2-sum problem
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += (right - left)
                    right -= 1
                else:
                    left += 1
        
        return res



class Solution:  #07/2021
    def triangleNumber(self, nums: List[int]) -> int:
        
        sortedNums = sorted(nums)
        res = 0
        
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                if sortedNums[left] + sortedNums[right] > sortedNums[i]:
                    # 下面这一步是算都duplicate combination, 符合条件就右 -= 1
                    res += (right - left)
                    right -= 1
                else:
                    # 不行的话就 左 += 1
                    left += 1
        
        # time O(n^2), one for loop in while loop
        return res