class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        res, n = len(nums), len(nums)
        cur = 0
        need = sum(nums) % p
        dp ={0: -1}
        
        for i, val in enumerate(nums):
            cur = (cur + val) % p
            dp[cur] = i
            remainder = (cur - need) % p
            if remainder in dp:
                res = min(res, i - dp[remainder])
            
        return res if res < n else -1
