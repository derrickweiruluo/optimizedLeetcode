class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        res = 0
        visited = set()
        
        for idx in range(len(nums)):
            length = 0
            while idx not in visited:
                length += 1
                visited.add(idx)
                idx = nums[idx]
            res = max(res, length) 
        
        return res
        
        
        
        # *** Below TLE, pass 853/858 TLE becuase revist visited index ***
#         length = 0
        
#         for idx in range(len(nums)):
#             visited = set()
            
#             while idx not in visited:
#                 visited.add(idx)
#                 idx = nums[idx]
#             length = max(length, len(visited))
        
#         return length
