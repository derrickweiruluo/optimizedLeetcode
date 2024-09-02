"""
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(nums, start_index, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
            for i in range(start_index, len(nums)):
                if i == start_index or nums[i] != nums[i - 1]:
                    dfs(nums, i + 1, path + [nums[i]], target - nums[i])

        dfs(candidates, 0, [], target)
        return res