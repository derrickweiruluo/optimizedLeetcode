'''
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
'''


# Each number may be unlimited number of times. 
# Time: N ^ (M/min_candidates), Space: O(M/min_cand)
class Solution:
    def combinationSum(self, candidates: List[int], target: int):
        res = []
        
        def dfs(nums, start, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(nums)):
                dfs(nums, i, path + [nums[i]], target - nums[i])
        
        dfs(candidates, 0, [], target)
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


# 2D DP too advance
# Time Complexity: O(M*M*N), N = len(candidates), M = target
# Space Complexity: O(M*M)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]