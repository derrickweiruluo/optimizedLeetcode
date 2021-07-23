class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        res = 0
        nums.sort()
        
        for i in range(2, len(nums)):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] + nums[i] < target:
                    res += (right - left)
                    left += 1
                else:
                    right -= 1
        
        
        return res
