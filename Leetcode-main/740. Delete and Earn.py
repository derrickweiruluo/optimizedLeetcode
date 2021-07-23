class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (max(nums) + 1)
        for num in nums:
            dp[num] += num
        
        print(dp)
        prev, curr = 0, 0
        for i in range(len(dp)):
            # print("BEFORE", prev, curr)
            # prev, curr = curr, max(prev + dp[i], curr)
            # print("AFTER",  prev, curr)
            
            oldCurr = curr
            curr = max(prev + dp[i], curr)
            prev = oldCurr
            
        return curr
