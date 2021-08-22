"""
Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

############
time O(n2)
除重步骤 at idx i, j, left, and right，细节写法

"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        if n < 4: return []
        
        res = []
        nums.sort()
        
        for i in range(n - 3):
            if i == 0 or nums[i] != nums[i - 1]:   # 1st
                for j in range(i + 1, n - 2):
                    if j == i + 1 or nums[j] != nums[j - 1]:     # 2nd
                        left, right = j + 1, n - 1
                        while left < right:
                            cur = nums[i] + nums[j] + nums[left] + nums[right]
                            if cur == target:
                                res.append([nums[i], nums[j], nums[left], nums[right]])
                                while left < right and nums[left] == nums[left + 1]:    # 3rd
                                    left += 1
                                while left < right and nums[right] == nums[right - 1]:  # 4th
                                    right -= 1
                                left +=1
                                right -= 1
                            elif cur < target:
                                left += 1
                            else:
                                right -= 1
        
        return res
