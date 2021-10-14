"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

 

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

 
Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105

###############

1.  len(nums)-2 is because we need at least 3 numbers to continue.
2.  if i > 0 and nums[i] == nums[i-1] is because when i = 0, it doesn't need to check if it's a duplicate element since it doesn't even have a previous element to compare with. And nums[i] == nums[i-1] is to prevent checking duplicate again. (This seems to be a good pattern which has been seen in other questions as well).

Time: (O(n*n) time)

"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue # 除重
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur < 0:
                    left += 1
                elif cur > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 # 除重
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 # 除重
                    left += 1
                    right -=1
        
        return res
