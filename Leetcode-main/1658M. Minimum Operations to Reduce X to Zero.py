class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        arr_sum = sum(nums)
        if sum(nums) < x:
            return -1 
        if sum(nums) == x:
            return len(nums) 
        
        compliment = sum(nums) - x
        left, cur_sum, res = 0, 0, 0
        
        for i, val in enumerate(nums):
            cur_sum += val
            while cur_sum > compliment:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == compliment:
                res = max(res, i - left + 1)
        
        return len(nums) - res if res > 0 else -1
    
    
