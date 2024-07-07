'''
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them
'''

# Example 1:

# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.

# Example 2:

# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.

# Example 3:

# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        '''Input: adjacentPairs = [[2,1],[3,4],[3,2]]
        Output: [1,2,3,4]'''
        
        graph = collections.defaultdict(list)
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(num):
            res.append(num)
            visited[num] = True
            for adj_num in graph[num]:
                if not visited[adj_num]:
                    dfs(adj_num)
        
        starting_num = [x for x in graph if len(graph[x]) == 1]
        visited = {x: False for x in graph}
        res = []
        dfs(starting_num[0])
        return res