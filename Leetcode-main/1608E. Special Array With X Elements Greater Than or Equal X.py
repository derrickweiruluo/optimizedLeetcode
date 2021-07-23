class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        if len(nums) <= nums[0]: return len(nums) # edge case
        
        for i in range(1, len(nums)):
            x_num = n - i
            if nums[i] >= x_num and nums[i - 1] <x_num:
                return x_num

        return -1
