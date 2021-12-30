
# 无重复数组 subset 
# Time complexity: O(2^n * n)
# Space complexity: O(n), for tracking the path array without counting the output res

# 如果真的要细扣的话Subset总共产生2^n个Subset但是每个Subset的长度是n数量级的所以Subset的复杂度应该是O(n*2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def dfs(nums, idx, path, res):
            res.append(path)
            for i in range(idx, len(nums)):
                dfs(nums, i + 1, path + [nums[i]], res)
        
        dfs(nums, 0, [], res)
        return res
    
    # #backtracking:
    # res = [[]]
    # res = [[], [1], [2], [3]]
    # res = [[], [1], [1,2], [1,3], [2], [2,3], [3]]
    # res = [[], [1], [1,2],[1,2,3], [1,3], [2], [2,3], [3]]



# 有重复数组 subset
# Time complexity: O(2^n * n)
# Space complexity: O(n) without counting the output res

# 如果真的要细扣的话Subset总共产生2^n个Subset但是每个Subset的长度是n数量级的所以Subset的复杂度应该是O(n*2^n)
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