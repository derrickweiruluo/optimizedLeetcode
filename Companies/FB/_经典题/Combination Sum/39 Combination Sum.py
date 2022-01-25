'''
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
'''


# The same number may be chosen from candidates an unlimited number of times. 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # https://leetcode.com/submissions/detail/586325101/
        
        res = []
        
        def dfs(nums, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i:], path + [nums[i]], target - nums[i])
        
        dfs(candidates, [], target)
        return res

#     [2,3,5]
#     2
#     22
#     222
#     2222,   yes, 2, 22, 222 go to next unique num
    
#     ---
#     23
#     233,    yes, 23 go to next unique num
#     2333,   X