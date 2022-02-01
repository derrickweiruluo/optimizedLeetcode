'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''


'''
这是46的followup，有重复的时候，为了避免重复, 
sort first
then DFS as 46

For i position, there're (n-i) possibilities, so the total possilities are: n(n-1)*(n-2)..1 = O(n!):*



https://leetcode.com/problems/permutations-ii/discuss/18607/Concise-JAVA-solution-based-on-DFS
Time complexity = O(n!)

'''

# Time: O(n!) for all permutation
# Space: O(n + k + n) -> O(n), hashtable is n, recursion is k, recursion of permutation is n 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(path, counter):
            if len(path) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                res.append(list(path))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    path.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(path, counter)
                    # revert the choice for the next exploration
                    path.pop()
                    counter[num] += 1

        counter = collections.Counter(nums)
        backtrack([], counter)

        return res



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        def dfs(nums, path):
            if not nums: res.append(path)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        
        dfs(nums, [])
        return res
        



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        
        def dfs(nums, path):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        
        dfs(nums, [])
        return res