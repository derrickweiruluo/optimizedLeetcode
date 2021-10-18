'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.


Ex1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Ex2:
Input: nums = [0]
Output: [[],[0]

The key to this problem is how to remove/avoid duplicates efficiently.

For the same depth, among the same numbers, only the first number can be used.

Time complexity: O(2^n * n)
Space complexity: O(n)
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        
        def dfs(startIdx, nums, path, res):
            res.append(path)
            for i in range(startIdx, len(nums)):
                if i == startIdx or nums[i] != nums[i - 1]:
                    dfs(i + 1, nums, path + [nums[i]], res)
        
        dfs(0, nums, [], res)
        return res


class Solution2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        nums.sort()
        lastPos = {}  # position of num's last position
        
        for i, num in enumerate(nums):
            idx = lastPos.get(num, 0)
            lastPos[num] = len(res) # 除重, 
            res += [cur + [num] for cur in res[idx:]] # 除重
        
        return res