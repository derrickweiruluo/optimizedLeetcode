class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        curr_start = 0
        curr_end = nums[0]
        counter = 1
        
        while curr_end < len(nums) - 1:
            counter += 1
            next_end = max(i + nums[i] for i in range(curr_start, curr_end + 1)) #高光用法
            curr_start = curr_end
            curr_end = next_end
            
        return counter
