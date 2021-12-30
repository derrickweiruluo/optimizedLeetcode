'''
find min-len subarray with value >= target
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        cur_sum = left = 0
        res = math.inf
        
        for i, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= target:
                res = min(res, i - left + 1)
                cur_sum -= nums[left]
                left += 1
        
        return res if res != math.inf else 0