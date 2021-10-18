"""
Given an integer array nums of unique elements, return all possible subsets (the power set).The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

https://zxi.mytechroad.com/blog/searching/leetcode-78-subsets/
Time complexity: O(2^n)
Space complexity: O(n)
"""


class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(nums, idx, path, res):
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(nums, i + 1, path + [nums[i]], res)
        
        dfs(nums, 0, [], res)
        return res

# res = [[]]
# res = [[], [1], [2], [3]]
# res = [[], [1], [1,2], [1,3], [2], [2,3], [3]]
# res = [[], [1], [1,2],[1,2,3], [1,3], [2], [2,3], [3]]

class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        for num in nums:
            res += [cur + [num] for cur in res]
            
        return res

# res = [[], [1]]
# res = [[], [1], [2], [1, 2]]
# res = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

      
      
      
