

# same as 39 with duplicates:


#  k is average length of each solution, and we need O(k)
# time: O(k * 2 ^ n), for solution is 2^n
# Space # O(n) for path and recursion. O(2n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        
        def dfs(nums, path, target, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(nums[i + 1:], path + [nums[i]], target - nums[i], res)
        
        dfs(candidates, [], target, res)
        return res
    
    