'''
找最长的subarray with sum  == k
'''

# prefix sum
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        
        seen = {0: -1}
        res = -math.inf
        curSum = 0
        
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum - k in seen:
                res = max(res, i - seen[curSum - k])
            if curSum not in seen:
                seen[curSum] = i
        
        return res if res != -math.inf else 0
            