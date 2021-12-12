'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
'''

# https://leetcode.com/problems/making-a-large-island/discuss/127015/C%2B%2B-with-picture-O(n*m)

'''
https://leetcode.com/problems/making-a-large-island/discuss/127032/C%2B%2BJavaPython-Straight-Forward-O(N2)-with-Explanations

Explanation
Only 2 steps:

Only 2 steps:

1. Explore every island using DFS, count its area, give it an island index and save the result to a {index: area} map. Note the grid elements are updated with their corresponding island index. Since the grid has elements 0 or 1. The island index is initialized with 2

2. Loop every cell == 0, check its connected island index and calculate total islands area. The possible connected island index is stored in a set to remove duplicate index.

Complexity
Time O(N^2), N is the lwidth
Space O(N^2), additional space used in DFS and mapping of {islandId: area}
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        width = len(grid)
        
        def validNext(x, y):           # yield 相邻的坐标
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < width and 0 <= y + j < width:
                    yield x + i, y + j
        
        def dfs(x, y, islandID):       # 计算相邻大陆的面积
            res = 0
            grid[x][y] = islandID
            for i, j in validNext(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, islandID)
            return res + 1
            
        islandID = 2                    # 题目是0, 1
        mapping = {0 : 0}               # hashmap of 大陆ID: 面积
        for x in range(width):
            for y in range(width):
                if grid[x][y] == 1:
                    mapping[islandID] = dfs(x, y, islandID)
                    islandID += 1
        
        maxArea = max(mapping.values())   # corner case，当当前已经有最大岛屿(没有case是flip one make bigger)
        for x in range(width):            # 找非陆地，测试sum of (相邻面积 + 1)
            for y in range(width):
                if grid[x][y] == 0:
                    possibleIslandIDs = set(grid[i][j] for i, j in validNext(x, y))
                    maxArea = max(maxArea, sum(mapping[islandID] for islandID in possibleIslandIDs) + 1)
                    
        return maxArea