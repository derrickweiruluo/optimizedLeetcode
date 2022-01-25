'''
find nums[i] + nums[j] + nums[k] == 0

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

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
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # advance if not duplicates for left or right
                    # advance after cleaning up potential duplicates
                    left += 1
                    right -=1
        
        return res