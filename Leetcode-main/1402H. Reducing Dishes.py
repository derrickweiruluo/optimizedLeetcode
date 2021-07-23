class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res, total = 0, 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        
        return res
      
      
# 这道题精辟在于 total_1 + total_2 + ..... total_n 直到 total不再增加


#   while nums and nums[-1] + total > 0
        # total += nums[i]
        # res += total
