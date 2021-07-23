class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return len(nums)
        
        idx = 1
        for i in range(1, len(nums) - 1):
            if nums[i - 1] != nums[i + 1]:
                nums[idx] = nums[i]
                idx += 1
        
        nums[idx] = nums[-1]
        return idx + 1
      
      
      
# Test Cases:
# [1,1,1,2,2,3]
# [0,0,1,1,1,1,2,3,3]
